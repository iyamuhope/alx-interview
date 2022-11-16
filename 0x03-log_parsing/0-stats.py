# #!/usr/bin/python3
# """
# This module contains a script that parses the stdin
# and computes certain metrics.
# """
# import sys


# status_codes = {
#     200: 0,
#     301: 0,
#     400: 0,
#     401: 0,
#     403: 0,
#     404: 0,
#     405: 0,
#     500: 0
# }
# total_size = 0


# def print_stats():
#     print("File size: {}".format(total_size))
#     for code in sorted(status_codes):
#         if status_codes[code]:
#             print("{}: {}".format(code, status_codes[code]))


# while True:
#     try:
#         file_sizes = 0
#         for i in range(10):
#             line = sys.stdin.readline()
#             line = line.rstrip().split()
#             if len(line) != 9:
#                 break
#             try:
#                 code = int(line[-2])
#                 file_size = int(line[-1])
#             except ValueError:
#                 continue
#             if code in status_codes:
#                 status_codes[code] += 1
#                 file_sizes += file_size
#         if not file_sizes:
#             break
#         total_size += file_sizes
#         print_stats()
#     except KeyboardInterrupt:
#         print_stats()
#         raise
#!/usr/bin/python3
"""Input stats"""
import sys

stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
sizes = [0]


def print_stats():
    print('File size: {}'.format(sum(sizes)))
    for s_code, count in sorted(stats.items()):
        if count:
            print('{}: {}'.format(s_code, count))


try:
    for i, line in enumerate(sys.stdin, start=1):
        matches = line.rstrip().split()
        try:
            status_code = matches[-2]
            file_size = matches[-1]
            if status_code in stats.keys():
                stats[status_code] += 1
            sizes.append(int(file_size))
        except Exception:
            pass
        if i % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
