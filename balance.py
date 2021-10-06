from matplotlib import pyplot

A = int(input("Anf A "))
B = int(input("Anf B "))
pyplot.scatter(0 , A, color = "red")
pyplot.scatter(0 , B, color = "blue")
pyplot.title("Modellexperiment zum chemischen Gleichgewicht")
pyplot.ylabel("Anzahl Streichhoelzer pro Person")
pyplot.xlabel("Zug")
for i in range(1,10):
    tmpA  = A // 2
    tmpB  = B // 10
    B += (A-tmpA)
    A = tmpA
    A += tmpB
    B -= tmpB
    pyplot.scatter(i , A, color = "red")
    pyplot.scatter(i , B, color = "blue")
pyplot.show()