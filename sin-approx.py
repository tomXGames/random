import math

x = math.pi/2
result = x

for i in range(1, 1000000):
    result = result*(1-(x/(math.pi*i)))*(1-(x/(math.pi*i*-1)))

print("Approximation: ", result)
print("math.sin(x): ", math.sin(x))

