#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:21:21 2021

@author: obe
"""

import matplotlib.pyplot as plt

x1 = [3, 4, 5, 6]
y1 = [5, 6, 3, 4]
x2 = [2, 5, 8]
y2 = [3, 4, 3]

#configura las caracteristicas del grafico
plt.plot(x1, y1, label='linea 1', linewidth=5, color='blue')
plt.plot(x2, y2, label='linea 2', linewidth=4, color='red')
#definir titulos y nombres de ejes
plt.title('Diagrama de lineas')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
#mostrar leyenda, cuadricula y figura
plt.legend()
plt.grid()
plt.show()