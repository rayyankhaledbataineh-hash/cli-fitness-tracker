# CLI Fitness Tracker

A Python command-line tool for logging training sessions and monitoring
training load.

Each session logs duration, intensity (RPE 1–10), sleep, soreness, and energy.
Training load is calculated as duration × RPE (the session-RPE method used in
sports science), with per-session and cumulative summaries.

## Commands

- `add` — log a session (all inputs validated for type and range)
- `list` — show all sessions with calculated load
- `delete` — remove a session
- `summarize` — totals and averages across all sessions

## Run

    python3 CLITrackerCode.py
