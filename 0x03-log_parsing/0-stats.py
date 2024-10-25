#!/usr/bin/python3
""" this module implement log parsing """
import sys
import signal


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
        # Split the line and extract the required elements
        parts = line.split()
        if len(parts) != 10:
            continue

        # Extract IP, date, request, status code, and file size
        ip_address = parts[0]
        date = parts[3][1:]
        request = parts[5] + ' ' + parts[6] + ' ' + parts[7]
        status_code = int(parts[8])
        file_size = int(parts[9])

        # Only process lines matching the specific request pattern
        if request == '"GET /projects/260 HTTP/1.1"':
            total_file_size += file_size

            # Increment status code count if it's in our list
            if status_code in status_code_count:
                status_code_count[status_code] += 1

            # Increment line count
            line_count += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

    except (ValueError, IndexError):
        # Skip lines that don't match the expected format
        continue

# If the program ends naturally, print final stats
print_stats()
