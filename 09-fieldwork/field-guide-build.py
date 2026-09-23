import html, re, pathlib

SCR = pathlib.Path(__file__).parent
TPL = SCR / "field-guide-template.html"
PAGE = pathlib.Path(r"C:\dev\ireps-academy\09-fieldwork\field-guide-2026-09-27.html")
DISC_FIELDS = "https://claude.ai/artifact/3ATyax5CnEhpHsxYpNAdvT"
DISC_RULES = "https://claude.ai/artifact/DUKvC3Khiibof3fJe7QMxu"
DISC_ERRORS = "https://claude.ai/artifact/GWgWkiECF5J53KTYGycYxb"
COMING = '<span class="coming">coming</span>'

def e(s):
    return html.escape(s, quote=False)

# ---------------------------------------------------------------- what's new
NEWS = [
    ("Meter Inspection", "Start an inspection yourself.", "Open the meter and press INSP. No office instruction is needed."),
    ("Discovery · Inspection", "Found a problem? Act on it, or say why not.", "For anything other than Meter Ok, None is no longer offered. Tick the action, or pick the reason you could not."),
    ("Disconnection", "Illegally Connected opens the disconnection by itself.", "Tick Disconnect meter. The disconnection opens with the instruction filled in and locked: Illegal Connection. You choose the level."),
    ("Meter Inspection", "SAME on every box.", "The same on the meter? Press SAME. If iREPS holds nothing, SAME puts NAv, and that is accepted."),
    ("Meter Inspection", "The status you find is what the meter becomes.", "Found a disconnected meter live again? Record Connected, then disconnect it again. When iREPS holds no status, the box starts empty and you choose."),
    ("Meter Inspection", "If it is there, photograph it.", "The CB size, the seal number and the keypad serial number now each carry a photo, the same picture the office gets from a discovery. Nothing there — NAv, or a reason why there is none — and no photo is asked for."),
    ("Meter Inspection", "What you confirm becomes the meter's record.", "An inspection used to change only the status, so a meter found fine could still show an old finding on its card. Now the finding and the details you confirm are written to the meter, and the card shows them straight after. Not the meter number, and not the GPS."),
    ("Inspection · Disconnection · Removal", "Every submit now has a window before and after.", "Before: what is about to be sent and what opens next. After: sent, or saved on this phone and not sent. No window means it did not send. Work that stayed on the phone waits under Admin → Storage, on the screen headed Offline Submission Forms, and only a Meter Discovery sends itself."),
    ("Disconnection · Removal", "A disconnection or removal you start yourself needs its instruction.", "Disconnection: Credit Control Instruction, Illegal Connection or Non Payment. Removal: Remove meter or Replace meter. After a finding it is filled in for you and locked."),
    ("Disconnection", "Meter off, but the supply is stolen?", "An illegal connection can bypass a meter that is already off. After a finding, the disconnection is accepted on a meter recorded as Disconnected."),
    ("Removal · Installation", "Replace meter: remove, then install.", "Faulty or Damaged: the removal opens, and the new meter goes in after it. Safety confirmed is gone, the removal is confirmed by one photo of the meter out, and a prepaid meter's reading is Remaining Credit, as on Discovery."),
    ("Removal · Reconnection", "Doing the work is the answer: one photo confirms it.", "The old Yes/No questions are gone. The removal asks for the photo that shows the meter is out; the reconnection for the photo that shows the supply is back on. Sending the form is the confirmation."),
    ("All forms", "Every list works without signal.", "The dropdowns are kept on the phone, so a new phone or a dead zone no longer leaves them empty."),
]

def news_html():
    items = "".join(
        f'<li><span class="formtag">{e(tag)}</span><p><b>{head}</b> {e(body)}</p></li>'
        for tag, head, body in NEWS)
    return ('<section class="part" id="new">\n    <h2>What\'s new</h2>\n'
            '    <p class="sub">Ten changes. The flows below show each one on the phone.</p>\n'
            f'    <ul class="news">{items}</ul>\n  </section>')

# ---------------------------------------------------------------- fields
# field: (name, tag, meaning, options)
CB_WHY = "Circuit Breaker Missing · Circuit Breaker Size Not Visible · Circuit Breaker Size Unreadable · Circuit Breaker Damaged · Circuit Breaker Inaccessible · No Dedicated Circuit Breaker · Distribution Board Inaccessible · Other"
SEAL_WHY = "Seal Missing · Seal Broken · Seal Damaged · Seal Number Not Visible · Seal Number Unreadable · Seal Removed · Meter Not Sealed · Other"
KEYPAD_WHY = "Keypad Missing · Keypad Not Installed · Keypad Integrated With Meter · Keypad Serial Number Not Visible · Keypad Serial Number Unreadable · Keypad Damaged · Keypad Inaccessible · Other"
ELEC_MAKES = "Conlog · Landis+gyr · Cashpower · Hexing · Powercom · Itron"
WATER_MAKES = "Conlog · Sensus · Elster Kent · Itron · Kamstrup · Lesira Teq · Aqua Loc · Reonet"
PLACEMENTS = "Kiosk · Pole Top · Pole Bottom · Boundary Wall · Meter Room · Wall Indoors · Inside Property · Other"
NA_REASONS = "Property Locked · Access Refused by Occupant · Unsafe / Dangerous Environment · Meter Box Inaccessible · Meter Obstructed · Property Demolished · Property Vacant · Other"
ANOMALIES = "Meter Ok: Operationally Ok, Bridge Suspicion, Bypass Suspicion. Meter Faulty: Not Accepting Sgc Tokens, Meter Display Blank, Negative Credit Units, Zero Reading - Conventional Meter, Meter Wheel Not Moving, Meter Wheel Running In Reverse. Meter Damaged: Meter Number Not Clearly Visible, Meter Burnt, Meter Button(s) Not Working, Meter Broken. Illegally Connected: Straight Connection (Meter Bypassed), Bridge Wire On The Meter."
NOT_ACTING = "Threatened or chased away · Customer refused · Unsafe to work on · Meter could not be reached · No meter available to replace · Office said to leave it · Other (type it)"
NO_READING = "Customer refused access · Display blank · Display damaged · Display not working · Meter box locked · Meter not accessible · Meter removed or missing · No access to premises · Other"

