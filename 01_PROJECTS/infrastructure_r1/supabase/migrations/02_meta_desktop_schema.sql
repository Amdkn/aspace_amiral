-- Migration 02: Meta Desktop Sovereign Hierarchy
-- Objective: Structure pages, sub-pages, and entities for the Meta Desktop

-- 1. Sovereign Spaces (Kernel, Life, Business, Solarpunk)
CREATE TABLE IF NOT EXISTS desktop_spaces (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug TEXT UNIQUE NOT NULL, -- e.g., 'kernel', 'life'
    name TEXT NOT NULL,
    icon TEXT,
    color TEXT,
    active BOOLEAN DEFAULT TRUE
);

-- 2. Hierarchical Pages (Recursive Tree)
CREATE TABLE IF NOT EXISTS desktop_pages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    space_id UUID REFERENCES desktop_spaces(id) ON DELETE CASCADE,
    parent_id UUID REFERENCES desktop_pages(id) ON DELETE CASCADE,
    path TEXT NOT NULL, -- e.g., '/telemetry', '/kanban'
    title TEXT NOT NULL,
    icon TEXT,
    role_access TEXT[] DEFAULT '{ALPHA, A1, A2}', -- RBAC for personas
    metadata JSONB DEFAULT '{}'::jsonb,
    UNIQUE(space_id, path)
);

-- 3. Sovereign Entity Registry (Doctors, Companions, etc.)
CREATE TABLE IF NOT EXISTS desktop_entities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    external_id TEXT UNIQUE, -- e.g., 'doctor-13', 'rick'
    name TEXT NOT NULL,
    role TEXT,
    persona_level TEXT NOT NULL, -- 'A0', 'A1', 'A2', 'A3'
    status TEXT DEFAULT 'INACTIVE',
    metadata JSONB DEFAULT '{}'::jsonb
);

-- 4. Telemetry Stream Definitions
CREATE TABLE IF NOT EXISTS telemetry_streams (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_id UUID REFERENCES desktop_entities(id) ON DELETE CASCADE,
    metric_name TEXT NOT NULL,
    unit TEXT,
    target_value NUMERIC,
    current_value NUMERIC,
    status_formula TEXT, -- e.g., 'val > 80 ? green : yellow'
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Insert Initial Spaces
INSERT INTO desktop_spaces (slug, name, icon, color) VALUES
('kernel', 'Kernel OS', '⚙️', 'sky'),
('life', 'Life OS', '🌿', 'nature'),
('business', 'Business OS', '💼', 'sky'),
('solarpunk', 'Solarpunk OS', '🌞', 'solar')
ON CONFLICT (slug) DO NOTHING;

-- Create Indexes
CREATE INDEX IF NOT EXISTS idx_pages_parent ON desktop_pages(parent_id);
CREATE INDEX IF NOT EXISTS idx_pages_space ON desktop_pages(space_id);
CREATE INDEX IF NOT EXISTS idx_entities_persona ON desktop_entities(persona_level);
