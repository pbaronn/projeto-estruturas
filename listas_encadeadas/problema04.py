# Lista Encadeada de Design 
# LeetCode: https://leetcode.com/problems/design-linked-list/description/
# Dificuldade: Medio

# Geovania Luiza Francisco

class MyLinkedList(object):

    class Node:
        def __init__(self, val=0):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = self.Node(0)  # nó dummy
        self.size = 0

    def get(self, index):
        # retorna -1 se índice inválido
        if index < 0 or index >= self.size:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        # não insere se índice maior que tamanho
        if index > self.size:
            return

        # índice negativo vira 0
        if index < 0:
            index = 0

        self.size += 1
        pred = self.head

        # encontra nó anterior
        for _ in range(index):
            pred = pred.next

        node = self.Node(val)

        # insere nó
        node.next = pred.next
        pred.next = node

    def deleteAtIndex(self, index):
        # ignora se índice inválido
        if index < 0 or index >= self.size:
            return

        self.size -= 1
        pred = self.head

        # encontra nó anterior
        for _ in range(index):
            pred = pred.next

        # remove nó
        pred.next = pred.next.next


# ----------------------------
# Testes
# ----------------------------

# Criar lista encadeada
obj = MyLinkedList()

# Adicionar no cabeçalho
obj.addAtHead(1)        # Lista: 1

# Adicionar na cauda
obj.addAtTail(3)        # Lista: 1 -> 3

# Adicionar no índice 1
obj.addAtIndex(1, 2)    # Lista: 1 -> 2 -> 3

# Obter valor no índice 1
print(obj.get(1))       # Esperado: 2

# Deletar nó no índice 1
obj.deleteAtIndex(1)    # Lista: 1 -> 3

# Obter valor no índice 1 novamente
print(obj.get(1))       # Esperado: 3