FORMS_FIELDS = [
  {
    "name": "Meter Inspection", "sub": "INSP · check a meter iREPS already holds",
    "how": "Field channel: open the meter and press INSP (a meter that is Field, Connected, Disconnected or Removed). Office channel: accept the instruction in My Work Orders. A manager who presses INSP issues it to a field worker instead.",
    "groups": [
      ("Access", [
        ("Access Outcome", "required", "ACCESS YES carries on. NO ACCESS saves the visit; the meter does not change.", "ACCESS YES · NO ACCESS"),
        ("NA Reason and photo", "no access", "Why you could not get to the meter, and a photo that shows it.", NA_REASONS),
      ]),
      ("The meter · SAME, or change it", [
        ("Why this matters", "", "What you confirm here is written to the meter record when the office accepts the inspection, and the meter card shows it straight after. That is why each box shows the Existing iREPS value, marks a change DIFFERENT, and asks you to confirm the differences before it sends. Two are never written from an inspection: the meter number (a wrong one is a supervisor's correction) and the GPS (that belongs to the discovery). A box you were never asked for is left alone — nothing is blanked because a question did not appear. A NO ACCESS visit changes nothing at all.", ""),
        ("Meter Number", "required + photo", "The number printed on the meter. Photograph it.", ""),
        ("Manufacturer", "required", "The make on the meter.", "Electricity: " + ELEC_MAKES + " · Other. Water: " + WATER_MAKES + " · Other."),
        ("Meter Model / Name", "required", "As printed on the meter.", ""),
        ("Meter Kind", "required", "Pick it from the list.", "Prepaid · Conventional"),
        ("Meter Category", "required", "Pick it from the list.", "Normal · Bulk"),
        ("Phase", "required", "Electricity only.", "Single · Three"),
        ("CB Size (Amps)", "value + photo, or why", "The circuit breaker size, typed in amps: record one and photograph it. None? DELETE and pick why — then no photo is asked for.", CB_WHY),
        ("Seal Number", "value + photo", "The number on the meter seal: record one and photograph it. None? DELETE and pick why — then no photo is asked for.", SEAL_WHY),
        ("Keypad Serial Number", "value + photo, or why", "Prepaid electricity meters only: record one and photograph it. None? DELETE and pick why — then no photo is asked for.", KEYPAD_WHY),
        ("Placement", "required", "Where the meter sits.", PLACEMENTS),
        ("Off-grid Supply", "required", "Is there a supply at the premise that does not come from the grid?", "Yes · No"),
        ("Meter GPS", "", "Put the pin on the meter. More than 5 m from iREPS shows up as a difference before you submit.", ""),
      ]),
      ("What you found", [
        ("Current Status", "required", "What you find now. The meter takes this status when you submit. It is filled in only when iREPS holds Connected or Disconnected; otherwise the box starts empty and you choose. A status that differs from iREPS is one of the differences you confirm before submitting.", "Connected · Disconnected"),
        ("Meter Anomaly and Anomaly Detail", "required", "What is wrong, if anything. Every detail except Operationally Ok needs an anomaly photo.", ANOMALIES),
        ("Other Anomalies", "", "Anything else you saw. Tick all that apply.", "Meter Blocked (By Munic) · Meter Bridged (By Munic) · Incomplete Service Points · Meter Not Registered · Keypad Faulty"),
        ("Normalisation", "required", "What you did about the finding. See Finding → action above. A fix on the spot needs a normalisation photo; Disconnect meter and Replace meter do not. Electricity only: a water inspection has no normalisation and records None.", "Meter Ok: None · Tamper removed · Keypad normalised · Service point completed · Meter registered. Anything else: Disconnect meter · Replace meter · and the four fixes."),
        ("Reason for not acting", "when not ticked", "Why the action that follows the finding was not done. No photo.", NOT_ACTING),
      ]),
      ("Before and after Submit", [
        ("Submit this inspection?", "before", "What is about to be sent: the meter, the status you found, the finding, and what opens next. GO BACK or SUBMIT.", ""),
        ("Confirm Differences", "when they differ", "Shown instead when what you captured differs from iREPS, listing every difference. GO BACK AND CORRECT or CONFIRM AND SUBMIT.", ""),
        ("SYNCING", "while sending", "Submitting meter inspection. Do not close the app.", ""),
        ("Inspection sent", "after", "It reached the office, and what opens next, or what the meter now is.", ""),
        ("Saved on this phone, not sent", "after", "It did not send: you are offline or the network was too slow. It waits in Admin → Offline Submission Forms and does not send itself. A disconnection or removal cannot start until it is sent.", ""),
      ]),
      ("Reading · conventional meters only", [
        ("Meter Reading", "reading or reason", "Type the reading and photograph it.", ""),
        ("No Reading Reason", "when blank", "Why there is no reading.", NO_READING),
      ]),
    ],
  },
  {
    "name": "Disconnection", "sub": "DISC · cut the supply",
    "how": "After a finding: opens by itself when you tick Disconnect meter. Field channel: open the meter and press DISC. Office channel: accept it in My Work Orders. Only a Connected meter can be disconnected.",
    "groups": [
      ("The instruction", [
        ("Disconnection Instruction", "required", "What you are disconnecting for. After a finding it is filled in and locked: Illegal Connection. From the office, the office's instruction is filled in. When you start it yourself you must pick one.", "Credit Control Instruction · Illegal Connection · Non Payment · Other"),
        ("From", "", "Shown when it follows a finding.", "Meter Inspection · Meter Discovery"),
        ("Instruction Notes and Instruction Photo", "optional", "Field channel only. A photo of a written instruction, if you have one.", ""),
      ]),
      ("On site", [
        ("Site Access Outcome", "required", "ACCESS YES carries on. NO ACCESS: reason and photo; the meter stays Connected.", "ACCESS YES · NO ACCESS"),
        ("Disconnection Level", "required", "What you physically did.", "Level 1 - Flip circuit breaker only · Level 2 - Remove wire on circuit breaker · Level 3 - Remove whole supply cable"),
        ("Disconnection Level Photo", "required", "A photo of the level you did.", ""),
        ("FWR General Comment", "optional", "A comment and a photo, if you need them.", ""),
      ]),
    ],
    "after": "Only a Connected meter can be disconnected, with one exception: a disconnection that follows a finding is accepted on a meter recorded as Disconnected, because an illegal connection can bypass a meter that is already off. Before Submit: \u201cSubmit this disconnection?\u201d with the meter, the instruction and the level. After: \u201cDisconnection sent\u201d, and the meter is Disconnected. Saved on the phone instead? It does not send itself.",
  },
  {
    "name": "Meter Installation", "sub": "Install · a new meter at a premise",
    "how": "Open the premise, press Install and choose ELEC or WATER, or NO ACCESS. After a Replace meter removal it opens by itself, for the new meter at the same premise.",
    "groups": [
      ("Electricity", [
        ("Meter Number", "required + photo", "Letters and digits only, as printed. Photograph it.", ""),
        ("Manufacturer", "required", "Starts empty: pick the make on the meter.", ELEC_MAKES),
        ("Model (Name)", "required", "As printed on the meter.", ""),
        ("Phase · Type · Category", "required", "The same words as Meter Discovery.", "Single · Three | Prepaid · Conventional | Normal · Bulk"),
        ("Seal No", "number or reason", "Type or scan it. None? Pick why.", SEAL_WHY),
        ("Keypad Serial No", "", "Prepaid only. Type or scan it. None? Pick why.", KEYPAD_WHY),
        ("CB Size (Amps)", "", "None? Pick why.", CB_WHY),
        ("Meter Placement", "required", "Where the meter sits.", PLACEMENTS),
        ("Meter GPS Position", "required", "Put the pin on the meter.", ""),
        ("Off-grid Supply?", "required", "Yes needs a photo.", "yes · no"),
        ("Anomaly and Anomaly Detail", "required", "The same list as Meter Discovery. Every detail except Operationally Ok needs an anomaly photo.", ANOMALIES),
      ]),
      ("Water", [
        ("Meter Number", "required + photo", "", ""),
        ("Category · Type · Manufacture · Model Name", "required", "", "Makes: " + WATER_MAKES),
        ("Token Reading or Meter Reading", "required + photo", "Token Reading on a prepaid meter; Meter Reading on a conventional one.", ""),
        ("Anomaly and GPS", "required", "As for electricity. No placement.", ""),
      ]),
    ],
  },
  {
    "name": "Meter Reconnection", "sub": "RECON · put the supply back on",
    "how": "Open a meter that iREPS holds as Disconnected and press RECON, or accept the office's instruction in My Work Orders. Only the confirmation changed on Sunday; the rest of the form is as you know it.",
    "groups": [
      ("What changed", [
        ("Confirm supply reconnected", "photo required", "“Take the photo that shows the supply is back on and safe. Submitting this form confirms the reconnection.” There is no Yes/No and no notes box any more: sending the form is the confirmation.", ""),
      ]),
      ("The rest of the form", [
        ("Reconnection Instruction", "", "Locked when the office issued it. Started yourself: pick it from the list, or Other and type it.", "Reconnect meter supply and confirm the supply has been made good again · Other"),
        ("Instruction Notes", "optional", "What you were told, in your own words.", ""),
        ("Site Access Outcome", "required", "NO ACCESS saves the visit; the meter stays Disconnected.", "ACCESS YES · NO ACCESS"),
      ]),
    ],
  },
  {
    "name": "Meter Discovery", "sub": "DISCOVER · what is new on Sunday",
    "how": 'Everything else about Meter Discovery is on its own pages: <a href="%s">the fields</a> · <a href="%s">the rules</a> · <a href="%s">the errors</a>. New on Sunday is the normalisation part, electricity only:' % (DISC_FIELDS, DISC_RULES, DISC_ERRORS),
    "raw_how": True,
    "groups": [
      ("Normalisation", [
        ("Normalisation", "required", "Meter Ok: None, or a fix you did. Anything else: None is gone; tick the action that follows, or give a reason.", "Illegally Connected → Disconnect meter · Meter Faulty or Meter Damaged → Replace meter"),
        ("Reason for not acting", "when not ticked", "Why the action was not done. No photo.", NOT_ACTING),
        ("Normalisation photo", "for a fix", "Only when you tick a fix done on the spot.", ""),
        ("After Submit", "", "Disconnect meter: \u201cPreparing the disconnection\u2026\u201d, then the disconnection opens. Replace meter: \u201cPreparing the removal\u2026\u201d, then the removal opens (being tested).", ""),
      ]),
    ],
  },
  {
    "name": "Meter Removal", "sub": "REM · take a meter out",
    "how": "Three ways in, all ending in the same form. Open it only when the meter is really coming out: if you cannot remove it, give the reason on the finding instead.",
    "groups": [
      ("How it starts", [
        ("The office issues it", "office channel", "You accept it in My Work Orders. The office's instruction, notes and photo are filled in and locked.", ""),
        ("You open it with REM", "field channel", "On a meter that is still there (Field, Connected or Disconnected). You have the instruction on paper or by phone: pick it from the list, type the notes, photograph the paper.", ""),
        ("It follows a finding", "linked", "You ticked Replace meter on an inspection or a discovery. It opens by itself, locked to Replace meter, with From: Meter Inspection.", ""),
        ("Any of the three", "", "Can end in NO ACCESS: the visit is saved, nothing is removed and nothing follows.", ""),
      ]),
      ("The instruction", [
        ("Removal Instruction", "required", "What you are doing. Under each choice the app says what will happen. Locked after a finding; when you start it yourself you must pick one.", "Remove meter — “The meter is taken away. Nothing follows.” · Replace meter — “The new meter goes in: the installation opens after this.” · Other"),
        ("From", "", "Shown when it follows a finding.", "Meter Inspection · Meter Discovery"),
        ("Instruction Notes", "optional", "What you were told, in your own words.", ""),
        ("Instruction Photo", "optional", "“Optional. Capture the written instruction if available.” The same as the disconnection and the reconnection.", ""),
      ]),
      ("On site", [
        ("Site Access Outcome", "required", "ACCESS YES carries on. NO ACCESS saves the visit; nothing is removed and nothing follows.", "ACCESS YES · NO ACCESS"),
        ("NA Reason and photo", "no access", "Why you could not reach the meter, and a photo.", NA_REASONS),
        ("Confirm meter removed", "photo required", "“Take the photo that shows the meter is out. Submitting this form confirms the removal.” There is nothing to tick: sending the form is the confirmation. Could not remove the meter? Do not open this form — give the reason on the finding. Could not reach it? Use NO ACCESS.", ""),
      ]),
      ("The reading", [
        ("Remaining Credit", "prepaid", "The credit left on the meter when it was removed. Type it and photograph it, or pick why you could not read it. The same as Meter Discovery.", "Display blank / no reading · Display damaged · Display unreadable · Unable to obtain balance · Meter not responding · Other"),
        ("Meter Reading", "conventional", "The reading when the meter was removed. Type it and photograph it, or pick why there is none.", NO_READING),
        ("Safety confirmed", "gone", "No longer asked.", ""),
      ]),
    ],
    "after": "Remove meter: “Removal sent” and the meter is Removed. Replace meter: “Meter Installation opens now”, linked to the removal, and the new meter is created in Field — it still needs COMM. From the meter card, Replace meter opens the installation too, but it is not linked to an earlier finding: the ERF and the premise tie them together.",
  },
]

