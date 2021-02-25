import sys
from Parser import Parser
from Solution import Solution
from Output import Output
from Metric import Metric

def main(in_file: str, out_file: str) -> None:
    parser = Parser(in_file)
    data_obj = parser.create_input() 
    print("data parsed!")
    sol = Solution(data_obj)
    
    print(f'Score: {Metric(sol).calculate()}')

    with open(out_file, 'w') as f:
        f.write(str(sol))

    #out = Output(sol, out_file)

    #out.write()


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) <= 2:
        print("Please provide 2 arguments for input and output files.")
        print("Running a.txt with output lol.txt")
        in_file = 'datasets/a.txt'
        out_file = 'output.txt'
    else:
        _, in_file, out_file = sys.argv
    main(in_file, out_file)

