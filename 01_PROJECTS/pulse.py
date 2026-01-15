import argparse
import sys
import os

# Add the 02_DEV directory to the path to import pulse_logger
sys.path.append(os.path.join(os.path.dirname(__file__), "pulse_monitor/02_DEV"))

from pulse_logger import log_pulse

def main():
    parser = argparse.ArgumentParser(description="A'Space OS Pulse CLI - Log business KPIs.")
    parser.add_argument("--metric", type=str, required=True, help="Name of the metric to log.")
    parser.add_argument("--value", type=float, required=True, help="Value of the metric.")
    
    args = parser.parse_args()
    
    try:
        log_pulse(args.metric, args.value)
        print(f"SUCCESS: Successfully logged pulse: {args.metric} = {args.value}")
    except Exception as e:
        print(f"ERROR: Error logging pulse: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
