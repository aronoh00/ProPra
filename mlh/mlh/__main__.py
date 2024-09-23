import sys
import argparse_subcommand as ap_sub

explanation = "My Little Helpers: a collection of small utility programs"


def main(argv: list[str]):
    parser = ap_sub.ArgumentParser(epilog=explanation)
    parser.scan("subcmds.*")  # or provide module object instead of str
    args = parser.parse_args(argv[1:])
    parser.execute_subcommand(args)  # or supply nothing, then parse_args() will be called internally


if __name__ == '__main__':
    main(sys.argv)
