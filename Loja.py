area=input()
area=float(area)

import math

latas24 = math.ceil(area/168)
latas54 = math.ceil(area/37.8)

nlatas24 = math.floor(area/168)
nlatas54 = math.ceil((area%168)/37.8)

print("a)",latas24,"lata(s) de 24 litros: R$ {:.2f}".format(latas24*91))
print("b)",latas54,"lata(s) de 5.4 litros: R$ {:.2f}".format(latas54*23))

print("c)",nlatas24,"lata(s) de 24 litros e",nlatas54,"lata(s) de 5.4 litros: R$ {:.2f}".format((nlatas24*91)+(nlatas54*23)))