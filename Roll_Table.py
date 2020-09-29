from bisect import bisect_left
import numpy as np

# As designed by Dan on StackOverflow:
# https://stackoverflow.com/questions/57217923/what-are-pythonic-methods-for-implementing-random-roll-tables

class OptionsWeightsLengthMismatchException(BaseException):
    """Raises when the number of elements in the options list doesn't match the number of elements in the weight list."""
    pass

# Using an class (OOP approach):
class RollTable:

    def __init__(self, options, weights) -> "RollTable":
        self.options = options
        print(np.array([1, 2]))
        print(np.array(weights))
        self.weights = np.array(weights)
        self._validate_inputs()
        pdf = weights/np.sum(weights)
        self.cdf = np.cumsum(pdf)

    def _validate_inputs(self) -> None:
        if len(self.options) != self.weights.size:
            raise OptionsWeightsLengthMismatchException(f"options and weights must have the same number of elements.")
        if max(self.weights.shape) != np.prod(self.weights.shape): # i.e. make sure it's 1D
            raise ValueError("Weights must be 1D, i.e. only one non-singular dimension.")

    def get_item(self):
        roll = np.random.random()
        idx = bisect_left(self.cdf, roll)
        return self.options[idx]


if __name__ == '__main__':
    encounters = ['Gravitite Bulettes', 'Strong Current', 'Wave of Despair', 'Dispel Magic Wave', 'Roperoid', 'Refuge']
    weights = []
    for _ in range(len(encounters)):
        weights.append(1)

    table_1 = RollTable(encounters, np.array(weights))

    for _ in range(10):
        print(table_1.get_item())
