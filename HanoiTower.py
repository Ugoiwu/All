nbrDisque = int(input("Nombre de disques ? "))
tours = [[0 for _ in range(nbrDisque)] for _ in range(3)]
print(tours)
for i in range(len(tours[0]), 0, -1): tours[0][abs(i-nbrDisque)] = i
print(tours)
def toursA(tours):
    toursAf = [[None for _ in range(3)] for _ in range(nbrDisque)] 
    for j in range(3):
        for i in range(len(tours[0])):
            toursAf[i][j] = str(tours[j][i])
    for i in toursAf:
        print(" ".join(i))

