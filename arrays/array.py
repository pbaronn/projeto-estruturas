#  Melhor Momento para Comprar e Vender Acao
# LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Dificuldade: Facil



def melhor_lucro(precos):
    #  lista vazia ou com um unico preco nao tem solucao
    if len(precos) < 2:
        return 0

    # Começa assumindo que o primeiro dia e o melhor para comprar
    menor_preco = precos[0]

    # Começa sem nenhum lucro
    maior_lucro = 0

    # Percorre a partir do segundo dia - indice 1
    for preco_atual in precos[1:]:

        # Calcula o lucro se vendesse hoje
        lucro_hoje = preco_atual - menor_preco

        # Atualiza o maior lucro se o de hoje for melhor
        if lucro_hoje > maior_lucro:
            maior_lucro = lucro_hoje

        # Atualiza o menor preço se o de hoje for menor
        if preco_atual < menor_preco:
            menor_preco = preco_atual

    return maior_lucro



# TESTES


#  exemplo do LeetCode
precos_teste_1 = [7, 1, 5, 3, 6, 4]
resultado_1 = melhor_lucro(precos_teste_1)
print("Teste 1:")
print("Entrada:", precos_teste_1)
print("Esperado: 5 | Obtido:", resultado_1)
print()

#  precos sempre caindo, lucro impossivel
precos_teste_2 = [7, 6, 4, 3, 1]
resultado_2 = melhor_lucro(precos_teste_2)
print("Teste precos em queda, sem lucro:")
print("Entrada:", precos_teste_2)
print("Esperado: 0 | Obtido:", resultado_2)
print()

#  melhor compra no inicio, melhor venda no fim
precos_teste_3 = [1, 2, 3, 4, 5]
resultado_3 = melhor_lucro(precos_teste_3)
print("Teste precos crescendo sempre:")
print("Entrada:", precos_teste_3)
print("Esperado: 4 | Obtido:", resultado_3)
print()

