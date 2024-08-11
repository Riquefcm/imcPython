peso = float(input ("Forneça seu peso em kg: "))
altura = float(input("Forneça sua altura em metros: ")) 

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 24.9:
    classificacao = "Peso normal"
elif imc < 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Seu imc é {imc:.2f}")
print(f"Você está com {classificacao}.")