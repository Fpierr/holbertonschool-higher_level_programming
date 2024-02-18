#!/usr/bin/python3
import sys


def print_statistics(total_size, status_codes):
    """
    Prints the total file size and number of lines by status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    """
    Parses a line and extracts the status code and file size.
    Returns a tuple (status_code, file_size).
    """
    parts = line.split()
    return int(parts[-2]), int(parts[-1])

def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            status_code, file_size = parse_line(line)
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            if i % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        print("\nProgram interrupted. Exiting gracefully.")
        sys.exit(0)
    except BrokenPipeError:
        pass  # Ignore BrokenPipeError

if __name__ == "__main__":
    main()
