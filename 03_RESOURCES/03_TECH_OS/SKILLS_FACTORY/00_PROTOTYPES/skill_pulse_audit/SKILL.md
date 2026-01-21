# 🛠️ SKILL: Pulse Audit (V1.0)

## 🚩 Purpose
This skill provides a closed-loop system for auditing n8n pulses and ensuring Supabase persistence. It prevents "Null" data injection by validating JSON mapping before execution.

## 🔄 BMad Loop Definition
1. **Trigger**: New incoming pulse signal.
2. **Audit**: Validate `agent_id`, `signal_type`, and `content`.
3. **Correction**: If fields are missing, attempt to map from `body` or apply defaults.
4. **Execution**: Push to n8n webhook.
5. **Verification**: Query Supabase to confirm row count increase.

## 🛠️ Components
- `/scripts/validate_mapping.py`: Pre-flight check for pulse payloads.
- `/scripts/test_persistence.py`: Post-flight verify in Supabase.

## 📜 Usage
`gemini run "Utilise pulse_audit pour valider et injecter : { 'signal': '...' }"`

## ⚠️ Safety Boundaries
- Max 3 retries on persistence failure before triggering a "Manager Alert".
- No deletion permissions on Supabase via this skill.
