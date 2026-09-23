> **Academy status:** Historical source; not current user instructions. Imported 2026-09-23. Source: `SRC-002` in the [source register](../SOURCE_REGISTER.csv). [Owner decisions](../OWNER_DECISIONS.md) take precedence over conflicting inherited statements.

# iREPS Full Functionality by Role Code Report

## 1. Executive Summary

iREPS is an integrated electricity revenue protection and enforcement system with two client applications — **iREPS Web** (React SPA) and **iREPS Mobile** (React Native / Expo) — backed by Firebase (Firestore + Cloud Functions + Auth).

**Roles:** Five role codes exist: **SPU** (Superuser), **ADM** (Admin), **MNG** (Manager), **SPV** (Supervisor), and **FWR** (Fieldworker). There is no LMU role. The SPV-MNC vs SPV-SUBC distinction is **not a separate role code** — it is derived from the Service Provider relationship type (`MNC` = Main Contractor, `SUBC` = Subcontractor). An SPV whose service provider has `relationshipType === "MNC"` or `clientType === "MNC"` gets elevated backend authority alongside MNG.

**Web** uses `RoleRoute` guards with four role-group arrays: `ALL_OPERATIONAL_ROLES` (SPU/ADM/MNG/SPV/FWR), `MANAGEMENT_ROLES` (SPU/ADM/MNG/SPV), `ADMIN_ROLES` (SPU/ADM/MNG), and `MREAD_STAGING_CONTROLLER_ROLES` (SPU/MNG/SPV). The sidebar menu is also filtered by these groups. Web provides registries, reports, operations dashboards, ward-scope exploration, maps, and admin tools.

**Mobile** uses role-flag conditionals in UI (`isSPU`, `isADM`, `isMNG`, `isSPV`, `isFWR`). It provides seven tabs: ERFs, Premises, TRNs, ASTs (Meters), Maps, Admin. The Admin tab has cards gated by role. Mobile's core strength is fieldwork: meter discovery, inspection, disconnection, reconnection, removal, meter reading, commissioning, premise creation, and evidence capture.

**Backend** cloud functions enforce role checks at the function level — some check `auth.token.role`, others check the caller's Firestore user document for `employment.role`. Critical functions (BGO creation, lifecycle instruction creation, management) use a dual MNG-or-SPV(MNC) authority pattern.

---

## 2. Key Files Inspected

### 2.1 iREPS Web

| Purpose | File |
|---|---|
| App entry | `C:\dev\ireps-web\src\main.jsx` (line 1–28) |
| App shell | `C:\dev\ireps-web\src\App.jsx` (line 1–7) |
| **All routes** | `C:\dev\ireps-web\src\routes\AppRoutes.jsx` (lines 1–463) |
| **Sidebar menu** | `C:\dev\ireps-web\src\layouts\ConsoleLayout.jsx` (lines 1–584) |
| **Auth provider** (role source) | `C:\dev\ireps-web\src\auth\AuthProvider.jsx` (lines 1–154) |
| Auth context | `C:\dev\ireps-web\src\auth\AuthContext.js` |
| Role route guard | `C:\dev\ireps-web\src\auth\RoleRoute.jsx` |
| Protected route guard | `C:\dev\ireps-web\src\auth\ProtectedRoute.jsx` |
| Auth hook | `C:\dev\ireps-web\src\auth\useAuth.js` |
| Login page | `C:\dev\ireps-web\src\pages\LoginPage.jsx` |
| Pending approval page | `C:\dev\ireps-web\src\pages\PendingApprovalPage.jsx` |
| Access denied page | `C:\dev\ireps-web\src\pages\AccessDeniedPage.jsx` |
| Dashboard page | `C:\dev\ireps-web\src\pages\DashboardPage.jsx` |
| Profile page | `C:\dev\ireps-web\src\pages\profile\ProfilePage.jsx` |
| Coming soon placeholder | `C:\dev\ireps-web\src\pages\ComingSoonPage.jsx` |
| Ward-scope: Map | `C:\dev\ireps-web\src\pages\maps\MapPage.jsx` |
| Ward-scope: ERFs | `C:\dev\ireps-web\src\pages\ward-scope\ErfsPage.jsx` |
| Ward-scope: Premises | `C:\dev\ireps-web\src\pages\ward-scope\PremisesPage.jsx` |
| Ward-scope: Meters | `C:\dev\ireps-web\src\pages\ward-scope\MetersPage.jsx` |
| Registry landing | `C:\dev\ireps-web\src\pages\registries\RegistryLandingPage.jsx` |
| Ward registry | `C:\dev\ireps-web\src\pages\registries\WardsRegistryPage.jsx` |
| ERF registry | `C:\dev\ireps-web\src\pages\registries\ErfsRegistryPage.jsx` |
| Premise registry | `C:\dev\ireps-web\src\pages\registries\PremisesRegistryPage.jsx` |
| Meter registry | `C:\dev\ireps-web\src\pages\registries\MetersRegistryPage.jsx` |
| MREAD registry | `C:\dev\ireps-web\src\pages\registries\MreadRegistryPage.jsx` |
| MREAD staging | `C:\dev\ireps-web\src\pages\registries\MreadStagingPage.jsx` |
| Account registry | `C:\dev\ireps-web\src\pages\registries\AccountsRegistryPage.jsx` |
| Reports landing | `C:\dev\ireps-web\src\pages\reports\ReportsLandingPage.jsx` |
| No Access report | `C:\dev\ireps-web\src\pages\reports\NoAccessReportPage.jsx` |
| User Activity report | `C:\dev\ireps-web\src\pages\reports\UserActivityReportPage.jsx` |
| Anomaly report | `C:\dev\ireps-web\src\pages\reports\AnomalyReportPage.jsx` |
| Normalisation report | `C:\dev\ireps-web\src\pages\reports\NormalisationReportPage.jsx` |
| Operations landing | `C:\dev\ireps-web\src\pages\operations\OperationsLandingPage.jsx` |
| TC Uploads | `C:\dev\ireps-web\src\pages\operations\TcUploadsPage.jsx` |
| TC Upload Details | `C:\dev\ireps-web\src\pages\operations\TcUploadDetailsPage.jsx` |
| TC BGO | `C:\dev\ireps-web\src\pages\operations\TcBgoPage.jsx` |
| TC Final Report | `C:\dev\ireps-web\src\pages\operations\TcFinalReportPage.jsx` |
| BGO Dashboard | `C:\dev\ireps-web\src\pages\operations\BgoDashboardPage.jsx` |
| BMD BGO | `C:\dev\ireps-web\src\pages\operations\BmdBgoPage.jsx` |
| MD BGO Rows | `C:\dev\ireps-web\src\pages\operations\MdBgoRowsPage.jsx` |
| TC BGO Dashboard | `C:\dev\ireps-web\src\pages\operations\TcBgoDashboardPage.jsx` |
| Geo-Fences page | `C:\dev\ireps-web\src\pages\operations\GeoFencesPage.jsx` |
| MREAD Staging Controller | `C:\dev\ireps-web\src\pages\admin\MreadStagingControllerPage.jsx` |
| Geo context | `C:\dev\ireps-web\src\context\GeoContext.jsx` |
| Warehouse context | `C:\dev\ireps-web\src\context\WarehouseContext.jsx` |
| Firebase init | `C:\dev\ireps-web\src\firebase\index.js` |
| Service providers API | `C:\dev\ireps-web\src\redux\serviceProvidersApi.js` |
| Users API | `C:\dev\ireps-web\src\redux\usersApi.js` |

### 2.2 iREPS Mobile

