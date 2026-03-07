# Estrutura de dados: Array - Problema 2 - Subarray de Soma Maxima
# Plataforma: LeetCode
# Link: https://leetcode.com/problems/maximum-subarray/
# Dificuldade: Medio


def soma_maxima_subarray(numeros):
    soma_atual = numeros[0]
    maior_soma = numeros[0]

    # Percorre a partir do segundo elemento
    for numero in numeros[1:]:
        # Decisao central do algoritmo: Vale mais continuar acumulando ou comecar novo subarray aqui?
        soma_atual = max(numero, soma_atual + numero)

        # Atualiza a maior soma encontrada ate agora
        if soma_atual > maior_soma:
            maior_soma = soma_atual

    return maior_soma



#################### Teste 1 - exemplo do LeetCode ###################
numeros_teste_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
resultado_1 = soma_maxima_subarray(numeros_teste_1)
print("Teste 1:")
print("Entrada:", numeros_teste_1)
print("Esperado: 6 | Obtido:", resultado_1)
print()

################### Teste 2 - todos positivos, soma total e a resposta ###################
numeros_teste_2 = [1, 2, 3, 4, 5]
resultado_2 = soma_maxima_subarray(numeros_teste_2)
print("Teste 2 - todos positivos:")
print("Entrada:", numeros_teste_2)
print("Esperado: 15 | Obtido:", resultado_2)
print()

#################### Teste 3 - todos negativos, resposta e o menos negativo ###################
numeros_teste_3 = [-3, -1, -2]
resultado_3 = soma_maxima_subarray(numeros_teste_3)
print("Teste 3  - todos negativos:")
print("Entrada:", numeros_teste_3)
print("Esperado: -1 | Obtido:", resultado_3)
print()

################### Teste 4 - unico elemento ###################
numeros_teste_4 = [7]
resultado_4 = soma_maxima_subarray(numeros_teste_4)
print("Teste 4  - unico elemento:")
print("Entrada:", numeros_teste_4)
print("Esperado: 7 | Obtido:", resultado_4)

