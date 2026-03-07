# Estrutura de dados: Lista Encadeada - Problema 2 - Mesclar Duas Listas Ordenadas
# Plataforma: LeetCode
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Dificuldade: Facil

# Pamela Baron

class No:
    def __init__(self, valor=0, proximo=None):
        self.valor = valor
        self.proximo = proximo


def mesclar_listas_ordenadas(lista1, lista2):
    # No auxiliar que serve como inicio fixo 
    sentinela = No(0)

    # Ponteiro que avança construindo a lista resultado
    atual = sentinela

    # Enquanto ambas as listas tiverem elementos
    while lista1 is not None and lista2 is not None:
        if lista1.valor <= lista2.valor:
            # O menor esta na lista1, encadea ele no resultado
            atual.proximo = lista1
            lista1 = lista1.proximo
        else:
            # O menor esta na lista2, encadea ele no resultado
            atual.proximo = lista2
            lista2 = lista2.proximo

        # Avanca o ponteiro do resultado
        atual = atual.proximo

    # Se sobrou algum elemento em uma das listas, encadea o restante direto
    if lista1 is not None:
        atual.proximo = lista1
    else:
        atual.proximo = lista2

    return sentinela.proximo



################### FUNCOES AUXILIARES PARA OS TESTES ###################

def lista_para_array(cabeca):
    resultado = []
    atual = cabeca
    while atual is not None:
        resultado.append(atual.valor)
        atual = atual.proximo
    return resultado

def array_para_lista(valores):
    if not valores:
        return None
    cabeca = No(valores[0])
    atual = cabeca
    for valor in valores[1:]:
        atual.proximo = No(valor)
        atual = atual.proximo
    return cabeca





################### Teste 1 - exemplo do LeetCode ###################
lista1 = array_para_lista([1, 2, 4])
lista2 = array_para_lista([1, 3, 4])
resultado_1 = mesclar_listas_ordenadas(lista1, lista2)
print("Teste 1:")
print("lista1: [1, 2, 4] | lista2: [1, 3, 4]")
print("Esperado: [1, 1, 2, 3, 4, 4] | Obtido:", lista_para_array(resultado_1))
print()

################### Teste 2 - ambas vazias ###################
resultado_2 = mesclar_listas_ordenadas(None, None)
print("Teste 2 (ambas vazias):")
print("Esperado: [] | Obtido:", lista_para_array(resultado_2))
print()

################### Teste 3  - uma lista vazia ###################
lista3 = array_para_lista([])
lista4 = array_para_lista([1, 2, 3])
resultado_3 = mesclar_listas_ordenadas(lista3, lista4)
print("Teste 3 (adicional - uma lista vazia):")
print("lista1: [] | lista2: [1, 2, 3]")
print("Esperado: [1, 2, 3] | Obtido:", lista_para_array(resultado_3))
print()

################### Teste 4  - sem elementos em comum ###################
lista5 = array_para_lista([1, 3, 5])
lista6 = array_para_lista([2, 4, 6])
resultado_4 = mesclar_listas_ordenadas(lista5, lista6)
print("Teste 4 (adicional - valores alternados):")
print("lista1: [1, 3, 5] | lista2: [2, 4, 6]")
print("Esperado: [1, 2, 3, 4, 5, 6] | Obtido:", lista_para_array(resultado_4))

