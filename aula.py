numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")


numero = float(input("Digite um número: "))

if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print("O número é zero.")


texto = input("Digite alguma coisa: ")

if texto.strip() == "":
    print("A string está vazia.")
else:
    print(f"A string não está vazia. Você digitou: '{texto}'")



idade = int(input("Digite a idade: "))

if idade <= 12:
    print("Faixa etária: Criança")
elif idade <= 17:
    print("Faixa etária: Adolescente")
elif idade <= 35:
    print("Faixa etária: Jovem")
elif idade < 65:
    print("Faixa etária: Adulto")
else:
    print("Faixa etária: Idoso")