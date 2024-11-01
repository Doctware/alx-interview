#!/usr/bin/python3
"""
UTF-8 Validation Module

This module provides a method to determine if a given data set
represents a valid UTF-8 encoding.

A character in UTF-8 can be 1 to 4 bytes long, and each byte of
the encoding has specific requirements that must be met for the
data to be considered valid UTF-8.
"""


def validUTF8(data):
    """
    Determines if a given list of integers represents a valid UTF-8 encoding.

    Each integer in the list represents a byte (8 bits), where the least
    significant 8 bits of each integer are considered.

    UTF-8 encoding details:
    - A character in UTF-8 can be 1 to 4 bytes.
    - The first byte in each character indicates the length of the sequence.
    - Following bytes in multibyte characters must start with '10' in binary.

    Args:
        data (List[int]): List of integers, each representingi
        a byte (0 <= byte <= 255).

    Returns:
        bool: True if data represents a valid UTF-8 encoding, else False.
    """
    # Number of bytes remaining in the current UTF-8 character
    remaining_bytes = 0

    # Masks for determining the pattern of the first byte
    first_byte_masks = [
        (0b10000000, 0b00000000),  # 1-byte character (0xxxxxxx)
        (0b11100000, 0b11000000),  # 2-byte character (110xxxxx)
        (0b11110000, 0b11100000),  # 3-byte character (1110xxxx)
        (0b11111000, 0b11110000)   # 4-byte character (11110xxx)
    ]

    # Loop over each byte in the data set
    for byte in data:
        # Only consider the last 8 bits of each integer
        byte &= 0xFF

        if remaining_bytes == 0:
            # Determine how many bytes are expected in this UTF-8 character
            for mask, pattern in first_byte_masks:
                if byte & mask == pattern:
                    remaining_bytes = mask.bit_length() - 1
                    break
            else:
                # No valid starting byte pattern found
                return False
        else:
            # Check if this byte is a continuation byte (10xxxxxx)
            if byte & 0b11000000 != 0b10000000:
                return False

        remaining_bytes -= 1

    # If all characters were matched correctly, remaining_bytes should be 0
    return remaining_bytes == 0
