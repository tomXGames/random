import math
import matplotlib.pyplot as plt
min = 100000000
shortest = 0
i = 0
fig, ax = plt.subplots()
ax2 = plt.twinx()
while i <= 20:
    time = (math.sqrt(i**2 + 5**2))/2 + ((math.sqrt((20-i)**2 + 5**2)))
    if time < min:
        min = time
        shortest = i
    ax.plot(i-10, time, 'o-', color='grey')
    ax2.plot([-10, i -10],[5, 0], color="lightgrey", alpha=0.01)
    ax2.plot([i-10,10], [0,-5], color="lightgrey", alpha=0.01)
    i += 0.001
print(min, shortest-10)
ax.plot(shortest -10, min, 'o', color="red")
ax2.plot([-10, shortest -10],[5, 0], color="blue")
ax2.plot([shortest-10,10], [0,-5], color="blue")
ax2.plot([-10, +10],[0,0], color="black")
plt.show()