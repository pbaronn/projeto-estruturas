# Pegue os presentes da pilha mais rica 
# LeetCode: https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/ 
# Dificuldade: Facil

# Geovania Luiza Francisco

import heapq
import math
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Transformar a lista de presentes em um max-heap
        # heapq do Python é min-heap, então usamos números negativos
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)  # Constrói o heap em O(n)

        # Repetir o processo k vezes
        for _ in range(k):
            # Pegar o presente mais rico (máximo)
            top = -heapq.heappop(max_heap)  # inverter o sinal de volta

            # Substituir o presente por sua raiz quadrada inteira
            heapq.heappush(max_heap, -math.isqrt(top))  # adicionar de volta ao heap

        # Retornar a soma de todos os presentes restantes
        # Somamos negativos e invertemos o sinal novamente
        return -sum(max_heap)

# ----------------------------
# Testes
# ----------------------------

sol = Solution()

# Teste 1: exemplo do enunciado
gifts1, k1 = [25, 64, 9, 4, 100], 4
print(f"pickGifts({gifts1}, {k1}) =", sol.pickGifts(gifts1, k1))  # Esperado: 29

# Teste 2: todos presentes iguais
gifts2, k2 = [1, 1, 1, 1], 4
print(f"pickGifts({gifts2}, {k2}) =", sol.pickGifts(gifts2, k2))  # Esperado: 4

# Teste 3: um presente grande
gifts3, k3 = [1000], 1
print(f"pickGifts({gifts3}, {k3}) =", sol.pickGifts(gifts3, k3))  # Esperado: 31 (raiz de 1000 ~ 31)

# Teste 4: sem remoções (k = 0)
gifts4, k4 = [2, 3, 5, 7], 0
print(f"pickGifts({gifts4}, {k4}) =", sol.pickGifts(gifts4, k4))  # Esperado: 17 (soma original)

# Teste 5: presentes pequenos, várias iterações
gifts5, k5 = [4, 9, 16], 5
print(f"pickGifts({gifts5}, {k5}) =", sol.pickGifts(gifts5, k5))  # Teste de várias iterações