contador_positivos = 0

for numero in range(1, 11):
    numero = int(input("digite seu numero: "))

    if numero > 0:
        contador_positivos += 1

print(contador_positivos)