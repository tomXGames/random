product = 1

for i in range(1, 50000000):
    if i%2 == 0:
        product *= i/(i+1)
    elif i%2 == 1: 
        product *= (i+1) /i

print(product*2)