t_fahrenheit = input()
t_fahrenheit = float(t_fahrenheit)

t_celsius = (t_fahrenheit - 32) * 5/9
t_kelvin = t_celsius + 273.15

print ("Convertendo", t_fahrenheit, "�F temos:") 
print (t_celsius, "�C e", t_kelvin,"K")
