# Targeted Batch Planning and Allocation — Field Catalogue

Module **FRM-029** · Baseline **25 September 2026** · Application: **Observed source; release unverified**.

Draft for review. Observed source and documented rules are evidence of implementation intent, not proof of deployment, runtime success or production acceptance. Read the source baseline and open questions before using this as a release-specific lesson.

[Body of Knowledge](targeted-batches-body-of-knowledge.md) · [User Manual](../02-user-manual/web/targeted-batches-user-manual.md) · [Field catalogue](targeted-batches-field-catalogue.md) · [Error register](targeted-batches-error-register.md) · [Practical examples](../10-assessments/targeted-batches-scenarios.md)

## Business definitions

Each row below defines information relevant to this module. A row can describe a structured group; individual source controls are separately inventoried below. Proposed fields have no claimed storage key.

| Field / group | Type | Meaning | Prerequisites and validation | Synthetic example |
| --- | --- | --- | --- | --- |
| Source/upload | File or source selection | Population from which work is prepared. | Validate format and context; do not treat an uploaded row as a discovered meter. | Synthetic sample file |
| Selected rows | Reference set | Exact work population. | Check counts, eligibility and exceptions before confirmation. | Training rows 1–3 |
| Target | User/team reference | Responsibility for the batch. | Server scope and allocation checks apply. | Training Team A |
| Management action | Controlled action | Confirm/allocate/unallocate/delete/take out. | Each action has distinct guards and must be verified separately. | Allocate |

## Source control catalogue

This extraction records literal and dynamic bindings, input types, options, disabled conditions and surrounding branch expressions. A conditional expression may show either branch; read its source before interpreting it as a visibility requirement. Shared wrapper controls are identified as wrappers. An unproven storage mapping or server requirement stays unverified, never silently optional. System-generated fields and transformations still require payload-by-payload acceptance review.

### FRM-029-C001 — pageSize

- **Meaning:** Source control for pageSize; interpret in the business definitions and its enclosing section.
- **UI binding:** `pageSize`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onPageSizeChange(Number(event.target.value))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:340](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L340).

### FRM-029-C002 — sourceFilter

- **Meaning:** Source control for sourceFilter; interpret in the business definitions and its enclosing section.
- **UI binding:** `sourceFilter`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `conditional branch: isRegisterLoading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>              setSourceFilter(event.target.value);<br>              resetToFirstPage();<br>            }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:1099](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1099).

### FRM-029-C003 — statusFilter

- **Meaning:** Source control for statusFilter; interpret in the business definitions and its enclosing section.
- **UI binding:** `statusFilter`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `conditional branch: isRegisterLoading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>              setStatusFilter(event.target.value);<br>              resetToFirstPage();<br>            }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:1115](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1115).

### FRM-029-C004 — Tick every batch listed below

- **Meaning:** Source control for Tick every batch listed below; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `input`; input hint `checkbox`.
- **Visibility/prerequisites:** `conditional branch: isRegisterLoading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!listedIds.length`.
- **Change handling:** `() => ticked.toggleListed(listedIds)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:1147](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1147).

### FRM-029-C005 — Filter TB ID

- **Meaning:** Source control for Filter TB ID; interpret in the business definitions and its enclosing section.
- **UI binding:** `tbIdFilter`; component `input`; input hint `text`.
- **Visibility/prerequisites:** `conditional branch: isRegisterLoading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>                      setTbIdFilter(event.target.value);<br>                      resetToFirstPage();<br>                    }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:1212](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1212).

### FRM-029-C006 — batchTypeFilter

- **Meaning:** Source control for batchTypeFilter; interpret in the business definitions and its enclosing section.
- **UI binding:** `batchTypeFilter`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `conditional branch: isRegisterLoading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>                      setBatchTypeFilter(event.target.value);<br>                      resetToFirstPage();<br>                    }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:1225](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1225).

### FRM-029-C007 — allocationFilter

- **Meaning:** Source control for allocationFilter; interpret in the business definitions and its enclosing section.
- **UI binding:** `allocationFilter`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `conditional branch: isRegisterLoading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>                      setAllocationFilter(event.target.value);<br>                      resetToFirstPage();<br>                    }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:1241](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1241).

