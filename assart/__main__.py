#!/usr/bin/env python3
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description='A simple S3 analytics reporting tool')
    parser.add_argument(
        '-u', '--unit', required=False, type=str, choices=['kB', 'MB', 'GB'], help='Unit of Size')
    args = parser.parse_args()
    print("Hello World!")
    if args.unit:
        print("Units:", args.unit)


if __name__ == "__main__":
    main()
