# Implementation Plan: Beth-Jerry Liaison (Pulse Auditor)

Implementation of the n8n-based bridge between Beth (Life OS) and Jerry (Business OS) with Supabase persistence and Veto logic.

## Phase 1: Infrastructure & Schema [phase:design]
- [x] Task: Supabase - Initialize Schema 49f41b0
    - [ ] Create `kpi_metrics` table for numerical pulse data.
    - [ ] Create `agent_signals` table for qualitative/textual alerts.
    - [ ] Create `system_state` table to track the "Beth Veto" status (🟢/🟡/🔴).
    > **Note (2026-01-15):** Renamed `system_state` to `governance_state` to avoid conflict with existing generic `system_state` KV table.
- [ ] Task: n8n - Connection Setup
    - [ ] Configure Supabase credentials in n8n.
    - [ ] Set up a webhook or file-watch trigger for incoming pulses.
- [ ] Task: Conductor - User Manual Verification 'Infrastructure & Schema' (Protocol in workflow.md)

## Phase 2: Classification & Audit [phase:dev]
- [ ] Task: n8n - Build Classification Workflow
    - [ ] Implement logic to distinguish S1 (Life) from S2 (Business) based on source/content.
    - [ ] Write S1 signals to `agent_signals`.
    - [ ] Write S2/KPI data to `kpi_metrics`.
- [ ] Task: Test - Pulse Storage
    - [ ] Create test pulses for both S1 and S2.
    - [ ] Verify correct routing and insertion in Supabase.
- [ ] Task: Conductor - User Manual Verification 'Classification & Audit' (Protocol in workflow.md)

## Phase 3: Veto Logic & Governance [phase:dev]
- [ ] Task: n8n - Implement Veto Protocol
    - [ ] Detect "Red" status in S1 pulses.
    - [ ] Update `system_state` to `HALT` on S1 Red.
    - [ ] Create a guard clause in S2 processing: if `system_state` is Red, block S2 storage/action.
- [ ] Task: Notification - Amadeus Alert
    - [ ] Implement a notification node (e.g., Email or local log) to alert Amadeus on Veto.
- [ ] Task: Test - Veto Enforcement
    - [ ] Send S1 Red pulse and verify S2 processing is blocked.
    - [ ] Verify Amadeus receives the notification.
- [ ] Task: Conductor - User Manual Verification 'Veto Logic & Governance' (Protocol in workflow.md)

## Phase 4: Final Integration & Cleanup [phase:test]
- [ ] Task: Verification - End-to-End Pulse Cycle
    - [ ] Run a full cycle from pulse generation to Supabase persistence.
- [ ] Task: Documentation - Update SOP
    - [ ] Document how to reset the Veto status manually in Supabase.
- [ ] Task: Conductor - User Manual Verification 'Final Integration & Cleanup' (Protocol in workflow.md)