### FRM-029-C008 — effectiveAllocatedToFilter

- **Meaning:** Source control for effectiveAllocatedToFilter; interpret in the business definitions and its enclosing section.
- **UI binding:** `effectiveAllocatedToFilter`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `conditional branch: isRegisterLoading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>                      setAllocatedToFilter(event.target.value);<br>                      resetToFirstPage();<br>                    }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:1256](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1256).

### FRM-029-C009 — Filter

- **Meaning:** Source control for Filter; interpret in the business definitions and its enclosing section.
- **UI binding:** `totalFilter`; component `input`; input hint `text`.
- **Visibility/prerequisites:** `conditional branch: isRegisterLoading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>                      setTotalFilter(event.target.value);<br>                      resetToFirstPage();<br>                    }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:1274](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1274).

### FRM-029-C010 — wardFilter

- **Meaning:** Source control for wardFilter; interpret in the business definitions and its enclosing section.
- **UI binding:** `wardFilter`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `conditional branch: isRegisterLoading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>                      setWardFilter(event.target.value);<br>                      resetToFirstPage();<br>                    }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:1288](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1288).

### FRM-029-C011 — Filter Geofence

- **Meaning:** Source control for Filter Geofence; interpret in the business definitions and its enclosing section.
- **UI binding:** `geofenceFilter`; component `input`; input hint `text`.
- **Visibility/prerequisites:** `conditional branch: isRegisterLoading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>                      setGeofenceFilter(event.target.value);<br>                      resetToFirstPage();<br>                    }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:1306](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1306).

### FRM-029-C012 — Filter Created By