def req_tag(t):
    return f'<span class="req">{e(t)}</span>' if t else ""

def fields_html():
    out = ['<section class="part" id="fields">',
           '    <h2>What each box means</h2>',
           '    <p class="sub">Tap a form. Required boxes are marked.</p>']
    for f in FORMS_FIELDS:
        title = e(f["name"]) + (" " + COMING if f.get("coming") else "")
        how = f["how"] if (f.get("raw_how") or "<span" in f["how"]) else e(f["how"])
        parts = [f'<details class="form"><summary><span>{title}<small>{e(f["sub"])}</small></span></summary><div class="inner"><p class="how">{how}</p>']
        for gname, fields in f["groups"]:
            if gname:
                parts.append(f'<h4 class="group">{e(gname)}</h4>')
            parts.append('<dl class="fields">')
            for name, tag, meaning, opts in fields:
                dd = e(meaning) + (f'<span class="opts">{e(opts)}</span>' if opts else "")
                parts.append(f'<div><dt>{e(name)}{req_tag(tag)}</dt><dd>{dd}</dd></div>')
            parts.append('</dl>')
        if f.get("after"):
            parts.append(f'<p class="how" style="margin-top:10px">{e(f["after"])}</p>')
        parts.append('</div></details>')
        out.append("".join(parts))
    out.append('  </section>')
    return "\n".join(out)

