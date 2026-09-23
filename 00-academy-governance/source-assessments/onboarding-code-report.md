> **Academy status:** Historical source; not current user instructions. Imported 2026-09-23. Source: `SRC-001` in the [source register](../SOURCE_REGISTER.csv). [Owner decisions](../OWNER_DECISIONS.md) take precedence over conflicting inherited statements.

# iREPS Role Onboarding Code Report

## 1. Executive Summary

Onboarding in iREPS is managed differently between iREPS Mobile and iREPS Web.

**iREPS Mobile** has a dedicated onboarding state machine with multiple screens (`/onboarding/*`) for password change, workbase selection, email/phone verification, profile completion, and waiting states. The gate logic lives in `app/_layout.js` (`AuthGate` component) and is backed by a secondary guard in `src/navigation/onboardingGuard.js`.

**iREPS Web** has no dedicated onboarding screens. It uses a single `PendingApprovalPage` catch-all with no interactive onboarding. Users who are not fully onboarded are blocked at the route guard level (`ProtectedRoute`).

Onboarding status is stored in Firestore at `users/{uid}.onboarding.status` and `users/{uid}.onboarding.steps.*`. Users are created by cloud functions in `functions/index.js`, each setting a role-specific initial onboarding status.

There are two parallel guard implementations in mobile (`AuthGate` in `_layout.js` vs `onboardingGuard.js`) that do not fully agree, and the `confirm-appointment` route is referenced but has no corresponding screen file — this is a confirmed gap.

---

## 2. Key Files Inspected

### iREPS Mobile

| File | Purpose |
|---|---|
| `app/_layout.js` | Primary routing gate (`AuthGate`) — reads onboarding status and redirects |
| `app/onboarding/_layout.js` | Onboarding Stack layout — registers onboarding screen titles |
| `app/onboarding/change-password.js` | First-login password change screen |
| `app/onboarding/select-workbase.js` | Workbase/jurisdiction selection screen |
| `app/onboarding/complete-invited-profile.js` | Invited-user profile completion (password, cell, workbase) |
| `app/onboarding/confirm-admin.js` | Admin-specific profile completion (password, cell, workbase) |
| `app/onboarding/awaiting-mng-confirmation.js` | Waiting screen for FWR pending MNG approval |
| `app/onboarding/waiting-sp.js` | Waiting screen for service-provider assignment |
| `app/onboarding/waiting-workbase.js` | Waiting screen for workbase assignment |
| `app/onboarding/verify-email.js` | Email verification screen |
| `app/onboarding/verify-phone.js` | Phone verification screen (SMS code) |
| `src/navigation/onboardingGuard.js` | Alternative onboarding guard with `getOnboardingRoute()` |
| `src/hooks/useAuth.js` | Auth hook — exposes role, status, workbase |
| `src/redux/authApi.js` | Auth API slice — signup, signin, updateProfile, setActiveWorkbase mutations |
| `src/redux/usersApi.js` | Users API — real-time users list with role-based visibility |
| `app/(tabs)/admin/index.js` | Admin dashboard — shows role-gated admin cards |
| `app/(tabs)/admin/users/index.js` | Users list — filters by role, onboardingStatus, accountStatus |
| `app/(tabs)/admin/pendingUsers/index.js` | Pending authorizations — shows `AWAITING-MNG-CONFIRMATION` users |
| `app/(auth)/signup.jsx` | FWR self-signup form |
| `app/(auth)/signin.jsx` | Sign-in form |
| `app/(tabs)/_layout.js` | Tab layout — ERFs, Premises, TRNs, ASTs, Maps, Admin tabs |

### iREPS Web

| File | Purpose |
|---|---|
| `src/routes/AppRoutes.jsx` | Main route definitions with `RoleRoute` wrappers |
| `src/auth/ProtectedRoute.jsx` | Route guard — checks auth + onboarding complete |
| `src/auth/RoleRoute.jsx` | Role-based route guard — checks `allowedRoles` |
| `src/auth/AuthProvider.jsx` | Auth context provider — reads Firestore profile stream |
| `src/auth/AuthContext.js` | React context (minimal — just `createContext(null)`) |
| `src/auth/useAuth.js` | Auth hook — reads context, exposes role flags |
| `src/pages/LoginPage.jsx` | Login page — redirects to pending-approval if !onboardingComplete |
| `src/pages/PendingApprovalPage.jsx` | Catch-all for incomplete onboarding — shows status info, no actions |

