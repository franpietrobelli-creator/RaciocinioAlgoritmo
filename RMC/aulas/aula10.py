import numpy as np

v = np.array([2, 5, 1])

A = np.array([
    [1, 4],
    [2, 5]
])
print("3 * A", 3 * A)

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(A.T)

# Sempre linha por coluna

A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])
print(A @ B)

A = np.array([
    [2, 1],
    [0, 3]
])
B = np.array([
    [4, 5],
    [6, 2]
])
print(A + B)
print(A - B)
print(A @ B)
print(B @ A)
print(A * B)

A = np.array([
    [2, 1],
    [3, 4]
])

x = np.array([5, 2])

print(A @ x)
print(x.shape)

imagem = np.array([
    [0, 50, 100],
    [150, 200, 255],
    [30, 80, 120]
])

nova = imagem + 20
nova = np.clip(nova, 0, 255)

print(nova)
