from flask import Flask
print(2 + 2 == 4)
print(7 > 10)
print(5 != 3) # diferente !=
print(10 == 2 * 5)

p = True
q = False
print(not p) # p é true = ent not p é falso
print(p and q) # como p é  verdadeiro e o q é falso = p and q é falso
print(q or p) # como p é verdadeiro o todo é verdadeiro independente da posição vai ser verdade com o or


nota = 8
frequencia = 73
print(nota >= 7) 
print(frequencia >= 75)
print((nota >= 7) and (frequencia >= 75)) #falhou uma falhou todas com o and

print(not p or q) # como todos elementos sao falsos ele da como falso, se um fosse verdadeiro daria verdade

print(not (p and q) or (not q and not p))
# or = V 
# and = ^ 
# ~ = no

valores = [True, False]

for p in valores:
    for q in valores:
        print(p, q, p and q)

valores = [True, False]

print(f"{'p':^6} {'q':^6} {'p e q':^6}")
print("-"*20)
for p in valores:
    for q in valores:
        print(f"{str(p):^6} {str(q):^6} {str(p and q):^6}")
# ¬(¬p) ≡ p
# ¬(p ∧ q) ≡ ¬p ∨ ¬q
# ¬(p ∨ q) ≡ ¬p ∧ ¬q
# Essas duas últimas são chamadas de leis De Morgan.

#Lei de Morgan
valores = [True, False]
for p in valores:
    for q in valores:
        lado1 = not (p and q)
        lado2 = (not p) or (not q)
        print(p, q, lado1, lado2)