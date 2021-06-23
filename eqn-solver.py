import re
coefficientFinder = re.compile("-*[0-9]*\.*[0-9]*[a-z]")
numberFinder = re.compile("-*[0-9]*\.*[0-9]*")
class Equation:
    def __init__(self, equation) -> None:
        self.coefficients = {}
        self.sum = 0
        equation = equation.replace(" ", "")
        equation = equation.replace("-", "+-")
        for i, side in enumerate(equation.split("=")):
            for part in side.split("+"):
                if coefficientFinder.fullmatch(part):
                    try:
                        self.coefficients[part[-1]] += float(part[:-1]) * (-1 if i == 1 else 1)
                    except KeyError:
                        self.coefficients[part[-1]] = float(part[:-1]) * (-1 if i == 1 else 1)
                elif numberFinder.fullmatch(part):
                    self.sum += float(part) * (-1 if i == 0 else 1)

class EquationNumber(Exception):
    pass

equations = []
matrix = []
variables = []
sums = []
for i in range(0, int(input("Number of Equations"))):
    eq = Equation(input("Equation: "))
    for var in eq.coefficients.keys():
        if var not in variables:
            variables.append(var)
    equations.append(eq)

if not len(equations) == len(variables):
    raise EquationNumber("The number of equations does not match the number of variables!")

for eq in equations:
    currentRow = []
    for var in variables:
        if var not in eq.coefficients:
            currentRow.append(0)
        else:
            currentRow.append(eq.coefficients[var])
    currentRow.append(eq.sum)
    matrix.append(currentRow)
matrix = sorted(matrix, key=lambda x: x[0])
print(matrix)

print(matrix)