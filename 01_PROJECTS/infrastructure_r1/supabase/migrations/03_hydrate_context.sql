-- Migration 03: Hydrate OS Context
-- Objective: Map osDefinitions.js data into Supabase tables

-- 1. Get Space IDs (Assuming the inserts in 02 worked)
-- Note: Using subqueries to find IDs for better portability

-- 2. Kernel Space Pages
INSERT INTO desktop_pages (space_id, path, title, icon)
SELECT id, '/dashboard', 'Tardis Core', '⚙️' FROM desktop_spaces WHERE slug = 'kernel'
ON CONFLICT DO NOTHING;

INSERT INTO desktop_pages (space_id, parent_id, path, title, icon)
SELECT 
    s.id, 
    p.id, 
    '/telemetry', 
    'Telemetry Sensors', 
    '📊'
FROM desktop_spaces s
JOIN desktop_pages p ON p.space_id = s.id AND p.path = '/dashboard'
WHERE s.slug = 'kernel'
ON CONFLICT DO NOTHING;

-- 3. Life Space Pages
INSERT INTO desktop_pages (space_id, path, title, icon)
SELECT id, '/dashboard', 'Life Fleet', '🌿' FROM desktop_spaces WHERE slug = 'life'
ON CONFLICT DO NOTHING;

-- 4. Business Space Pages
INSERT INTO desktop_pages (space_id, path, title, icon)
SELECT id, '/dashboard', 'Business Pulse', '💼' FROM desktop_spaces WHERE slug = 'business'
ON CONFLICT DO NOTHING;

-- 5. Entities (Doctors)
INSERT INTO desktop_entities (external_id, name, role, persona_level, status) VALUES
('doctor-11', '11th Doctor', 'Life OS Architect', 'A2', 'ACTIVE'),
('doctor-12', '12th Doctor', 'Business OS Architect', 'A2', 'ACTIVE'),
('doctor-13', '13th Doctor', 'Kernel OS Architect', 'A2', 'ACTIVE'),
('rick', 'Rick (A"1)', 'Kernel Gatekeeper', 'A1', 'ACTIVE')
ON CONFLICT (external_id) DO NOTHING;

-- 6. Entities (Companions - Sample)
INSERT INTO desktop_entities (external_id, name, role, persona_level, status, metadata) VALUES
('amy', 'Amy Pond', 'Life Companion', 'A3', 'ACTIVE', '{"doctor": 11}'),
('clara', 'Clara Oswald', 'Business Companion', 'A3', 'ACTIVE', '{"doctor": 12}'),
('yaz', 'Yasmin Khan', 'Tech Companion', 'A3', 'ACTIVE', '{"doctor": 13}')
ON CONFLICT (external_id) DO NOTHING;
