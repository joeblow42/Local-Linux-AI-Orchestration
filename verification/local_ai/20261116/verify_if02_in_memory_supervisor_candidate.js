"use strict";
// OFFLINE CANDIDATE FAKE ONLY; does not implement LangGraph, Pipe or G1.
// Run with: node verify_if02_in_memory_supervisor_candidate.js
// Model tests cannot prove durable locking, concurrency, backend authorization,
// actual frontend delivery, HTTP status codes, or cancellation of Ollama calls.
class CandidateSupervisor {
  constructor(){this.serial=0;this.tasks=new Map();this.requests=new Map();this.available=true;}
  submit(actor,key,payload="workflow"){
    if(!this.available)return {ok:false,error:"unavailable"};
    if(!actor||!key)return {ok:false,error:"invalid_request"};
    const k=actor+":"+key,existing=this.requests.get(k);
    if(existing){
      if(existing.payload!==payload)return {ok:false,error:"idempotency_conflict"};
      const t=this.tasks.get(existing.id);
      return {ok:true,task_id:existing.id,state:t.state,state_version:t.version,duplicate:true};
    }
    const id="tsk_"+String(++this.serial).padStart(4,"0");
    this.tasks.set(id,{actor,state:"accepted",version:1,steps:0,checkpoint_ok:true});
    this.requests.set(k,{id,payload});
    return {ok:true,task_id:id,state:"accepted",state_version:1};
  }
  status(actor,id){
    if(!this.available)return {ok:false,error:"unavailable"};
    const t=this.tasks.get(id);
    if(!t||t.actor!==actor)return {ok:false,error:"not_found"};
    if(!t.checkpoint_ok)return {ok:false,error:"recovery_error"};
    return {ok:true,task_id:id,state:t.state,state_version:t.version};
  }
  start(id){const t=this.tasks.get(id);if(t&&t.state==="accepted"){t.state="running";t.version++;return true;}return false;}
  step(id){const t=this.tasks.get(id);if(!t||t.state!=="running")return false;t.steps++;return true;}
  cancel(actor,id){
    if(!this.available)return {ok:false,error:"unavailable"};
    const t=this.tasks.get(id);
    if(!t||t.actor!==actor)return {ok:false,error:"not_found"};
    if(!t.checkpoint_ok)return {ok:false,error:"recovery_error"};
    if(["completed","cancelled","failed","incomplete","recovery_error"].includes(t.state))
      return {ok:true,cancel_accepted:false,state:t.state,state_version:t.version};
    if(t.state!=="cancel_requested"){t.state="cancel_requested";t.version++;}
    return {ok:true,cancel_accepted:true,state:t.state,state_version:t.version};
  }
  finish(id,outcome){
    const t=this.tasks.get(id);
    if(!t||["completed","cancelled","failed","incomplete","recovery_error"].includes(t.state))return false;
    if(t.state==="cancel_requested"&&outcome!=="cancelled")return false;
    if(t.state==="running"&&!["completed","failed"].includes(outcome))return false;
    if(t.state==="accepted")return false;
    t.state=outcome;t.version++;return true;
  }
  uiStop(id){return !!id;}
}

