p1 = float(input())
p2 = float(input())
p3 = float(input())
fre = float(input())

fre = int(fre*100)
media = round(((p1*2)+(p2*2)+(p3*3))/(2+2+3),1)

print("Frequencia:","{:.0f}".format(fre)+"%")
print("Media:","{:.1f}".format(media))

if fre < 75:
    print("Aluno reprovado por faltas!")
else:
    if media > 9:
        print("Aluno aprovado com louvor!")
    else:
        if media >= 6 and media <= 9:
            print("Aluno aprovado!")
        else:
            if media >= 4 and media < 6:
                print("Aluno de recupera��o!")
            else:
                if media < 4:
                    print("Aluno reprovado!")
                  
                
            
        
    