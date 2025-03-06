import os
os.system ("clear || cls")
#Entrada de dados
altura = float(input("Digite a altura da parede em (m): "))
largura = float(input("Digite a largura da parede em (m): "))

area = altura * largura   
tinta = area / 2  #O litro de tinta cobre 2m^2

#Saida de dados
print(f"A área da parede é: {area:.2f} m^2\nVocê ira precisar de {tinta:.2f} litros de tinta")