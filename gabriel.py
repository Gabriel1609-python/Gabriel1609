for i in range(10, 0, -1):
    print(i)

print("fogo")

def atividade5():
   
   numero = int(input("Digite um número inteiro positivo: "))

   if numero < 2:
    print("Não há números pares entre 2 e", numero)
   else:
    soma = 0
    i = 2
    while i <= numero:
        soma += i
        i += 2  
    print("A soma dos números pares de 2 até", numero, "é:", soma)