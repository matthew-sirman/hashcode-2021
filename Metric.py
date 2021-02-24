from Solution import Solution


class Metric:
    def __init__(self, sol: Solution) -> None:
        self.__sol = sol

    def calculate(self) -> float:
        pass

