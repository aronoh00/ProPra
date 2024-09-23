import argparse_subcommand as ap_sub

meaning = "some help text for the subcommand"


def add_arguments(parser: ap_sub.ArgumentParser):   # configure the subcommand's sub-argparser
    parser.usage = "mlh lsnew [-h] [-age maxage] file [file ...]"
    parser.add_argument("-a", "--age", default='48h')
    parser.add_argument("file", type=str, nargs="+", help="file to commit")

def execute(args: ap_sub.Namespace):    # run the subcommand
    print(args)