# ---------------------------------------------------------------- errors
# (kind, message(s), means, do)
INSP_ERRORS = [
  ("Before submit", ["Not ready to submit yet"], "A red box above SUBMIT names the first thing still missing. Fix it and the next one shows, until the box is gone.", "Read the line, fix that box, look again."),
  ("Before submit", ["Choose the status you found: Connected or Disconnected"], "The status box is empty. iREPS holds no status for this meter, so nothing was filled in for you.", "Pick Connected or Disconnected: what you see at the meter now."),
  ("Office refused", ["An inspection records the meter as Connected or Disconnected only"], "The status that reached the office was neither.", "Open the form again and pick Connected or Disconnected."),
  ("Office refused", ["Say why the meter was not disconnected.", "Say why the meter was not replaced."], "The finding needs an action, and it is not ticked and has no reason.", "Tick Disconnect meter or Replace meter, or pick the reason you could not."),
  ("Office refused", ["Say what was done about this finding."], "Nothing is ticked under Normalisation for a finding that needs action.", "Tick the action, or give the reason."),
  ("Office refused", ["Choose one: disconnect or replace."], "Both jobs are ticked. A meter is either disconnected or replaced.", "Untick one."),
  ("Office refused", ["None cannot be used with another action."], "None is ticked together with work you did.", "Untick None."),
  ("Office refused", ["The work was done, so there is no reason for not acting."], "The action is ticked and a reason is given too.", "Clear the reason."),
  ("Office refused", ["A reason for not acting belongs to a finding that needs action."], "Meter Ok with a reason.", "Clear the reason."),
  ("Office refused", ["Type the reason."], "The reason is Other with nothing typed.", "Type the real reason."),
  ("Before submit", ["Photo proof of the normalisation is required."], "You ticked a fix done on the spot without photographing it.", "Photograph what you fixed."),
  ("Before submit", ["An anomaly photo is required for this finding"], "The finding needs a picture. Only Operationally Ok needs none.", "Photograph what you found."),
  ("Office refused", ["Meter number photo is required"], "No photo of the meter number.", "Photograph the meter number."),
  ("Before submit", ["A photo of the CB size is required", "A photo of the seal number is required", "A photo of the keypad serial number is required"], "You recorded a circuit breaker size, a seal number or a keypad serial number and did not photograph it. What is there is photographed.", "Photograph it. If there is nothing there, clear the box and pick why instead — then no photo is asked for."),
  ("Office refused", ["CB size is required, or say why there is none", "Keypad serial number is required, or say why there is none"], "The box is empty and no reason is picked.", "Press SAME, type it, or DELETE and pick why."),
  ("Office refused", ["Inspection reading or no-reading reason is required for conventional meters", "Inspection meter reading must be numeric", "Meter reading photo is required when inspection reading is captured"], "The conventional meter reading is missing, not a number, or has no photo.", "Type the reading in digits and photograph it, or pick the No Reading Reason."),
  ("Office refused", ["Inspection comparison differences must be confirmed before submit"], "What you captured differs from iREPS and was not confirmed.", "Submit again and confirm the differences, if they are real."),
  ("Office refused", ["No-access reason is required", "No access photo is required"], "NO ACCESS without a reason or a photo.", "Pick the reason and take the photo."),
  ("Office refused", ["Meter inspection requires a known meter kind: prepaid or conventional", "Inspection is blocked because the existing iREPS meter kind is unknown. Update the meter record before creating an INSPECTION."], "iREPS does not know whether this meter is prepaid or conventional.", "Tell your supervisor with the meter number. The office must fix the meter record first."),
  ("Office refused", ["DECOMMISSIONED meters cannot be inspected", "Only FIELD, CONNECTED, DISCONNECTED, or REMOVED meters can be inspected"], "The meter is not in a state that can be inspected.", "If the meter is really there, tell your supervisor with the meter number."),
  ("On the phone", ["Not Allowed", "Only MNG, SPV(MNC), FWR, or SPV(SUBC) can start this lifecycle action."], "Your role cannot start this work.", "Tell your supervisor."),
  ("Office refused", ["Only FWR or SPV actors can originate this lifecycle transaction from the field"], "Only a field worker or supervisor can start work in the field.", "Tell your supervisor. A manager issues the work instead."),
  ("Office refused", ["Inspection instruction is required"], "The office instruction was issued with no words.", "Tell your supervisor: the instruction must be issued again."),
  ("On the phone", ["Offline", "You are offline. Use SAVE to keep this INSP execution form locally, then submit when online."], "No signal.", "Press SAVE. Submit when you have signal."),
  ("After submit", ["Saved on this phone, not sent", "You are offline, so the inspection was NOT sent. It is saved on this phone. When you are online, open it from Admin → Offline Submission Forms and press SUBMIT.", "The network was too slow, so the inspection was NOT sent."], "The inspection is on the phone only. It does not send itself. If your finding called for work, the window adds: the disconnection cannot start until the inspection has been sent.", "When you have signal, open Admin → Offline Submission Forms and press SUBMIT. Then do the disconnection or removal."),
  ("On the phone", ["Offline: nothing was sent", "You are offline. Press SAVE to keep this inspection on the phone, then submit it when you are online."], "You pressed SUBMIT with no signal.", "Press SAVE, then send it from Admin → Offline Submission Forms when you are online."),
  ("Office refused", ["Submission Failed", "Meter inspection submission failed."], "Something went wrong with no better message.", "Try once more. If it fails again, report it with the meter number and the time."),
  ("Office refused", ["inspection payload is required", "TRN id is required", "accessData is required", "assignment.instruction.code is required"], "The phone sent something the office did not expect, usually from an old app.", "Close the app and open it again to update it. Then report it with a screenshot."),
]

