# Estrutura de dados: Array + Dicionario Hash Map -  Problema 1 - Soma de Dois Numeros
# Plataforma: LeetCode 
# Link:  https://leetcode.com/problems/two-sum/
# Dificuldade: Facil



def soma_dois_numeros(numeros, alvo):
    # Dicionario que vai guardar: { numero_visto: indice_dele }
    numeros_vistos = {}
    for indice, numero_atual in enumerate(numeros):

       # calcular o complemento para quanto falta para chegar no alvo
        complemento = alvo - numero_atual

        # Se o complemento ja foi visto antes, encontra o par
        if complemento in numeros_vistos:
            indice_do_complemento = numeros_vistos[complemento]
            return [indice_do_complemento, indice]
        numeros_vistos[numero_atual] = indice # Se nao foi encontrado ainda, guarda o numero atual no dicionario

    # Se nenhum par for encontrado, retornamos lista vazia
    return []





################### Teste 1 - exemplo do LeetCode ###################
numeros_teste_1 = [2, 7, 11, 15]
alvo_teste_1 = 9
resultado_1 = soma_dois_numeros(numeros_teste_1, alvo_teste_1)
print("Teste 1:")
print("Entrada:", numeros_teste_1, "| Alvo:", alvo_teste_1)
print("Esperado: [0, 1] | Obtido:", resultado_1)
print()

################### Teste 2 do  LeetCode ###################
numeros_teste_2 = [3, 2, 4]
alvo_teste_2 = 6
resultado_2 = soma_dois_numeros(numeros_teste_2, alvo_teste_2)
print("Teste 2:")
print("Entrada:", numeros_teste_2, "| Alvo:", alvo_teste_2)
print("Esperado: [1, 2] | Obtido:", resultado_2)
print()

################### Teste 3 de numeros negativos ###################
numeros_teste_3 = [-3, 4, 3, 90]
alvo_teste_3 = 0
resultado_3 = soma_dois_numeros(numeros_teste_3, alvo_teste_3)
print("Teste 3 - numeros negativos:")
print("Entrada:", numeros_teste_3, "| Alvo:", alvo_teste_3)
print("Esperado: [0, 2] | Obtido:", resultado_3)
print()

################### Teste 4  de numeros repetidos ###################
numeros_teste_4 = [3, 3]
alvo_teste_4 = 6
resultado_4 = soma_dois_numeros(numeros_teste_4, alvo_teste_4)
print("Teste 4  - numeros repetidos:")
print("Entrada:", numeros_teste_4, "| Alvo:", alvo_teste_4)
print("Esperado: [0, 1] | Obtido:", resultado_4)

