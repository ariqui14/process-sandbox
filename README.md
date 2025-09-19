# process-sandbox
A lightweight tool that runs commands in a restricted environment to demonstrate Linux capability with tools like 'subprocess'. 'os'. etc...

This Sandbox should run a given command, restrict CPU or Memory usage, optionally block network access

There's a basic command runner (MVP)
  -Use subprocess.run() to run any user-provided command.
  -Capture and display stdout/stderr

Use the Python resource module (resource.setrlimit) to limit CPU time and memory usage for the process. 

Blocking Network Access
-use subprocess with unshare or firejail
-or wrap socket in Python to deny new connections

Users can add a JSON/YAML config

Logging uses Python's logging module

#Usage examples