| Purpose | File |
|---|---|
| Root layout | `C:\dev\ireps-mobile\app\_layout.js` (lines 1–~160) |
| Entry screen | `C:\dev\ireps-mobile\app\index.js` |
| Tab layout (7 tabs) | `C:\dev\ireps-mobile\app\(tabs)\_layout.js` (lines 1–125) |
| Tab index (redirect) | `C:\dev\ireps-mobile\app\(tabs)\index.js` |
| Auth layout | `C:\dev\ireps-mobile\app\(auth)\_layout.js` |
| Sign in | `C:\dev\ireps-mobile\app\(auth)\signin.jsx` |
| Sign up | `C:\dev\ireps-mobile\app\(auth)\signup.jsx` |
| Onboarding layout | `C:\dev\ireps-mobile\app\onboarding\_layout.js` |
| Change password | `C:\dev\ireps-mobile\app\onboarding\change-password.js` |
| Select workbase | `C:\dev\ireps-mobile\app\onboarding\select-workbase.js` |
| Awaiting MNG confirmation | `C:\dev\ireps-mobile\app\onboarding\awaiting-mng-confirmation.js` |
| Confirm admin | `C:\dev\ireps-mobile\app\onboarding\confirm-admin.js` |
| Complete invited profile | `C:\dev\ireps-mobile\app\onboarding\complete-invited-profile.js` |
| Verify email | `C:\dev\ireps-mobile\app\onboarding\verify-email.js` |
| Verify phone | `C:\dev\ireps-mobile\app\onboarding\verify-phone.js` |
| Waiting SP | `C:\dev\ireps-mobile\app\onboarding\waiting-sp.js` |
| Waiting workbase | `C:\dev\ireps-mobile\app\onboarding\waiting-workbase.js` |
| ERFs tab (layout + index) | `C:\dev\ireps-mobile\app\(tabs)\erfs\_layout.js`, `index.js` |
| Ward-ERF sync | `C:\dev\ireps-mobile\app\(tabs)\erfs\ward-erfs-sync.js` |
| Premises tab | `C:\dev\ireps-mobile\app\(tabs)\premises\_layout.js`, `index.js` |
| Premise form | `C:\dev\ireps-mobile\app\(tabs)\premises\formPremise.js` |
| Premise Account Data form | `C:\dev\ireps-mobile\app\(tabs)\premises\formAccountData.js` |
| Premise meter installation form | `C:\dev\ireps-mobile\app\(tabs)\premises\form-meter-installation.js` |
| Premise media | `C:\dev\ireps-mobile\app\(tabs)\premises\premiseMedia.js` |
| NA screen | `C:\dev\ireps-mobile\app\(tabs)\premises\NaScreen.js` |
| TRNs tab | `C:\dev\ireps-mobile\app\(tabs)\trns\_layout.js`, `index.js` (~1667 lines) |
| ASTs/Meters tab (layout) | `C:\dev\ireps-mobile\app\(tabs)\asts\_layout.js` (lines 1–276) |
| ASTs list | `C:\dev\ireps-mobile\app\(tabs)\asts\index.js` |
| Meter inspection | `C:\dev\ireps-mobile\app\(tabs)\asts\inspection.js` (~150K) |
| Meter disconnection | `C:\dev\ireps-mobile\app\(tabs)\asts\disconnection.jsx` (~88K) |
| Meter reconnection | `C:\dev\ireps-mobile\app\(tabs)\asts\reconnection.jsx` (~86K) |
| Meter removal | `C:\dev\ireps-mobile\app\(tabs)\asts\removal.jsx` (~85K) |
| Meter reading | `C:\dev\ireps-mobile\app\(tabs)\asts\meter-reading.js` (~114K) |
| Meter commissioning | `C:\dev\ireps-mobile\app\(tabs)\asts\commissioning.jsx` (~50K) |
| Meter details | `C:\dev\ireps-mobile\app\(tabs)\asts\details.js` |
| Meter evidence/media | `C:\dev\ireps-mobile\app\(tabs)\asts\media.js` |
| Meter [id] hub | `C:\dev\ireps-mobile\app\(tabs)\asts\[id]\index.js` |
| Meter calendar | `C:\dev\ireps-mobile\app\(tabs)\asts\[id]\calendar.js` |
| Meter timeline | `C:\dev\ireps-mobile\app\(tabs)\asts\[id]\timeline.js` |
| Meter monthly revenue | `C:\dev\ireps-mobile\app\(tabs)\asts\[id]\monthly-revenue.js` |
| Maps tab | `C:\dev\ireps-mobile\app\(tabs)\maps\` |
| Admin tab (layout) | `C:\dev\ireps-mobile\app\(tabs)\admin\_layout.js` |
| Admin dashboard | `C:\dev\ireps-mobile\app\(tabs)\admin\index.js` (lines 1–185) |
| Admin: Service Providers | `C:\dev\ireps-mobile\app\(tabs)\admin\service-providers\` |
| Admin: User (single) | `C:\dev\ireps-mobile\app\(tabs)\admin\user\` |
| Admin: Users (list) | `C:\dev\ireps-mobile\app\(tabs)\admin\users\` |
| Admin: Pending | `C:\dev\ireps-mobile\app\(tabs)\admin\pendingUsers\index.js` |
| Admin: Settings | `C:\dev\ireps-mobile\app\(tabs)\admin\settings\` |
| Admin: Reports | `C:\dev\ireps-mobile\app\(tabs)\admin\reports\index.js` |
| Admin: Operations hub | `C:\dev\ireps-mobile\app\(tabs)\admin\operations\index.js` |
| Operations: My Workorders | `C:\dev\ireps-mobile\app\(tabs)\admin\operations\my-workorders.js` (~112K) |
| Operations: Teams | `C:\dev\ireps-mobile\app\(tabs)\admin\operations\teams.js` |
| Operations: Geo-Fences | `C:\dev\ireps-mobile\app\(tabs)\admin\operations\geo-fences.js` |
| Operations: Field Analytics | `C:\dev\ireps-mobile\app\(tabs)\admin\operations\field-analytics.js` |
| Operations: Revenue Analytics | `C:\dev\ireps-mobile\app\(tabs)\admin\operations\revenue-analytics.js` |
| Operations: Quality Assurance | `C:\dev\ireps-mobile\app\(tabs)\admin\operations\quality-assurance.js` |
| Operations: TRN Origin | `C:\dev\ireps-mobile\app\(tabs)\admin\operations\trn-origin.js` |
| Admin: Storage | `C:\dev\ireps-mobile\app\(tabs)\admin\storage\index.js` |
| Storage: Forms queue | `C:\dev\ireps-mobile\app\(tabs)\admin\storage\forms-submission-queue.js` |
| Storage: Sales sync | `C:\dev\ireps-mobile\app\(tabs)\admin\storage\sales-sync.js` |
| Storage: Premise offline | `C:\dev\ireps-mobile\app\(tabs)\admin\storage\premise-offline-storage.js` |
| Storage: Account queue | `C:\dev\ireps-mobile\app\(tabs)\admin\storage\account-data-submission-queue.js` |
| Auth hook | `C:\dev\ireps-mobile\src\hooks\useAuth.js` (lines 1–44) |
| Auth API (Redux) | `C:\dev\ireps-mobile\src\redux\authApi.js` (~19KB) |
| ERFs API | `C:\dev\ireps-mobile\src\redux\erfsApi.js` (~19KB) |
| Premises API | `C:\dev\ireps-mobile\src\redux\premisesApi.js` (~14KB) |
| TRNs API | `C:\dev\ireps-mobile\src\redux\trnsApi.js` (~20KB) |
| ASTs API | `C:\dev\ireps-mobile\src\redux\astsApi.js` (~11KB) |
| BGO API | `C:\dev\ireps-mobile\src\redux\bgoApi.js` (~23KB) |
| Sales API | `C:\dev\ireps-mobile\src\redux\salesApi.js` (~21KB) |
| Lifecycle Instruction API | `C:\dev\ireps-mobile\src\redux\lifecycleInstructionApi.js` (~28KB) |
| Geo API | `C:\dev\ireps-mobile\src\redux\geoApi.js` (~13KB) |
| SP API | `C:\dev\ireps-mobile\src\redux\spApi.js` (~8KB) |
| Teams API | `C:\dev\ireps-mobile\src\redux\teamsApi.js` (~7KB) |
| Users API | `C:\dev\ireps-mobile\src\redux\usersApi.js` (~4KB) |
| Account Data API | `C:\dev\ireps-mobile\src\redux\accountDataApi.js` (~6KB) |
| Geofence API | `C:\dev\ireps-mobile\src\redux\geofenceApi.js` (~3KB) |
| Settings API | `C:\dev\ireps-mobile\src\redux\settingsApi.js` (~2KB) |
| Lookup Options API | `C:\dev\ireps-mobile\src\redux\irepsLookupOptionsApi.js` |
| Select Lookups API | `C:\dev\ireps-mobile\src\redux\irepsSelectLookupsApi.js` (~7KB) |
| Offline slice | `C:\dev\ireps-mobile\src\redux\offlineSlice.js` |
| Warehouse context | `C:\dev\ireps-mobile\src\context\WarehouseContext.js` |
| Discovery context | `C:\dev\ireps-mobile\src\context\DiscoveryContext.js` |
| Geo context | `C:\dev\ireps-mobile\src\context\GeoContext.js` |
| Installation context | `C:\dev\ireps-mobile\src\context\InstallationContext.js` |
| Map context | `C:\dev\ireps-mobile\src\context\MapContext.js` |
| Navigation guards | `C:\dev\ireps-mobile\src\navigation\GuardedGate.js`, `GuardedStack.js`, `onboardingGuard.js`, `AuthBootstrap.js` |
| Meter Discovery form | `C:\dev\ireps-mobile\src\features\meters\FormMeterDiscovery.js` (~59K) |
| Meter Installation form | `C:\dev\ireps-mobile\src\features\meters\FormMeterIstallation.js` (~61K) |
| Water Meter Entry | `C:\dev\ireps-mobile\src\features\meters\WaterMeterEntry.js` |
| ERF screen | `C:\dev\ireps-mobile\src\features\erfs\erfsScreen.js` |
| User Helper | `C:\dev\ireps-mobile\src\features\userHelper.js` |

### 2.3 Backend / Functions

| Purpose | File |
|---|---|
| **Main functions index** (all exports) | `C:\dev\ireps-web\functions\index.js` (lines 1–4950) |
| BGO callables | `C:\dev\ireps-web\functions\bgo\callables.js` (lines 1–1289) |
| BGO acceptance callable | `C:\dev\ireps-web\functions\bgo\acceptanceCallable.js` |
| BGO delete callable | `C:\dev\ireps-web\functions\bgo\deleteCallable.js` |
| BGO helpers (authority resolution) | `C:\dev\ireps-web\functions\bgo\helpers.js` (lines 1–782) |
| TC Uploads callables | `C:\dev\ireps-web\functions\tcUploads\callables.js` |
| Commissioning callables | `C:\dev\ireps-web\functions\commissioning\callable.js` |
| Geofence callables | `C:\dev\ireps-web\functions\geofences\callables.js` |
| Teams callables | `C:\dev\ireps-web\functions\teams\callables.js` |
| Meter lifecycle callables | `C:\dev\ireps-web\functions\meterLifecycle\callables.js` |
| Meter lifecycle instruction callable | `C:\dev\ireps-web\functions\meterLifecycle\instructionCallable.js` |
| Meter lifecycle accept/reject | `C:\dev\ireps-web\functions\meterLifecycle\acceptRejectCallable.js` |
| Meter lifecycle manage | `C:\dev\ireps-web\functions\meterLifecycle\manageInstructionCallable.js` |
| Registry rebuilders | `C:\dev\ireps-web\functions\registry\*` |
| MREAD registry functions | `C:\dev\ireps-web\functions\registry\mread\index.js` |
| Lookups | `C:\dev\ireps-web\functions\lookups\index.js` |
| Data cleansing | `C:\dev\ireps-web\functions\dataCleansing\callables.js` |
| Reports triggers | `C:\dev\ireps-web\functions\reports\trnReports.js` |
| Firebase init (shared) | `C:\dev\src\firebase\index.js` |
| Firestore rules | `C:\dev\ireps-web\firestore.rules` (lines 1–10) |

---

## 3. Full Functionality Catalogue

### 3.1 Login / Sign In

- **Public meaning:** Email and password authentication for iREPS.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:** `LoginPage` (`C:\dev\ireps-web\src\pages\LoginPage.jsx`), `Signin` (`C:\dev\ireps-mobile\app\(auth)\signin.jsx`)
- **Related routes:** `/login` (Web)
- **Related backend functions:** Firebase Auth via SDK (no custom cloud function for sign-in)
- **Main user actions:** Enter email + password, sign in
- **Data involved:** Firebase Auth user; `users/{uid}` Firestore profile
- **Role access:** No role required (unauthenticated)
- **Confirmed files:** `LoginPage.jsx`, `signin.jsx`

### 3.2 Signup / Registration

- **Public meaning:** Self-registration for fieldworkers; invites for higher roles.
- **Web or Mobile or Both:** Mobile only
- **Main screen/page/component:** `Signup` (`C:\dev\ireps-mobile\app\(auth)\signup.jsx`)
- **Related routes:** `/(auth)/signup` (Mobile)
- **Related backend functions:** `signupFieldWorker` (`C:\dev\ireps-web\functions\index.js`, line 2551)
- **Main user actions:** Enter name, surname, email, password, select service provider
- **Data involved:** Firebase Auth user, `users/{uid}` doc with role=FWR, `accountStatus="PENDING"`
- **Role access:** No role required (unauthenticated → becomes FWR after MNG authorization)
- **Confirmed files:** `signup.jsx`, `index.js:2551`

### 3.3 Onboarding

- **Public meaning:** Step-by-step account setup after first login: change password, verify email, verify phone, select workbase, confirm admin appointment, await manager approval.
- **Web or Mobile or Both:** Mobile only
- **Main screens/components:** 10 onboarding screens in `C:\dev\ireps-mobile\app\onboarding\`:
  - `change-password.js` — force password change
  - `select-workbase.js` — pick LM/municipality
  - `awaiting-mng-confirmation.js` — pending approval status
  - `confirm-admin.js` — ADM/MNG self-confirm
  - `complete-invited-profile.js` — invited user profile completion
  - `verify-email.js` — email verification
  - `verify-phone.js` — phone verification
  - `waiting-sp.js` — wait for SP assignment
  - `waiting-workbase.js` — wait for workbase assignment
- **Related backend functions:** `updatePassword` (authApi), `setActiveWorkbase` (authApi), `updateProfile` (authApi)
- **Main user actions:** Complete each step sequentially
- **Data involved:** `users/{uid}` — `onboarding.steps`, `onboarding.status`, `access.workbases`, `access.activeWorkbase`
- **Role access:** All roles during first login
- **Confirmed files:** All 10 files in `onboarding/`

### 3.4 Workbase Selection

- **Public meaning:** Choose which Local Municipality (workbase) the user is currently operating in.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:** `SelectWorkbase` (`C:\dev\ireps-mobile\app\onboarding\select-workbase.js`), Web: workbase pill in topbar
- **Related routes:** None standalone; part of onboarding flow and ConsoleLayout
- **Related backend functions:** `setActiveWorkbase` mutation in authApi
- **Main user actions:** Select from available workbases
- **Data involved:** `users/{uid}.access.activeWorkbase`
- **Role access:** All roles
- **Confirmed files:** `select-workbase.js`, `AuthProvider.jsx` (lines 99–100), `authApi.js`

### 3.5 Dashboard

- **Public meaning:** Landing page after login showing role, workbase, and navigation.
- **Web or Mobile or Both:** Web
- **Main screen/page/component:** `DashboardPage` (`C:\dev\ireps-web\src\pages\DashboardPage.jsx`)
- **Related routes:** `/dashboard` (Web, default redirect from `/`)
- **Related backend functions:** None
- **Main user actions:** View role info, navigate to other sections
- **Data involved:** User profile (role, SP, workbase)
- **Role access:** ALL_OPERATIONAL_ROLES (SPU, ADM, MNG, SPV, FWR)
- **Confirmed files:** `DashboardPage.jsx`, `AppRoutes.jsx` (line ~66)

### 3.6 Admin Area

- **Public meaning:** Central hub for user management, service providers, teams, settings, and staging control.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:**
  - Web: `/admin` → `ComingSoonPage` with cards (Users, Teams, Settings) — `ADMIN_ROLES` only. Several specific routes exist under `/admin/*`
  - Mobile: `AdminDashboard` (`C:\dev\ireps-mobile\app\(tabs)\admin\index.js`) with role-gated cards
- **Related routes (Web):**
  - `/admin/service-providers` (ComingSoonPage, MANAGEMENT_ROLES)
  - `/admin/users` (ComingSoonPage, MANAGEMENT_ROLES)
  - `/admin/teams` (ComingSoonPage, MANAGEMENT_ROLES)
  - `/admin/mread-staging-controller` (MreadStagingControllerPage, MREAD_STAGING_CONTROLLER_ROLES)
  - `/admin/settings` (ComingSoonPage, ADMIN_ROLES)
- **Related backend functions:** `createAdminUser`, `inviteAdminUser`, `inviteManagerUser`, `inviteSupervisorUser`, `authorizeFieldWorker`, `createServiceProvider`, `updateServiceProvider`
- **Main user actions:** Varies by card
- **Data involved:** users, serviceProviders, teams, settings collections
- **Role access:** Web sidebar: ADMIN_ROLES for Admin landing, MANAGEMENT_ROLES for sub-pages. Mobile: varies by card (see matrix)
- **Confirmed files:** `admin/index.js` (mobile), `AppRoutes.jsx` (lines ~327–430)

### 3.7 User Management

- **Public meaning:** View, create, invite, and authorize users by role.
- **Web or Mobile or Both:** Mobile (primary), Web (Coming Soon)
- **Main screen/page/component:**
  - Mobile: `UserLookup` (`user/index.js`), `UsersList` (`users/index.js`), `PendingUsers` (`pendingUsers/index.js`)
  - Web: `/admin/users` → ComingSoonPage
- **Related routes:** `/(tabs)/admin/user`, `/(tabs)/admin/users`, `/admin/pendingUsers` (Mobile)
- **Related backend functions:**
  - `createAdminUser` — SPU only (line 652)
  - `inviteAdminUser` — SPU only (line 2407)
  - `inviteManagerUser` — SPU/ADM only (line 1973)
  - `inviteSupervisorUser` — MNG only (line 2178)
  - `signupFieldWorker` — unauthenticated (line 2551)
  - `authorizeFieldWorker` — MNG only (line 2763)
- **Main user actions:**
  - Single user lookup: all roles except GST
  - Users list: SPV and above
  - Pending authorizations: MNG and above (approve/reject FWR)
  - Create ADM: SPU only
  - Create MNG: SPU/ADM
  - Create SPV: MNG only
  - Authorize FWR: MNG only
- **Data involved:** `users/` collection, Firebase Auth
- **Role access:** See matrix
- **Confirmed files:** `admin/index.js` (lines 62–103), `index.js` lines 652–2862

### 3.8 Pending Authorisations

- **Public meaning:** Review and approve/reject newly registered fieldworkers awaiting manager confirmation.
- **Web or Mobile or Both:** Mobile only
- **Main screen/page/component:** `PendingUsers` (`C:\dev\ireps-mobile\app\(tabs)\admin\pendingUsers\index.js`)
- **Related routes:** `/admin/pendingUsers` (Mobile)
- **Related backend functions:** `authorizeFieldWorker` (line 2763)
- **Main user actions:** View pending FWR list, approve (authorize) or reject
- **Data involved:** `users/` collection — `accountStatus`, `onboarding.status`
- **Role access:** MNG and above (isSPU || isADM || isMNG) — confirmed in `admin/index.js` line 92
- **Confirmed files:** `admin/index.js` (line 92), `pendingUsers/index.js`

### 3.9 Service Provider Management

- **Public meaning:** View, create, and manage service providers (main contractors and subcontractors).
- **Web or Mobile or Both:** Mobile (primary), Web (Coming Soon)
- **Main screen/page/component:**
  - Mobile: `service-providers/`, `formCreateSp.js`
  - Web: `/admin/service-providers` → ComingSoonPage
- **Related routes:** `/(tabs)/admin/service-providers` (Mobile)
- **Related backend functions:**
  - `createServiceProvider` — SPU/ADM only (`index.js` line 435); enforced classification = "MNC"
  - `updateServiceProvider` — SPU/ADM for clients/status; broader for profile/offices (`spApi.js` lines 169–177)
- **Main user actions:** View SP list, view SP detail, create SP (SPU/ADM), edit SP profile
- **Data involved:** `serviceProviders/` collection — `profile`, `clients[]`, `ownership`, `workbases`, `offices`
- **Role access:**
  - View: all operational roles
  - Create: SPU/ADM only
  - Edit profile/offices: SPU/ADM/MNG/SPV
  - Edit clients/status: SPU/ADM only
- **Confirmed files:** `spApi.js` (lines 169–177), `index.js` lines 435–651

### 3.10 Workbase / Municipality Access

- **Public meaning:** Each user is assigned one or more Local Municipality workbases. The active workbase drives data scope.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:** `SelectWorkbase` (mobile onboarding), workbase pill in web topbar
- **Related routes:** None standalone
- **Related backend functions:** `setActiveWorkbase` in authApi; workbase inheritance in `inviteManagerUser`, `inviteSupervisorUser`
- **Main user actions:** Select active workbase; managers inherit workbases from SP's LM clients
- **Data involved:** `users/{uid}.access.workbases[]`, `.access.activeWorkbase`
- **Role access:** All roles
- **Confirmed files:** `AuthProvider.jsx` lines 99–100, `select-workbase.js`

### 3.11 ERFs / Cadastral Records

- **Public meaning:** View and manage cadastral ERF (erven) records within a ward.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:**
  - Web: `ErfsPage` (`ward-scope/ErfsPage.jsx`, route `/ward-scope/erfs`), `ErfsRegistryPage` (`registries/ErfsRegistryPage.jsx`, route `/registries/erfs`)
  - Mobile: `ErfsScreen` (`src/features/erfs/erfsScreen.js`), tab `/(tabs)/erfs`
- **Related routes:** `/ward-scope/erfs`, `/registries/erfs` (Web); `/(tabs)/erfs` (Mobile)
- **Related backend functions:** `rebuildErfPremiseCount`, `rebuildErfMeterCounts`, `rebuildErfTrnCount` (triggers)
- **Main user actions:** Browse ERFs, view ERF details, view linked premises/meters/TRNs
- **Data involved:** `ireps_erfs/` collection; ERF → Premise → Meter hierarchy
- **Role access:** Web: MANAGEMENT_ROLES; Mobile: all operational roles
- **Confirmed files:** `ErfsPage.jsx`, `ErfsRegistryPage.jsx`, `erfsScreen.js`

### 3.12 Maps

- **Public meaning:** Interactive map showing wards, ERFs, premises, meters, and geofences.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:**
  - Web: `MapPage` (`maps/MapPage.jsx`, route `/ward-scope/map`)
  - Mobile: Maps tab `/(tabs)/maps`
- **Related routes:** `/ward-scope/map`, `/maps` (redirects to `/ward-scope/maps`) (Web)
- **Related backend functions:** `createGeoFence`, `onGeoFenceCreated`
- **Main user actions:** View map, select ward/ERF/premise/meter, view geofences
- **Data involved:** Ward boundaries, ERF polygons, premise points, meter points, geofences
- **Role access:** MANAGEMENT_ROLES (Web); all operational roles (Mobile)
- **Confirmed files:** `MapPage.jsx`, maps tab directory

### 3.13 Premises

- **Public meaning:** View and manage premise records (properties with meters). Create new premises from the field.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:**
  - Web: `PremisesPage` (`ward-scope/PremisesPage.jsx`), `PremisesRegistryPage` (`registries/PremisesRegistryPage.jsx`)
  - Mobile: Premises tab `/(tabs)/premises`; `formPremise.js`, `formAccountData.js`, `NaScreen.js`
- **Related routes:** `/ward-scope/premises`, `/registries/premises` (Web); `/(tabs)/premises` (Mobile)
- **Related backend functions:** `onPremiseCreateCallable` (`index.js` line 4365), `onPremiseCreated`, `onPremiseUpdated` triggers
- **Main user actions:** Browse/filter premises, create premise, capture account data (FAD), record no-access, view premise media
- **Data involved:** `premises/` collection; `accounts/` collection
- **Role access:** Web: MANAGEMENT_ROLES; Mobile: all operational roles for viewing; FWR/SPV for creation
- **Confirmed files:** `PremisesPage.jsx`, `PremisesRegistryPage.jsx`, `premises/index.js`, `formPremise.js`

### 3.14 Meters (ASTs)

- **Public meaning:** View and manage asset status tracking (AST) for electricity meters. Full lifecycle operations.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:**
  - Web: `MetersPage` (`ward-scope/MetersPage.jsx`), `MetersRegistryPage` (`registries/MetersRegistryPage.jsx`)
  - Mobile: ASTs tab `/(tabs)/asts` with sub-screens: inspection, disconnection, reconnection, removal, meter-reading, commissioning, details, media, [id] hub, calendar, timeline, monthly revenue
- **Related routes:** `/ward-scope/meters`, `/registries/meters` (Web); `/(tabs)/asts/*` (Mobile)
- **Related backend functions:**
  - `onMeterDiscoveryCallable` (line 2934)
  - `onMeterInstallationCallable` (line 4590)
  - `onMeterLifecycleTrnCallable`
  - `onMeterCreated`, `onMeterUpdated` triggers
  - `onMeterDiscoveryCreated` trigger (line 1471)
  - `rebuildMeterRegistryRowCallable`
- **Main user actions:** (see Meter Lifecycle section below)
- **Data involved:** `asts/` collection, `meter_master/` collection, `trns/` collection
- **Role access:** Web: MANAGEMENT_ROLES for registry/ward-scope; Mobile: all roles for field lifecycle operations
- **Confirmed files:** All files in `asts/` directory and mobile features

### 3.15 Meter Lifecycle Operations

This is the core fieldwork of iREPS Mobile. Each is a separate screen:

| Operation | Mobile Screen | Backend Callable | Purpose |
|---|---|---|---|
| **Meter Discovery** | `FormMeterDiscovery.js` (59K) | `onMeterDiscoveryCallable` | Discover new meters in the field, capture meter no, type, reading, status |
| **Meter Installation** | `FormMeterIstallation.js` (61K) | `onMeterInstallationCallable` | Install a meter at a premise, create AST record |
| **Meter Inspection** | `inspection.js` (150K) | `onMeterLifecycleTrnCallable` | Inspect existing meter, record status, anomalies |
| **Meter Disconnection** | `disconnection.jsx` (88K) | `onMeterLifecycleTrnCallable` | Disconnect meter, record level, evidence |
| **Meter Reconnection** | `reconnection.jsx` (86K) | `onMeterLifecycleTrnCallable` | Reconnect previously disconnected meter |
| **Meter Removal** | `removal.jsx` (85K) | `onMeterLifecycleTrnCallable` | Remove meter from premise |
| **Meter Reading** | `meter-reading.js` (114K) | `onMeterLifecycleTrnCallable` | Capture meter reading and evidence |
| **Commissioning** | `commissioning.jsx` (50K) | `onCreateMeterCommissioningCallable` | Commission a newly installed meter |
| **Water Meter Entry** | `WaterMeterEntry.js` | N/A (local) | Water meter specific entry form |

- **Role access:** All operational roles on mobile can perform these operations in the field. WMS-issued instructions follow an accept/reject flow.
- **Confirmed files:** All files listed in ASTs directory

### 3.16 Transactions / TRNs

- **Public meaning:** View all field-generated transactions (discovery, installation, inspection, disconnection, reconnection, removal, reading, no-access).
- **Web or Mobile or Both:** Both
- **Main screen/page/component:**
  - Web: TRNs visible within ward-scope/meters and registries (no standalone TRN registry route discovered)
  - Mobile: TRNs tab `/(tabs)/trns` (~1667 lines)
- **Related routes:** `/(tabs)/trns` (Mobile)
- **Related backend functions:** `onTrnWritten` trigger (`reports/trnReports.js`)
- **Main user actions:** Browse/filter TRNs, view TRN detail, view media/evidence
- **Data involved:** `trns/` collection — all field operations create TRN documents
- **Role access:** Web: MANAGEMENT_ROLES (via registries); Mobile: all operational roles
- **Confirmed files:** `trns/index.js` (~1667 lines), `trnsApi.js` (~20KB)

### 3.17 MREAD Registry

- **Public meaning:** Meter reading registry — a structured view of meter reading data.
- **Web or Mobile or Both:** Web
- **Main screen/page/component:** `MreadRegistryPage` (`C:\dev\ireps-web\src\pages\registries\MreadRegistryPage.jsx`, ~134K)
- **Related routes:** `/registries/mread` (Web)
- **Related backend functions:** `rebuildRegistryMreadCallable`, `rebuildRegistryMreadRowCallable`
- **Main user actions:** Browse/filter MREAD records
- **Data involved:** MREAD registry collection
- **Role access:** MANAGEMENT_ROLES
- **Confirmed files:** `MreadRegistryPage.jsx`, `mread/index.js`

### 3.18 MREAD Staging

- **Public meaning:** Work-in-progress staging area for meter reading cycles before publication.
- **Web or Mobile or Both:** Web
- **Main screen/page/component:** `MreadStagingPage` (`C:\dev\ireps-web\src\pages\registries\MreadStagingPage.jsx`, ~86K)
- **Related routes:** `/registries/mread-staging` (Web)
- **Related backend functions:** `listMreadStagingCycles`, `listMreadStagingSessions`, `listMreadStagingRows`, `generateMreadStaging`
- **Main user actions:** Browse cycles, sessions, rows; generate staging data
- **Data involved:** MREAD staging collections
- **Role access:** MANAGEMENT_ROLES (view), MREAD_STAGING_CONTROLLER_ROLES (SPU/MNG/SPV) for controller
- **Confirmed files:** `MreadStagingPage.jsx`, `MreadStagingControllerPage.jsx`

### 3.19 Other Registries

All confirmed as Web registry pages:

- **Ward Registry:** `WardsRegistryPage.jsx` (25K), `/registries/wards`, MANAGEMENT_ROLES
- **ERF Registry:** `ErfsRegistryPage.jsx` (40K), `/registries/erfs`, MANAGEMENT_ROLES
- **Premise Registry:** `PremisesRegistryPage.jsx` (29K), `/registries/premises`, MANAGEMENT_ROLES
- **Meter Registry:** `MetersRegistryPage.jsx` (34K), `/registries/meters`, MANAGEMENT_ROLES
- **Account Registry:** `AccountsRegistryPage.jsx` (55K), `/registries/accounts`, MANAGEMENT_ROLES

All confirmed in `AppRoutes.jsx` lines 80–161.

### 3.20 Reports

- **Public meaning:** Operational and management reports for oversight.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:**
  - Web: `ReportsLandingPage`, `NoAccessReportPage`, `UserActivityReportPage`, `AnomalyReportPage`, `NormalisationReportPage`
  - Mobile: `reports/index.js` with cards for: Meter Registry, Premise Registry, ERF Registry, Ward Registry, Workbase Registry, Service Provider Registry, User Registry, No Access Report, User Activity Report, Normalisation Report, Anomaly Report, Prepaid Revenue Report, Prepaid Revenue Dashboard
- **Related routes (Web):** `/reports`, `/reports/no-access`, `/reports/user-activity`, `/reports/anomaly`, `/reports/normalisation`
- **Related routes (Mobile):** `/admin/reports/*`
- **Related backend functions:** `onTrnWritten` trigger for report data
- **Main user actions:** View reports, filter by date/ward/LM, export (not confirmed)
- **Data involved:** Registry collections, TRNs, sales data
- **Role access:** Web: MANAGEMENT_ROLES; Mobile: all operational roles (isSPU/isADM/isMNG/isSPV/isFWR)
- **Confirmed files:** All report page files, `reports/index.js` (lines 1–187)

### 3.21 TC Uploads

- **Public meaning:** Upload and manage TC (Token/Coin) meter data files.
- **Web or Mobile or Both:** Web
- **Main screen/page/component:** `TcUploadsPage`, `TcUploadDetailsPage`, `TcBgoPage`, `TcFinalReportPage`, `TcBgoDashboardPage`
- **Related routes:** `/operations/tc-uploads`, `/operations/tc-uploads/:tcId`, `/operations/tc-uploads/:tcId/bgo`, `/operations/tc-uploads/:tcId/bgo-dashboard`, `/operations/tc-uploads/:tcId/final-report`
- **Related backend functions:** `onUploadAndValidateTcCallable`, `onRefreshTcUploadGeofenceReadinessCallable`, `onDeleteTcUploadCallable`
- **Main user actions:** Upload TC data, validate, manage BGO linkage, view final reports
- **Data involved:** `tcUploads/` collection
- **Role access:** MANAGEMENT_ROLES
- **Confirmed files:** `TcUploadsPage.jsx`, `callables.js` (tcUploads)

### 3.22 BGO (Back Office Operations)

- **Public meaning:** Allocate TC upload rows as work batches (BGO) to field teams/individuals.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:**
  - Web: `BgoDashboardPage`, `BmdBgoPage`, `MdBgoRowsPage`
  - Mobile: Operations hub → My Workorders → accept/reject flows
- **Related routes:** `/operations/bgo-dashboard`, `/operations/bgo`, `/operations/md-bgo-rows` (Web); `/admin/operations/my-workorders` (Mobile)
- **Related backend functions:**
  - `onCreateBgoCallable` — MNG or SPV(MNC) only (`bgo/callables.js` line 735)
  - `onAcceptRejectBgoBatchCallable` — FWR or SPV assigned to batch only (`bgo/acceptanceCallable.js` line 714)
  - `onReverseBgoBatchAcceptanceCallable` — MNG or SPV(MNC) only (line 1147)
  - `onDeleteUnacceptedBgoCallable` — MNG or SPV(MNC) only (`bgo/deleteCallable.js` line 273)
- **Main user actions:**
  - Create BGO batches (MNG / SPV-MNC)
  - Accept/reject assigned BGO batches (FWR / SPV)
  - Reverse acceptance (MNG / SPV-MNC)
  - Delete unaccepted (MNG / SPV-MNC)
- **Data involved:** `bgo/` collections, TC rows, TRNs
- **Role access:** Create: MNG or SPV(MNC); Accept/Reject: assigned FWR or SPV
- **Confirmed files:** `bgo/callables.js`, `bgo/acceptanceCallable.js`, `bgo/helpers.js` (line 163)

### 3.23 WMS / Workorder Management

- **Public meaning:** Ward Management System — lifecycle instructions issued to field teams for meter operations.
- **Web or Mobile or Both:** Mobile (primary), Web (Coming Soon)
- **Main screen/page/component:**
  - Mobile: `my-workorders.js` (~112K) — accept, reject, execute assigned lifecycle instructions
  - Web: `/operations/wms-dashboard` → ComingSoonPage
- **Related routes:** `/admin/operations/my-workorders` (Mobile), `/operations/wms-dashboard` (Web)
- **Related backend functions:**
  - `onCreateMeterLifecycleInstructionCallable` — MNG or SPV(MNC) only (`instructionCallable.js` line 269)
  - `onAcceptRejectLifecycleInstructionCallable` — assigned FWR or SPV only (`acceptRejectCallable.js` line 346)
  - `onManageLifecycleInstructionCallable` — MNG or SPV(MNC) only (`manageInstructionCallable.js` line 483)
- **Main user actions:**
  - Create lifecycle instructions (MNG/SPV-MNC)
  - Accept/reject assigned instructions (FWR/SPV)
  - Execute: inspection, disconnection, reconnection, removal, meter reading
  - Reassign or cancel instructions (MNG/SPV-MNC)
- **Data involved:** `meterLifecycle/` collection, TRNs, ASTs
- **Role access:** Create: MNG or SPV(MNC); Execute: assigned FWR or SPV; Manage: MNG or SPV(MNC)
- **Confirmed files:** `my-workorders.js`, `instructionCallable.js`, `acceptRejectCallable.js`, `manageInstructionCallable.js`

### 3.24 Operations Hub

- **Public meaning:** Central hub for all operational management tools on mobile.
- **Web or Mobile or Both:** Mobile
- **Main screen/page/component:** `OperationsHub` (`C:\dev\ireps-mobile\app\(tabs)\admin\operations\index.js`)
- **Related routes:** `/admin/operations` (Mobile)
- **Main user actions:** Access WMS Dashboard, Operational Teams, My Workorders, Geo-Fencing, Field Analytics, Revenue Analytics, Quality Assurance
- **Data involved:** Various
- **Role access:** All operational roles
- **Confirmed files:** `operations/index.js` (lines 1–183)

### 3.25 Geo-Fences

- **Public meaning:** Define geospatial boundaries for work jurisdictions, used for work allocation and validation.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:**
  - Web: `GeoFencesPage` (`C:\dev\ireps-web\src\pages\operations\GeoFencesPage.jsx`)
  - Mobile: `geo-fences.js` (25K)
- **Related routes:** `/operations/geo-fences` (Web), `/admin/operations/geo-fences` (Mobile)
- **Related backend functions:** `createGeoFence` (`geofences/callables.js`), `onGeoFenceCreated` trigger
- **Main user actions:** Create geofence polygon, view geofence contents, manage members
- **Data involved:** `geofences/` collection
- **Role access:** Web: MANAGEMENT_ROLES; Mobile: all operational roles
- **Confirmed files:** `GeoFencesPage.jsx`, `geo-fences.js`

### 3.26 Teams

- **Public meaning:** Create and manage operational teams for work allocation.
- **Web or Mobile or Both:** Mobile (primary), Web (Coming Soon)
- **Main screen/page/component:** `teams.js` (29K) (`C:\dev\ireps-mobile\app\(tabs)\admin\operations\teams.js`)
- **Related routes:** `/admin/operations/teams` (Mobile), `/operations/teams` (Web → ComingSoon)
- **Related backend functions:** `createTeam`, `renameTeam`, `addTeamMember`, `removeTeamMember`, `deleteTeam` (`teams/callables.js`)
- **Main user actions:** Create team, add/remove members, rename, delete
- **Data involved:** `teams/` collection
- **Role access:** MANAGEMENT_ROLES
- **Confirmed files:** `teams.js`, `teams/callables.js`

### 3.27 Evidence / Media / Photos

- **Public meaning:** Capture and view photographic evidence for fieldwork operations.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:**
  - Mobile: `media.js` (ASTs), `premiseMedia.js` (Premises); media sections within each lifecycle form
  - Web: Media visible within TRN details and registry pages
- **Related routes:** `/(tabs)/asts/media` (Mobile)
- **Related backend functions:** None dedicated; media stored as part of TRN documents
- **Main user actions:** Capture photo, view evidence gallery
- **Data involved:** Firebase Storage for images; TRN documents store media refs
- **Role access:** All operational roles for capture; MANAGEMENT_ROLES for viewing on web
- **Confirmed files:** `media.js`, `premiseMedia.js`, TRN media labels in `trns/index.js` (lines 17–48)

### 3.28 Location / GPS / Geofence Validation

- **Public meaning:** Capture GPS location for fieldwork, validate against geofences.
- **Web or Mobile or Both:** Mobile
- **Main screen/page/component:** `GeoContext` (`C:\dev\ireps-mobile\src\context\GeoContext.js`), used across all field forms
- **Related routes:** N/A (embedded in forms)
- **Related backend functions:** `doesEntityBelongToGeoFence`, `normalizeGeoFenceRefs` (`geofences/helpers.js`)
- **Main user actions:** Auto-capture coordinates, validate location is within assigned geofence
- **Data involved:** GPS coordinates in TRN accessData
- **Role access:** All operational roles
- **Confirmed files:** `GeoContext.js` (9KB), `geofences/helpers.js`

### 3.29 Offline Storage / Sync

- **Public meaning:** Queue fieldwork data locally when offline and sync when connectivity returns.
- **Web or Mobile or Both:** Mobile only
- **Main screen/page/component:** Storage screens:
  - `forms-submission-queue.js` — queued meter discovery forms
  - `sales-sync.js` — prepaid sales data sync
  - `premise-offline-storage.js` — queued premise forms
  - `account-data-submission-queue.js` — queued account data (FAD) forms
- **Related routes:** `/(tabs)/admin/storage/*` (Mobile)
- **Related backend functions:** None dedicated; standard mutations with offline retry
- **Main user actions:** View queued items, manually sync, download sales data
- **Data involved:** Local storage (AsyncStorage/KV stores), Firestore
- **Role access:** All operational roles
- **Confirmed files:** All four storage files, `offlineSlice.js`

### 3.30 Sales / Prepaid Revenue

- **Public meaning:** View prepaid electricity sales data for revenue analysis.
- **Web or Mobile or Both:** Mobile
- **Main screen/page/component:** Sales data integrated into AST detail views (calendar, timeline, monthly revenue), reports (prepaid revenue report/dashboard), revenue analytics
- **Related routes:** `/(tabs)/asts/[id]/calendar`, `/[id]/timeline`, `/[id]/monthly-revenue`, `/admin/reports/prepaid-revenue-*`, `/admin/operations/revenue-analytics`
- **Related backend functions:** None dedicated; sales data via `salesApi` queries
- **Main user actions:** View sales history per meter, view revenue trends, download monthly sales
- **Data involved:** `sales/` collection (monthly aggregates and atomic records)
- **Role access:** All operational roles
- **Confirmed files:** `salesApi.js` (~21KB), `calendar.js`, `monthly-revenue.js`, `prepaid-revenue-report.js`, `prepaid-revenue-dashboard.js`

### 3.31 Account Data / FAD (Field Account Data)

- **Public meaning:** Capture account holder information during fieldwork.
- **Web or Mobile or Both:** Both
- **Main screen/page/component:**
  - Mobile: `formAccountData.js` (Premises tab)
  - Web: `AccountsRegistryPage.jsx` (55K)
- **Related routes:** `/(tabs)/premises/formAccountData` (Mobile), `/registries/accounts` (Web)
- **Related backend functions:** `onCreateAccountDataCallable`, `onFieldAccountDataWritten`, `onAccountMasterWritten` triggers
- **Main user actions:** Capture account holder details, view account registry
- **Data involved:** `accounts/` and `account_master/` collections
- **Role access:** Mobile: all operational roles for capture; Web: MANAGEMENT_ROLES for registry
- **Confirmed files:** `formAccountData.js`, `AccountsRegistryPage.jsx`, `dataCleansing/callables.js`

### 3.32 Settings / Dropdown Configuration

- **Public meaning:** Manage system-wide dropdown/lookup values (meter types, anomalies, manufacturers).
- **Web or Mobile or Both:** Mobile (primary), Web (Coming Soon)
- **Main screen/page/component:**
  - Mobile: `settings/index.js` (`C:\dev\ireps-mobile\app\(tabs)\admin\settings\index.js`)
  - Web: `/admin/settings` → ComingSoonPage
- **Related routes:** `/(tabs)/admin/settings` (Mobile)
- **Related backend functions:** `onIrepsSelectOptionsCallable`, `onIrepsSelectLookupAdminCallable`
- **Main user actions:** Edit dropdown options, manage select lookups
- **Data involved:** `ireps_select_options/`, `ireps_select_lookups/` collections
- **Role access:** SPU/ADM only (isSPU || isADM in mobile `admin/index.js` line 102)
- **Confirmed files:** `settings/index.js`, `admin/index.js` (line 102), `lookups/index.js`

### 3.33 Profile

- **Public meaning:** View and edit own user profile.
- **Web or Mobile or Both:** Web
- **Main screen/page/component:** `ProfilePage` (`C:\dev\ireps-web\src\pages\profile\ProfilePage.jsx`)
- **Related routes:** `/profile` (Web)
- **Related backend functions:** `updatePassword`, `updateProfile` mutations in authApi
- **Main user actions:** View profile info, update profile, change password
- **Data involved:** `users/{uid}` document
- **Role access:** ALL_OPERATIONAL_ROLES
- **Confirmed files:** `ProfilePage.jsx`, `AppRoutes.jsx` (line ~443)

### 3.34 Field Analytics

- **Public meaning:** Dashboard for field deployment performance metrics.
- **Web or Mobile or Both:** Mobile
- **Main screen/page/component:** `field-analytics.js` (7K) (`C:\dev\ireps-mobile\app\(tabs)\admin\operations\field-analytics.js`)
- **Related routes:** `/admin/operations/field-analytics` (Mobile)
- **Related backend functions:** Not confirmed in code
- **Main user actions:** View deployment performance
- **Data involved:** Not fully confirmed
- **Role access:** All operational roles
- **Confirmed files:** `field-analytics.js`

### 3.35 Quality Assurance

- **Public meaning:** Review and approve meter discovery documents.
- **Web or Mobile or Both:** Mobile
- **Main screen/page/component:** `quality-assurance.js` (1.3K) (`C:\dev\ireps-mobile\app\(tabs)\admin\operations\quality-assurance.js`)
- **Related routes:** `/admin/operations/quality-assurance` (Mobile)
- **Related backend functions:** Not confirmed
- **Main user actions:** Review discovery docs, approve
- **Data involved:** TRNs, ASTs
- **Role access:** All operational roles (but small file — likely placeholder)
- **Confirmed files:** `quality-assurance.js`

### 3.36 TRN Origin

- **Public meaning:** View TRN origination context and traceability.
- **Web or Mobile or Both:** Mobile
- **Main screen/page/component:** `trn-origin.js` (44K) (`C:\dev\ireps-mobile\app\(tabs)\admin\operations\trn-origin.js`)
- **Related routes:** `/admin/operations/trn-origin` (Mobile)
- **Related backend functions:** Not confirmed
- **Main user actions:** Trace TRN origin, view context
- **Data involved:** TRNs collection
- **Role access:** All operational roles
- **Confirmed files:** `trn-origin.js`

### 3.37 Ward-ERF Sync

- **Public meaning:** Download ward/ERF data to mobile device for offline use.
- **Web or Mobile or Both:** Mobile
- **Main screen/page/component:** `ward-erfs-sync.js` (16K) (`C:\dev\ireps-mobile\app\(tabs)\erfs\ward-erfs-sync.js`)
- **Related routes:** `/(tabs)/erfs/ward-erfs-sync` (Mobile)
- **Related backend functions:** None dedicated
- **Main user actions:** Sync ward ERF data to device
- **Data involved:** `ireps_erfs/` collection
- **Role access:** All operational roles
- **Confirmed files:** `ward-erfs-sync.js`

---

## 4. Role-by-Functionality Matrix

**Role codes:** SPU (Superuser), ADM (Admin), MNG (Manager), SPV-MNC (Main Contractor Supervisor), SPV-SUBC (Subcontractor Supervisor), FWR (Fieldworker)

**Important note on SPV-MNC vs SPV-SUBC:**

- There is **no separate role code** for SPV-MNC vs SPV-SUBC. Both use role=`"SPV"`.
- The distinction is based on the **Service Provider relationship type** stored in the user's `employment.serviceProvider`:
  - An SPV whose service provider has `relationshipType === "MNC"` (or `clientType === "MNC"`, or `isMnc === true`) is treated as **SPV-MNC** and gets elevated backend authority (can create BGO batches, lifecycle instructions, manage instructions).
  - An SPV whose service provider has `relationshipType === "SUBC"` (i.e., the SP's `clients[]` array has an entry with `clientType === "SP"` and `relationshipType === "SUBC"`, making it a subcontractor) is treated as **SPV-SUBC** — they lack the elevated authority but can still accept/reject assigned work.
- This logic is implemented in `resolveBgoCreateAuthority` (`C:\dev\ireps-web\functions\bgo\helpers.js`, lines 163–195) and replicated in `meterLifecycle/instructionCallable.js` (lines 93–127) and `meterLifecycle/manageInstructionCallable.js` (lines 122–159).
- In the matrix below, where the distinction matters, SPV-MNC and SPV-SUBC are listed separately. Where they are identical, they share a cell.

| Functionality | SPU | ADM | MNG | SPV-MNC | SPV-SUBC | FWR | Web | Mobile | Notes |
| ------------- | --- | --- | --- | ------- | -------- | --- | --- | ------ | ----- |
| Login / Sign In | Full | Full | Full | Full | Full | Full | ✓ | ✓ | All roles |
| Signup (FWR self-reg) | N/A | N/A | N/A | N/A | N/A | Full | — | ✓ | Becomes FWR after MNG authorization |
| Onboarding | Full | Full | Full | Full | Full | Full | — | ✓ | Step-by-step after first login |
| Workbase Selection | Full | Full | Full | Full | Full | Full | ✓ | ✓ | |
| Dashboard | Full | Full | Full | Full | Full | Full | ✓ | — | Web only; ALL_OPERATIONAL_ROLES |
| Admin Area | Full | Full | View | No access | No access | No access | ✓ | ✓ | Web: ADMIN_ROLES for landing page |
| User: Single Lookup | Full | Full | Full | Full | Full | Full | — | ✓ | All operational roles |
| User: List All | Full | Full | Full | Full | No access | No access | — | ✓ | SPV and above |
| Pending Authorizations | Full | Full | Full | No access | No access | No access | — | ✓ | MNG and above only |
| Create ADM | Full | No access | No access | No access | No access | No access | — | ✓ | SPU only |
| Invite ADM | Full | No access | No access | No access | No access | No access | — | ✓ | SPU only |
| Create MNG | Full | Full | No access | No access | No access | No access | — | ✓ | SPU/ADM only |
| Create SPV | No access | No access | Full | No access | No access | No access | — | ✓ | MNG only; scoped to MNG's SP tree |
| Authorize FWR | No access | No access | Full | No access | No access | No access | — | ✓ | MNG only |
| Service Provider: View | Full | Full | Full | Full | Full | Full | ✓ | ✓ | |
| Service Provider: Create | Full | Full | No access | No access | No access | No access | — | ✓ | SPU/ADM only |
| Service Provider: Edit Profile | Full | Full | Full | Full | No access | No access | — | ✓ | |
| Service Provider: Edit Clients | Full | Full | No access | No access | No access | No access | — | ✓ | SPU/ADM only |
| ERFs: View/Browse | Full | Full | Full | Full | Full | Full | ✓ | ✓ | |
| Maps | Full | Full | Full | Full | Full | Full | ✓ | ✓ | |
| Premises: View | Full | Full | Full | Full | Full | Full | ✓ | ✓ | |
| Premises: Create | Full | Full | Full | Full | Full | Full | — | ✓ | All operational roles via mobile |
| Premises: Account Data | Full | Full | Full | Full | Full | Full | — | ✓ | |
| Meters: View | Full | Full | Full | Full | Full | Full | ✓ | ✓ | |
| Meter Discovery | Full | Full | Full | Full | Full | Full | — | ✓ | Core field operation |
| Meter Installation | Full | Full | Full | Full | Full | Full | — | ✓ | Core field operation |
| Meter Inspection | Full | Full | Full | Full | Full | Full | — | ✓ | Core field operation |
| Meter Disconnection | Full | Full | Full | Full | Full | Full | — | ✓ | Core field operation |
| Meter Reconnection | Full | Full | Full | Full | Full | Full | — | ✓ | Core field operation |
| Meter Removal | Full | Full | Full | Full | Full | Full | — | ✓ | Core field operation |
| Meter Reading | Full | Full | Full | Full | Full | Full | — | ✓ | Core field operation |
| Meter Commissioning | Full | Full | Full | Full | Full | Full | — | ✓ | Core field operation |
| TRNs: View | Full | Full | Full | Full | Full | Full | ✓ | ✓ | |
| Registries (all) | Full | Full | Full | Full | No access | No access | ✓ | — | MANAGEMENT_ROLES only |
| MREAD Registry | Full | Full | Full | Full | No access | No access | ✓ | — | MANAGEMENT_ROLES |
| MREAD Staging (view) | Full | Full | Full | Full | No access | No access | ✓ | — | MANAGEMENT_ROLES |
| MREAD Staging Controller | Full | No access | Full | Full | No access | No access | ✓ | — | SPU/MNG/SPV |
| Reports: View | Full | Full | Full | Full | Full | Full | ✓ | ✓ | Web: MANAGEMENT_ROLES; Mobile: all operational |
| TC Uploads | Full | Full | Full | Full | No access | No access | ✓ | — | Web only; MANAGEMENT_ROLES |
| BGO: Create Batch | Full | Full | Full | Full | No access | No access | ✓ | ✓ | MNG or SPV(MNC) only |
| BGO: Accept/Reject | No access | No access | No access | Full | Full | Full | — | ✓ | Assigned FWR/SPV only |
| BGO: Reverse Acceptance | Full | Full | Full | Full | No access | No access | — | ✓ | MNG or SPV(MNC) only |
| BGO: Delete Unaccepted | Full | Full | Full | Full | No access | No access | — | ✓ | MNG or SPV(MNC) only |
| WMS: Create Instruction | Full | Full | Full | Full | No access | No access | — | ✓ | MNG or SPV(MNC) only |
| WMS: Accept/Reject | No access | No access | No access | Full | Full | Full | — | ✓ | Assigned FWR/SPV only |
| WMS: Manage/Cancel | Full | Full | Full | Full | No access | No access | — | ✓ | MNG or SPV(MNC) only |
| Operations Hub | Full | Full | Full | Full | Full | Full | — | ✓ | Mobile only |
| Geo-Fences: View | Full | Full | Full | Full | Full | Full | ✓ | ✓ | |
| Geo-Fences: Create | Full | Full | Full | Full | No access | No access | ✓ | ✓ | MANAGEMENT_ROLES; web + mobile |
| Teams: View/Manage | Full | Full | Full | Full | No access | No access | ✓ | ✓ | MANAGEMENT_ROLES |
| Evidence/Media: Capture | Full | Full | Full | Full | Full | Full | — | ✓ | Field forms |
| Evidence/Media: View | Full | Full | Full | Full | Full | Full | ✓ | ✓ | |
| Location/GPS | Full | Full | Full | Full | Full | Full | — | ✓ | Embedded in field forms |
| Offline Storage | Full | Full | Full | Full | Full | Full | — | ✓ | Mobile only |
| Sales/Revenue: View | Full | Full | Full | Full | Full | Full | — | ✓ | Mobile only |
| Settings/Dropdowns | Full | Full | No access | No access | No access | No access | — | ✓ | SPU/ADM only |
| Profile | Full | Full | Full | Full | Full | Full | ✓ | — | Web only |
| Field Analytics | Full | Full | Full | Full | Full | Full | — | ✓ | Mobile only |
| Quality Assurance | Full | Full | Full | Full | Full | Full | — | ✓ | Mobile; small — likely placeholder |
| TRN Origin | Full | Full | Full | Full | Full | Full | — | ✓ | Mobile only |
| Ward-ERF Sync | Full | Full | Full | Full | Full | Full | — | ✓ | Mobile only |

**LMU:** Not confirmed in code. Zero matches across both web and mobile codebases.

---

## 5. Web Functionality Summary

| Functionality | Purpose | Roles with access | Page/Route | Confirmed files |
|---|---|---|---|---|
| **Login** | Email/password sign-in | Unauthenticated | `/login` | `LoginPage.jsx` |
| **Dashboard** | Landing page with role/workbase info | All operational roles | `/dashboard` | `DashboardPage.jsx` |
| **Pending Approval** | Shown when onboarding is incomplete | All during onboarding | `/pending-approval` | `PendingApprovalPage.jsx` |
| **Access Denied** | Shown when role lacks permission | Any denied role | `/access-denied` | `AccessDeniedPage.jsx` |
| **Map** | Interactive map | MANAGEMENT_ROLES | `/ward-scope/map` | `MapPage.jsx` |
| **ERFs** | Browse ERFs by ward | MANAGEMENT_ROLES | `/ward-scope/erfs` | `ErfsPage.jsx` |
| **Premises** | Browse premises | MANAGEMENT_ROLES | `/ward-scope/premises` | `PremisesPage.jsx` |
| **Meters** | Browse meters | MANAGEMENT_ROLES | `/ward-scope/meters` | `MetersPage.jsx` |
| **Ward Registry** | Ward structure overview | MANAGEMENT_ROLES | `/registries/wards` | `WardsRegistryPage.jsx` |
| **ERF Registry** | ERF inventory | MANAGEMENT_ROLES | `/registries/erfs` | `ErfsRegistryPage.jsx` |
| **Premise Registry** | Premise inventory | MANAGEMENT_ROLES | `/registries/premises` | `PremisesRegistryPage.jsx` |
| **Meter Registry** | Meter inventory | MANAGEMENT_ROLES | `/registries/meters` | `MetersRegistryPage.jsx` |
| **MREAD Registry** | Meter reading records | MANAGEMENT_ROLES | `/registries/mread` | `MreadRegistryPage.jsx` |
| **MREAD Staging** | Reading cycle staging | MANAGEMENT_ROLES | `/registries/mread-staging` | `MreadStagingPage.jsx` |
| **Account Registry** | Account holder records | MANAGEMENT_ROLES | `/registries/accounts` | `AccountsRegistryPage.jsx` |
| **No Access Report** | Blocked access events | MANAGEMENT_ROLES | `/reports/no-access` | `NoAccessReportPage.jsx` |
| **User Activity Report** | Field-user activity | MANAGEMENT_ROLES | `/reports/user-activity` | `UserActivityReportPage.jsx` |
| **Anomaly Report** | Anomaly events | MANAGEMENT_ROLES | `/reports/anomaly` | `AnomalyReportPage.jsx` |
| **Normalisation Report** | Normalisation patterns | MANAGEMENT_ROLES | `/reports/normalisation` | `NormalisationReportPage.jsx` |
| **Operations Landing** | Operations overview | MANAGEMENT_ROLES | `/operations` | `OperationsLandingPage.jsx` |
| **TC Uploads** | Upload/manage TC data | MANAGEMENT_ROLES | `/operations/tc-uploads` | `TcUploadsPage.jsx` |
| **TC Upload Details** | TC file detail | MANAGEMENT_ROLES | `/operations/tc-uploads/:tcId` | `TcUploadDetailsPage.jsx` |
| **TC BGO** | TC row BGO allocation | MANAGEMENT_ROLES | `/operations/tc-uploads/:tcId/bgo` | `TcBgoPage.jsx` |
| **TC Final Report** | TC operation report | MANAGEMENT_ROLES | `/operations/tc-uploads/:tcId/final-report` | `TcFinalReportPage.jsx` |
| **BGO Dashboard** | BGO allocation overview | MANAGEMENT_ROLES | `/operations/bgo-dashboard` | `BgoDashboardPage.jsx` |
| **BMD BGO** | BMD BGO allocation | MANAGEMENT_ROLES | `/operations/bgo` | `BmdBgoPage.jsx` |
| **MD BGO Rows** | MD BGO rows view | MANAGEMENT_ROLES | `/operations/md-bgo-rows` | `MdBgoRowsPage.jsx` |
| **Geo-Fences** | Geofence management | MANAGEMENT_ROLES | `/operations/geo-fences` | `GeoFencesPage.jsx` |
| **MREAD Staging Controller** | Control staging cycles | SPU/MNG/SPV | `/admin/mread-staging-controller` | `MreadStagingControllerPage.jsx` |
| **Admin Landing** | Admin hub (Coming Soon) | ADMIN_ROLES | `/admin` | `ComingSoonPage.jsx` |
| **Service Providers** | SP oversight (Coming Soon) | MANAGEMENT_ROLES | `/admin/service-providers` | `ComingSoonPage.jsx` |
| **Users** | User oversight (Coming Soon) | MANAGEMENT_ROLES | `/admin/users` | `ComingSoonPage.jsx` |
| **Teams** | Team management (Coming Soon) | MANAGEMENT_ROLES | `/admin/teams` | `ComingSoonPage.jsx` |
| **Settings** | Config (Coming Soon) | ADMIN_ROLES | `/admin/settings` | `ComingSoonPage.jsx` |
| **Profile** | User profile | All operational roles | `/profile` | `ProfilePage.jsx` |

---

## 6. Mobile Functionality Summary

| Functionality | Purpose | Roles with access | Screen/Route | Confirmed files |
|---|---|---|---|---|
| **Sign In** | Email/password sign-in | Unauthenticated | `/(auth)/signin` | `signin.jsx` |
| **Sign Up** | FWR self-registration | Unauthenticated | `/(auth)/signup` | `signup.jsx` |
| **Onboarding (10 screens)** | Account setup flow | All during onboarding | `/onboarding/*` | 10 files in `onboarding/` |
| **ERFs Tab** | Browse ERFs, sync wards | All operational roles | `/(tabs)/erfs` | `erfs/_layout.js`, `erfs/` |
| **Premises Tab** | Browse/create premises, FAD | All operational roles | `/(tabs)/premises` | `premises/_layout.js`, `premises/` |
| **TRNs Tab** | View all transactions | All operational roles | `/(tabs)/trns` | `trns/index.js` (~1667 lines) |
| **ASTs/Meters Tab** | Meter list + full lifecycle | All operational roles | `/(tabs)/asts` | `asts/_layout.js` + 11 sub-screens |
| **Meter Inspection** | Inspect meter, record status | All operational roles | `/(tabs)/asts/inspection` | `inspection.js` (150K) |
| **Meter Disconnection** | Disconnect meter | All operational roles | `/(tabs)/asts/disconnection` | `disconnection.jsx` (88K) |
| **Meter Reconnection** | Reconnect meter | All operational roles | `/(tabs)/asts/reconnection` | `reconnection.jsx` (86K) |
| **Meter Removal** | Remove meter | All operational roles | `/(tabs)/asts/removal` | `removal.jsx` (85K) |
| **Meter Reading** | Capture meter reading | All operational roles | `/(tabs)/asts/meter-reading` | `meter-reading.js` (114K) |
| **Meter Commissioning** | Commission new meter | All operational roles | `/(tabs)/asts/commissioning` | `commissioning.jsx` (50K) |
| **Meter Details + Hub** | Meter detail, calendar, timeline, revenue | All operational roles | `/(tabs)/asts/[id]` | `[id]/index.js`, `calendar.js`, `timeline.js`, `monthly-revenue.js` |
| **Meter Media** | View meter evidence | All operational roles | `/(tabs)/asts/media` | `media.js` |
| **Maps Tab** | Interactive map | All operational roles | `/(tabs)/maps` | `maps/` directory |
| **Admin Tab** | Role-gated admin hub | All operational roles | `/(tabs)/admin` | `admin/index.js` |
| **Admin: Service Providers** | View/manage SPs | All operational roles | `/(tabs)/admin/service-providers` | `service-providers/` |
| **Admin: User Lookup** | Look up single user | All operational roles | `/(tabs)/admin/user` | `user/index.js` |
| **Admin: Users List** | List all users | SPV and above | `/(tabs)/admin/users` | `users/index.js` |
| **Admin: Pending** | Authorize FWR | MNG and above | `/admin/pendingUsers` | `pendingUsers/index.js` |
| **Admin: Settings** | Dropdown config | SPU/ADM only | `/(tabs)/admin/settings` | `settings/index.js` |
| **Admin: Reports** | Registry & activity reports | All operational roles | `/admin/reports` | `reports/index.js` |
| **Admin: Operations Hub** | WMS, teams, geo-fences, analytics | All operational roles | `/admin/operations` | `operations/index.js` |
| **Ops: WMS Dashboard** | Ward workorder cockpit | All operational roles | `/admin/operations/dashboard` | `dashboard/` |
| **Ops: My Workorders** | Accept/reject/execute lifecycle work | All operational roles | `/admin/operations/my-workorders` | `my-workorders.js` (112K) |
| **Ops: Teams** | Create/manage teams | MANAGEMENT_ROLES | `/admin/operations/teams` | `teams.js` (29K) |
| **Ops: Geo-Fences** | Create/view geofences | All operational roles | `/admin/operations/geo-fences` | `geo-fences.js` (25K) |
| **Ops: Field Analytics** | Field performance | All operational roles | `/admin/operations/field-analytics` | `field-analytics.js` |
| **Ops: Revenue Analytics** | Prepaid revenue analysis | All operational roles | `/admin/operations/revenue-analytics` | `revenue-analytics.js` |
| **Ops: Quality Assurance** | Review discovery docs | All operational roles | `/admin/operations/quality-assurance` | `quality-assurance.js` |
| **Ops: TRN Origin** | TRN traceability | All operational roles | `/admin/operations/trn-origin` | `trn-origin.js` (44K) |
| **Storage: Forms Queue** | Offline discovery forms | All operational roles | `/admin/storage/forms-submission-queue` | `forms-submission-queue.js` |
| **Storage: Sales Sync** | Download prepaid sales | All operational roles | `/admin/storage/sales-sync` | `sales-sync.js` |
| **Storage: Premise Queue** | Offline premise forms | All operational roles | `/admin/storage/premise-offline-storage` | `premise-offline-storage.js` |
| **Storage: Account Queue** | Offline FAD queue | All operational roles | `/admin/storage/account-data-submission-queue` | `account-data-submission-queue.js` |

---

## 7. Backend Permission Summary

| Function | Who can call it | What it does | Confirmed file:line | Notes |
|---|---|---|---|---|
| `createServiceProvider` | SPU, ADM (`auth.token.role`) | Create new service provider (MNC classification enforced) | `index.js:435–454` | |
| `updateServiceProvider` | SPU, ADM (can edit clients/status); MNG, SPV (can edit profile/offices) | Update service provider | `index.js:543`, `spApi.js:169–177` | Role checked in frontend mutation |
| `createAdminUser` | SPU only (`auth.token.role`) | Create ADM user in Auth + Firestore | `index.js:652–668` | |
| `inviteAdminUser` | SPU only (implied, needs confirmation) | Invite ADM user | `index.js:2407` | |
| `inviteManagerUser` | SPU, ADM (caller Firestore profile `employment.role`) | Create MNG user, inherit workbases from SP's LM clients | `index.js:1973–2015` | |
| `inviteSupervisorUser` | MNG only (caller Firestore profile `employment.role`) | Create SPV user, scoped to MNG's SP tree | `index.js:2178–2218` | |
| `signupFieldWorker` | Unauthenticated (no role check) | Create FWR Auth user + Firestore doc; resolves responsible MNG | `index.js:2551` | |
| `authorizeFieldWorker` | MNG only (caller Firestore profile `employment.role`) | Activate FWR account; add workbases and teams from MNG's SP tree | `index.js:2763–2800` | |
| `onMeterDiscoveryCallable` | Authenticated (no role check) | Create TRN for meter discovery; duplicate check against `meter_master` | `index.js:2934` | |
| `onPremiseCreateCallable` | Authenticated (no role check) | Create premise document; idempotency + duplicate guard | `index.js:4365` | |
| `onMeterInstallationCallable` | Authenticated (no role check) | Create TRN for meter installation; duplicate check | `index.js:4590` | |
| `onCreateBgoCallable` | MNG or SPV(MNC) (`resolveBgoCreateAuthority`) | Create BGO batch from TC rows | `bgo/callables.js:730–737` | SPV must have MNC relationship |
| `onAcceptRejectBgoBatchCallable` | Assigned FWR or SPV (`actor.role`) | Accept or reject BGO batch allocation | `bgo/acceptanceCallable.js:714` | |
| `onReverseBgoBatchAcceptanceCallable` | MNG or SPV(MNC) (`resolveBgoCreateAuthority`) | Reverse a BGO batch acceptance | `bgo/acceptanceCallable.js:1141–1149` | |
| `onDeleteUnacceptedBgoCallable` | MNG or SPV(MNC) (`resolveBgoCreateAuthority`) | Delete unaccepted BGO batch | `bgo/deleteCallable.js:268–275` | |
| `onCreateMeterLifecycleInstructionCallable` | MNG or SPV(MNC) (`resolveCreateInstructionAuthority`) | Create lifecycle instruction for field team | `meterLifecycle/instructionCallable.js:261–273` | |
| `onAcceptRejectLifecycleInstructionCallable` | Assigned FWR or SPV | Accept or reject lifecycle instruction | `meterLifecycle/acceptRejectCallable.js:346` | |
| `onManageLifecycleInstructionCallable` | MNG or SPV(MNC) (`resolveManageAuthority`) | Reassign or cancel lifecycle instruction | `meterLifecycle/manageInstructionCallable.js:475–487` | |
| `onCreateMeterCommissioningCallable` | Authenticated (no explicit role check) | Commission newly installed meter | `commissioning/callable.js` | |
| `createTeam` / `renameTeam` / `addTeamMember` / `removeTeamMember` / `deleteTeam` | Not confirmed in code (check `teams/callables.js` for role checks) | Team CRUD operations | `teams/callables.js` | |
| `createGeoFence` | Not confirmed (check `geofences/callables.js`) | Create geofence polygon | `geofences/callables.js` | |
| `onUploadAndValidateTcCallable` | Not confirmed (check `tcUploads/callables.js`) | Upload and validate TC file | `tcUploads/callables.js` | |
| `onIrepsSelectOptionsCallable` | Not confirmed | Fetch dropdown options | `lookups/index.js` | |
| `onIrepsSelectLookupAdminCallable` | Not confirmed | Admin lookup management | `lookups/index.js` | |
| `rebuild*Callable` functions | Not confirmed | Registry rebuild operations | `registry/*` | |
| `onNoAccessRecorded` (trigger) | Triggered by TRN creation (no auth) | Record no-access on premise when TRN has `hasAccess="no"` | `index.js:1776` | Firestore trigger |
| `onPremiseCreated` / `onPremiseUpdated` (triggers) | Triggered by premise write (no auth) | Rebuild related counts and registries | `index.js:734, 1018` | Firestore triggers |
| `onMeterCreated` / `onMeterUpdated` (triggers) | Triggered by meter write (no auth) | Sync geofence membership, rebuild registries | `index.js:3764, 3828` | Firestore triggers |
| `onMeterDiscoveryCreated` (trigger) | Triggered by discovery TRN (no auth) | Process new meter discovery | `index.js:1471` | Firestore trigger |
| `onServiceProviderUpdated` (trigger) | Triggered by SP update (no auth) | Propagate SP changes | `index.js:4177` | Firestore trigger |
| `onFieldAccountDataWritten` / `onAccountMasterWritten` (triggers) | Triggered by account data writes (no auth) | Rebuild account registries | `dataCleansing/triggers.js` | Firestore triggers |
| `onTrnWritten` (trigger) | Triggered by TRN writes (no auth) | Report generation trigger | `reports/trnReports.js` | Firestore trigger |
| `onGeoFenceCreated` (trigger) | Triggered by geofence write (no auth) | Initialize geofence membership | `geofences/triggers.js` | Firestore trigger |
| `onMeterCommissioningTrnCreated` (trigger) | Triggered by commissioning TRN (no auth) | Process commissioning | `commissioning/trigger.js` | Firestore trigger |

**Firestore Rules:** `C:\dev\ireps-web\firestore.rules` (lines 1–10) allows any authenticated user to read/write any document. All fine-grained permissions are enforced at the application layer (web `RoleRoute`, mobile UI conditionals) and cloud function level.

---

## 8. Public User Guide Notes

| # | Public guide name | Simple meaning | Who uses it | Web or Mobile |
|---|---|---|---|---|
| 1 | **Sign In** | Log into iREPS with your email and password. | All users | Both |
| 2 | **Sign Up** | Register as a new fieldworker. | New fieldworkers | Mobile |
| 3 | **Account Setup (Onboarding)** | Complete your profile, verify your identity, and select your municipality. | All users after first login | Mobile |
| 4 | **Dashboard** | Your home screen showing your role, municipality, and navigation. | All users | Web |
| 5 | **Profile** | View and update your personal account details. | All users | Web |
| 6 | **Map** | Explore wards, properties, and meters on an interactive map. | Managers, supervisors, admins | Both |
| 7 | **ERFs (Cadastral Records)** | Browse land parcel records and see what is on each erf. | All users (mobile), managers+ (web) | Both |
| 8 | **Premises** | View and manage property records where meters are installed. | All users (mobile), managers+ (web) | Both |
| 9 | **Meters (ASTs)** | View the meter inventory and track each meter's status. | All users (mobile), managers+ (web) | Both |
| 10 | **Meter Discovery** | Record a newly found meter in the field. | Fieldworkers and supervisors | Mobile |
| 11 | **Meter Installation** | Record a newly installed meter at a property. | Fieldworkers and supervisors | Mobile |
| 12 | **Meter Inspection** | Inspect an existing meter and record its condition. | Fieldworkers and supervisors | Mobile |
| 13 | **Meter Disconnection** | Disconnect a meter and record the reason and evidence. | Fieldworkers and supervisors | Mobile |
| 14 | **Meter Reconnection** | Reconnect a previously disconnected meter. | Fieldworkers and supervisors | Mobile |
| 15 | **Meter Removal** | Remove a meter from a property. | Fieldworkers and supervisors | Mobile |
| 16 | **Meter Reading** | Capture a meter's current reading. | Fieldworkers and supervisors | Mobile |
| 17 | **Meter Commissioning** | Commission a newly installed meter into the system. | Fieldworkers and supervisors | Mobile |
| 18 | **Transactions (TRNs)** | View all field operations as a transaction log. | All users (mobile), managers+ (web) | Both |
| 19 | **No Access Recording** | Record when a property cannot be accessed. | Fieldworkers and supervisors | Mobile |
| 20 | **Evidence Capture** | Take photos as proof of field work. | Fieldworkers and supervisors | Mobile |
| 21 | **Account Data (FAD)** | Capture account holder information at a property. | Fieldworkers and supervisors | Mobile |
| 22 | **Registries** | Central lookup tables for wards, ERFs, premises, meters, readings, and accounts. | Managers and above | Web |
| 23 | **MREAD Registry** | View the master meter reading records. | Managers and above | Web |
| 24 | **MREAD Staging** | Manage meter reading cycles before they are published. | Managers, supervisors, superusers | Web |
| 25 | **Reports** | View operational reports: no-access, anomalies, normalisation, user activity, revenue. | All users | Both |
| 26 | **TC Uploads** | Upload and manage prepaid meter data files. | Managers and above | Web |
| 27 | **BGO (Work Allocation)** | Allocate work from TC uploads to field teams as batches. | Managers and main-contractor supervisors | Both |
| 28 | **Workorders (WMS)** | Issue, accept, and execute lifecycle work instructions. | All users | Mobile |
| 29 | **My Workorders** | View and respond to work assigned to you. | Fieldworkers and supervisors | Mobile |
| 30 | **Teams** | Create and manage operational teams. | Managers and above | Mobile |
| 31 | **Geo-Fences** | Define geographic work boundaries for field teams. | Managers and above | Both |
| 32 | **Offline Mode** | Work without internet; data syncs when you reconnect. | Fieldworkers and supervisors | Mobile |
| 33 | **Prepaid Revenue** | View electricity sales data and revenue trends. | All users | Mobile |
| 34 | **Field Analytics** | View field team performance metrics. | All users | Mobile |
| 35 | **Quality Assurance** | Review and approve field discovery records. | All users | Mobile |
| 36 | **User Management** | Create users, manage roles, and authorize new fieldworkers. | Admins and managers | Mobile |
| 37 | **Service Provider Management** | View and manage contractor and subcontractor records. | Managers and above | Mobile |
| 38 | **Settings** | Configure system dropdowns (meter types, anomalies, manufacturers). | Superusers and admins | Mobile |
| 39 | **Workbase Selection** | Switch between the municipalities you operate in. | All users | Both |
| 40 | **Ward-ERF Sync** | Download ward and ERF data to your device for offline use. | Fieldworkers and supervisors | Mobile |

---

## 9. Gaps / Contradictions / Not Confirmed

1. **LMU role** — Does not exist in the codebase. Zero matches across web, mobile, and functions. Not a role code.

2. **SPV-MNC vs SPV-SUBC** — Not separate role codes. The distinction is based solely on the Service Provider's `relationshipType` or `clientType` being `"MNC"` vs `"SUBC"`. This is checked in three backend authority resolvers: `resolveBgoCreateAuthority`, `resolveCreateInstructionAuthority`, and `resolveManageAuthority`. The web frontend does not distinguish between them in route guards — all SPV users are in MANAGEMENT_ROLES. The mobile frontend does not expose the distinction in UI conditionals. Only the backend uses it for BGO creation, instruction creation, and instruction management.

3. **Web "Coming Soon" pages** — Several web routes render `ComingSoonPage` with descriptive cards but are not yet implemented: `/admin` (landing), `/admin/service-providers`, `/admin/users`, `/admin/teams`, `/admin/settings`, `/operations/teams`, `/operations/wms-dashboard`. These are accessible via the sidebar but show placeholder content.

4. **MREAD Billing tab** — `C:\dev\ireps-mobile\app\(tabs)\mread-billing\` is an empty directory. The tab does not appear in the tab layout. Not yet implemented.

5. **Sales tab** — Referenced in tab layout titles (`sales: "Sales"`) but no `sales` tab directory exists in `(tabs)`. Sales functionality is embedded in Admin > Reports, Admin > Storage, and AST detail views.

6. **Roles in Firestore triggers** — Most backend triggers (`onPremiseCreated`, `onMeterCreated`, `onNoAccessRecorded`, `onMeterDiscoveryCreated`, etc.) run without authentication context (Firestore-triggered). They cannot perform role checks. Access control relies on the callable function that wrote the triggering document.

7. **Teams callables role checks** — Not fully confirmed. The `teams/callables.js` file was not read in detail. Assigned MANAGEMENT_ROLES based on web route guard and mobile UI gating.

8. **Geo-fence create callable role check** — Not fully confirmed in the backend. Web route uses MANAGEMENT_ROLES guard.

9. **TC Upload callable role check** — Not fully confirmed in the backend. Web route uses MANAGEMENT_ROLES guard.

10. **Quality Assurance** — Mobile screen is only ~1.3KB, likely a placeholder or thin wrapper.

11. **Firestore rules** — Rules allow any authenticated user to read/write any document (`request.auth != null`). This means the client-side application and cloud functions are the sole permission enforcement points. There is no Firestore-level role-based access control.

12. **Role source discrepancy** — Some cloud functions check `auth.token.role` (custom claims), while others load the caller's Firestore `users/{uid}` document and read `employment.role`. This creates two possible sources of truth for role. The `createAdminUser` function sets custom claims with `role: "ADM"` (line 694), but other functions (e.g., `inviteManagerUser`, `signupFieldWorker`) only set the Firestore `employment.role` field, not custom claims. This may cause inconsistency for functions that check `auth.token.role`.

13. **Mobile role guard** — Unlike the web app, the mobile app has no equivalent of `RoleRoute` for screen-level authorization. It relies entirely on UI conditionals (`isSPU &&`, `isADM &&`, etc.) to show/hide cards and navigation elements. A technically skilled user could potentially access screens by manipulating navigation state, though backend functions provide the real enforcement.

14. **Web `ward-scope/map` vs `ward-scope/maps`** — Route `/maps` redirects to `/ward-scope/maps` (line ~333) but the actual route is defined as `/ward-scope/map` (singular, line ~313). This is a minor URL inconsistency.

---

## 10. Recommended Public Guide Structure

Based on the code findings, the public iREPS User Guide should be structured as follows:

### Section 1: About iREPS
- What iREPS is (electricity revenue protection and enforcement)
- iREPS Web vs iREPS Mobile — what each is for
- The five user roles explained simply

### Section 2: Getting Started
- Signing in (both platforms)
- Signing up as a fieldworker (mobile)
- Completing onboarding (mobile)

### Section 3: Everyday Fieldwork (Mobile)
Group by the natural field workflow:

1. **Finding your way:** Map, ERFs, ward sync
2. **Working with premises:** Viewing premises, creating a premise, recording account data, recording no-access
3. **Working with meters:**
   - Meter discovery (finding new meters)
   - Meter installation
   - Meter inspection
   - Meter disconnection
   - Meter reconnection
   - Meter removal
   - Meter reading
   - Meter commissioning
4. **Evidence and photos**
5. **Working offline**
6. **My Workorders** — responding to assigned work

### Section 4: Oversight and Reporting (Web)
1. **Dashboard and navigation**
2. **The Map**
3. **Ward-scope browsing:** ERFs, premises, meters
4. **Registries:** Ward, ERF, premise, meter, MREAD, account
5. **MREAD staging and controller**
6. **Reports:** No-access, user activity, anomaly, normalisation

### Section 5: Operations Management (Web + Mobile)
1. **TC Uploads** (Web)
2. **BGO allocation** (Web creates, Mobile accepts)
3. **WMS workorders** (Mobile creates/accepts/executes)
4. **Teams** (Mobile)
5. **Geo-fences** (Both)
6. **Field and revenue analytics** (Mobile)

### Section 6: Administration (Mobile)
1. **User management:** Creating admins, managers, supervisors; authorizing fieldworkers
2. **Service provider management**
3. **Pending authorizations**
4. **Settings and dropdowns**

### Section 7: Reference
- Role permission table
- Glossary of terms (ERF, AST, TRN, BGO, WMS, MREAD, FAD, TC, LM, MNC, SUBC)

### Appendix: Role-by-Functionality Quick Reference
The matrix from Section 4 above, simplified for public consumption.
