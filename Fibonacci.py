numero = -1
while numero < 1 :
    entrada = input("Digite a posição máxima: ")
    try:
        numero = int(entrada)
    except ValueError:
        numero = -1
    if numero < 1:
        print("Entrada inválida.")

numero_atras = 0
numero_2atras = 0
for i in range(0,numero):
    n_atual = numero_atras + numero_2atras
    if n_atual == 0:
        n_atual = 1
    numero_2atras = numero_atras
    numero_atras = n_atual

    print(n_atual,end='')
    if i < numero-1:
        print(', ' ,end='')
