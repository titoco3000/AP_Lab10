numero = -1
while numero < 0 :
    entrada = input("Digite a posição máxima: ")
    try:
        numero = int(entrada)
    except ValueError:
        numero = -1
    if numero < 0:
        print("Entrada inválida.")
    
if numero == 0:
    resultado = 0
else:
    resultado = 1
    for i in range(numero, 0, -1):
        resultado*=i

print(f"{numero}! = {resultado}")