function runCandidateTests(){
  const cases=[];
  function t(id,test){try{if(test()!==true)throw Error("assertion false");cases.push({id,result:"PASS"});}catch(e){cases.push({id,result:"FAIL",error:String(e)});}}
  function fresh(){const s=new CandidateSupervisor(),a=s.submit("operator","req-1");return {s,id:a.task_id};}
  t("T01_lost_ack_retry_same_id",()=>{let {s,id}=fresh(),r=s.submit("operator","req-1");return r.task_id===id&&r.duplicate&&s.tasks.size===1;});
  t("T02_distinct_keys_distinct_tasks",()=>{let {s,id}=fresh(),r=s.submit("operator","req-2");return r.task_id!==id&&s.tasks.size===2;});
  t("T03_status_reads_running_version",()=>{let {s,id}=fresh();return s.start(id)&&s.status("operator",id).state==="running"&&s.status("operator",id).state_version===2;});
  t("T04_cancel_ack_not_terminal",()=>{let {s,id}=fresh();s.start(id);let x=s.cancel("operator",id);return x.cancel_accepted&&x.state==="cancel_requested"&&s.status("operator",id).state!=="cancelled";});
  t("T05_cancel_blocks_new_step",()=>{let {s,id}=fresh();s.start(id);s.step(id);s.cancel("operator",id);return !s.step(id)&&s.tasks.get(id).steps===1;});
  t("T06_cancel_before_completion_wins",()=>{let {s,id}=fresh();s.start(id);s.cancel("operator",id);return !s.finish(id,"completed")&&s.status("operator",id).state==="cancel_requested";});
  t("T07_accepted_cancel_then_terminal",()=>{let {s,id}=fresh();s.start(id);s.cancel("operator",id);return s.finish(id,"cancelled")&&s.status("operator",id).state==="cancelled";});
  t("T08_completed_before_cancel_wins",()=>{let {s,id}=fresh();s.start(id);s.finish(id,"completed");let x=s.cancel("operator",id);return !x.cancel_accepted&&x.state==="completed";});
  t("T09_duplicate_cancel_no_version_change",()=>{let {s,id}=fresh();s.start(id);let x=s.cancel("operator",id),y=s.cancel("operator",id);return x.cancel_accepted&&y.cancel_accepted&&x.state_version===y.state_version;});
  t("T10_other_actor_no_cancel",()=>{let {s,id}=fresh(),v=s.status("operator",id).state_version,x=s.cancel("other",id);return !x.ok&&x.error==="not_found"&&v===s.status("operator",id).state_version;});
  t("T11_unknown_task_no_success",()=>{let {s}=fresh(),x=s.status("operator","tsk_missing");return !x.ok&&x.error==="not_found"&&!x.state;});
  t("T12_unavailable_does_not_accept",()=>{let {s}=fresh(),n=s.tasks.size;s.available=false;let x=s.submit("operator","req-2");return !x.ok&&x.error==="unavailable"&&s.tasks.size===n;});
  t("T13_ui_stop_not_supervisor_cancel",()=>{let {s,id}=fresh();s.start(id);s.uiStop(id);return s.status("operator",id).state==="running";});
  t("T14_stale_ui_version_rejected",()=>{let {s,id}=fresh();s.start(id);s.cancel("operator",id);let view=s.status("operator",id),old={state:"running",state_version:2};if(old.state_version>view.state_version)view=old;return view.state==="cancel_requested";});
  t("T15_missing_checkpoint_not_completed",()=>{let {s,id}=fresh();s.tasks.get(id).checkpoint_ok=false;let x=s.status("operator",id);return !x.ok&&x.error==="recovery_error"&&!x.state;});
  t("T16_failed_terminal_cannot_cancel",()=>{let {s,id}=fresh();s.start(id);s.finish(id,"failed");let x=s.cancel("operator",id);return !x.cancel_accepted&&x.state==="failed";});
  t("T17_terminal_state_no_regression",()=>{let {s,id}=fresh();s.start(id);s.finish(id,"completed");return !s.finish(id,"failed")&&s.status("operator",id).state==="completed";});
  t("T18_idempotency_reuse_changed_payload_denied",()=>{let {s}=fresh(),n=s.tasks.size,x=s.submit("operator","req-1","different");return !x.ok&&x.error==="idempotency_conflict"&&s.tasks.size===n;});
  t("T19_cancel_accepted_before_start_fences",()=>{let {s,id}=fresh();s.cancel("operator",id);return !s.start(id)&&!s.step(id)&&s.status("operator",id).state==="cancel_requested";});
  t("T20_unauthorized_status_no_leak",()=>{let {s,id}=fresh(),x=s.status("different",id);return !x.ok&&x.error==="not_found"&&!x.task_id&&!x.state;});
  return {result:cases.every(x=>x.result==="PASS")?"CANDIDATE_FAKE_MODEL_PASS":"CANDIDATE_FAKE_MODEL_FAIL",cases,passed:cases.filter(x=>x.result==="PASS").length,failed:cases.filter(x=>x.result!=="PASS").length,scope:"standalone in-memory fake only",executed_external_provider_calls:0,executed_openwebui_calls:0,executed_langgraph_calls:0,executed_G1_calls:0};
}

const summary=runCandidateTests();
console.log(JSON.stringify(summary,null,2));
if(summary.failed) process.exitCode=1;
