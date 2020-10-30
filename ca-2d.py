import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


dimension=int(sys.argv[1])
iteraciones=int(sys.argv[2])

kernel=np.zeros([dimension, dimension], dtype = int)
kernel[int((dimension-1)/2),int((dimension-1)/2)]=1

class CellularAutomata2D:
    def __init__(self,dimension,matriz):
        self.dimension=dimension
        self.matriz_init=matriz

    def itera(self,kernel):
        lista_coordenadas=[]
        dimension=self.dimension

        for i in range(dimension):
            for j in range(dimension):
                if kernel[i,j]==1:
                    pass
                else:
                    arriba=kernel[(i-1) % dimension, j]
                    abajo=kernel[(i+1) % dimension, j]
                    derecha=kernel[i,(j+1) % dimension]
                    izquierda=kernel[i,(j-1) % dimension]

                    d1=kernel[(i-1) % dimension,(j-1) % dimension]
                    d2=kernel[(i-1) % dimension,(j+1) % dimension]
                    d3=kernel[(i+1) % dimension, (j-1) % dimension]
                    d4=kernel[(i+1) % dimension, (j+1) % dimension]

                    suma = arriba+abajo+derecha+izquierda+d1+d2+d3+d4

                    if (suma == 1) or (suma == 2):
                        lista_coordenadas.append([i,j])

        for coor in lista_coordenadas:
            self.matriz_init[coor[0],coor[1]]=1


### Generamos una instancia de la clase
CA=CellularAutomata2D(dimension, kernel)

### Generamos un giff de las figuras de la matriz en las distintas iteraciones
fig = plt.figure()
ims = []
for i in range(iteraciones):
    CA.itera(CA.matriz_init)
    im = plt.imshow(CA.matriz_init, animated=True)
    ims.append([im])


ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=1000)

plt.show()

writer = animation.PillowWriter(fps=25)
ani.save("demo_CA2D.gif", writer=writer)
