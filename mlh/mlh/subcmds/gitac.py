import argparse_subcommand as ap_sub

meaning = "some help text for the subcommand"


def add_arguments(parser: ap_sub.ArgumentParser):   # configure the subcommand's sub-argparser
    parser.usage = "mlh gitac [-h] [-m commit msg] file [file ...]"
    parser.add_argument("-m", "--message", type=str, help="commit msg")
    parser.add_argument("file", type=str, nargs="+", help="file to commit")

def execute(args: ap_sub.Namespace):    # run the subcommand
    print(args)