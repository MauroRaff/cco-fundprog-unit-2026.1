nota = int(input("Digite sua nota: "))

while nota < 0 or nota > 10:
    print("Nota inválida")
    nota = int(input("Digite a nota novamente: "))
