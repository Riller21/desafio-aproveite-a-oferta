T = int(input("Digite o número de casos de teste (T): "))

for i in range(1, T + 1):
    N_K = input("Digite N e K separados por espaço: ")
    N_K_2 = N_K.split()
    N = int(N_K_2[0])
    K = int(N_K_2[1])
    num_final_de_garrafas = (N // K) + (N % K) 
    print(num_final_de_garrafas)
