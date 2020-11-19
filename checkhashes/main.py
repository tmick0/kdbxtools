
import argparse
import csv
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("password_csv")
    parser.add_argument("hash_dump")

    args = parser.parse_args()

    with open(args.password_csv, 'r') as csvfh, open(args.hash_dump, 'r') as dumpfh:
        reader = csv.reader(csvfh)
        writer = csv.writer(sys.stdout)
        needle_it = iter(reader)
        haystack_it = iter(dumpfh)

        try:
            advance = 3
            while True:
                if advance & 1:
                    needle, username, desc = next(needle_it)
                if advance & 2:
                    haystack, count = next(haystack_it).strip().split(":")

                if needle == haystack:
                    writer.writerow([needle, count, username, desc])

                if needle <= haystack:
                    advance = 1
                else:
                    advance = 2

        except StopIteration:
            pass
        