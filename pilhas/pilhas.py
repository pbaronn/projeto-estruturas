# Parenteses Validos 
# LeetCode: https://leetcode.com/problems/valid-parentheses/
# Dificuldade: Facil



def parenteses_validos(texto):
    # Dicionario que mapeia cada fecha para o seu abre correspondente
    pares = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # A pilha vai guardar os simbolos de abertura encontrados
    pilha = []

    for caractere in texto:
        if caractere in pares:
            # E um simbolo de fechamento
            # Verificamos se o topo da pilha e o par correto
            if pilha and pilha[-1] == pares[caractere]:
                pilha.pop()   # Par correto: desempilhamos
            else:
                return False  # Par errado ou pilha vazia: invalido
        else:
            # E um simbolo de abertura: empilhamos
            pilha.append(caractere)

    # Se a pilha estiver vazia, todos os pares foram fechados corretamente
    return len(pilha) == 0

# TESTES


#  par simples valido
resultado_1 = parenteses_validos("()")
print("Teste 1:")
print("Entrada: '()'")
print("Esperado: True | Obtido:", resultado_1)
print()

#  multiplos tipos validos
resultado_2 = parenteses_validos("()[]{}")
print("Teste multiplos tipos:")
print("Entrada: '()[]{}'")
print("Esperado: True | Obtido:", resultado_2)
print()

#  tipos cruzados, invalido
resultado_3 = parenteses_validos("(]")
print("Teste tipos cruzados:")
print("Entrada: '(]'")
print("Esperado: False | Obtido:", resultado_3)
print()

#  aninhado valido
resultado_4 = parenteses_validos("{[()]}")
print("Teste aninhado valido:")
print("Entrada: '{[()]}'")
print("Esperado: True | Obtido:", resultado_4)
print()

# apenas abertura, sem fechamento
resultado_5 = parenteses_validos("((([")
print("Teste so abertura:")
print("Entrada: '(((['")
print("Esperado: False | Obtido:", resultado_5)
