
# Ciclo em Lista Encadeada 
# LeetCodE:  https://leetcode.com/problems/linked-list-cycle/
# Dificuldade: Facil


class No:
    def __init__(self, valor=0, proximo=None):
        self.valor = valor
        self.proximo = proximo


def tem_ciclo(cabeca):
    # Lista vazia ou com unico no sem ciclo nao tem ciclo
    if cabeca is None or cabeca.proximo is None:
        return False

    tartaruga = cabeca          # Avanca 1 passo por vez
    lebre = cabeca.proximo      # Avanca 2 passos por vez

    while lebre is not None and lebre.proximo is not None:
        # Se os dois se encontrarem, ha ciclo
        if tartaruga == lebre:
            return True

        tartaruga = tartaruga.proximo        # 1 passo
        lebre = lebre.proximo.proximo        # 2 passos

    # Se a lebre chegou ao final (None), nao ha ciclo
    return False



# FUNCAO PARA TESTES - cria lista e opcionalmente cria um ciclo


def criar_lista_com_ciclo(valores, posicao_ciclo):
    # posicao_ciclo = -1 significa sem ciclo
    if not valores:
        return None

    nos = [No(v) for v in valores]

    for i in range(len(nos) - 1):
        nos[i].proximo = nos[i + 1]

    if posicao_ciclo != -1:
        # O ultimo no aponta de volta para a posicao indicada
        nos[-1].proximo = nos[posicao_ciclo]

    return nos[0]


# TESTES


#  lista com ciclo 
lista_1 = criar_lista_com_ciclo([3, 2, 0, -4], posicao_ciclo=1)
resultado_1 = tem_ciclo(lista_1)
print("Teste com ciclo:")
print("Valores: [3, 2, 0, -4], ciclo no indice 1")
print("Esperado: True | Obtido:", resultado_1)
print()

# lista sem ciclo
lista_2 = criar_lista_com_ciclo([1, 2, 3, 4], posicao_ciclo=-1)
resultado_2 = tem_ciclo(lista_2)
print("Teste sem ciclo:")
print("Valores: [1, 2, 3, 4]")
print("Esperado: False | Obtido:", resultado_2)
print()

#  lista com dois nos e ciclo
lista_3 = criar_lista_com_ciclo([1, 2], posicao_ciclo=0)
resultado_3 = tem_ciclo(lista_3)
print("Teste  dois nos com ciclo:")
print("Valores: [1, 2], ciclo no indice 0")
print("Esperado: True | Obtido:", resultado_3)
print()

#  lista com um unico no sem ciclo
lista_4 = criar_lista_com_ciclo([1], posicao_ciclo=-1)
resultado_4 = tem_ciclo(lista_4)
print("Teste unico no sem ciclo:")
print("Valores: [1]")
print("Esperado: False | Obtido:", resultado_4)