DISC_ERRORS_LIST = [
  ("On the phone", ["Not Eligible", "Only CONNECTED meters can be disconnected.", "Meter Not Eligible For Disconnection"], "You started the disconnection yourself on a meter iREPS does not hold as Connected. A disconnection that follows a finding is accepted on a meter recorded as Disconnected; one you start with DISC is not.", "Inspect it first (INSP), record what you found, and tick Disconnect meter. The disconnection then opens by itself."),
  ("Office refused", ["Only CONNECTED meters can be disconnected"], "The same, from the office.", "As above: inspect first, and let the disconnection open from the finding."),
  ("Before submit", ["Disconnection instruction is required"], "You started the disconnection yourself and picked no instruction.", "Pick one: Credit Control Instruction, Illegal Connection or Non Payment."),
  ("Before submit", ["Disconnection level is required", "Valid disconnection level is required"], "No level chosen.", "Choose the level you did."),
  ("Before submit", ["Disconnection level evidence required", "Disconnection level evidence media is required"], "No photo of the level.", "Photograph the level you did."),
  ("Before submit", ["No-access reason is required", "No access photo is required"], "NO ACCESS without a reason or a photo.", "Pick the reason and take the photo."),
  ("Office refused", ["Disconnection instruction is required", "assignment.instruction.text is required"], "The instruction did not reach the office, or an office instruction was issued with no words.", "If you started it yourself, pick the instruction. If the office issued it, tell your supervisor."),
  ("On the phone", ["Missing DCN Instruction", "DCN execution must be opened from an accepted WMS instruction."], "The form was opened without an instruction or a meter.", "Open it from My Work Orders (office channel), or open the meter and press DISC (field channel)."),
  ("On the phone", ["Offline: nothing was sent", "You are offline. Press SAVE to keep this disconnection on the phone, then submit it when you are online."], "You pressed SUBMIT with no signal.", "Press SAVE, then send it from Admin → Offline Submission Forms when you are online."),
  ("After submit", ["Saved on this phone, not sent", "The network was too slow, so the disconnection was NOT sent. It is saved on this phone. Open it from Admin → Offline Submission Forms and press SUBMIT again."], "The office did not answer in time. On the record the meter is not disconnected yet, and the form does not send itself.", "Open Admin → Offline Submission Forms and press SUBMIT. Do not do a second disconnection."),
  ("After SAVE", ["Saved on this phone", "This disconnection is saved on this phone only. It has NOT been sent. To send it, open it from Admin → Offline Submission Forms and press SUBMIT."], "You pressed SAVE, so nothing went to the office.", "Send it from Admin → Offline Submission Forms before the end of the day."),
  ("On the phone", ["Draft Save Failed", "Failed to save disconnection draft locally."], "The phone could not store the form. Nothing is kept.", "Do not leave the form. Free space on the phone and try again."),
  ("Office refused", ["Only FWR or SPV actors can originate this lifecycle transaction from the field"], "Only a field worker or supervisor can start work in the field.", "Tell your supervisor."),
  ("Office refused", ["Submission Failed", "Meter disconnection submission failed."], "Something went wrong with no better message.", "Try once more. If it fails again, report it with the meter number and the time."),
  ("Office refused", ["assignment.targets must contain at least one USER, TEAM, or SP target", "TRN id is required", "ast.astData.astId is required"], "The phone sent something the office did not expect.", "Report it with a screenshot."),
]

