> **Academy status:** Imported draft; release verification required. Imported 2026-09-23. Source: `SRC-009` in the [source register](../../00-academy-governance/SOURCE_REGISTER.csv). [Owner decisions](../../00-academy-governance/OWNER_DECISIONS.md) take precedence over conflicting inherited statements.

# Form: Change a sign-in email

| | |
| --- | --- |
| Screens | Your own: **Account Settings** → Email → CHANGE (`app/(tabs)/admin/user/user-settings.js`). Somebody else's: **Users** → the person → SIGN-IN EMAIL → CHANGE EMAIL (`app/(tabs)/admin/users/[uid].js`) |
| Back end | Your own: Firebase's own link. Somebody else's: `changeUserEmail`. Both: `syncSignInEmail` |
| Rules | `AU-R001` sections 6, 7.5, 7.6 and 11 |

## One email per person

The email you sign in with **is** your email in iREPS. There is no second one to edit.

Before 22 September 2026, Account Settings let you type a new email and save it. That changed only what iREPS showed — you still had to sign in with the old one. That is how somebody could end up signing in as `…@gmail.comm` while iREPS said `…@gmail.com`. That edit is gone.

If the two ever differ, the sign-in email wins: when you open the app, iREPS puts your sign-in email back on your record.

## Changing your own

1. Account Settings → **Email** → CHANGE.
2. Type the new email, and your password, and tap **SEND LINK**. The password proves it is you; Firebase will not send the link without it.
3. **A confirmation window** shows the old and the new email.
4. **Progress** while the link is sent.
5. **A result window**: check your new inbox.

**Nothing changes until you open that link** in the new inbox. Until then, keep signing in with the old email. So a typo in the new email cannot lock you out — the link goes nowhere, and your old email still works.

Once you open the link, your sign-in email is the new one and you are signed out. Sign in with the new email and the same password.

## Changing somebody else's

For somebody who cannot get email at the address they have — a typo, or a mailbox that is closed. Unlike your own, **it changes at once**, with no link.

| You are | You may change |
| --- | --- |
| SPU | Anybody's |
| Admin | Anybody's but the SPU's |
| Manager | Field workers and supervisors of your own service providers |

You never change your own this way — use Account Settings.

1. Users → the person → **CHANGE EMAIL**.
2. Type their new email and tap **Change**.
3. **A confirmation window** names the person and the new email.
4. **Progress** while it changes.
5. **A result window** shows the old and the new email, taken from iREPS itself.

Their password, role, authorisation and workbase do not change. If iREPS is open on their phone they are signed out at that moment. Tell them to sign in with the new email and their usual password.

The screen shows **Email on their record**, which can be out of date. iREPS changes the real sign-in email whatever the record says, and the result window names the real old one.

## Every change is kept

Each change is written down beside the person: the old and new sign-in email, the email their record held before, who made the change and when. When iREPS puts somebody's sign-in email back on their record, the address it replaces is kept there too, so nothing typed into the old Account Settings is lost.

## Error Register — your own

| What you see | What happened | What to do |
| --- | --- | --- |
| **Check your new inbox** — "We sent a link to the new email. Your sign-in email changes when you open it. Until then, keep signing in with the old one. Once it changes you will be signed out: sign in with the new email and the same password." | The link went out | Open it in the new inbox |
| **Password not right** — "Type the password you sign in with." | The password you typed is wrong | Type it again |
| **Nothing to change** — "That is already your sign-in email." | You typed the email you already have | Nothing |
| **Check the email** — "That does not look like an email address." | Mistyped, for example no @ | Correct it |
| **Email already used** — "Another iREPS account uses that email. Choose another." | Somebody already signs in with it. Where Firebase keeps that private you see Check your new inbox instead, and no link arrives | Choose another |
| **Sign in again** — "For your safety, iREPS needs a fresh sign-in before you change your email." | You have been signed in a long time | Sign out, sign in, try again |
| **Too many tries** — "Wait a few minutes and try again." | Too many requests from this phone | Wait |
| **No connection** — "Check your signal and try again." | No signal | Move to signal |
| **Email not changed** — "Try again, and tell your manager if it keeps happening." | Something else | Try again, then report |

## Error Register — somebody else's

| What you see | What happened | What to do |
| --- | --- | --- |
| **Email changed** — "They now sign in as NEW instead of OLD, with the same password as before. If iREPS is open on their phone they are signed out, and sign in again with the new email." | It changed | Tell them |
| The same, plus "Their record still shows the old email; it catches up the next time they open the app." | It changed, but the record did not follow straight away | Nothing — it catches up |
| **Nothing to change** — "That is already their sign-in email." | It already was | Nothing |
| **Check the email** — "That does not look like an email address." | Mistyped | Correct it |
| **Email already used** — "Another iREPS account uses that email." | Somebody else signs in with it | Find out who |
| **Not yours to change** — "You may only change the email of people you manage." | Not one of your people | Ask an admin |
| **Use Account Settings** — "Change your own email from Account Settings." | It is your own account | Use Account Settings |
| **No connection** — "Check your signal and try again." | No signal | Move to signal |
| **Email not changed** — the reason iREPS gave, or "Try again, and tell your manager if it keeps happening." | Something else | Try again, then report |

## What it does not do

- It does not change a password. That is Lost access? or Change password.
- It does not tell the person. You tell them.
- It is not on the web console yet.
