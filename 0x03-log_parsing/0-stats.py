#!/usr/bin/python3
"""
This module contains a script that parses the stdin
and computes certain metrics.
"""
import sys


status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
total_size  = 0

while True:
    try:
        file_sizes = 0
        for i in range(10):
            line = sys.stdin.readline()
            line = line.split(" ")
            if len(line) != 9:
                break
            try:
                code = int(line[7])
                file_size = int(line[8].rstrip("\n"))
            except ValueError:
                continue
            if code in status_codes:
                status_codes[code] += 1
                file_sizes += file_size

        if not file_sizes:
            break

        total_size += file_sizes
        print("File size: {}".format(total_size))
        for code in sorted(status_codes):
            if status_codes[code]:
                print("{}: {}".format(code, status_codes[code]))

    except KeyboardInterrupt:
        print("File size: {}".format(total_size))
        for code in sorted(status_codes):
            if status_codes[code]:
                print("{}: {}".format(code, status_codes[code]))
        raise KeyboardInterrupt