from Solution import Solution


class Output:
    def __init__(self, sol: Solution, out_file: str) -> None:
        self.__output_file
        self.__sol = sol

    def write(self) -> None:
        with open(self.__output_file, "w"):
            pass

