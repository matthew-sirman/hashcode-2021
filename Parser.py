class Parser:
    def __init__(self, input_file: str) -> None:
        self.__in_file = input_file
        lines = []
        with open(input_file, "r") as in_file:
            for line in in_file:
                lines.append(line)

