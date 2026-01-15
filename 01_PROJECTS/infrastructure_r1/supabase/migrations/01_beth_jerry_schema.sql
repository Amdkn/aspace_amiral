-- Migration 01: Beth-Jerry Liaison Schema

-- 1. Create agent_signals table (S1 - Life OS)
-- Stores qualitative signals from agents (e.g., "Energy is low")
CREATE TABLE IF NOT EXISTS agent_signals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    agent_id TEXT NOT NULL, -- e.g., "beth", "jerry"
    signal_type TEXT NOT NULL, -- "S1" or "S2"
    content TEXT NOT NULL, -- The raw message
    metadata JSONB DEFAULT '{}'::JSONB -- Extra context
);

-- 2. Create kpi_metrics table (S2 - Business OS)
-- Stores numerical/structured KPI data
CREATE TABLE IF NOT EXISTS kpi_metrics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    metric_name TEXT NOT NULL, -- e.g., "monthly_revenue"
    value NUMERIC NOT NULL,
    unit TEXT, -- e.g., "USD", "count"
    source TEXT NOT NULL, -- e.g., "stripe", "manual"
    metadata JSONB DEFAULT '{}'::JSONB
);

-- 3. Create governance_state table (Governance)
-- Tracks the Beth Veto status (Global System State)
CREATE TABLE IF NOT EXISTS governance_state (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    status TEXT NOT NULL CHECK (status IN ('GREEN', 'YELLOW', 'RED')),
    reason TEXT, -- Why is the system in this state?
    active BOOLEAN DEFAULT TRUE
);

-- Initialize system state to GREEN
INSERT INTO governance_state (status, reason) VALUES ('GREEN', 'System initialized');
