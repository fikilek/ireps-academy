window.FLOWS = [
{
  name:"Meter Inspection", short:"The whole form, Meter Ok",
  intro:"From the meter to Submit. <b>From the office?</b> Accept the instruction in My Work Orders and open it there: the form is the same.",
  steps:[
    {title:"Meter 04040404040", tag:"CONNECTED · CONVENTIONAL", rows:[
      {l:"Meter No", v:"04040404040"},{l:"Status", v:"Connected"},
      {l:"Actions", btns:["COMM","*INSP","DISC","RECON","REM","MREAD"]}],
     cap:"Field channel: you start it yourself. Open the meter and press INSP. No office instruction is needed."},
    {title:"Meter Inspection", tag:"Meter 04040404040", rows:[
      {l:"Meter No", v:"04040404040"},{l:"Current Status", v:"Connected"},
      {l:"Access Outcome", btns:["*ACCESS YES","NO ACCESS"], s:"focus"}],
     cap:"Can you get to the meter? ACCESS YES carries on. NO ACCESS: pick the reason, take the photo, submit. The meter does not change."},
    {title:"Meter Inspection", tag:"Inspection Capture", rows:[
      {l:"Meter Number", x:"Existing iREPS value: 04040404040", v:"", c:["*SAME"], s:"focus"},
      {l:"Manufacturer", x:"Existing iREPS value: NAv", v:"", c:["SAME"]},
      {l:"Meter Model / Name", x:"Existing iREPS value: CL-2000", v:"", c:["SAME"]}],
     cap:"Every box starts empty. Above it is what iREPS holds. The same on the meter? Press SAME."},
    {title:"Meter Inspection", tag:"Inspection Capture", rows:[
      {l:"Meter Number", x:"Existing iREPS value: 04040404040", v:"04040404040", c:["DELETE"]},
      {l:"Manufacturer", x:"Existing iREPS value: NAv", v:"NAv", c:["DELETE"], s:"focus"},
      {l:"Meter Model / Name", x:"Existing iREPS value: CL-2000", v:"", c:["SAME"]}],
     cap:"SAME copies what iREPS holds. When iREPS holds nothing, SAME puts NAv, and NAv is accepted."},
    {title:"Meter Inspection", tag:"Inspection Capture", rows:[
      {l:"Placement", x:"Existing iREPS value: Kiosk", v:"Boundary Wall", c:["DIFFERENT","DELETE"], s:"focus"},
      {l:"Phase", x:"Existing iREPS value: Single", v:"Single", c:["DELETE"]}],
     cap:"Different on the meter? Press DELETE, then pick or type what you really see. The app marks it DIFFERENT — and what you confirm is written to the meter, so put in what is really there."},
    {title:"Meter Inspection", tag:"Inspection Capture", rows:[
      {l:"CB Size (Amps)", x:"Existing iREPS value: 60", v:"", c:["SAME"]},
      {l:"CB Comment", v:"Circuit Breaker Missing", x:"Select why", s:"focus"},
      {l:"Seal Number", x:"Existing iREPS value: NAv", v:"SE-44821", c:["*PHOTO","DELETE"]}],
     cap:"Record a size, a seal number or a keypad serial and you photograph it too. No circuit breaker, seal or keypad? DELETE the box and pick why, for example Circuit Breaker Missing — then there is nothing to photograph. CB size is typed in amps; the keypad serial is only asked on prepaid meters."},
    {title:"Meter Inspection", tag:"Inspection Capture", rows:[
      {l:"Current Status", x:"Existing iREPS value: Connected", v:"Connected", c:["DELETE"], s:"focus"},
      {l:"Meter GPS", v:"Captured · 3 m from iREPS"}],
     cap:"Current Status is what you find now: Connected or Disconnected. When you submit, the meter takes this status."},
    {title:"Meter Inspection", tag:"Anomaly · Normalisation", rows:[
      {l:"Meter Anomaly", v:"Meter Ok"},{l:"Anomaly Detail", v:"Operationally Ok"},
      {l:"Normalisation", t:["+None","~Tamper removed","~Keypad normalised","~Service point completed","~Meter registered"], s:"choose focus"}],
     cap:"Meter Ok: None stays ticked. Fixed something on the spot? Tick it and take the normalisation photo. A Bridge or Bypass Suspicion needs an anomaly photo."},
    {title:"Meter Inspection", tag:"Conventional Meter Reading", rows:[
      {l:"Meter Reading", v:"018452", c:["PHOTO"], s:"focus"},
      {l:"No Reading Reason", v:"", x:"Only when there is no reading"}],
     cap:"Conventional meter: type the reading and photograph it, or pick why there is no reading. Prepaid meters have no reading here."},
    {title:"Meter Inspection", tag:"SUBMIT INSP", rows:[],
     dialog:{h:"Submit this inspection?", p:"Meter 04040404040. Status found: Connected. Finding: Meter Ok. Nothing opens after this.", btns:["GO BACK","*SUBMIT"]},
     cap:"Press SUBMIT INSP. The app shows you what it is about to send, and what opens next. Read it, then press SUBMIT."},
    {title:"Meter Inspection", tag:"SUBMIT INSP", rows:[],
     dialog:{h:"Confirm Differences", p:"iREPS found 1 field difference(s). Placement. iREPS: Kiosk. Captured: Boundary Wall. Confirm only if these are true field differences and not capture mistakes.", btns:["GO BACK AND CORRECT","*CONFIRM AND SUBMIT"]},
     cap:"When something differs from iREPS you get this window instead: it lists every difference. Confirm only real differences, never a typing mistake."},
    {title:"Meter Inspection", tag:"Sending", rows:[],
     dialog:{spin:true, h:"SYNCING", p:"Submitting meter inspection. DO NOT CLOSE THE APP OR NAVIGATE AWAY"},
     cap:"Wait while it sends. Do not close the app."},
    {title:"Meter Inspection", tag:"Sent", rows:[],
     dialog:{h:"Inspection sent", p:"Meter 04040404040 is recorded as Connected.", btns:["*OK"]},
     cap:"The result window tells you it was sent, and what the meter now is. What you confirmed is now the meter's record: open the card and it reads the way you left it."},
    {title:"Meter Inspection", tag:"No signal", rows:[],
     dialog:{h:"Saved on this phone, not sent", p:"You are offline, so the inspection was NOT sent. It is saved on this phone. When you are online, open it from Admin \u2192 Offline Submission Forms and press SUBMIT.", btns:["*OK"]},
     cap:"No signal or too slow: the inspection waits on the phone. It does NOT send itself. Open Admin \u2192 Offline Submission Forms and press SUBMIT."}
  ]
},
{
  name:"Disconnect meter", short:"Bypass found on an inspection",
  intro:"You find the meter bypassed. The inspection records it, and the disconnection opens by itself. It works the same on a Meter Discovery.",
  steps:[
    {title:"Meter Inspection", tag:"Anomaly", rows:[
      {l:"Meter Anomaly", v:"Illegally Connected"},{l:"Anomaly Detail", v:"Straight Connection (Meter Bypassed)"},
      {l:"Anomaly photo", v:"", c:["*REQUIRED"], s:"focus"}],
     cap:"Record what you found: Illegally Connected, and the detail. Take the anomaly photo: it is required."},
    {title:"Meter Inspection", tag:"Normalisation", rows:[
      {l:"Normalisation", t:["~Disconnect meter","~Replace meter","~Tamper removed","~Keypad normalised","~Service point completed","~Meter registered"], s:"choose focus"}],
     note:{k:"warn", t:"This meter needs to be disconnected. Tick it, or say below why it was not done."},
     cap:"None is no longer offered. Tick Disconnect meter, or say why you could not."},
    {title:"Meter Inspection", tag:"Normalisation", rows:[
      {l:"Normalisation", t:["+Disconnect meter","~Replace meter","~Tamper removed","~Keypad normalised","~Service point completed","~Meter registered"], s:"choose"}],
     note:{k:"info", t:"Disconnect meter recorded."},
     cap:"No normalisation photo for this. The disconnection that follows carries the proof."},
    {title:"Meter Inspection", tag:"SUBMIT INSP", rows:[],
     dialog:{h:"Submit this inspection?", p:"Meter 04040404040. Status found: Connected. Finding: Illegally Connected. Next: the disconnection form opens.", btns:["GO BACK","*SUBMIT"]},
     cap:"Before it sends, the app names the finding and tells you the disconnection opens next."},
    {title:"Meter Inspection", tag:"Sent", rows:[],
     dialog:{h:"Inspection sent", p:"The disconnection form opens now.", btns:["*OK"]},
     cap:"Sent. Press OK and the disconnection opens."},
    {title:"Disconnect 04040404040", tag:"CONNECTED", rows:[
      {l:"Disconnection Instruction", v:"Illegal Connection", c:["LOCKED"], s:"locked focus"},
      {l:"From", v:"Meter Inspection", s:"locked"},
      {l:"Site Access Outcome", btns:["*ACCESS YES","NO ACCESS"]}],
     cap:"The disconnection opens by itself. The instruction is already filled in, Illegal Connection, and cannot be changed. From shows it came from your inspection."},
    {title:"Disconnect 04040404040", tag:"Disconnection Level", rows:[
      {l:"Level", v:"Level 2 - Remove wire on circuit breaker", s:"choose focus",
       x:"Level 1 - Flip circuit breaker only · Level 2 - Remove wire on circuit breaker · Level 3 - Remove whole supply cable"},
      {l:"Disconnection Level Photo", v:"", c:["REQUIRED"]}],
     cap:"You choose the level you actually did on site."},
    {title:"Disconnect 04040404040", tag:"Disconnection Level", rows:[
      {l:"Level", v:"Level 2 - Remove wire on circuit breaker"},
      {l:"Disconnection Level Photo", v:"", c:["*REQUIRED"], s:"focus"}],
     cap:"Photograph the level you did. Without it the form will not submit."},
    {title:"Disconnect 04040404040", tag:"SUBMIT DISCONNECTION", rows:[],
     dialog:{h:"Submit this disconnection?", p:"Meter 04040404040. Instruction: Illegal Connection. Level: Level 2 - Remove wire on circuit breaker.", btns:["GO BACK","*SUBMIT"]},
     cap:"The app shows what it is about to send. Check the level, then press SUBMIT."},
    {title:"Disconnect 04040404040", tag:"Sent", rows:[],
     dialog:{h:"Disconnection sent", p:"Meter 04040404040 is now Disconnected.", btns:["*OK"]},
     cap:"The meter is now Disconnected, and this disconnection is linked to your inspection."}
  ]
},
{
  name:"Found live again", short:"The re-offender",
  intro:"iREPS says the meter is Disconnected, but it is live again. Record what you found, then disconnect it again.",
  steps:[
    {title:"Meter 04040404040", tag:"DISCONNECTED · PRE-PAID", rows:[
      {l:"Status", v:"Disconnected"},
      {l:"Actions", btns:["COMM","*INSP","DISC","RECON","REM","MREAD"]}],
     cap:"The meter shows Disconnected but it is live. Do not press RECON: that is for a reconnection. Press INSP."},
    {title:"Meter Inspection", tag:"Inspection Capture", rows:[
      {l:"Current Status", x:"Existing iREPS value: Disconnected", v:"Connected", c:["DELETE"], s:"focus"}],
     cap:"Current Status: record what you found, Connected. The meter takes this status."},
    {title:"Meter Inspection", tag:"Anomaly · Normalisation", rows:[
      {l:"Meter Anomaly", v:"Illegally Connected"},{l:"Anomaly Detail", v:"Bridge Wire On The Meter"},
      {l:"Normalisation", t:["+Disconnect meter","~Replace meter","~Tamper removed"], s:"choose focus"}],
     cap:"Anomaly: Illegally Connected. Tick Disconnect meter. Take the anomaly photo, then submit."},
    {title:"Disconnect 04040404040", tag:"CONNECTED", rows:[
      {l:"Disconnection Instruction", v:"Illegal Connection", c:["LOCKED"], s:"locked"},
      {l:"From", v:"Meter Inspection", s:"locked"},
      {l:"Level", v:"Level 3 - Remove whole supply cable", s:"choose focus"},
      {l:"Disconnection Level Photo", v:"Taken", c:["PHOTO"]}],
     cap:"The disconnection opens by itself. Choose the level, photograph it, submit."},
    {title:"Disconnect 04040404040", tag:"Sent", rows:[],
     dialog:{h:"Disconnection sent", p:"Meter 04040404040 is now Disconnected.", btns:["*OK"]},
     cap:"Disconnected again, on the record."},
    {title:"What the office sees", tag:"Not a phone screen", rows:[
      {l:"Earlier", v:"Disconnection · meter Disconnected"},
      {l:"Today", v:"Meter Inspection · found Connected · Illegally Connected"},
      {l:"Today, linked to the inspection", v:"Disconnection · Level 3"}],
     note:{k:"ok", t:"Each step has its own number and its own photos, linked to the one before."},
     cap:"Each step has its own record and photos, linked together. That is the proof of a repeat offender."}
  ]
},
{
  name:"Could not do it", short:"A reason instead of the action",
  intro:"You found a bypass but could not disconnect. Say why. Nothing opens after it.",
  steps:[
    {title:"Meter Inspection", tag:"Normalisation", rows:[
      {l:"Meter Anomaly", v:"Illegally Connected"},
      {l:"Normalisation", t:["~Disconnect meter","~Replace meter","~Tamper removed"], s:"choose"},
      {l:"Reason for not acting", v:"Threatened or chased away", s:"choose focus",
       x:"Threatened or chased away · Customer refused · Unsafe to work on · Meter could not be reached · No meter available to replace · Office said to leave it · Other"}],
     note:{k:"warn", t:"This meter needs to be disconnected. Tick it, or say below why it was not done."},
     cap:"Leave Disconnect meter unticked and pick the reason. No photo is needed for the reason."},
    {title:"Meter Inspection", tag:"Normalisation", rows:[
      {l:"Reason for not acting", v:"Other", s:"choose"},
      {l:"Type the reason", v:"Dog loose in the yard", s:"focus"}],
     cap:"Other? Type the reason. Other on its own is not accepted."},
    {title:"Meter Inspection", tag:"SUBMIT INSP", rows:[],
     dialog:{h:"Submit this inspection?", p:"Meter 04040404040. Status found: Connected. Finding: Illegally Connected. Nothing opens after this.", btns:["GO BACK","*SUBMIT"]},
     cap:"The window says it plainly: nothing opens after this. That is what a reason means."},
    {title:"Meter Inspection", tag:"Sent", rows:[],
     dialog:{h:"Inspection sent", p:"Meter 04040404040 is recorded as Connected.", btns:["*OK"]},
     cap:"Sent. The office sees your reason and decides what happens next."}
  ]
},
{
  name:"From a Meter Discovery", short:"New meter, illegally connected",
  intro:"On a Meter Discovery the meter is created first, so the disconnection waits a few seconds.",
  steps:[
    {title:"Meter Discovery", tag:"Anomalies & Actions", rows:[
      {l:"Anomaly", v:"Illegally Connected"},{l:"Anomaly Detail", v:"Straight Connection (Meter Bypassed)"},
      {l:"Normalisation", t:["+Disconnect meter","~Replace meter","~Tamper removed"], s:"choose focus"}],
     cap:"The same as an inspection: Illegally Connected, tick Disconnect meter, take the anomaly photo, submit."},
    {title:"Meter Discovery", tag:"Sent", rows:[],
     dialog:{spin:true, h:"METER SAVED", p:"Preparing the disconnection…"},
     cap:"The meter is saved first. Wait a few seconds while the app gets it ready."},
    {title:"Disconnect 04040404041", tag:"CONNECTED", rows:[
      {l:"Disconnection Instruction", v:"Illegal Connection", c:["LOCKED"], s:"locked focus"},
      {l:"From", v:"Meter Discovery", s:"locked"},
      {l:"Level", v:"", x:"Choose the level you did"}],
     cap:"The disconnection opens by itself, locked to Illegal Connection, from Meter Discovery. Choose the level, photograph it, submit."},
    {title:"Meter Discovery", tag:"If it takes too long", rows:[],
     dialog:{h:"Meter saved, disconnection still to do", p:"The meter is not ready yet. Open the disconnection from the meter card on the ASTs screen.", btns:["*OK"]},
     cap:"Not ready within 20 seconds? Nothing is lost. Open the meter and press DISC."},
    {title:"Meter Discovery", tag:"No signal", rows:[],
     dialog:{h:"Saved Offline", p:"No internet connection. This meter was saved on the phone and will be sent when you are online. The disconnection cannot be started until it has been sent.", btns:["*OK"]},
     cap:"No signal: the meter waits on the phone and the disconnection cannot start. Once the meter has been sent, open it and press DISC."}
  ]
},
{
  name:"Disconnection on its own", short:"Field channel, DISC",
  intro:"No finding in front of it. <b>From the office?</b> Accept it in My Work Orders: the office's instruction is already filled in.",
  steps:[
    {title:"Meter 04040404040", tag:"CONNECTED · PRE-PAID", rows:[
      {l:"Status", v:"Connected"},
      {l:"Actions", btns:["COMM","INSP","*DISC","RECON","REM","MREAD"]}],
     cap:"Press DISC. Only a Connected meter can be disconnected."},
    {title:"Disconnect 04040404040", tag:"CONNECTED", rows:[
      {l:"Disconnection Instruction", v:"Non Payment", s:"choose focus", x:"Credit Control Instruction · Illegal Connection · Non Payment · Other"},
      {l:"Instruction Notes", v:"", x:"Optional"},
      {l:"Instruction Photo", v:"", x:"Optional. Capture the written instruction if available."}],
     cap:"Pick the instruction you are working to: it is now required. Notes and a photo of a written instruction stay optional."},
    {title:"Disconnect 04040404040", tag:"Site Access Outcome", rows:[
      {l:"Site Access Outcome", btns:["*ACCESS YES","NO ACCESS"]},
      {l:"Level", v:"Level 1 - Flip circuit breaker only", s:"choose focus"},
      {l:"Disconnection Level Photo", v:"Taken", c:["PHOTO"]}],
     cap:"ACCESS YES: choose the level and photograph it. NO ACCESS: reason and photo, and the meter stays Connected."},
    {title:"Disconnect 04040404040", tag:"SUBMIT DISCONNECTION", rows:[],
     dialog:{h:"Submit this disconnection?", p:"Meter 04040404040. Instruction: Non Payment. Level: Level 1 - Flip circuit breaker only.", btns:["GO BACK","*SUBMIT"]},
     cap:"Check what it is about to send, then SUBMIT."},
    {title:"Disconnect 04040404040", tag:"Sent", rows:[],
     dialog:{h:"Disconnection sent", p:"Meter 04040404040 is now Disconnected.", btns:["*OK"]},
     cap:"The meter is now Disconnected."}
  ]
},
{
  name:"Meter off, supply stolen", short:"The bypass",
  intro:"The meter is off but the house has power: the supply never passes through the meter. You can still cut it.",
  steps:[
    {title:"Meter Inspection", tag:"Inspection Capture", rows:[
      {l:"Current Status", x:"Existing iREPS value: Disconnected", v:"Disconnected", c:["DELETE"], s:"focus"},
      {l:"Meter Anomaly", v:"Illegally Connected"},
      {l:"Anomaly Detail", v:"Straight Connection (Meter Bypassed)"}],
     cap:"Record what you found: the meter is off, Disconnected, and the supply goes around it. Photograph it."},
    {title:"Meter Inspection", tag:"Normalisation", rows:[
      {l:"Normalisation", t:["+Disconnect meter","~Replace meter","~Tamper removed"], s:"choose focus"}],
     cap:"Tick Disconnect meter, the same as always."},
    {title:"Disconnect 04040404040", tag:"DISCONNECTED", rows:[
      {l:"Disconnection Instruction", v:"Illegal Connection", c:["LOCKED"], s:"locked"},
      {l:"From", v:"Meter Inspection", s:"locked"},
      {l:"Level", v:"Level 3 - Remove whole supply cable", s:"choose focus"}],
     note:{k:"info", t:"A disconnection that follows a finding is accepted on a meter that is already off."},
     cap:"The disconnection opens even though the meter is recorded as Disconnected. Cut the illegal supply and record the level you did."},
    {title:"Disconnect 04040404040", tag:"Sent", rows:[],
     dialog:{h:"Disconnection sent", p:"Meter 04040404040 is now Disconnected.", btns:["*OK"]},
     cap:"Started on its own with DISC, this would be refused: only a Connected meter can be disconnected. After a finding it goes through."}
  ]
},
{
  name:"Replace meter", short:"Remove the old, install the new",
  intro:"A damaged or faulty meter. One instruction, Replace meter, in two stages: the removal, then the installation.",
  steps:[
    {title:"Meter Inspection", tag:"Anomaly \u00b7 Normalisation", rows:[
      {l:"Meter Anomaly", v:"Meter Damaged"},{l:"Anomaly Detail", v:"Meter Button(s) Not Working"},
      {l:"Normalisation", t:["+Replace meter","~Disconnect meter","~Tamper removed"], s:"choose focus"}],
     cap:"Damaged or faulty: tick Replace meter. Take the anomaly photo. No normalisation photo here \u2014 the removal and the installation carry the proof."},
    {title:"Meter Inspection", tag:"SUBMIT INSP", rows:[],
     dialog:{h:"Submit this inspection?", p:"Meter 04298620077. Status found: Connected. Finding: Meter Damaged. Next: the removal form opens. The new meter goes in after it.", btns:["GO BACK","*SUBMIT"]},
     cap:"The window tells you both stages are coming."},
    {title:"Meter Inspection", tag:"Sent", rows:[],
     dialog:{h:"Inspection sent", p:"The removal form opens now. The new meter goes in after it.", btns:["*OK"]},
     cap:"Press OK and the removal opens."},
    {title:"Remove 04298620077", tag:"The old meter comes out", rows:[
      {l:"Removal Instruction", v:"Replace meter", c:["LOCKED"], s:"locked focus", x:"The new meter goes in: the installation opens after this."},
      {l:"From", v:"Meter Inspection", s:"locked"},
      {l:"Site Access Outcome", btns:["*ACCESS YES","NO ACCESS"]}],
     cap:"The instruction is filled in and locked, and shows it came from your inspection."},
    {title:"Remove 04298620077", tag:"Confirm meter removed", rows:[
      {l:"Confirm meter removed", v:"", c:["*PHOTO REQUIRED"], s:"focus",
       x:"Take the photo that shows the meter is out. Submitting this form confirms the removal."}],
     cap:"One photo: the meter out of the wall. There is nothing to tick — submitting the form is the confirmation. Safety confirmed is no longer asked."},
    {title:"Remove 04298620077", tag:"The reading", rows:[
      {l:"Remaining Credit", v:"", x:"The credit left on the meter when it was removed. If it cannot be read, pick why."},
      {l:"Reason Remaining Credit Could Not Be Captured", v:"Display damaged", s:"choose focus",
       x:"Display blank / no reading \u00b7 Display damaged \u00b7 Display unreadable \u00b7 Unable to obtain balance \u00b7 Meter not responding \u00b7 Other"}],
     cap:"Prepaid: type the credit and photograph it, or pick why you could not read it. Take that photo before you pull the meter out — it is your before picture. A conventional meter asks for Meter Reading instead, with the no-reading reasons."},
    {title:"Remove 04298620077", tag:"SUBMIT REMOVAL", rows:[],
     dialog:{h:"Submit this removal?", p:"Meter 04298620077. Instruction: Replace meter. Next: Meter Installation opens.", btns:["GO BACK","*SUBMIT"]},
     cap:"Check it, then SUBMIT."},
    {title:"Remove 04298620077", tag:"Sent", rows:[],
     dialog:{h:"Removal sent", p:"Meter 04298620077 is removed. Meter Installation opens now.", btns:["*OK"]},
     cap:"Press OK and the installation opens for the new meter."},
    {title:"Meter Installation", tag:"The new meter goes in", rows:[
      {l:"Meter Number", v:"0426777553", c:["PHOTO"], s:"focus"},
      {l:"Manufacturer", v:"", x:"Starts empty: pick the make on the new meter"},
      {l:"Anomaly", v:"Meter Ok"}],
     cap:"The new meter at the same premise. Fill it in as usual and submit."},
    {title:"What the office sees", tag:"Not a phone screen", rows:[
      {l:"Old meter 04298620077", v:"Removed"},
      {l:"New meter 0426777553", v:"Created, state Field \u2014 it still needs COMM"},
      {l:"The installation", v:"Replaces the old meter, linked to the removal"},
      {l:"Your inspection", v:"Holds the removal number and the installation number"}],
     note:{k:"ok", t:"One finding, three records, each linked to the one before."},
     cap:"The new meter starts in Field, the same as any new meter: it still needs COMM."}
  ]
},
{
  name:"Meter Removal", short:"Take a meter out, on its own",
  intro:"No finding in front of it. <b>From the office?</b> Accept it in My Work Orders: the office's instruction stands.",
  steps:[
    {title:"Meter 04040404040", tag:"CONNECTED \u00b7 CONVENTIONAL", rows:[
      {l:"Status", v:"Connected"},
      {l:"Actions", btns:["COMM","INSP","DISC","RECON","*REM","MREAD"]}],
     cap:"Press REM. A meter that is Field, Connected or Disconnected can be removed."},
    {title:"Remove 04040404040", tag:"Removal Instruction", rows:[
      {l:"Removal Instruction", v:"Remove meter", s:"choose focus",
       x:"Remove meter \u2014 the meter is taken away, nothing follows \u00b7 Replace meter \u2014 the new meter goes in, the installation opens after this \u00b7 Other"},
      {l:"Instruction Notes", v:"", x:"Optional"}],
     cap:"Pick one, it is required. Under each choice the app tells you what will happen. Replace meter opens the installation after this one, but it is not linked to an earlier finding: the ERF and the premise tie them together."},
    {title:"Remove 04040404040", tag:"Confirm meter removed", rows:[
      {l:"Site Access Outcome", btns:["*ACCESS YES","NO ACCESS"]},
      {l:"Confirm meter removed", v:"", c:["*PHOTO REQUIRED"], s:"focus",
       x:"Take the photo that shows the meter is out. Submitting this form confirms the removal."}],
     cap:"NO ACCESS saves the visit and nothing is removed. Otherwise: the photo of the meter out. Could not remove it at all? Do not open this form — give the reason on the finding."},
    {title:"Remove 04040404040", tag:"The reading", rows:[
      {l:"Meter Reading", v:"018452", c:["PHOTO"], s:"focus"},
      {l:"No Reading Reason", v:"", x:"Only when there is no reading"}],
     cap:"Conventional: type the reading and photograph it, or pick why there is none."},
    {title:"Remove 04040404040", tag:"SUBMIT REMOVAL", rows:[],
     dialog:{h:"Submit this removal?", p:"Meter 04040404040. Instruction: Remove meter. Nothing opens after this.", btns:["GO BACK","*SUBMIT"]},
     cap:"The window says plainly that nothing follows a Remove meter."},
    {title:"Remove 04040404040", tag:"Sent", rows:[],
     dialog:{h:"Removal sent", p:"Meter 04040404040 is now Removed.", btns:["*OK"]},
     cap:"The meter is Removed."}
  ]
}
];
