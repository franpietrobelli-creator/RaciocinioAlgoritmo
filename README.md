# Raciocínio Algorítmico e RMC (1º semestre)

Exercícios em Python feitos nas aulas do 1º semestre de Engenharia de Software (PUCPR), das disciplinas **RMC** e **Raciocínio Algorítmico**.

```
RMC/
├── aulas/        exercícios das aulas de RMC
└── main.py       script inicial criado pelo PyCharm
Raciocinio_Algoritmico/
├── api.py        primeira API em Flask
├── aula3.py      API Flask de calculadora
└── Aula_HTML-CSS/  páginas da aula de HTML e CSS
```

---

## RMC (`RMC/aulas/`)

| Arquivo | Assunto | O que o código faz |
|---|---|---|
| `aula1.py` | Entrada e saída | Lê uma temperatura em Celsius e converte para Fahrenheit |
| `aula2.py` | Strings | Indexação e fatiamento de strings (`texto[0:4]`, `texto[::-1]`, passo de 2 em 2) e `split()` para separar o nome completo |
| `aula4.py` | Lógica | `all()` e `any()` para testar condições numa lista, e anotações de um exercício de proposições lógicas |
| `aula5.py` | Bases numéricas | Converte entre decimal, binário e hexadecimal com `bin()`, `hex()` e `int(texto, base)` |
| `aula6.py` | Funções | Define funções matemáticas (`f(x) = x²`, `g(p, q)`) e faz composição de funções |
| `aula7.py` | Gráficos | Usa o Matplotlib para desenhar gráficos de funções, como `x²` e `x³ - 2x + 1`, com título, eixos e grade |
| `aula8.py` | Conjuntos | União (`\|`), interseção (`&`), diferença (`-`), diferença simétrica (`^`), pertinência (`in`) e conjuntos por compreensão |
| `aula9.py` | Produto cartesiano | Gera o produto cartesiano de dois conjuntos |
| `aula10.py` | Matrizes com NumPy | Multiplicação por escalar, transposta, soma, subtração, produto de matrizes (`@`) e um exemplo de clarear uma "imagem" com `np.clip` |
| `aaa.py` | NumPy | Teste rápido de `shape` em um array |
| `aula22.py` | Flask | Primeira API em Flask, com as rotas `/` e `/ola/<nome>` |
| `aula22-TLDN001102622.py` | Lógica proposicional | Operadores `and`, `or` e `not`, tabelas-verdade e verificação das Leis de De Morgan |
| `exerciciosA2.py` | Exercícios | Calcula quadrado, cubo, raiz quadrada e área de um triângulo |
| `exTDE1.ipynb` | Exercícios do TDE 1 | Notebook com 15 exercícios: idade, divisão de itens, área e perímetro, conversões de unidade e temperatura, par/ímpar, média ponderada, troca de variáveis, fatiamento de strings e mais |
| `game.py` | Jogo | **Adivinhe o número**: o computador sorteia um número de 1 a 100 e diz se o palpite é maior ou menor até você acertar (digite `0` para sair) |
| `geme_velha.py` | Jogo | **Jogo da velha** para 2 jogadores no terminal, que valida as jogadas e verifica vitória (linhas, colunas e diagonais) e empate |

`RMC/main.py` é o script de exemplo que o PyCharm cria junto com um projeto novo.

---

## Raciocínio Algorítmico (`Raciocinio_Algoritmico/`)

### `api.py`: primeira API em Flask
- `GET /`: retorna "Hello, Word!"
- `GET /soma?a=2&b=3&c=texto`: lê os parâmetros da URL e devolve um JSON com o resultado de `a * b` e o texto `c`. A rota se chama `soma`, mas o código multiplica os valores.

### `aula3.py`: calculadora em Flask
- `GET /calcular/<a>/<b>`: recebe dois números inteiros na própria URL e devolve um JSON com a soma, a subtração e a multiplicação deles

Exemplo: `http://127.0.0.1:5000/calcular/8/3` devolve `{"a": 8, "b": 3, "soma": 11, "subtracao": 5, "multiplicacao": 24}`.

### `Aula_HTML-CSS/`
- `index.html`: página simples com título, parágrafos e estilo CSS (fonte, cores e espaçamento)
- `inicio.html`: exemplo de **prioridade de seletores CSS**: o seletor de tag (`h2`), de classe (`.texto`) e de id (`#123`) aplicam cores diferentes, e o mais específico vence

---

## Como rodar

```bash
pip install numpy matplotlib flask
python RMC/aulas/aula1.py                 # exercícios de terminal
python RMC/aulas/game.py                  # jogo de adivinhação
python Raciocinio_Algoritmico/aula3.py    # sobe a API em http://127.0.0.1:5000
```

Os arquivos HTML podem ser abertos direto no navegador.

---

O trabalho de Machine Learning está no repositório [Notavel](https://github.com/franpietrobelli-creator/Notavel), e os TDEs de RMC estão em [TDEs_RMC](https://github.com/franpietrobelli-creator/TDEs_RMC).
