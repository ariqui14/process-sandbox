#!/usr/bin/env python3
"""
sandbox.py - A lightweight process sandbox in Python
Author: Ariel Quinain
GitHub: ariqui14

Features:
- Run commands safely in a subprocess
- Apply CPU and memory limits
- (Optional) stub for network restrictions
"""

import subprocess
import argparse
import sys
import psutil, os, logging, platform

# ---------------------------------
# Logging Setup
# ---------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

# ---------------------------------
# Resource Limits
# ---------------------------------
def set_limits(cpu_limit: int, memory_limit: int):
    """Simulate CPU/memory limit check on Windows."""
    process = psutil.Process(os.getpid())
    logging.info(f"Monitoring process: CPU limit={cpu_limit}s, Memory limit={memory_limit} bytes")
    
    # crude check for memory usage
    mem_usage = process.memory_info().rss
    if mem_usage > memory_limit:
        logging.warning("Memory limit exceeded! (simulated)")
    
    # CPU enforcement would need a monitor loop + termination
# ---------------------------------
# Sandbox Runner
# ---------------------------------
def run_in_sandbox(command: str, cpu_limit=2, memory_limit=256*1024*1024):
    """
    Run a command inside the sandbox.
    - command: string command to run
    - cpu_limit: CPU time limit in seconds
    - memory_limit: memory limit in bytes
    """
    logging.info(f"Running: {command}")

    try:
        kwargs = dict(
        shell=True,
        capture_output=True,
        text=True
        )

        # Only add preexec_fn if NOT on Windows
        if platform.system() != "Windows":
            kwargs["preexec_fn"] = lambda: set_limits(cpu_limit, memory_limit)

        result = subprocess.run(command, **kwargs)

        logging.info(f"Exit Code: {result.returncode}")
        logging.info(f"Output:\n{result.stdout}")
        if result.stderr:
            logging.warning(f"Errors:\n{result.stderr}")
    except Exception as e:
        logging.error(f"Sandbox failed: {e}")


# ---------------------------------
# Network Restriction (Stub)
# ---------------------------------
def restrict_network():
    """
    Placeholder: implement network restrictions here.
    Options:
    - Use unshare/firejail
    - Override socket in Python
    - Run in Docker
    """
    logging.warning("Network restriction not yet implemented.")


# ---------------------------------
# CLI
# ---------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a command in a Python sandbox")
    parser.add_argument("--cmd", required=True, help="Command to run")
    parser.add_argument("--cpu", type=int, default=2, help="CPU time limit (seconds)")
    parser.add_argument("--mem", type=int, default=256, help="Memory limit (MB)")
    parser.add_argument("--no-net", action="store_true", help="Disable network access (not implemented)")

    args = parser.parse_args()

    mem_bytes = args.mem * 1024 * 1024

    if args.no_net:
        restrict_network()

    run_in_sandbox(args.cmd, args.cpu, mem_bytes)
