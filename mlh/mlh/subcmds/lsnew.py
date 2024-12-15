import argparse_subcommand as ap_sub
import argparse
import re
import os.path
import time
from datetime import datetime

meaning = "some help text for the subcommand"


def add_arguments(parser: ap_sub.ArgumentParser):   # configure the subcommand's sub-argparser
    parser.usage = "mlh lsnew [-h] [-age maxage] file [file ...]"
    parser.add_argument("-a", "--age", default='48h', type=parse_age)
    parser.add_argument("file", type=str, nargs="+", help="file to commit")


def execute(args: ap_sub.Namespace):    # run the subcommand
    max_age = args.age
    current_time = time.time()

    valid_files = []
    for filename in args.file:
        try:
            mtime = os.path.getmtime(filename)
            file_age = current_time - mtime
            if file_age < max_age:
                valid_files.append((filename, mtime))
        except FileNotFoundError:
            pass

    valid_files.sort(key=lambda x: x[1], reverse=True)

    for filename, mtime in valid_files:
        formated_time = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
        print(f"{formated_time} {filename}")


# Converts age string to seconds
def parse_age(age: str) -> int:
    match = re.match(r"(\d+)([smhd])", age)
    if not match:
        raise argparse.ArgumentTypeError(f"Invalid age formate: {age}")

    value, unit = int(match.group(1)), match.group(2)
    if unit == "d":
        return value * 86400        # 1 day = 60 * 60 * 24 seconds
    elif unit == "h":
        return value * 3600         # 1 hour = 60 * 60 seconds
    elif unit == "m":
        return value * 60           # 1 minute = 60 seconds
    elif unit == "s":
        return value                # 1 second = 1 second
    else:
        raise argparse.ArgumentTypeError(f"Unsupported time unit: {unit}")
