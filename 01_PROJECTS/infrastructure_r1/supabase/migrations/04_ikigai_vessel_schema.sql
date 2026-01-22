-- Migration 04: Ikigai & Vessel Hierarchy
-- Objective: Map USS Orville, USS Discovery and Crew Roles

-- 1. Vessels Table
CREATE TABLE IF NOT EXISTS vessels (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug TEXT UNIQUE NOT NULL, -- 'orville', 'discovery'
    name TEXT NOT NULL,
    class TEXT DEFAULT 'GALAXY_OS',
    status TEXT DEFAULT 'DOCKING',
    metadata JSONB DEFAULT '{}'::jsonb
);

-- 2. Ship Decks (Hierarchical Navigation within Vessles)
CREATE TABLE IF NOT EXISTS vessel_decks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    vessel_id UUID REFERENCES vessels(id) ON DELETE CASCADE,
    level INTEGER NOT NULL,
    name TEXT NOT NULL,
    function TEXT, -- 'Command', 'Engineering', 'Medical', 'Botanical'
    metadata JSONB DEFAULT '{}'::jsonb
);

-- 3. Crew Assignments (Linking Entities to Ship Decks)
CREATE TABLE IF NOT EXISTS crew_assignments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_id UUID REFERENCES desktop_entities(id) ON DELETE CASCADE,
    deck_id UUID REFERENCES vessel_decks(id) ON DELETE CASCADE,
    role_description TEXT,
    active BOOLEAN DEFAULT TRUE,
    joined_at TIMESTAMPTZ DEFAULT NOW()
);

-- Insert Initial Vessels
INSERT INTO vessels (slug, name, class) VALUES
('orville', 'USS Orville', 'Harmonic_Explorer'),
('discovery', 'USS Discovery', 'Science_Pathfinder')
ON CONFLICT (slug) DO NOTHING;

-- Map Sample Decks for Orville (Beth Harmony)
INSERT INTO vessel_decks (vessel_id, level, name, function)
SELECT id, 1, 'Bridge', 'Command' FROM vessels WHERE slug = 'orville'
UNION ALL
SELECT id, 5, 'Bio-Regeneration', 'Medical' FROM vessels WHERE slug = 'orville'
UNION ALL
SELECT id, 8, 'Social Lounge', 'Harmony' FROM vessels WHERE slug = 'orville'
ON CONFLICT DO NOTHING;

-- Map Sample Decks for Discovery (Beth Growth)
INSERT INTO vessel_decks (vessel_id, level, name, function)
SELECT id, 1, 'Spore Drive Core', 'Engineering' FROM vessels WHERE slug = 'discovery'
UNION ALL
SELECT id, 10, 'Universal Library', 'Knowledge' FROM vessels WHERE slug = 'discovery'
ON CONFLICT DO NOTHING;
