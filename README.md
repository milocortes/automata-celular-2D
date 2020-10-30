# Autómata Celular 2D

Se realizó la implementación de un Autómata Celular en 2D con las siguientes características:

1. Vecindad de Von Neumann
2. Estados: 1 y 0
3. Reglas
	* Si la celda está activa, permanece activa
	* En otro caso, se suman los estados de las celdas vecinas, si las activas son 1 o 2 entonces la celda se activa, en caso contrario permanece inactiva.
### Ejecución del programa

El programa recibe dos argumentos. El primero corresponde al tamaño de la matriz y el segundo a la cantidad de iteraciones.
```
python ca-2d.py dim iteraciones
```
![](demo_CA2D.gif) 