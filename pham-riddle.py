import matplotlib.pyplot as plt
import random

point = [0,0]

def t1(matrix):
    return [matrix[0] * 0.86 + matrix[1] * 0.03 + 0, matrix[0] * -0.03 + matrix[1] * 0.86 + 1.5]

def t2(matrix):
    return [matrix[0] * 0.2 + matrix[1] * -0.25 + 0, matrix[0] * 0.21 + matrix[1] * 0.23 + 1.5]

def t3(matrix):
    return [matrix[0] * -0.15 + matrix[1] * 0.27 + 0, matrix[0] * 0.25 + matrix[1] * 0.26 + 0.45]

def t4(matrix):
    return [matrix[0] * 0 + matrix[1] * 0 + 0, matrix[0] * 0 + matrix[1] * 0.17 + 0]

for i in range(5000):
    z = random.randint(1,100)
    if(z <= 83): point = t1(point)
    elif(84 <= z <= 91): point = t2(point)
    elif (92 <= z <= 99): point = t3(point)
    else: point = t4(point)
    plt.plot(point[0], point[1], ".")
        
plt.show()