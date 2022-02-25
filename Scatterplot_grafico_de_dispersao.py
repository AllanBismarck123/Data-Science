import matplotlib.pyplot as plt
from pyparsing import line

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 3300, 100]

titulo = "ScatterPlot: Gráfico de Dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x,y, color = "#FF8C00", linestyle = "--")
plt.scatter(x, y, label = "Meus pontos", color = "black", marker = ".", s = z)
plt.legend()
#plt.show()
plt.savefig("Figura1.png", dpi = 300)