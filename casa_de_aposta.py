#PROJETO 1 - CASA DE APOSTA / LOTERIA
import random


#Usuario informar a quantidade de numeros necessarios que ele queira.
quantidade_numero = int(input("Olá, digite a quantidade de numeros necessárias para gera-los: "))

contador = 0

#Gerar a quantidade de numeros necessarias.
while contador < quantidade_numero:
    numero = random.randint(0, quantidade_numero)
    print(numero, end=" ")
    numero = contador
    contador += 1
print("Prontinho, boa sorte!!!")