- **Meaning:** Source control for Filter Created By; interpret in the business definitions and its enclosing section.
- **UI binding:** `createdByFilter`; component `input`; input hint `text`.
- **Visibility/prerequisites:** `conditional branch: isRegisterLoading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>                      setCreatedByFilter(event.target.value);<br>                      resetToFirstPage();<br>                    }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:1319](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1319).

### FRM-029-C013 — input

- **Meaning:** Source control for input; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `input`; input hint `checkbox`.
- **Visibility/prerequisites:** `conditional branch: isRegisterLoading`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `() => ticked.toggle(upload.id)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-164:1356](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchesPage.jsx#L1356).

### FRM-029-C014 — input

- **Meaning:** Source control for input; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `input`; input hint `checkbox`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `event => setShowAll(event.target.checked)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-163:296](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/TargetedBatchAllocationMapPage.jsx#L296).

### FRM-029-C015 — input

- **Meaning:** Source control for input; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `input`; input hint `file`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `handleFileChange`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-169:126](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/TargetedBatchUploadModal.jsx#L126).

### FRM-029-C016 — For example: allocated to the wrong team

- **Meaning:** Source control for For example: allocated to the wrong team; interpret in the business definitions and its enclosing section.
- **UI binding:** `reason`; component `textarea`; input hint `textarea`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `isUnallocating`.
- **Change handling:** `(event) => setReason(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-168:133](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/TargetedBatchUnallocateModal.jsx#L133).

### FRM-029-C017 — targetId

- **Meaning:** Responsibility for the batch.
- **UI binding:** `targetId`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>              const selected = targetOptions.find(<br>                (target) => target.id === event.target.value,<br>              );<br>              onSelectTarget(selected &#124;&#124; null);<br>            }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-171:107](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/allocation/TargetedBatchAllocationTargetPanel.jsx#L107).

### FRM-029-C018 — pageSize

- **Meaning:** Source control for pageSize; interpret in the business definitions and its enclosing section.
- **UI binding:** `pageSize`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `event => { setPageSize(Number(event.target.value)); setPage(1); }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-172:19](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/draft/TargetedBatchDraftTable.jsx#L19).

### FRM-029-C019 — For example: batched by mistake, the meter belongs to next month's work

- **Meaning:** Source control for For example: batched by mistake, the meter belongs to next month's work; interpret in the business definitions and its enclosing section.
- **UI binding:** `reasonText`; component `textarea`; input hint `textarea`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onReasonChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-174:70](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/rows/TargetedBatchTakeOutWindows.jsx#L70).

### FRM-029-C020 — input

- **Meaning:** Source control for input; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `input`; input hint `checkbox`.
- **Visibility/prerequisites:** `conditional branch: salesRows.length > 0; conditional branch: viewMode === VIEW_MODES.PLANNING`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => setShowNormal(event.target.checked)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-180:459](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/NonGpsBatchPlanningPage.jsx#L459).

### FRM-029-C021 — groupName

- **Meaning:** Source control for groupName; interpret in the business definitions and its enclosing section.
- **UI binding:** `groupName`; component `input`; input hint `radio`.
- **Visibility/prerequisites:** `conditional branch: isOpen && position && typeof document !== "undefined"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `() => setChoice(String(value))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-181:131](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/components/NonGpsQuickSelect.jsx#L131).

### FRM-029-C022 — groupName

- **Meaning:** Source control for groupName; interpret in the business definitions and its enclosing section.
- **UI binding:** `groupName`; component `input`; input hint `radio`.
- **Visibility/prerequisites:** `conditional branch: isOpen && position && typeof document !== "undefined"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `() => {<br>                        setChoice(OTHER);<br>                        otherInputRef.current?.focus();<br>                      }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-181:144](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/components/NonGpsQuickSelect.jsx#L144).

### FRM-029-C023 — otherText

- **Meaning:** Source control for otherText; interpret in the business definitions and its enclosing section.
- **UI binding:** `otherText`; component `input`; input hint `text`.
- **Visibility/prerequisites:** `conditional branch: isOpen && position && typeof document !== "undefined"`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => {<br>                      setOtherText(event.target.value);<br>                      setChoice(OTHER);<br>                    }`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-181:156](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/components/NonGpsQuickSelect.jsx#L156).

### FRM-029-C024 — placeholder

- **Meaning:** Source control for placeholder; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `input`; input hint `type`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-182:85](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/components/NonGpsStreetPlanning.jsx#L85).

### FRM-029-C025 — value

- **Meaning:** Source control for value; interpret in the business definitions and its enclosing section.
- **UI binding:** `value`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-182:100](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/components/NonGpsStreetPlanning.jsx#L100).

### FRM-029-C026 — batchableTargets.length === 0<br>          ? "No batchable Sales meters are available on this street"<br>          : partiallySelected<br>            ? `${selectedCount} of ${batchableTargets.length} batchable Sales meters selected — select the remaining meters`<br>            : allSelected<br>              ? "Deselect all batchable Sales meters on this street"<br>              : "Select all batchable Sales meters on this street"

- **Meaning:** Responsibility for the batch.
- **UI binding:** ``; component `input`; input hint `checkbox`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `batchableTargets.length === 0`.
- **Change handling:** `() => onToggleStreet?.(street)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-182:166](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/components/NonGpsStreetPlanning.jsx#L166).

### FRM-029-C027 — pageSize

- **Meaning:** Source control for pageSize; interpret in the business definitions and its enclosing section.
- **UI binding:** `pageSize`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onPageSizeChange(Number(event.target.value))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-182:210](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/components/NonGpsStreetPlanning.jsx#L210).

### FRM-029-C028 — filters.town

- **Meaning:** Source control for filters.town; interpret in the business definitions and its enclosing section.
- **UI binding:** `filters.town`; component `SelectColumnFilter`; input hint `SelectColumnFilter`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `townOptions`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(value) => onFilterChange("town", value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-182:368](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/components/NonGpsStreetPlanning.jsx#L368).

### FRM-029-C029 — Search Town / Area

- **Meaning:** Source control for Search Town / Area; interpret in the business definitions and its enclosing section.
- **UI binding:** `searchText`; component `input`; input hint `search`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => handleTownSearchChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-182:721](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/components/NonGpsStreetPlanning.jsx#L721).

### FRM-029-C030 — Search street

- **Meaning:** Source control for Search street; interpret in the business definitions and its enclosing section.
- **UI binding:** `searchText`; component `input`; input hint `search`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => handleStreetSearchChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-182:825](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/sales/components/NonGpsStreetPlanning.jsx#L825).

### FRM-029-C031 — Meter, sales-all-meters ID, account, customer or town

- **Meaning:** Source control for Meter, sales-all-meters ID, account, customer or town; interpret in the business definitions and its enclosing section.
- **UI binding:** `rowSearch`; component `input`; input hint `input`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onRowSearchChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-170:145](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/allocation/TargetedBatchAllocationRowsPanel.jsx#L145).

### FRM-029-C032 — pageSize

- **Meaning:** Source control for pageSize; interpret in the business definitions and its enclosing section.
- **UI binding:** `pageSize`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onPageSizeChange(event.target.value)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-170:155](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/allocation/TargetedBatchAllocationRowsPanel.jsx#L155).

### FRM-029-C033 — input

- **Meaning:** Source control for input; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `input`; input hint `checkbox`.
- **Visibility/prerequisites:** `conditional branch: filteredRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `onToggleAllVisibleRows`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-170:178](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/allocation/TargetedBatchAllocationRowsPanel.jsx#L178).

### FRM-029-C034 — input

- **Meaning:** Source control for input; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `input`; input hint `checkbox`.
- **Visibility/prerequisites:** `conditional branch: filteredRows.length === 0`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `!selectable`.
- **Change handling:** `() => onToggleRow(row._rowKey)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-170:211](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/allocation/TargetedBatchAllocationRowsPanel.jsx#L211).

### FRM-029-C035 — pageSize

- **Meaning:** Source control for pageSize; interpret in the business definitions and its enclosing section.
- **UI binding:** `pageSize`; component `select`; input hint `select`.
- **Visibility/prerequisites:** `No direct enclosing conditional captured; check caller and route prerequisites.`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `No direct prop captured`.
- **Change handling:** `(event) => onPageSizeChange(Number(event.target.value))`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-173:56](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/rows/TargetedBatchRowsTable.jsx#L56).

### FRM-029-C036 — takeOut.blockedReason(row) &#124;&#124; "Take this meter out of the batch"

- **Meaning:** Source control for takeOut.blockedReason(row) || "Take this meter out of the batch"; interpret in the business definitions and its enclosing section.
- **UI binding:** ``; component `input`; input hint `checkbox`.
- **Visibility/prerequisites:** `conditional branch: rows.length === 0; conditional branch: takeOut`.
- **Requirement/options:** `Not established by control prop alone`; `See schema / owning shared component`.
- **Editability:** `Boolean(takeOut.blockedReason(row))`.
- **Change handling:** `() => takeOut.onToggle(row.rowKey)`.
- **Validation:** `Not resolved by matching this control to a local schema key; review source validator and backend.`.
- **Persistence:** UI binding shown; persisted path must be verified against payload builder.
- **Evidence:** [FS-173:158](https://github.com/fikilek/ireps-web/blob/ddd3121e2e82334731504e87d755fbdfc29d37ac/src/pages/operations/targeted-batches/rows/TargetedBatchRowsTable.jsx#L158).

## Validation layers and review gaps

Client controls guide input; form schemas check the local form; payload builders can transform values; server validators independently decide acceptance; downstream handlers may update projections. These layers must be checked separately. Blank, zero, false and NAv are not interchangeable.

Eight multi-meter capture permutations remain deferred in the source rule’s release plan; ambiguous Test 15 still needs an agreed association rule. Reported DEV fixes are not a published acceptance certificate.

[Download the detailed control inventory (CSV)](targeted-batches-field-catalogue.csv).

[Inspect the extracted client validation expressions (CSV)](targeted-batches-validation-evidence.csv). Expressions preserve nested conditions; extraction is not a claim that every backend check is mapped.
