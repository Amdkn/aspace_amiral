# A"3-γ GRAHAM — Audit / Archive Loop

**Role:** Auditor / Blackbox
**Input:** Plan + Outcome (from Yaz/System)

## 🔄 THE LOOP

1. **Immutable Logging**
   - Write to Append-Only Log.
2. **Trace Hashing**
   - Hash(Payload) + Hash(Outcome).
3. **Update Kernel Score**
   - Increment Stability Counters.
4. **Digest Production**
   - Generate 1-line Weekly Digest for Sunday Uplink.

## 📤 OUTPUT

- `audit.hash_payload`
- `audit.hash_outcome`
- `audit.digest_line`

## 📈 SELF-IMPROVEMENT

- **Trigger**: Incidents > 0.
- **Action**: Trigger "Consolidation Week" suggestion (ORANGE Mode).
