nome = "Python"
print(nome[0])
print(nome[1])
print(nome[5])
print(nome[0:2])
print(nome[0:4])
print(nome[2:5])

texto = "Algoritmo"
print(texto[-1]) #Ultimo caractere
print(texto[-2]) # penultimo
print(texto[-3])
print(texto[:3]) # do inicio ate a posição 3
print(texto[3:]) # da posição até o final
print(texto[:]) # copia completo
print(texto[0:9:2]) # pula de 2 em 2
print(texto[::3]) # caracteres iniciando de 0 e saltando de 3 em 3

nome_comp = input("Escreva nome completo:")
nome = nome_comp.split() # O .split() é um método de strings que divide uma string em partes, retornando uma lista.
print(f"Primeiro nome:{nome[2][1]}") # O f antes das aspas cria uma f-string (formatted string literal), um recurso do Python para inserir expressões diretamente dentro de uma string.

