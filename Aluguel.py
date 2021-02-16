Qdias = float(input())
Qkilometros = float(input())

resultado = Qdias*30 + Qkilometros*0.01
desconto = resultado*0.10

print("{:.2f}".format(resultado-desconto))