INST_ERRORS = [
  ("Office refused", ["Duplicate Meter", "Meter already exists in AST collection"], "That meter number is already in iREPS.", "Check the number digit by digit. If it is right, report it: one meter cannot be in two places."),
  ("On the phone", ["Meter number may only contain letters and digits. Remove dashes, slashes, dots or other symbols."], "The number has a symbol in it.", "Type only the letters and digits. Keep noughts at the front."),
  ("On the phone", ["Saved as Draft", "This meter draft was saved locally. It can only be submitted after the parent premise has been successfully saved."], "The premise has not reached the office yet.", "Sync the premise first, then the meter."),
  ("On the phone", ["Saved Offline", "No internet connection. This submission was saved locally and will sync automatically when online."], "No signal. It goes by itself later.", "Carry on. Check the queue before the end of the day."),
  ("On the phone", ["Saved Locally", "The submission is taking too long. Your meter data has been safely saved locally and can be submitted again later."], "The office did not answer in time. The work is safe on the phone.", "Do not capture the meter again. It sends from the queue."),
  ("On the phone", ["Draft Save Failed", "Failed to save meter Installation draft locally."], "The phone could not store the form. Nothing is kept.", "Do not leave the form. Free space on the phone and try again."),
  ("Office refused", ["A valid saved premise id is required before meter installation can be submitted", "Parent premise does not exist in premises collection"], "The premise is not in the office system.", "Sync the premise. If it was deleted, make it again."),
  ("On the phone", ["Permission Denied", "Location is required for forensic evidence."], "iREPS is not allowed to use the phone's location.", "Allow location for iREPS in the phone's settings."),
  ("On the phone", ["Error", "Premise data not found."], "The form lost the premise.", "Open the premise again and start again."),
  ("Office refused", ["Meter number photo is required", "Anomaly photo is required", "Electricity meter placement is required", "Meter category must be Normal or Bulk", "Meter type must be prepaid or conventional", "Electricity meter phase must be single or three"], "A box or photo reached the office empty or wrong.", "Open the form again and fix the box named."),
  ("Office refused", ["Failed to submit meter installation transaction"], "Something went wrong with no better message.", "Try once more. If it fails again, report it with the meter number and the time."),
  ("After submit", ["Meter removed", "Meter removed. The new meter still needs to be installed: open Meter Installation at this premise."], "After a Replace meter removal, the installation could not open by itself.", "Open the premise, press Install, choose ELEC. Nothing is lost."),
]

