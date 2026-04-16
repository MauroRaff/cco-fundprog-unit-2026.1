idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 60:
    print("Maior de idade")

elif idade >= 60:
    print("Idoso")

else:
    print("Menor de idade")