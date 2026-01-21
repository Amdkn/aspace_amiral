# Kernel - A'Space OS Core Logic

## Purpose
This directory contains the **consolidated core logic** of the A'Space OS.
Following Rick's (R0) directive: "I'm seeing core logic buried in `01_PROJECTS`. That's rookie stuff."

## Contents

### `pulse_logger.py`
Core business KPI logging functionality. Used by:
- `01_PROJECTS/pulse.py` - CLI interface for logging pulses
- `verify_phase_1.py` and `verify_phase_2.py` - Verification scripts

**Key Functions:**
- `log_pulse(metric, value)` - Logs a business KPI pulse with timestamp

## Architecture
The kernel follows the **Simple Loop Architecture**:
1. **Conductor** (`Amiral's Conductor`) plans and orchestrates
2. **Ralph** (`Gemini Ralph Loop`) executes tasks in loops
3. **BMad** (`bmad-method`) provides the reference manual

## Usage
```python
# Import from kernel
import sys
sys.path.append('kernel')
from pulse_logger import log_pulse

# Log a pulse
log_pulse("revenue", 1500.50)
```

## Migration Notes
- Original location: `01_PROJECTS/pulse_monitor/02_DEV/pulse_logger.py`
- Consolidated to: `kernel/pulse_logger.py`
- Original files remain for backward compatibility during transition

## Platform Notes
- **Windows**: Uses `msvcrt` for file locking
- **Linux/macOS**: Uses `fcntl` for file locking (implemented)

---
**Status:** Phase 1 - Anti-fragile Foundation
**Author:** R0 (Rick)