### Cloud Functions (shared backend)

| File | Purpose |
|---|---|
| `functions/index.js` (lines 660–739) | `createAdminUser` — SPU-only, creates ADM with `PENDING` |
| `functions/index.js` (lines 2000–2160) | `inviteManagerUser` — SPU/ADM, creates MNG with `PENDING`, `mustChangePassword` |
| `functions/index.js` (lines 2199–2398) | `inviteSupervisorUser` — MNG-only, creates SPV with `PENDING`, `mustChangePassword` |
| `functions/index.js` (lines 2420–2479) | `inviteAdminUser` — SPU-only, creates ADM with `AWAITING_INITIAL_SIGNUP` |
| `functions/index.js` (lines 2551–2769) | `signupFieldWorker` — guest, creates FWR with `AWAITING-MNG-CONFIRMATION` |
| `functions/index.js` (lines 2770–2918) | `authorizeFieldWorker` — MNG-only, sets FWR to `WORKBASE_REQUIRED` |
| `functions/scripts/bootstrap_test_spu_from_export.js` | SPU seed script — validates SPU has `onboarding.status = "COMPLETED"` |

---

## 3. Role-by-Role Onboarding Report

---

### SPU — Superuser

- **Role identification:**
  - Firestore: `profile.employment.role === "SPU"` (`functions/scripts/bootstrap_test_spu_from_export.js`, line 185)
  - Custom claims: `{ role: "SPU" }` (same file, line 54)
  - Web: `AuthProvider.jsx`, line 11: `isSPU: role === "SPU"`
  - Mobile: `useAuth.js`, line 23: `isSPU: role === "SPU"`
  - Service provider: `employment.serviceProvider.id === "smarsId"`, `employment.serviceProvider.name === "Smars"` (bootstrap script, lines 192-199)

- **After login:**
  - Web: `ProtectedRoute.jsx` checks `isOnboardingComplete`. Since SPU has `onboarding.status === "COMPLETED"` from seed data, goes to `/dashboard`.
  - Mobile: `AuthGate` in `_layout.js` sees `status === "COMPLETED"` (line 117), redirects to `/(tabs)/erfs`.

- **First-time onboarding:** None. SPU is pre-seeded as fully onboarded.

- **Onboarding screens/steps:** Not applicable.

- **Required information:** SPU must already exist in Firebase Auth and Firestore. Seed script requires:
  - `uid` (hard-coded: `fXBACUfMzybcqC0AbeNeyYyTeRu1` in test env)
  - `email: "spu@smars.co.za"`
  - `role: "SPU"`
  - `onboarding.status: "COMPLETED"`
  - `accountStatus: "ACTIVE"`

- **User actions/buttons:** None during onboarding. Post-login: can access all admin tabs (`app/(tabs)/admin/index.js`, lines 58–183 — all sections visible to SPU).

- **Completion condition:** Pre-completed.

- **Storage/check location:** Firestore `users/{uid}.onboarding.status`. Web checks at `AuthProvider.jsx`, line 126-127. Mobile checks at `useAuth.js`, line 33.

- **Destination after onboarding:** Mobile: `/(tabs)/erfs`. Web: `/dashboard`.

- **Restrictions/guards:**
  - SPU can see all users (`users/index.js`, line 82: `if (isSPU || isADM) return users`)
  - SPU can see all pending authorizations (`pendingUsers/index.js`, line 73: `if (isSPU || isADM) return pendingPool`)
  - SPU can create ADM users (`createAdminUser` callable, line 665: `if (caller.token.role !== "SPU")`)
  - SPU can invite ADM users (`inviteAdminUser` callable)
  - SPU can invite MNG users (`inviteManagerUser` callable)
  - SPU has access to all admin cards (`admin/index.js`)

- **Confirmed files:**
  - `functions/scripts/bootstrap_test_spu_from_export.js`
  - `src/auth/AuthProvider.jsx` (web)
  - `src/hooks/useAuth.js` (mobile)
  - `app/_layout.js` (mobile)
  - `src/routes/AppRoutes.jsx` (web)

- **Gaps or unclear areas:**
  - SPU creation is manual/scripted — not confirmed in code how the production SPU is initially created (beyond the test bootstrap script).
  - The admin tab on mobile (`admin/index.js`, line 62) shows "Service Providers" to all roles including FWR, which contradicts the `12_admin_role_access.md` doc that says FWR has no admin access.

---

