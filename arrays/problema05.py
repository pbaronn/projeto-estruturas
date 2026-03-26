# Fim do Array Mínimo
# LeetCode: https://leetcode.com/problems/minimum-array-end/description/ 
# Dificuldade: Medio

# Geovania Luiza Francisco

def minEnd(n: int, x: int) -> int:
    n -= 1  # porque o primeiro já é o próprio x
    result = x
    bit = 1
    
    while n > 0:
        if (x & bit) == 0:
            if (n & 1):
                result |= bit
            n >>= 1
        bit <<= 1
    
    return result




# Teste 1: exemplo do enunciado
n1, x1 = 3, 4
print(f"minEnd({n1}, {x1}) =", minEnd(n1, x1))  # Esperado: 6

# Teste 2: exemplo do enunciado
n2, x2 = 2, 7
print(f"minEnd({n2}, {x2}) =", minEnd(n2, x2))  # Esperado: 15

# Teste 3: n = 1, o menor caso possível
n3, x3 = 1, 5
print(f"minEnd({n3}, {x3}) =", minEnd(n3, x3))  # Esperado: 5 (apenas x)

# Teste 4: x já com bits altos
n4, x4 = 4, 8
print(f"minEnd({n4}, {x4}) =", minEnd(n4, x4))  # Deve retornar valor >= 8

# Teste 5: n grande e x pequeno
n5, x5 = 10, 1
print(f"minEnd({n5}, {x5}) =", minEnd(n5, x5))  # Teste de múltiplas iterações