import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", type=str, default="argparse.config", help="config file")
parser.add_argument("-m", "--maxdepth", "--depth", "-d", type=int, default=1, help="max depth")
parser.add_argument("-b", "--batch", type=str, nargs="+", required=True, help="list of batch files")
args = parser.parse_args()

print(f"config: {args.config}")
print(f"maxdepth: {args.maxdepth}")
print(f"batch: {args.batch}")
