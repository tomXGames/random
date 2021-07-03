import time
product = 2
start = time.time()
for i in range(1, 10000000):
    if i%2 == 0:
        product *= i/(i+1)
    elif i%2 == 1: 
        product *= (i+1) /i
print(product)
end = time.time()
print(end - start)