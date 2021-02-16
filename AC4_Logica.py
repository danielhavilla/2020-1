validacao = 0

while not validacao == 1:    
  Qnomes = input("Digite a quantidade de nomes entre 3 e 10: ")
  if Qnomes.isdigit():   
    Qnomes = int(Qnomes)
    if Qnomes > 3 and Qnomes <= 10:            
      validacao = 1
    else:
      print ("Valor digitado inválido.")        
  else:
    print ("Valor digitado inválido.")     

L = []

for x in range(1,Qnomes+1):
  validacao = 0    
  while not validacao == 1:
    if x == 4:
      L.append("Teste")
      validacao = 1
    else:           
      nome = input("Digite um nome:")            
      if nome.isalpha():
        L.append(nome.capitalize())
        validacao = 1
      else:
        print ("Nome inválido digite apenas letras.")  

del(L[2])

contagem = L.count("Ana")

if contagem == 0: 
  print("O nome Ana não apareceu na lista")
else:    
  indice = L.index("Ana")       
  print("O nome Ana apareceu", contagem, "vez(es) na lista. Primeira ocorrência - índice:", indice)

L.sort()    
print(L)
