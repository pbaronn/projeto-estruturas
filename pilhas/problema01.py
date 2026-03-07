# Estrutura de dados: Pilha - Problema 1- Pilha com Minimo
# Plataforma: LeetCode
# Link: https://leetcode.com/problems/min-stack/
# Dificuldade: Medio

class PilhaComMinimo:

    def __init__(self):
        self.pilha_principal = []
        self.pilha_minimos   = []

    def empilhar(self, valor):
        self.pilha_principal.append(valor)

        # O minimo atual e o menor entre o novo valor e o minimo anterior
        if self.pilha_minimos:
            minimo_atual = min(valor, self.pilha_minimos[-1])
        else:
            minimo_atual = valor  # Primeira insercao: o proprio valor e o minimo

        self.pilha_minimos.append(minimo_atual)

    def desempilhar(self):
        # Remove das duas pilhas sempre juntas
        self.pilha_principal.pop()
        self.pilha_minimos.pop()

    def topo(self):
        return self.pilha_principal[-1]

    def minimo(self):
        # O topo da pilha de minimos e sempre o menor valor atual
        return self.pilha_minimos[-1]




################### Teste 1 - sequencia do LeetCode ###################
print("Teste 1 - sequencia do LeetCode:")
pilha = PilhaComMinimo()
pilha.empilhar(-2)
pilha.empilhar(0)
pilha.empilhar(-3)
print("Empilhou -2, 0, -3")
print("Minimo esperado: -3 | Obtido:", pilha.minimo())
pilha.desempilhar()
print("Desempilhou")
print("Topo esperado: 0 | Obtido:", pilha.topo())
print("Minimo esperado: -2 | Obtido:", pilha.minimo())
print()

################### Teste 2  - minimo nao muda quando valores maiores sao removidos ###################
print("Teste 2 - minimo estavel:")
pilha2 = PilhaComMinimo()
pilha2.empilhar(5)
pilha2.empilhar(3)
pilha2.empilhar(7)
print("Empilhou 5, 3, 7")
print("Minimo esperado: 3 | Obtido:", pilha2.minimo())
pilha2.desempilhar()
print("Desempilhou 7")
print("Minimo esperado: 3 | Obtido:", pilha2.minimo())
print()

################### Teste 3  - minimo muda apos remover o proprio minimo ###################
print("Teste 3 - remover o minimo:")
pilha3 = PilhaComMinimo()
pilha3.empilhar(2)
pilha3.empilhar(1)
print("Empilhou 2, 1")
print("Minimo esperado: 1 | Obtido:", pilha3.minimo())
pilha3.desempilhar()
print("Desempilhou 1 (era o minimo)")
print("Minimo esperado: 2 | Obtido:", pilha3.minimo())
print()

################### Teste 4  - unico elemento ###################
print("Teste 4 - unico elemento:")
pilha4 = PilhaComMinimo()
pilha4.empilhar(42)
print("Empilhou 42")
print("Topo esperado: 42 | Obtido:", pilha4.topo())
print("Minimo esperado: 42 | Obtido:", pilha4.minimo())

