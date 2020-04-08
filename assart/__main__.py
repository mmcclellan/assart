#!/usr/bin/env python3
import argparse
import boto3
import os


def main():
    parser = argparse.ArgumentParser(description='A simple S3 analytics reporting tool')
    parser.add_argument(
        '-u', '--unit', required=False, type=str, choices=['kB', 'MB', 'GB'], help='Unit of Size')
    args = parser.parse_args()
    s3 = boto3.resource('s3')
    buckets = list(s3.buckets.all())
    records = []
    for bucket in buckets:
        record = {}
        record['bucket_name'] = bucket.name
        record['creation_date'] = str(bucket.creation_date)
        records.append(record)
    print(records)


if __name__ == "__main__":
    main()
