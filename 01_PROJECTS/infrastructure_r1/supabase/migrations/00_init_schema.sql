-- Initialize A'Space OS Sovereign Memory Schema

-- Table for business health signals
CREATE TABLE IF NOT EXISTS pulses (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    metric TEXT NOT NULL,
    value NUMERIC NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb
);

-- Table for global OS state tracking
CREATE TABLE IF NOT EXISTS system_state (
    key TEXT PRIMARY KEY,
    value JSONB NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Index for faster metric lookups
CREATE INDEX IF NOT EXISTS idx_pulses_metric ON pulses(metric);
CREATE INDEX IF NOT EXISTS idx_pulses_timestamp ON pulses(timestamp);
