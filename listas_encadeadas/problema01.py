# Estrutura de dados: Lista Encadeada - Problema 1 - Inverter Lista Encadeada
# Plataforma: LeetCode
# Link: https://leetcode.com/problems/reverse-linked-list/
# Dificuldade: Facil


# Definicao do No da lista encadeada
class No:
    def __init__(self, valor=0, proximo=None):
        self.valor = valor
        self.proximo = proximo


def inverter_lista(cabeca):
    anterior = None
    atual = cabeca

    while atual is not None:
        # Salva o proximo antes de perder a referencia
        proximo = atual.proximo

        # Inverte o ponteiro: o atual agora aponta para o anterior
        atual.proximo = anterior

        # Avanca os dois ponteiros uma posicao
        anterior = atual
        atual = proximo

    return anterior



################### FUNCOES AUXILIARES PARA OS TESTES ###################

def lista_para_array(cabeca):
    # Converte a lista encadeada em array para facilitar a visualizacao
    resultado = []
    atual = cabeca
    while atual is not None:
        resultado.append(atual.valor)
        atual = atual.proximo
    return resultado

def array_para_lista(valores):
    # Converte um array em lista encadeada
    if not valores:
        return None
    cabeca = No(valores[0])
    atual = cabeca
    for valor in valores[1:]:
        atual.proximo = No(valor)
        atual = atual.proximo
    return cabeca





################### Teste 1 - exemplo do LeetCode ###################
lista_1 = array_para_lista([1, 2, 3, 4, 5])
resultado_1 = inverter_lista(lista_1)
print("Teste 1:")
print("Entrada: [1, 2, 3, 4, 5]")
print("Esperado: [5, 4, 3, 2, 1] | Obtido:", lista_para_array(resultado_1))
print()

################### Teste 2 - dois elementos ###################
lista_2 = array_para_lista([1, 2])
resultado_2 = inverter_lista(lista_2)
print("Teste 2 (dois elementos):")
print("Entrada: [1, 2]")
print("Esperado: [2, 1] | Obtido:", lista_para_array(resultado_2))
print()

################### Teste 3 - lista com um elemento ###################
lista_3 = array_para_lista([42])
resultado_3 = inverter_lista(lista_3)
print("Teste 3 (adicional - unico elemento):")
print("Entrada: [42]")
print("Esperado: [42] | Obtido:", lista_para_array(resultado_3))
print()

################### Teste 4 - lista vazia ###################
lista_4 = array_para_lista([])
resultado_4 = inverter_lista(lista_4)
print("Teste 4 (adicional - lista vazia):")
print("Entrada: []")
print("Esperado: [] | Obtido:", lista_para_array(resultado_4))