### ADM — Admin

- **Role identification:**
  - Firestore: `profile.employment.role === "ADM"`
  - Web: `AuthProvider.jsx`, line 12: `isADM: role === "ADM"`
  - Mobile: `useAuth.js`, line 24: `isADM: role === "ADM"`
  - Two creation paths exist with different initial states (see below)

- **After login:**
  - **Path A** (`createAdminUser`): Created with `onboarding.status = "PENDING"`, no workbases, no `mustChangePassword`. Web: goes to `PendingApprovalPage`. Mobile: AuthGate sees `PENDING`, then checks `mustChangePassword` (false) and `activeWorkbase` (null) → redirects to `/onboarding/select-workbase`.
  - **Path B** (`inviteAdminUser`): Created with `onboarding.status = "AWAITING_INITIAL_SIGNUP"`, all workbases pre-loaded, `activeWorkbase` pre-set to first workbase, no `mustChangePassword`. This user's path is unclear — neither the old guard nor the new AuthGate explicitly handles `AWAITING_INITIAL_SIGNUP`.

- **First-time onboarding:**
  - Path A: On mobile, probably hits `select-workbase` since `activeWorkbase` is null.
  - Path B: `_layout.js` AuthGate has a `default: return` (line 122), meaning it falls through with no redirect. This is a gap.
  - `confirm-admin.js` exists for ADM profile finalization but is never directly routed to by the current AuthGate (which routes ADM/MNG to `confirm-appointment` — a non-existent screen).

