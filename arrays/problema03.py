# Estrutura de dados: Array - Problema 3 - Produto do Array Exceto Si Mesmo
# Plataforma: LeetCode
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Dificuldade: Medio

# Pamela Baron


def produto_exceto_si_mesmo(numeros):
    tamanho = len(numeros)

    # Array de resultado, inicialmente preenchido com 1
    resultado = [1] * tamanho

    # Primeira passagem: para cada posicao, guardar o produto de tudo a esquerda
    produto_da_esquerda = 1
    for i in range(tamanho):
        resultado[i] = produto_da_esquerda
        produto_da_esquerda *= numeros[i]

    # Segunda passagem: multiplicar pelo produto de tudo a direita
    produto_da_direita = 1
    for i in range(tamanho - 1, -1, -1):
        resultado[i] *= produto_da_direita
        produto_da_direita *= numeros[i]

    return resultado





################### Teste 1 - exemplo do LeetCode ###################
numeros_teste_1 = [1, 2, 3, 4]
resultado_1 = produto_exceto_si_mesmo(numeros_teste_1)
print("Teste 1:")
print("Entrada:", numeros_teste_1)
print("Esperado: [24, 12, 8, 6] | Obtido:", resultado_1)
print()

################### Teste 2 - com zero no array ###################
numeros_teste_2 = [-1, 1, 0, -3, 3]
resultado_2 = produto_exceto_si_mesmo(numeros_teste_2)
print("Teste 2 - com zero:")
print("Entrada:", numeros_teste_2)
print("Esperado: [0, 0, 9, 0, 0] | Obtido:", resultado_2)
print()

################### Teste 3 - dois elementos ###################
numeros_teste_3 = [3, 4]
resultado_3 = produto_exceto_si_mesmo(numeros_teste_3)
print("Teste 3 - dois elementos:")
print("Entrada:", numeros_teste_3)
print("Esperado: [4, 3] | Obtido:", resultado_3)
print()

################### Teste 4  - numeros negativos ###################
numeros_teste_4 = [-1, -2, -3]
resultado_4 = produto_exceto_si_mesmo(numeros_teste_4)
print("Teste 4 - negativos:")
print("Entrada:", numeros_teste_4)
print("Esperado: [6, 3, 2] | Obtido:", resultado_4)

