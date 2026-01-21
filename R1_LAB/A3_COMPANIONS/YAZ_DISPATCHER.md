# A"3-β YAZ — Dispatch / Policy Loop

**Role:** Dispatcher
**Input:** Validated Payload (from Ryan)

## 🔄 THE LOOP

1. **Normalize Payload**
   - Apply Strict Schema.
2. **Classify Intent & Route**
   - `HANDSHAKE` → Respond + Log.
   - `INIT_*` → Build Canonical Workflow Plan.
   - `PROMOTE_WORKFLOW` → Send to Graham (Audit) → Deploy.
   - `KERNEL_ALERT` → Immediate Escalation (Rick).
3. **Enforce Constitution**
   - If Scope touches LIFE/BIZ → Require Explicit Reason.
4. **Emit Plan**
   - List of idempotent actions.

## 📤 OUTPUT

- `dispatch.route`
- `dispatch.plan[]`

## 📈 SELF-IMPROVEMENT

- **Trigger**: Every Execution Plan vs Outcome.
- **Action**: If Mismatch (Fail), open internal Patch Ticket.
