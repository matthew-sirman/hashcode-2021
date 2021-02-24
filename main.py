import sys
from Parser import Parser
from Solution import Solution
from Output import Output


def main(in_file: str, out_file: str) -> None:
    parser = Parser(in_file)


if __name__ == "__main__":
    if sys.argc != 2:
        print("Please provide 2 arguments for input and output files.")
    else:
        in_file, out_file = sys.argv
        main(in_file, out_file)

