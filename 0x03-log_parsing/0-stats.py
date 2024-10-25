#!/usr/bin/python3
''' 
Module for log parsing.

This script reads lines from standard input in the following format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
It processes each line, keeping track of:
- The total file size across all lines.
- The count of specific status codes (200, 301, 400, 401, 403, 404, 405, 500).
Every 10 lines, or upon keyboard interruption (CTRL + C)
it prints the following statistics:
- Total file size.
- Number of occurrences for each status code that appears at least once.
'''

import sys
import signal

# Initialize total file size and status code counts
total = 0
counter = 0
sc_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
           '403': 0, '404': 0, '405': 0, '500': 0}


def print_data(total):
    '''
    Prints the statistics collected so far.

    Args:
        total (int): The cumulative file size from all processed lines.

    Output:
        - Prints the total file size.
        - Prints the number of occurrences
        for each relevant status code in ascending order.
    '''
    print('File size: {}'.format(total))
    for key, value in sorted(sc_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


def signal_handler(sig, frame):
    '''
    Handles the SIGINT (CTRL + C) signal.

    This function is called when the user interrupts the program using
    CTRL + C.
    It prints the final statistics before terminating the program.

    Args:
        sig: Signal number.
        frame: Current stack frame (unused).
    '''
    print_data(total)
    sys.exit(0)


# Attach the signal handler to handle CTRL + C (SIGINT)
signal.signal(signal.SIGINT, signal_handler)

try:
    # Read each line from stdin
    for line in sys.stdin:
        # Split the line into components based on spaces
        rline = line.split(" ")
        
        # Ensure the line has enough parts (status code and file size at the end)
        if len(rline) > 6:
            code = rline[-2]  # Status code
            if code in sc_dict:
                sc_dict[code] += 1  # Increment count for valid status code
            filesize = int(rline[-1])  # File size
            total += filesize  # Add to the total file size
            counter += 1

        # Print statistics after every 10 lines
        if counter == 10:
            print_data(total)
            counter = 0  # Reset the counter after printing

except Exception as ex:
    # Ignore malformed lines and continue processing
    pass

finally:
    # Print final statistics after program ends or is interrupted
    print_data(total)
