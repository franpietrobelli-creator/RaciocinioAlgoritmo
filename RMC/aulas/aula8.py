A = {2, 5, 3, 4, 8, 15, 10}
B = {2, 3, 5, 9}
print(A, type(A))
print(2 in A)
print(5 in A)
print(A | B)
print(A & B)
print(A - B)
print( A ^ B)
print (A <= B)

pares = {x for x in range(1, 101) if x % 2 ==0}
mult3 = {x for x in range(1, 101) if x % 3 ==0}
print(pares & mult3)

A = {8, 9, 10, 11}
B = {2, 3, 5, 8}
C = {2, 4, 6, 8, 10}
resultado = (A | B) - C
print(resultado)

C = {101, 102, 103, 104, 105, 106, 107, 108}
A = {102, 104, 106, 108}
B = {101, 102, 103, 105, 108}
print(A | B) # OU = |
print(A & B) 
print(A, type(A))
print((A | B) - C)
print(B - A)
print(A & B - C)

