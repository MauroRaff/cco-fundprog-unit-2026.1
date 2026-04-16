soma_numeros = 0

for numero in range(1, 9):
    numero = int(input("digite seu numero: "))
    if numero % 2 == 0:
        soma_numeros += numero
    
print(soma_numeros)