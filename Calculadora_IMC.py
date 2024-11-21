def imc(peso, altura):
    imc = round(peso / (altura ** 2),2)
    if imc < 18.5:
        print( f"Abaixo do peso, o seu imc é {imc}")
    elif imc > 18.5 and imc < 24.9:
        print( f"Peso normal, o seu imc é {imc}")
    elif imc > 25 and imc < 29.9:
        print( f"Sobrepeso, o seu imc é {imc}")
    else:
        print( f"Obesidade, o seu imc é {imc}")

peso = float(input("Digite o seu peso: "))
altura = float(input("Qual é a sua altura: "))

imc(peso, altura)
