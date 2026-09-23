> **Academy status:** Historical original; contains superseded role and offline claims. Imported 2026-09-23. Source: `SRC-003` in the [source register](../SOURCE_REGISTER.csv). [Owner decisions](../OWNER_DECISIONS.md) take precedence over conflicting inherited statements.

# iREPS Mobile — User Manual

> **App**: iREPS Mobile  
> **Platform**: iOS & Android  
> **Purpose**: Field data collection for municipal infrastructure and revenue management  

---

## Table of Contents

1. [What is iREPS?](#1-what-is-ireps)
2. [Getting Started](#2-getting-started)
   - [Signing Up](#21-signing-up)
   - [Signing In](#22-signing-in)
   - [Onboarding Steps](#23-onboarding-steps)
3. [Understanding the Geo-Scope](#3-understanding-the-geo-scope)
   - [The Five Levels](#31-the-five-levels)
   - [Cascade Clearing](#32-cascade-clearing)
   - [Changing Your Scope](#33-changing-your-scope)
4. [Tab-by-Tab Guide](#4-tab-by-tab-guide)
   - [ERFs Tab](#41-erfs-tab)
   - [Premises Tab](#42-premises-tab)
   - [TRNs Tab](#43-trns-tab)
   - [Meters / ASTs Tab](#44-meters--asts-tab)
   - [Maps Tab](#45-maps-tab)
   - [Admin Tab](#46-admin-tab)
5. [Meter Lifecycle Workflows](#5-meter-lifecycle-workflows)
   - [Meter Inspection](#51-meter-inspection)
   - [Meter Disconnection](#52-meter-disconnection)
   - [Meter Reconnection](#53-meter-reconnection)
   - [Meter Removal](#54-meter-removal)
   - [Meter Reading](#55-meter-reading)
6. [Working Offline](#6-working-offline)
7. [WMS Dashboard](#7-wms-dashboard)
8. [Roles & Permissions](#8-roles--permissions)
9. [Glossary](#9-glossary)

---

## 1. What is iREPS?

iREPS is a mobile field-work application for municipal property and revenue management. It enables field workers, supervisors, and managers to:

- **Browse and manage ERFs** (cadastral land parcels) within municipalities and wards
- **Register and inspect premises** (physical properties tied to ERFs)
- **Capture meter data** — discover, inspect, disconnect, reconnect, remove, and read electricity/water meters
- **Track work orders (TRNs)** — view issued work, accept/reject assignments, and complete field tasks
- **View maps** with live geographic layers for ERFs, premises, and meters
- **Work offline** — fill forms without connectivity; data syncs automatically when you're back online
- **Monitor operations** via the WMS Dashboard with real-time workorder analytics

---

## 2. Getting Started

### 2.1 Signing Up

1. Open the iREPS app. You'll see the **Sign In** screen.
2. Tap **"Don't have an account? Sign Up"** at the bottom.
3. Fill in the registration form:
   - **Surname** and **Name** — your full name
   - **Email** — a valid email address you can verify
   - **Password** — minimum 8 characters
   - **Confirm Password** — must match your password
   - **Service Provider** — tap to select from the list of registered service providers
4. Tap **Submit**.
5. Your account will be created as a **Guest (GST)** and will proceed through onboarding (see [2.3](#23-onboarding-steps)).

### 2.2 Signing In

1. Open the app. Enter your **email** and **password**.
2. Tap **Sign In**.
3. If your onboarding is complete, you'll be taken to the main dashboard.  
   If onboarding is still in progress, you'll see the relevant onboarding screen.

> **Forgot password?** Tap the **"Lost access?"** link on the sign-in screen to initiate password recovery.

### 2.3 Onboarding Steps

After signing up, your account goes through these stages:

| Step | Screen | What Happens |
|------|--------|--------------|
| **1. Verify Email** | `verify-email` | Check your inbox and click the verification link |
| **2. Awaiting SP** | `waiting-sp` | Your Service Provider reviews and confirms your registration |
| **3. Awaiting Manager** | `awaiting-mng-confirmation` | A Manager authorizes your account |
| **4. Complete Profile** | `complete-invited-profile` | (Invited users) Set your name, surname, and password |
| **5. Select Workbase** | `select-workbase` | Choose the Local Municipality (LM) you'll work in |
| **6. Change Password** | `change-password` | If required, set a new password on first login |

Once your status reaches **COMPLETED**, you can use the app normally.

---

## 3. Understanding the Geo-Scope

iREPS organizes all data geographically. Before you work with ERFs, premises, or meters, you must understand the **Geo-Scope**.

### 3.1 The Five Levels

The scope cascades from large to small:

```
Local Municipality (LM)  →  Ward  →  ERF  →  Premise  →  Meter
       (Level 5)            (L4)     (L3)    (L2)        (L1)
```

- **LM**: Your Local Municipality — set when you choose your workbase during onboarding.
- **Ward**: An administrative subdivision within the LM. You can switch wards at any time.
- **ERF**: A cadastral land parcel. Selecting an ERF filters premises and meters to that parcel.
- **Premise**: A physical property (house, building) on an ERF.
- **Meter**: An electricity or water meter installed at a premise.

### 3.2 Cascade Clearing

When you change a higher level, **all lower levels are automatically cleared**:

- Changing the **LM** clears ward, ERF, premise, and meter selections.
- Changing the **Ward** clears ERF, premise, and meter selections.
- Selecting an **ERF** clears premise and meter selections.
- Selecting a **Premise** clears the meter selection.

This keeps your data context consistent.

### 3.3 Changing Your Scope

- **Switch Wards**: Use the ward selector in the ERFs tab or the Geo Cascading Selector on the Maps screen.
- **Select an ERF**: Tap any ERF in the ERFs list or tap an ERF marker on the map.
- **Select a Premise**: Tap a premise in the Premises list or a premise marker on the map.
- **Select a Meter**: Tap a meter in the Meters/ASTs list or a meter marker on the map.

The app **remembers your last active ward** and restores it when you sign back in.

---

## 4. Tab-by-Tab Guide

The bottom tab bar has six tabs. Here's what each one does.

### 4.1 ERFs Tab

**Icon**: 🎯 (map-marker-radius-outline)

The ERFs tab shows all cadastral land parcels in your selected ward.

- **Ward ERF Sync**: On first visit to a ward, tap **Sync** to download ERF data for offline use. The sync screen shows:
  - Available wards in your LM
  - Sync status for each ward (synced, syncing, not synced)
  - **Drop Ward** button to remove a ward's cached data
- **Browsing ERFs**: Once synced, browse the list of ERFs. Each card shows:
  - ERF number
  - Number of premises on the ERF
  - Geographic coordinates
- **Select an ERF** by tapping it. This narrows the premises and meters views to that ERF.

### 4.2 Premises Tab

**Icon**: 🏢 (office-building-marker-outline)

The Premises tab shows physical properties within your current scope.

- **Ward Scope**: Shows all premises in the selected ward.
- **ERF Scope**: Shows only premises on the selected ERF.
- **Premise Cards**: Each card displays:
  - Address details (street, suburb, city)
  - Property type (Residential, Commercial, Industrial, etc.)
  - Occupancy status (Occupied / Vacant)
  - Services (Electricity, Water)
- **Actions on a premise**:
  - **View on Map** — jump to the Maps tab centered on the premise
  - **Edit Premise** — update premise details via a form
  - **View Media** — see photos attached to the premise
- **Add Premise**: Use the **+** button to create a new premise.
- **Meter Discovery**: Tap **Discover Meter** to record a newly found meter at a premise.
- **Filter & Search**: Use the filter bar to search premises by address, type, or occupancy.

### 4.3 TRNs Tab

**Icon**: 🔄 (swap-horizontal)

TRNs (Transactions) are work records. This tab shows all transactions in your current scope.

- **Transaction List**: Each TRN card shows:
  - **TRN Type** (Inspection, Disconnection, Reconnection, Removal, Meter Reading)
  - **Workflow State** (ISSUED, ACCEPTED, REJECTED, COMPLETED, CANCELLED)
  - **Execution Outcome** (Success, No Access, No Reading, N/A)
  - **Origin** (Office-issued or Field-created)
  - **Timestamp** — when the TRN was created
  - **Media evidence** — photos attached to the TRN
- **View TRN Details**: Tap a TRN to see full details including:
  - Assignment information (bucket, issued by, accepted/rejected timestamps)
  - Execution outcome details and notes
  - All attached media (instruction photos, meter readings, anomaly evidence, etc.)
- **Filter TRNs**: Use the filter to narrow by type, state, outcome, or search text.

### 4.4 Meters / ASTs Tab

**Icon**: 🔢 (counter)

ASTs (Assets) are meters. This tab shows all electricity and water meters in your scope.

- **Meter List**: Each card shows:
  - Meter number (AST No.)
  - Meter type (Electricity / Water)
  - Lifecycle status (Active, Decommissioned, etc.)
  - Associated premise
- **Filter & Search**: 
  - **Search** by meter number
  - **Filter** by meter type, lifecycle status, and other attributes
  - **Stats** modal shows aggregate counts for the current filtered view
  - **Quick Reset** clears all filters
- **Tap a meter** to see detailed information including installation data.
- **Meter Lifecycle Actions** (see [Section 5](#5-meter-lifecycle-workflows)):
  - Inspection
  - Disconnection
  - Reconnection
  - Removal
  - Meter Reading

### 4.5 Maps Tab

**Icon**: 🗺️ (map-outline)

The Maps tab provides a geospatial view of your data.

- **Map Display**: Shows ERF boundaries, premise markers, and meter markers on an interactive map.
- **Layer Toggles**: Turn layers on/off:
  - **ERFs** — shows ERF polygons and centroids
  - **Premises** — shows premise location markers
  - **Meters (ASTs)** — shows meter location markers
  - **SC** — Service connection lines
- **Geo Cascading Selector**: Tap the selector button to browse and switch LM → Ward → ERF directly from the map.
- **Marker Interactions**:
  - **Tap an ERF** to select it and see its boundary
  - **Tap a Premise** to see premise details and actions (edit, meter discovery, meter installation)
  - **Tap a Meter** to select it and view details
- **Premise Marker Drag**: In **Edit Mode**, you can drag premise markers to correct their position. Changes are saved to the server.
- **Map Controls**:
  - Zoom in/out with pinch gestures
  - Toggle map type (standard/satellite)
  - Fly to your current selected location

### 4.6 Admin Tab

**Icon**: 🛡️ (shield-account-outline)

The Admin tab provides management and reporting functions. What you see depends on your role.

#### Operational Management
- **Service Providers** — view and manage registered contractors (all roles)
- **User** — view a specific platform user (all roles)
- **Users** — browse all platform users (SPU, ADM, MNG, SPV)
- **Pending Authorizations** — review and approve new field worker registrations (SPU, ADM, MNG)

#### System Configuration (SPU & ADM only)
- **Dropdown Settings** — manage dropdown options: meter types, anomaly types, manufacturers, etc.

#### Reporting & Intelligence
- **Management Reports** — 15+ report types across three categories:
  - *Registry & Inventory*: Meter, Premise, ERF, Ward, Workbase, Service Provider, User reports
  - *Activity Reports*: No Access, User Activity, Normalisation, Anomaly reports
  - *Revenue Reports*: Prepaid Revenue Report & Dashboard
- **Operations Management Center** — tools for workorder management:
  - **WMS Dashboard** — workorder lifecycle analytics (see [Section 7](#7-wms-dashboard))
  - **Operational Teams** — personnel deployment
  - **My Workorders** — view your assigned work
  - **Geo-Fencing** — spatial jurisdiction boundaries
  - **Field Analytics** — deployment performance metrics
  - **Revenue Analytics** — LM prepaid revenue data

#### Local Storage
- **Meter Discovery Forms Storage** — queue of offline meter audit forms
- **Sales Storage** — queue of offline sales data
- **Premise Forms Storage** — queue of offline premise submissions
- **Account Data Queue** — queue of offline account data (FAD) forms

---

## 5. Meter Lifecycle Workflows

The Meters tab supports five field-work workflows. Each follows the same pattern: accept a work order → capture data and photos → submit.

### 5.1 Meter Inspection

**Purpose**: Inspect an existing meter and record its condition.

1. Navigate to the meter (via Meters list or map).
2. Start an **Inspection** workflow.
3. Complete the inspection form:
   - **Meter Number** photo (verification)
   - **Meter Reading** photo (current reading)
   - **Anomaly Photo** (if any issue is found)
   - **Seal Photo** (tamper seal condition)
   - **Keypad Photo** (meter keypad condition)
   - **CB Photo** (circuit breaker condition)
   - **Notes** — any observations
4. Tap **Submit**. The TRN is created with your findings.

### 5.2 Meter Disconnection

**Purpose**: Physically disconnect a meter from service.

1. Navigate to the meter.
2. Start a **Disconnection** workflow.
3. Complete the form:
   - **Meter Reading Evidence** — photo of the final reading
   - **Disconnection Level Evidence** — photo showing the disconnection point
   - **Safety Evidence** — photo confirming safe disconnection
   - **Notes**
4. Submit. The meter status is updated to reflect disconnection.

### 5.3 Meter Reconnection

**Purpose**: Reconnect a previously disconnected meter.

1. Navigate to the meter.
2. Start a **Reconnection** workflow.
3. Complete the form:
   - **Meter Reading Evidence** — photo of the reading at reconnection
   - **Reconnection Evidence** — photo confirming proper reconnection
   - **Notes**
4. Submit.

### 5.4 Meter Removal

**Purpose**: Remove a meter entirely (decommissioning).

1. Navigate to the meter.
2. Start a **Removal** workflow.
3. Complete the form:
   - **Meter Reading Evidence** — final reading before removal
   - **Removal Evidence** — photo of the removed meter
   - **Notes**
4. Submit.

### 5.5 Meter Reading

**Purpose**: Capture a routine meter reading for billing purposes.

1. Navigate to the meter.
2. Start a **Meter Reading** workflow.
3. Capture:
   - **Meter Reading Photo** — clear photo of the meter display
   - **Reading value** — the numeric reading
   - **Token Reading Photo** (if applicable)
4. Submit.

---

## 6. Working Offline

iREPS is designed for offline-first operation. Field workers often work in areas with poor or no connectivity.

### How It Works

1. **Sync Data Before Going Offline**: When online, sync your ward's ERF data from the ERFs tab. This caches ERFs, premises, meters, and TRNs to your device via MMKV storage.

2. **Fill Forms Offline**: When you submit a form without connectivity:
   - The form is saved to a **local queue** on your device
   - You'll see a confirmation that the form was queued
   - You can continue working on other tasks

3. **Automatic Sync**: When connectivity is restored:
   - The background sync service detects the network
   - All queued forms are processed automatically
   - Photos are uploaded to Firebase Storage
   - Form data is submitted to the server via Cloud Functions

### Offline Queues

There are four separate queues visible in Admin → Local Storage:
- **Meter Discovery Forms** — meter audit/discovery submissions
- **Sales Storage** — prepaid sales data
- **Premise Forms** — premise creation/editing submissions
- **Account Data Queue** — Form Account Data (FAD) submissions

### Queue Statuses

| Status | Meaning |
|--------|---------|
| **PENDING** | Waiting to be sent |
| **SYNCING** | Currently being submitted |
| **SUCCESS** | Successfully submitted (removed next cycle) |
| **FAILED** | Submission failed — will retry automatically |

### Managing Offline Data

- **View queues**: Admin → Local Storage → select a queue
- **Ward ERF Sync**: ERFs tab → Sync — refresh cached data for a ward
- **Drop a ward**: ERFs tab → Drop — removes cached data for that ward

---

## 7. WMS Dashboard

The **Work Management System (WMS) Dashboard** is the operational cockpit for managers and supervisors.  
**Location**: Admin → Operations Management Center → WMS Dashboard

### What You'll See

- **Header Card**: Current ward name, LM name, and an Office/Field work split badge
- **Manager Controls**: Summary stats — Total, Awaiting, Accepted, Rejected, Completed, Cancelled
- **Work Source Breakdown**: Counts by Office-issued vs Field-created
- **Workflow State Breakdown**: Counts by ISSUED, ACCEPTED, REJECTED, COMPLETED, CANCELLED
- **Execution Outcomes**: Counts by Success, No Access, No Reading, and other outcomes
- **Top Buckets**: Progress bars for the top 3 work assignment buckets
- **MLCT Breakdown**: 5 rows showing each meter lifecycle type with workflow counts
- **Attention Queue**: Items needing manager attention:
  - 🔴 **Rejected Work** — workorders rejected by field workers
  - 🟡 **Awaiting Over 1 Hour** — work not accepted/rejected within 1 hour
  - 🟡 **Accepted Over 4 Hours** — accepted but not completed within 4 hours
  - 🔴 **No Access** — completed without physical meter access
  - 🟡 **No Reading** — completed without valid meter reading
  - 🟡 **Data Check** — unexpected or missing workflow state

### Filtering

Use the dashboard filter bar to narrow the view:
- **Date**: Today, Yesterday, This Week, or All
- **Source**: All, Office only, or Field only

---

## 8. Roles & Permissions

iREPS has a 6-level role hierarchy. Each role has different capabilities.

| Role | Code | Level | What They Can Do |
|------|------|-------|------------------|
| **Service Provider User** | SPU | 5 | Full system access. Create ADM and MNG users. Manage dropdown settings. Access all reports. |
| **Admin** | ADM | 4 | Manage MNG users. Configure system settings. Access all reports. Authorize field workers. |
| **Manager** | MNG | 3 | Invite SPV users. Authorize FWR users. View operations dashboard. Oversee field teams. |
| **Supervisor** | SPV | 2 | Supervise field teams. Quality assurance. View team activity. |
| **Field Worker** | FWR | 1 | Data collection. Meter discovery. Premise capture. Execute assigned workorders. |
| **Guest** | GST | 0 | Unauthenticated. Can only sign in or sign up. |

> **Note**: Higher roles inherit the permissions of lower roles. For example, an Admin (ADM) can do everything a Manager (MNG), Supervisor (SPV), and Field Worker (FWR) can do.

---

## 9. Glossary

### Business Terms

| Term | Meaning |
|------|---------|
| **ERF** | A cadastral land parcel — the smallest land division in the municipal property system |
| **TRN** | Transaction — a work record capturing a field action (inspection, reading, installation, etc.) |
| **AST** | Asset — a meter or infrastructure item (electricity or water) |
| **LM** | Local Municipality — the geographic boundary of a municipal administration |
| **Ward** | An administrative subdivision within an LM |
| **Workbase** | The default LM scope assigned to a user |
| **Premise** | A physical property location tied to an ERF |

### Workflow Terms

| Term | Meaning |
|------|---------|
| **ISSUED** | Workorder created and assigned to a user |
| **ACCEPTED** | User accepted the workorder |
| **REJECTED** | User rejected the workorder |
| **COMPLETED** | Workorder executed with an outcome |
| **CANCELLED** | Workorder cancelled by a manager |
| **Success** | Work completed with valid data captured |
| **No Access** | Unable to physically access the meter |
| **No Reading** | Access available but no valid reading captured |
| **N/A** | No outcome recorded yet |

### Technical Terms

| Term | Meaning |
|------|---------|
| **WMS** | Work Management System — workorder lifecycle management |
| **MLCT** | Meter Lifecycle Type — categories of meter work (Inspection, Disconnection, Reconnection, Removal, Reading) |
| **WDB** | Workorder Dashboard — the WMS analytics dashboard |
| **PCode** | Place Code — a geographic code in the admin hierarchy (e.g., `lmPcode`, `wardPcode`) |
| **Geo-Scope** | The five-level geographic hierarchy (LM → Ward → ERF → Premise → Meter) |
| **Offline Queue** | Locally stored form submissions waiting to sync when connectivity returns |
| **MMKV** | High-performance local storage used for caching data on the device |

---

> **Need Help?** Contact your Service Provider administrator or system manager.  
> **Document Version**: 1.0 — Last updated: July 2025
