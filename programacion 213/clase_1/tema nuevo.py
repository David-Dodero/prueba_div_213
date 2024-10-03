contacto= [["ana", 23],["juan",45],["sol",65]]

contacto.append(["LUIS"])

contacto[3].append(22)
#print(contacto)

contacto.pop() #elimina a luis


matrix= [[2,3,4],
          [6,3,1]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])