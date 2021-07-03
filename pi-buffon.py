from random import random
import math

n = 10**6
a = 0
for i in range(0, n):
    x = random()*1000
    winkel = random()* math.pi*2
    y = math.sin(winkel)+ x
    if not (y //1)%2 == (x //1) %2:
        a += 1
print(n*2/a)