DISCO_ERRORS = [
  ("Before submit", ["Say why the meter was not disconnected.", "Say why the meter was not replaced."], "The finding needs an action, and it is not ticked and has no reason.", "Tick the action, or pick the reason."),
  ("Before submit", ["Choose one: disconnect or replace."], "Both jobs are ticked.", "Untick one."),
  ("Before submit", ["None cannot be used with another action."], "None is ticked with work you did.", "Untick None."),
  ("Before submit", ["Type the reason."], "Other with nothing typed.", "Type the real reason."),
  ("Before submit", ["Photo proof of Normalisation required"], "A fix on the spot without a photo.", "Photograph what you fixed."),
  ("Office refused", ["The work was done, so there is no reason for not acting."], "The action is ticked and a reason is given too.", "Clear the reason."),
  ("Office refused", ["A reason for not acting belongs to a finding that needs action."], "Meter Ok with a reason.", "Clear the reason."),
  ("Office refused", ["This action is not on the list."], "An old word reached the office, usually from an app that was not updated.", "Close the app and open it again to update it."),
  ("On the phone", ["Meter saved, disconnection still to do", "The meter is not ready yet. Open the disconnection from the meter card on the ASTs screen."], "The meter took longer than 20 seconds to be ready. The meter is saved.", "Open the meter and press DISC."),
  ("On the phone", ["Saved Offline", "No internet connection. This meter was saved on the phone and will be sent when you are online. The disconnection cannot be started until it has been sent."], "No signal. The meter waits on the phone.", "Get signal. Once the meter has been sent, open it and press DISC."),
  ("For managers", ["Meter saved", "This meter still needs to be disconnected. Issue the disconnection to a field worker from the meter card (DISC)."], "A manager does not do field work.", "Issue the disconnection to a field worker."),
]

