
import argparse
import getpass
import hashlib
import csv
from pykeepass import PyKeePass

def coalesce(*args):
    for a in args:
        if a is not None:
            return a


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("kdbx", help="input path for keepass database file")
    parser.add_argument("csv", help="output path for csv file")
    parser.add_argument("--keyfile", "-k", default=None, help="path to keyfile, if required")

    args = parser.parse_args()

    with PyKeePass(args.kdbx, password=getpass.getpass(), keyfile=args.keyfile) as kdb, open(args.csv, 'w') as csvfh:
        writer = csv.writer(csvfh)

        for entry in kdb.entries:
            if entry.password:
                h = hashlib.sha1(entry.password.encode('utf-8')).hexdigest().upper()
                writer.writerow([h,
                                 coalesce(entry.username, "").replace("\n", ""),
                                 coalesce(entry.title, "").replace("\n", "")])

