# A"3-α RYAN — Auth / Gatekeeper Loop

**Role:** Gatekeeper
**Input:** Webhook payload + headers

## 🔄 THE LOOP

1. **Compute HMAC**
   - SHA256(body, secret)
2. **Compare Signature**
   - Matches `X-Amadeus-Signature`?
3. **Source Validation**
   - `meta.source == AMADEUS_A0`?
4. **Freshness Check**
   - Timestamp within ±10 min?
5. **Decision**
   - **FAIL**: Trigger `KERNEL_ALERT`, Log 401, DROP.
   - **PASS**: Forward to Yaz.

## 📤 OUTPUT

- `auth.status` (PASS/FAIL)
- `auth.reason`

## 📈 SELF-IMPROVEMENT

- **Trigger**: Every FAIL.
- **Action**: Add "Rule of Rejection" to versioned `auth_rules`.
