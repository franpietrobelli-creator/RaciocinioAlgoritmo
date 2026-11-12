import matplotlib.pyplot as plt
x = [0,1,2,3]
y = [0,1,4,9]
plt.plot(x, y)
plt.show()

def f(x):
    return x**2
x = list(range(-5, 6))
y = [f(i) for i in x]
plt.plot(x, y) #gera um gráfico de linha conectando os pontos (x[i], y[i]) para cada i
plt.show()

x = list(range(-8, 9))
y = [f(i) for i in x] #gera uma lista de valores de y aplicando a função f a cada elemento de x
plt.plot(x, y)
plt.title("Gráfico de f(x)")#adiciona um título ao gráfico
plt.xlabel("x")#adiciona rótulo ao eixo x
plt.ylabel("y") #adiciona rótulo ao eixo y
plt.grid() #adiciona uma grade ao gráfico
plt.show() #exibe o gráfico na tela

x = list(range(-10, 11))
y = [f(i) for i in x]
plt.plot(x, y)
plt.title("Gráfico de f(x)=x ^2")
plt.xlabel("x")
plt.ylabel("y") 
plt.grid() 
plt.show()  

def f(x):
    return x**2
def g(x):
    return x**x+1
x = list(range(-5, 6))

plt.plot(x, [f(i) for i in x])
plt.plot(x, [g(i) for i in x])
plt.grid()
plt.show()

def f(x):
    return x**3-2*x+1
x = list(range(-10, 10))
y = [f(i) for i in x]
plt.plot(x, y)
plt.title("Gráfico de f(x)=x^3-2x+1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

def g(x):
    return x**2-4*x+3/2
x = list(range(-9, 9))
y = [g(i) for i in x]
plt.plot(x, y)
plt.title("Gráfico de g(x)=x^2-4x+3/2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()