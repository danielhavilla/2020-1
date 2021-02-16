nboi = int(input())

listaID = []
listaP = []

for x in range(0,nboi):
    
    ID,P = input().split(" ")
    
    listaID.append(ID)
    listaP.append(float(P))
    
    if x == 0:
        maior = menor = listaP[x]
        id_maior = listaID[x]    
        id_menor = listaID[x]    
    else:
        if listaP[x] > maior:
            maior = listaP[x]
            id_maior = listaID[x]  
        if listaP[x] < menor:
            menor = listaP[x]
            id_menor = listaID[x]  

print ("Gordo: id:",id_maior,"peso: {:.2f}".format(maior)+"Kg")
print ("Magro: id:",id_menor,"peso: {:.2f}".format(menor)+"Kg")










