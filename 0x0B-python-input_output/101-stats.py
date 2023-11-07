#!/usr/bin/python3
"""Reads from standard input and computes metrics.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int) -- The accumulated read file size.
        status_codes (dict) -- The accumulated cnt of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_codes = {}
    size = 0
    cnt = 0

    try:
        for lne in sys.stdin:
            if cnt == 10:
                print_stats(size, status_codes)
                cnt = 1
            else:
                cnt += 1

            lne = lne.split()

            try:
                size += int(lne[-1])
            except (IndexError, ValueError):
                pass

            try:
                if lne[-2] in valid_codes:
                    if status_codes.get(lne[-2], -1) == -1:
                        status_codes[lne[-2]] = 1
                    else:
                        status_codes[lne[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
