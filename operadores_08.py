import os
os.system ("clear || cls")
#Entrada de dados
km = float(input("Quantos foram os km rodados ?: "))
dia = int(input("Foi alugado por quantos dias?: "))

valorkm = km * 0.15
valordia = dia * 60.00
valorf = valorkm + valordia
#Saida de dados
print(f"Foi cobrado {valorkm} pelo (km)\nFoi cobrado {valordia} pelos dias de uso\nO valor total a pagar é {valorf}: ")