numero = -1
while numero < 1 :
    entrada = input("Digite a posição máxima: ")
    try:
        numero = int(entrada)
    except ValueError:
        numero = -1
    if numero < 1:
        print("Entrada inválida.")
        
resultado = 0

for i in range(0,numero):
    resultado += ((i+1)*2 -1)/(i+1)

print("A soma dessa sequencia é",resultado)
