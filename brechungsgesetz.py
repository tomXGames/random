import math

medium = [1, 1.00024, 1.00026, 1.00028, 1.0003, 1.0003]
angle = math.radians(87)
for i in range(1, len(medium)):
    n1 = medium[i-1]
    n2 = medium[i]
    angle = math.asin((n1*math.sin(angle))/n2)
print(math.degrees(angle))

brechungszahlen = {
    "diamant": 2.417,
    "eis": 1.310,
    "ethanol": 1.362,
    "fensterglas": 1.5,
    "plexiglas": 1.491,
    "quarzglas": 1.458,
    "steinsalz": 1.544,
    "wasser": 1.333,
    "zuckerlösung 30%": 1.38,
    "zuckerlösung 80%": 1.49,
    "vakuum": 1.00027
}
print(math.radians(44)*brechungszahlen["quarzglas"])
print(math.degrees(math.asin((math.radians(44)*brechungszahlen["quarzglas"])%1)))