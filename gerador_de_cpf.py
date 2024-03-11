#Import
import random
import os

#Limpa o terminal
os.system('cls')

#CPF
nove_digitos = []

#Gerador do CPF
for i in range(9):
    nove_digitos.append(random.randint(0, 9))

#CALCULO DO PRIMEIRO DIGITO
#Multiplicador para o decimo digito
multiplicador = 10

#Lista para o calculo
nove_digitos_multiplicados = []

#Calcula por 10, 9, 8...
for digit in nove_digitos:
    nove_digitos_multiplicados.append(digit * multiplicador)
    multiplicador -= 1

#Soma todos os elementos da lista
soma_dos_digitos_multiplicados = sum(nove_digitos_multiplicados)

#Resto da divisão
soma_dos_digitos_multiplicados %= 11

#Se digito for menor que 2
if (soma_dos_digitos_multiplicados < 2):
    primeiro_digito = 0

#Se digito for igual ou maior que 2
elif (soma_dos_digitos_multiplicados >= 2):
    primeiro_digito = 11 - soma_dos_digitos_multiplicados

#Adicionar o decimo digito
nove_digitos.append(primeiro_digito)

#CALCULO DO SEGUNDO DIGITO
#Multiplicador
multiplicador = 11

#Lista dos resultados
dez_digitos_multiplicados = []

#Loop para multiplicar
for caractere in nove_digitos:
    dez_digitos_multiplicados.append(caractere * multiplicador)
    multiplicador -= 1

#Soma os elementos da lista
soma_dos_digitos_multiplicados = sum(dez_digitos_multiplicados)

#Resto da divisão
soma_dos_digitos_multiplicados %= 11

#Se digito for menor que 2
if (soma_dos_digitos_multiplicados < 2):
    segundo_digito = 0

#Se digito for igual ou maior que 2
elif (soma_dos_digitos_multiplicados >= 2):
    segundo_digito = 11 - soma_dos_digitos_multiplicados

#Adicionar o decimo digito
nove_digitos.append(segundo_digito)

cpf = ''

#Lista para variavel
for i in nove_digitos:
    cpf += str(i)

print(cpf)
