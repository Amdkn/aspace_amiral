# Specification: Beth-Jerry Liaison (Pulse Auditor)

## Overview
Implement a liaison system between Beth (Life OS) and Jerry (Business OS) using n8n as the orchestration engine and Supabase as the persistence layer. The system will audit incoming "Pulses" (KPIs and signals), classify them according to the S1 (Life) / S2 (Business) Canon, and enforce Beth's "Sovereign Veto" logic.

## Functional Requirements
- **Pulse Intake (Beth/Jerry):**
    - Support JSON Pulses (`business_kpi.json` format).
    - Support Text-based signals (e.g., "Energy is low").
- **Audit & Classification (n8n):**
    - **S1 (Life OS - Beth):** Health, Ikigai, and capacity signals. These are preventative and have priority.
    - **S2 (Business OS - Jerry):** Revenue, traction, and offer performance. These are growth-oriented.
- **Persistence (Supabase):**
    - Store pulses in structured tables: `kpi_metrics` for numerical data and `agent_signals` for qualitative alerts.
- **Governance Logic (The Veto):**
    - If an S1 pulse triggers a critical alert (Red), n8n must execute an "Emergency Stop" protocol:
        - Alert Amadeus (A0).
        - Pause processing of S2 (Business) growth objectives.

## Non-Functional Requirements
- **Priority:** S1 signals must be processed with lower latency/higher priority than S2.
- **Auditability:** Every pulse must be timestamped and linked to its source agent.
- **Reliability:** Failed writes to Supabase must trigger a retry mechanism or an alert to Amadeus.

## Acceptance Criteria
- [ ] n8n correctly identifies S1 vs S2 pulses based on metadata/content.
- [ ] Pulses are successfully stored in the correct Supabase tables.
- [ ] A "Red" S1 pulse successfully triggers the Emergency Stop workflow.
- [ ] S2 pulses are blocked or flagged when a Beth Veto is active.

## Out of Scope
- Frontend dashboard implementation (this track focuses on the backend/logic layer).
- Automatic resolution of Beth alerts (requires human/Amadeus intervention).
