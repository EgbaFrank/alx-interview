#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""
import signal
import sys
import re


pattern = re.compile(r'''
    ^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}   # IP Address
    \s-\s\[\d{4}-\d{2}-\d{2}              # Date (YYYY-MM-DD)
    \s\d{2}:\d{2}:\d{2}\.\d{6}\]          # Time (HH:MM:SS.microseconds)
    \s"GET\s/projects/260\sHTTP/1.1"        # HTTP request
    \s(\d{3})                             # Status code
    \s(\d+)$                              # File size
''', re.VERBOSE)

line_count = 0
statuses = {}
set_status = {200, 301, 400, 401, 403, 404, 405, 500}
total_size = 0


def print_stats():
    """Prints accumulated file size and status counts"""
    print(f"File size: {total_size}", flush=True)
    for key in sorted(statuses):
        print(f"{key}: {statuses[key]}", flush=True)


def handle_signal(sig, frame):
    """Handles SIGINT (CRL + C)"""
    print_stats()
    sys.exit(0)

# Capture SIGINT (Ctrl + C)
signal.signal(signal.SIGINT, handle_signal)


for line in sys.stdin:
    line_count += 1

    match = pattern.match(line.strip())

    if match:
        status, file_size = match.groups()

        try:
            status = int(status)
        except ValueError:
            continue

        if status in set_status:
            statuses[status] = statuses.get(status, 0) + 1

        total_size += int(file_size)

        if line_count == 10:
            print_stats()
            line_count = 0
