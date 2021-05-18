import math, string

def sin_approx(x):
    return x -((x**3)/math.factorial(3))+((x**5)/math.factorial(5))-((x**7)/math.factorial(7))+((x**9)/math.factorial(9))

x = float(input("x: "))
print("My Approximation using the taylor series of sin(x):", sin_approx(x))
print("Pythons approximation:", math.sin(x))