- **Onboarding screens/steps:**
  - `confirm-admin.js` (exists but not registered in `onboarding/_layout.js` and AuthGate doesn't route there)
  - Expected flow based on `confirm-admin.js` code: password rotation → cell phone → workbase selection → finalize
  - `complete-invited-profile.js` (generic invited-user flow — also not directly routed by AuthGate)

- **Required information:**
  - New permanent password (min 6 characters)
  - Cell phone number (pre-filled from profile if available)
  - Active workbase selection

- **User actions/buttons:**
  - `confirm-admin.js`, line 239: "ACTIVATE GLOBAL COMMAND" button calls `handleFinalize`
  - `handleFinalize` (line 43): validates passwords match, re-authenticates with default "password", rotates to new password, updates profile with `onboarding.status = "COMPLETED"`, navigates to `/(tabs)/erfs`

- **Completion condition:**
  - `onboarding.status === "COMPLETED"` and `onboarding.steps.profileCompleted === true` (set in `handleFinalize`, line 87)
  - `access.activeWorkbase` set to selected workbase
  - `mustChangePassword` set to false (in `select-workbase.js`, line 43)

- **Storage/check location:**
  - Firestore `users/{uid}` document
  - Web: `AuthProvider.jsx`, line 126-127: `isOnboardingComplete = onboardingStatus === "COMPLETED"`
  - Mobile: `useAuth.js`, line 33: `status: profile?.onboarding?.status || "IDLE"`

- **Destination after onboarding:**
  - Mobile: `/(tabs)/erfs` (set in `confirm-admin.js`, line 103; `complete-invited-profile.js`, line 90; `select-workbase.js`, line 50)
  - Web: `/dashboard` (via `ProtectedRoute.jsx` redirection)

- **Restrictions/guards:**
  - Can see all users (same as SPU) — `users/index.js`, line 82
  - Can see all pending authorizations — `pendingUsers/index.js`, line 73
  - Can invite MNG — `inviteManagerUser`, line 2013: `callerRole !== "SPU" && callerRole !== "ADM"`
  - Cannot invite SPV (MNG only) — `inviteSupervisorUser`, line 2229: `callerRole !== "MNG"`
  - Cannot invite ADM (SPU only) — `inviteAdminUser`
  - Has access to Settings (mobile: `admin/index.js`, line 93)
  - On web: `AppRoutes.jsx` shows ADM in `ADMIN_ROLES = ["SPU", "ADM", "MNG"]`, `MANAGEMENT_ROLES` and `ALL_OPERATIONAL_ROLES`

- **Confirmed files:**
  - `functions/index.js` (lines 660-739 for `createAdminUser`, lines 2420-2479 for `inviteAdminUser`)
  - `app/onboarding/confirm-admin.js`
  - `app/onboarding/complete-invited-profile.js`
  - `app/onboarding/select-workbase.js`
  - `app/onboarding/change-password.js`
  - `app/_layout.js`
  - `src/routes/AppRoutes.jsx` (web)

- **Gaps or unclear areas:**
  - `createAdminUser` creates ADM with no workbases (`access.activeWorkbase: null`, line 706) — this user would be stuck in workbase selection on mobile but has no workbases to select.
  - `inviteAdminUser` creates ADM with status `AWAITING_INITIAL_SIGNUP` — this status is not handled by either `AuthGate` or `onboardingGuard.js`.
  - `confirm-appointment` route referenced in `_layout.js` (line 100) for MNG/ADM does not exist as a file.
  - `confirm-admin.js` exists but is never routed to by AuthGate.

---

### LMU — Local Municipality User

- **Role identification:** Not confirmed in code. No role code `LMU` found in any role detection logic, role flags, route guards, or cloud functions. The codebase defines roles as: `SPU`, `ADM`, `MNG`, `SPV`, `FWR`, `GST`.

- **After login:** Not applicable — role not found.

- **First-time onboarding:** Not applicable.

- **Onboarding screens/steps:** Not applicable.

- **Required information:** Not applicable.

- **User actions/buttons:** Not applicable.

- **Completion condition:** Not applicable.

- **Storage/check location:** Not applicable.

- **Destination after onboarding:** Not applicable.

- **Restrictions/guards:** Not applicable.

- **Confirmed files:** Searched all role-related files — no `LMU` reference found. `src/hooks/useAuth.js` (mobile) only defines `isSPU`, `isADM`, `isMNG`, `isSPV`, `isFWR`. `AuthProvider.jsx` (web) only defines those five. `functions/index.js` uses `SPU`, `ADM`, `MNG`, `SPV`, `FWR`. `src/docs/AUTH_FLOW.md` lists only: SPU, ADM, MNG, SPV, FWR, GST.

- **Gaps or unclear areas:**
  - If `LMU` is an intended role, it does not exist in the current codebase.
  - "LM" (Local Municipality) appears as a client type in service provider relationships (`clientType === "LM"` at `functions/index.js`, line 2049), but not as a user role.

---

### MNG — Manager

- **Role identification:**
  - Firestore: `profile.employment.role === "MNG"`
  - Web: `AuthProvider.jsx`, line 13: `isMNG: role === "MNG"`
  - Mobile: `useAuth.js`, line 25: `isMNG: role === "MNG"`
  - Created via `inviteManagerUser` callable (SPU/ADM only)

- **After login:**
  - Created with `onboarding.status = "PENDING"`, `onboarding.mustChangePassword = true`, `access.activeWorkbase = null`, pre-populated `access.workbases` inherited from SP clients.
  - Mobile: AuthGate sees `status === "PENDING"` and `mustChangePassword === true` → redirects to `/onboarding/change-password` (`_layout.js`, line 67-69).
  - After password change, `mustChangePassword` is set to false, status still `PENDING`, and `activeWorkbase` is null → AuthGate next check at line 85 redirects to `/onboarding/select-workbase`.
  - Web: `ProtectedRoute` sends to `PendingApprovalPage`.

- **First-time onboarding:**
  - Must change temporary password (default: `"password"`, set at `functions/index.js`, line 2093)
  - Must select active workbase

- **Onboarding screens/steps:**
  1. `change-password.js` — "FIRST LOGIN: MANDATORY PASSWORD CHANGE"
     - Validates: password non-empty, min 6 chars, passwords match
     - On success: updates `onboarding.mustChangePassword = false`, navigates to `/onboarding/select-workbase`
  2. `select-workbase.js` — displays inherited workbases as a list
     - User taps a workbase → sets `access.activeWorkbase`, sets `onboarding.status = "COMPLETED"`, navigates to `/(tabs)/erfs`

- **Required information:**
  - New password (min 6 characters)
  - Active workbase selection (from pre-assigned list)

- **User actions/buttons:**
  - `change-password.js`: "Save New Password" button calls `handleSave`
  - `select-workbase.js`: Tap on workbase list item → auto-saves and navigates

- **Completion condition:**
  - `onboarding.mustChangePassword === false`
  - `access.activeWorkbase` is set
  - `onboarding.status === "COMPLETED"`

- **Storage/check location:**
  - `change-password.js`, line ~115: updates Firestore `users/{uid}` with `onboarding.mustChangePassword: false`
  - `select-workbase.js`, lines 39-45: updates Firestore with `onboarding.status = "COMPLETED"` and `onboarding.mustChangePassword = false`

- **Destination after onboarding:**
  - Mobile: `/(tabs)/erfs`
  - Web: `/dashboard`

- **Restrictions/guards:**
  - Can invite SPV (`inviteSupervisorUser` callable, MNG-only)
  - Can authorize FWR (`authorizeFieldWorker` callable, MNG-only)
  - Can see own SP users + SUBC users (`users/index.js`, lines 109-112)
  - Can see pending authorizations filtered by own SP tree (`pendingUsers/index.js`, lines 77-82)
  - Has access to Pending Authorizations, Users, Operations, Reports (`admin/index.js`)
  - Cannot access Settings (`admin/index.js`, line 93: `{(isSPU || isADM) && (...)}`)
  - Web: `AppRoutes.jsx` puts MNG in `ADMIN_ROLES`, `MANAGEMENT_ROLES`, `MREAD_STAGING_CONTROLLER_ROLES`

- **Confirmed files:**
  - `functions/index.js` (lines 2000–2160: `inviteManagerUser`)
  - `app/onboarding/change-password.js`
  - `app/onboarding/select-workbase.js`
  - `app/_layout.js` (AuthGate)
  - `app/(tabs)/admin/index.js`
  - `app/(tabs)/admin/users/index.js`

- **Gaps or unclear areas:**
  - `complete-invited-profile.js` also exists and handles password + workbase in one screen, but AuthGate routes MNG through `change-password` → `select-workbase` as two separate screens instead.
  - `_layout.js` line 97-101 routes MNG to `/onboarding/confirm-appointment` when status is `AWAITING-MNG-CONFIRMATION` or `AWAITING-ADM-CONFIRMATION` and `isMNG || isADM`. But MNG is created with `PENDING`, not those statuses, so this path is unreachable for MNG in practice.

---

### SPV-MNC — Main Contractor Supervisor

- **Role identification:**
  - Firestore: `profile.employment.role === "SPV"`
  - No separate role code for SPV-MNC vs SPV-SUBC — distinction is derived from the service provider's client relationships.
  - SPV-MNC identified by: the user's SP is NOT a SUBC of another SP (i.e., it is an MNC).
  - In `users/index.js`, line 92-97: `viewerIsSubc = viewerSp?.clients?.some(client => client?.clientType === "SP" && client?.relationshipType === "SUBC")`. If the user's SP does NOT have a SUBC relationship as a client, the user is SPV-MNC.

- **After login:**
  - Created via `inviteSupervisorUser` (MNG only). Same initial state as MNG: `onboarding.status = "PENDING"`, `mustChangePassword = true`, `access.activeWorkbase = null`, pre-populated workbases from SP's LM clients.
  - Mobile onboarding flow: same as MNG — `change-password` → `select-workbase`.
  - Web: `PendingApprovalPage`.

- **First-time onboarding:** Same as MNG.

- **Onboarding screens/steps:** Same as MNG — password change then workbase selection.

- **Required information:** Same as MNG.

- **User actions/buttons:** Same as MNG.

- **Completion condition:** Same as MNG.

- **Storage/check location:** Same as MNG.

- **Destination after onboarding:** `/(tabs)/erfs` (mobile), `/dashboard` (web).

- **Restrictions/guards:**
  - Can see users from own SP + SUBCs (`users/index.js`, line 114-121: SPV-MNC logic mirrors MNG)
  - Cannot access Pending Authorizations (`admin/index.js`, line 87: `{(isSPU || isADM || isMNG) && (...)}`)
  - Can access Users list but not Pending Authorizations
  - Web: `AppRoutes.jsx` puts SPV in `ALL_OPERATIONAL_ROLES`, `MANAGEMENT_ROLES`, `MREAD_STAGING_CONTROLLER_ROLES`
  - Cannot invite anyone (no cloud function allows SPV to create users)

- **Confirmed files:**
  - `functions/index.js` (lines 2199–2398: `inviteSupervisorUser`)
  - `app/(tabs)/admin/users/index.js` (lines 114-121)
  - `app/(tabs)/admin/index.js`

- **Gaps or unclear areas:**
  - The MNC/SUBC distinction for SPV is only checked client-side in `users/index.js` for filtering visible users. The cloud function `inviteSupervisorUser` does not distinguish — any SPV is created with the same shape regardless of whether the service provider is MNC or SUBC.

---

### SPV-SUBC — Subcontractor Supervisor

- **Role identification:**
  - Same Firestore role: `profile.employment.role === "SPV"`
  - Distinguished by: the user's SP has a client relationship where `clientType === "SP"` and `relationshipType === "SUBC"` pointing to a parent SP (`users/index.js`, lines 92-97).

- **After login:** Same as SPV-MNC. No difference in onboarding flow.

- **First-time onboarding:** Same as SPV-MNC.

- **Onboarding screens/steps:** Same as SPV-MNC.

- **Required information:** Same.

- **User actions/buttons:** Same.

- **Completion condition:** Same.

- **Storage/check location:** Same.

- **Destination after onboarding:** Same.

- **Restrictions/guards:**
  - Key difference from SPV-MNC: can only see users from own SP (not SUBCs under them).
  - `users/index.js`, lines 118-120: `if (viewerIsSubc) { return userSpId === viewerSpId; }`
  - Same access restrictions for admin features as SPV-MNC otherwise.

- **Confirmed files:**
  - `app/(tabs)/admin/users/index.js` (lines 92-97, 118-120)

- **Gaps or unclear areas:**
  - No server-side enforcement of the SPV-MNC vs SPV-SUBC distinction for user visibility — it is purely client-side filtering.
  - The distinction is not documented in `src/docs/AUTH_FLOW.md` or `src/docs/12_admin_role_access.md`.

---

### FWR — Fieldworker

- **Role identification:**
  - Firestore: `profile.employment.role === "FWR"`
  - Web: `AuthProvider.jsx`, line 15: `isFWR: role === "FWR"`
  - Mobile: `useAuth.js`, line 27: `isFWR: role === "FWR"`
  - Self-registered via `signupFieldWorker` callable (no auth required)

- **After login (or after signup):**
  - Created with: `onboarding.status = "AWAITING-MNG-CONFIRMATION"`, `accountStatus = "PENDING"`, empty workbases, `mustChangePassword = false`.
  - Mobile: AuthGate sees `AWAITING-MNG-CONFIRMATION` → redirects to `/onboarding/awaiting-mng-confirmation` (`_layout.js`, lines 94-106).
  - Web: `PendingApprovalPage` shows account status info.

- **First-time onboarding:**
  1. Self-signup: fills in email, password, name, surname, service provider (`app/(auth)/signup.jsx`)
  2. Waits for MNG authorization (`awaiting-mng-confirmation.js`)
  3. After MNG authorizes: onboarding status changes to `WORKBASE_REQUIRED`, workbases are populated
  4. Selects workbase (`select-workbase.js`)

- **Onboarding screens/steps:**
  1. `signup.jsx` — Formik form with validation (name, surname, email, password min 8 chars, confirm password, service provider selection modal)
  2. `awaiting-mng-confirmation.js` — Passive waiting screen showing service provider name and approval status. Has "Sign Out" button and "Welcome Screen" button.
  3. `select-workbase.js` — After authorization, selects from inherited workbases.

- **Required information:**
  - Email, password (min 8 chars), name, surname, service provider selection (at signup)
  - Active workbase selection (after MNG authorization)
  - No password change needed (FWR sets their own password at signup, `mustChangePassword = false`)

- **User actions/buttons:**
  - `signup.jsx`: "Sign Up" button calls `signupGst` mutation
  - `awaiting-mng-confirmation.js`: "Sign Out" and "Welcome Screen" buttons
  - `select-workbase.js`: Tap workbase → auto-submit

- **Completion condition:**
  - MNG authorization: `authorizeFieldWorker` callable sets `accountStatus = "ACTIVE"`, `onboarding.status = "WORKBASE_REQUIRED"`, populates `access.workbases` (`functions/index.js`, lines 2894-2900)
  - Workbase selection: sets `onboarding.status = "COMPLETED"`, `access.activeWorkbase`

- **Storage/check location:**
  - Firestore: set at creation in `signupFieldWorker` (`functions/index.js`, lines 2712-2716)
  - Updated by `authorizeFieldWorker` (`functions/index.js`, line 2898)
  - Updated by `select-workbase.js` (line 41)

- **Destination after onboarding:**
  - Mobile: `/(tabs)/erfs`
  - Web: `/dashboard`

- **Restrictions/guards:**
  - Cannot see any other users (`users/index.js`, line 81: `if (isFWR) return []`)
  - Cannot access Pending Authorizations (gated at `admin/index.js`, line 87)
  - Has read-only access to ERFs, Premises, TRNs, ASTs, Maps tabs
  - Web: `AppRoutes.jsx` puts FWR in `ALL_OPERATIONAL_ROLES` only (not `MANAGEMENT_ROLES` or `ADMIN_ROLES`)
  - Can access Operations, Reports, Storage on mobile (`admin/index.js`, lines 109-181)

- **Confirmed files:**
  - `functions/index.js` (lines 2551–2769: `signupFieldWorker`, lines 2770–2918: `authorizeFieldWorker`)
  - `app/(auth)/signup.jsx`
  - `app/onboarding/awaiting-mng-confirmation.js`
  - `app/onboarding/select-workbase.js`
  - `app/_layout.js`
  - `app/(tabs)/admin/users/index.js` (line 81)
  - `app/(tabs)/admin/index.js` (line 87)

- **Gaps or unclear areas:**
  - `signupFieldWorker` sends no actual email to the responsible MNG (line 2735-2737: `// TODO: send email to responsibleMng.profile.email`). The MNG must manually check pending authorizations.
  - FWR signup password is min 8 chars (signup validation) but the onboarding password change screens require only 6 chars — inconsistency.

---

## 4. Shared Onboarding Logic

### Onboarding Status Field

All roles use `users/{uid}.onboarding.status` in Firestore as the single source of truth. Known status values:
- `"COMPLETED"` — fully onboarded
- `"PENDING"` — initial state for invited users (MNG, SPV, some ADM paths)
- `"AWAITING_INITIAL_SIGNUP"` — one ADM creation path
- `"AWAITING-MNG-CONFIRMATION"` — FWR after self-signup
- `"WORKBASE_REQUIRED"` — FWR after MNG authorization
- `"IDLE"` — default fallback (`useAuth.js`, line 33)

### Onboarding Steps Sub-Object

`onboardingGuard.js` (mobile) uses `profile.onboarding.steps`:
- `signupCompleted`
- `serviceProviderAssigned`
- `workbasesAssigned`
- `activeWorkbaseSelected`
- `emailVerified`
- `phoneVerified`
- `profileCompleted`

These steps are set in specific screens (`syncEmailVerified`, `verify-phone`, `complete-invited-profile`, `confirm-admin`) but the primary AuthGate in `_layout.js` does **not** use the steps object at all — it uses only `onboarding.status` and `onboarding.mustChangePassword`. This creates a parallel tracking system.

### Route Protection

**Web** (`ProtectedRoute.jsx`, lines 24-30):
1. Not authenticated → `/login`
2. Profile missing → `/pending-approval`
3. Onboarding not complete → `/pending-approval`
4. All pass → render children

**Mobile** (`_layout.js` AuthGate, lines 54-122):
1. Not authenticated → `/signin`
2. `mustChangePassword` + `PENDING` → `/onboarding/change-password`
3. No `activeWorkbase` → `/onboarding/select-workbase`
4. `AWAITING-MNG-CONFIRMATION` / `AWAITING-ADM-CONFIRMATION` → `/onboarding/awaiting-mng-confirmation` or `/onboarding/confirm-appointment` (for MNG/ADM)
5. `COMPLETED` → `/(tabs)/erfs`

### Workbase Concept

All operational roles (SPU, ADM, MNG, SPV, FWR) must have `access.activeWorkbase` set to complete onboarding. Workbases are inherited from service provider → LM client relationships.

### Onboarding Completion Trigger

On mobile, onboarding is marked complete in two places:
- `select-workbase.js`, line 41: `"onboarding.status": "COMPLETED"` (primary path for most roles)
- `complete-invited-profile.js`, line 84: `"onboarding.status": "COMPLETED"` (invited-user path)
- `confirm-admin.js`, line 83: `"onboarding.status": "COMPLETED"` (admin path)
- `setActiveWorkbase` mutation, line 318 (`authApi.js`): only sets if not already completed

---

## 5. Role Differences

| Aspect | SPU | ADM | MNG | SPV-MNC | SPV-SUBC | FWR |
|---|---|---|---|---|---|---|
| **Created by** | Manual/script | SPU | SPU/ADM | MNG | MNG | Self-signup |
| **Initial onboarding status** | `COMPLETED` | `PENDING` or `AWAITING_INITIAL_SIGNUP` | `PENDING` | `PENDING` | `PENDING` | `AWAITING-MNG-CONFIRMATION` |
| **Must change password** | No | Path-dependent | Yes | Yes | Yes | No (sets own) |
| **Workbases pre-assigned** | Yes | Path-dependent | Yes | Yes | Yes | Empty (assigned by MNG) |
| **Approval needed** | No | No | No | No | No | Yes (MNG) |
| **Can create users** | ADM, MNG | MNG | SPV | None | None | None |
| **Sees all users** | Yes | Yes | Own SP + SUBCs | Own SP + SUBCs | Own SP only | None |
| **Access to settings** | Yes | Yes | No | No | No | No |
| **Pending authorizations** | Yes | Yes | Yes (filtered) | No | No | No |

---

## 6. Public User Guide Notes

The following can safely be explained in the public iREPS User Guide:

1. **Login is email + password.** All users sign in the same way.

2. **First-time invited users (MNG, SPV, some ADM)** must change their temporary password and select an active municipality (workbase) on first login via the mobile app.

3. **Field workers (FWR)** self-register via the mobile app, then wait for a manager to approve their account. After approval, they select their workbase.

4. **Superusers (SPU) and some Admins (ADM)** are set up by the system administrator and may skip onboarding steps.

5. **The iREPS Web app** is a desktop console. It requires onboarding to be completed on mobile first — incomplete accounts see an "Account not ready yet" page.

6. **Onboarding statuses visible to managers:** PENDING, AWAITING-MNG-CONFIRMATION, WORKBASE_REQUIRED, COMPLETED. Managers can see and filter users by these statuses in the admin panel.

7. **Workbases** determine which municipal data a user can access. A manager or admin assigns workbases; the user selects their active one.

8. **Email and phone verification** screens exist in the mobile app but are not required for all roles in the current flow.

9. **Role hierarchy (high-level):** SPU (full access) → ADM (system admin) → MNG (manager, can invite SPV and approve FWR) → SPV (supervisor) → FWR (field worker). Each role has progressively narrower access.

---

## 7. Questions / Gaps

1. **`LMU` role does not exist in code.** No role code, no role flag, no route guard, no cloud function references `LMU`. If this is an intended role, it needs to be built.

2. **`confirm-appointment` route is referenced but has no screen file.** `app/_layout.js`, line 100 routes MNG/ADM with `AWAITING-*-CONFIRMATION` status to `/onboarding/confirm-appointment`, but no file exists at `app/onboarding/confirm-appointment.js`. This would cause a navigation error.

3. **Two parallel onboarding guards.** `onboardingGuard.js` uses a steps-based machine. `_layout.js` AuthGate uses a status-based machine. They disagree on routing logic, and it is not clear which one is canonical.

4. **`createAdminUser` creates ADM with no workbases.** The user would be stuck — they'd reach workbase selection but have an empty list.

5. **`AWAITING_INITIAL_SIGNUP` status has no handler.** The `inviteAdminUser` flow sets this status, but neither AuthGate nor onboardingGuard handles it — the user would fall through to default with no redirect.

6. **`confirm-admin.js` is never routed to.** The file exists and contains a full admin onboarding flow, but AuthGate routes MNG/ADM to `confirm-appointment` (missing) instead of `confirm-admin`.

7. **`complete-invited-profile.js` is never routed to by AuthGate.** It exists and overlaps with `confirm-admin.js` but neither guard targets it.

8. **`verify-email` and `verify-phone` screens exist but are unreachable in the current AuthGate.** The old `onboardingGuard.js` routes to them, but the active AuthGate never does.

9. **FWR signup password is min 8 chars** (signup validation) vs **invited-user password is min 6 chars** (onboarding screens). Inconsistency.

10. **No email sent to MNG when FWR signs up.** The code has a TODO comment at `functions/index.js`, lines 2735-2737. MNG must manually check the Pending Authorizations screen.

11. **SPV-MNC vs SPV-SUBC distinction is client-side only.** The server has no enforcement. A SPV-SUBC could potentially see other SP users if they bypassed the client filter.

12. **Web has no onboarding UI at all.** Users with incomplete onboarding see a static page with no ability to change password, select workbase, or verify contact details. All onboarding actions require the mobile app.

13. **Onboarding `_layout.js` does not register all onboarding screens.** It only explicitly registers `complete-invited-profile`, `awaiting-mng-confirmation`, `select-workbase`, `waiting-sp`, and `waiting-workbase`. Screens like `change-password`, `confirm-admin`, `verify-email`, and `verify-phone` rely on Expo Router's file-based auto-discovery — meaning they work but lack custom header titles.
