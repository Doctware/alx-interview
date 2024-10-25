#!/usr/bin/python3
""" this module implement log parsing """
import sys
import signal
import re


# Initialize metrics
total_file_size = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


# Regular expression pattern for the input log line format
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>.*?)\] '
    r'"GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)'
)


def print_stats():
    """
    Prints the statistics collected so far,
    including total file size and status code counts.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


def signal_handler(sig, frame):
    """
    Signal handler for keyboard interruption (CTRL + C).
    Prints the collected statistics before exiting.
    """
    print_stats()
    sys.exit(0)


# Set up signal handling for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
for line in sys.stdin:
    try:
        # Use regex to parse the line
        match = log_pattern.match(line)
        if match:
            status_code = int(match.group('status'))
            file_size = int(match.group('size'))

            # Update total file size
            total_file_size += file_size

            # Increment status code count if it's in our list
            if status_code in status_code_count:
                status_code_count[status_code] += 1

            # Increment line count
            line_count += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

    except Exception as e:
        # Skip lines that don't match the expected format
        continue

# If the program ends naturally, print final stats
print_stats()
