import random

max_n = 100
secret_number = random.randint(1, max_n)
tentativas = 0
acertou = False

print("Bem-vindo ao jogo Adivinhe o Número")
print(f"Tente adivinhar o número secreto entre 1 e {max_n}.")
print("Para finalizar o jogo, digite 0.")

while not acertou:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == 0:
        print("Jogo encerrado.")
        break
    if palpite == secret_number:
        acertou = True
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        print("====================== FIM DE JOGO ======================")
    elif palpite < 1 or palpite > max_n:
        print("Número fora do intervalo considerado. Jogada inválida.")
    elif palpite == 0:
        print("Jogo finalizado antecipadamente | YOU LOST THE GAME.")
        break
    elif palpite < secret_number:
        print(f"O número secreto é MAIOR!, Vamos para a tentativa {tentativas + 1}.")
    else:
        print(f"O número secreto é MENOR!, Vamos para a tentativa {tentativas + 1}.")