REM_ERRORS = [
  ("Before submit", ["Removal instruction is required"], "You started the removal yourself and picked no instruction.", "Pick one: Remove meter or Replace meter."),
  ("Before submit", ["The photo showing the meter is out is required"], "No photo of the removed meter. That photo is the confirmation.", "Photograph the meter out of the wall. If it is still in place, do not submit a removal: give the reason on the finding instead."),
  ("Before submit", ["The reading, or why it could not be captured, is required"], "Neither a reading nor a reason.", "Type the Remaining Credit (prepaid) or the Meter Reading (conventional), or pick why you could not read it."),
  ("Before submit", ["Remaining credit photo is required", "Removal meter reading evidence required"], "You typed a reading but did not photograph it.", "Photograph the display showing what you typed."),
  ("Before submit", ["No-access reason is required", "No access photo is required"], "NO ACCESS without a reason or a photo.", "Pick the reason and take the photo."),
  ("Office refused", ["Remaining credit, or why it could not be captured, is required", "Meter reading or no-reading reason is required"], "The reading reached the office empty with no reason.", "Open the form again, type the reading or pick why."),
  ("Office refused", ["Meter reading must be numeric", "Token reading must be numeric"], "The reading is not a number.", "Digits only, with a decimal point if you need one."),
  ("Office refused", ["Prepaid meters must use token reading, not meter reading", "Conventional meters must use meter reading, not token reading"], "The wrong kind of reading was sent for this meter.", "Report it with the meter number: the meter record may say the wrong kind."),
    ("On the phone", ["Meter Not Eligible For Removal", "Only FIELD, CONNECTED, or DISCONNECTED meters can be removed."], "The meter is in a state that cannot be removed. REM is only offered on a meter that is still there, so you see this only when the record changed while you were working.", "Sync the phone and open the meter again. If it still refuses, tell your supervisor with the meter number."),
  ("On the phone", ["Missing REMOVAL Instruction", "REMOVAL execution must be opened from an accepted WMS instruction."], "The form was opened without an instruction or a meter.", "Open it from My Work Orders (office channel), or open the meter and press REM (field channel)."),
  ("After submit", ["Meter removed", "Meter removed. The new meter still needs to be installed: open Meter Installation at this premise."], "The removal went through, but the installation could not open by itself.", "Open the premise, press Install and choose ELEC. Nothing is lost."),
  ("On the phone", ["Offline: nothing was sent", "You are offline. Press SAVE to keep this removal on the phone, then submit it when you are online."], "You pressed SUBMIT with no signal.", "Press SAVE, then send it from Admin → Offline Submission Forms when you are online."),
  ("After submit", ["Saved on this phone, not sent", "The network was too slow, so the removal was NOT sent. It is saved on this phone. Open it from Admin → Offline Submission Forms and press SUBMIT again. The new meter cannot be installed until the removal has been sent."], "The removal is on the phone only and does not send itself.", "Open Admin → Offline Submission Forms and press SUBMIT. The new meter waits until it has gone."),
  ("After SAVE", ["Saved on this phone", "This removal is saved on this phone only. It has NOT been sent. To send it, open it from Admin → Offline Submission Forms and press SUBMIT."], "You pressed SAVE, so nothing went to the office.", "Send it from Admin → Offline Submission Forms before the end of the day."),
  ("On the phone", ["Draft Save Failed", "Failed to save removal draft locally."], "The phone could not store the form. Nothing is kept.", "Do not leave the form. Free space on the phone and try again."),
  ("Office refused", ["Only FWR or SPV actors can originate this lifecycle transaction from the field"], "Only a field worker or supervisor can start work in the field.", "Tell your supervisor. A manager issues the removal instead."),
  ("For managers", ["Inspection sent", "This meter still needs to be replaced. Issue the removal to a field worker from the meter card (REM)."], "A manager does not do field work.", "Issue the removal to a field worker."),
  ("Office refused", ["Submission Failed", "Meter removal submission failed."], "Something went wrong with no better message.", "Try once more. If it fails again, report it with the meter number and the time."),
]

RECON_ERRORS = [
  ("Before submit", ["The photo showing the supply is back on is required"], "No photo of the reconnected supply. That photo is the confirmation.", "Photograph the supply back on and safe, then submit."),
  ("Gone", ["Supply reconnected answer is required", "Supply must be confirmed as reconnected before submit"], "These two can no longer happen: the Yes/No question is gone.", "Nothing to do. If you ever see them, the phone is running an old app: close it and open it again."),
]

ERR_FORMS = [
  ("Meter Inspection", INSP_ERRORS, False, ""),
  ("Disconnection", DISC_ERRORS_LIST, False, ""),
  ("Meter Installation", INST_ERRORS, False, ""),
  ("Meter Reconnection", RECON_ERRORS, False, ""),
  ("Meter Discovery · normalisation", DISCO_ERRORS, False, 'Every other Meter Discovery message is on <a href="%s">the Meter Discovery errors page</a>.' % DISC_ERRORS),
  ("Meter Removal", REM_ERRORS, False, ""),
]

def errors_html():
    out = ['<section class="part" id="errors">',
           '    <h2>When the app refuses your work</h2>',
           '    <p class="sub">Find the message by its first few words. Each one says what it means and what to do. <b>Refused means nothing was saved:</b> fix it and submit again.</p>',
           '    <div class="filter"><input id="q" type="search" placeholder="Type the first words of the message" aria-label="Search the messages"><span class="count" id="count"></span></div>']
    for name, rows, coming, note in ERR_FORMS:
        title = e(name) + (" " + COMING if coming else "")
        parts = [f'<details class="form"><summary><span>{title}<small>{len(rows)} messages</small></span></summary><div class="inner">']
        if note:
            parts.append(f'<p class="how">{note}</p>')
        for kind, msgs, means, do in rows:
            q = "".join(f"<q>{e(m)}</q>" for m in msgs)
            parts.append(f'<div class="err-entry"><span class="kind">{e(kind)}</span>{q}<p>{e(means)}</p><p class="do">{e(do)}</p></div>')
        parts.append('</div></details>')
        out.append("".join(parts))
    out.append('  </section>')
    return "\n".join(out)

FOOT = ('Written from the app\'s own code on 22 and 23 September 2026, for the release of Sunday 27 September '
        '(rules MN-R001 1.4.0 and UI-R003 1.4.0). Meter Discovery has its own pages: '
        f'<a href="{DISC_FIELDS}">fields</a> · <a href="{DISC_RULES}">rules</a> · <a href="{DISC_ERRORS}">errors</a>. '
        'A message that is not here? Send a screenshot to the office and it gets added.')

page = TPL.read_text(encoding="utf-8")
page = page.replace("<!--NEW-->", news_html())
page = page.replace("<!--FIELDS-->", fields_html())
page = page.replace("<!--ERRORS-->", errors_html())
page = page.replace("<!--FOOT-->", FOOT)
page = page.replace("/*FLOWS*/", (SCR / "field-guide-flows.js").read_text(encoding="utf-8"))
assert "<!--" not in page.replace("<!-- ", ""), "marker left"
PAGE.write_text(page, encoding="utf-8")
print("written", len(page), "bytes")
