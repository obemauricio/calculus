#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:32:01 2021

@author: obe
"""

import matplotlib.pyplot as plt
import random

x1 = random.sample(range(0, 10), 5)
y1 = random.sample(range(0, 10), 5)
x2 = random.sample(range(0, 10), 5)
y2 = random.sample(range(0, 10), 5)

#configurar las caracteristicas del grafico
plt.bar(x1, y1, label='Datos 1', width=0.7, color='black')
plt.bar(x2, y2, label='Datos 2', width=0.7, color='red')
#definir titulos y nombres de ejes
plt.title('Grafico de barras')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
#mostrar leyendas y figura
plt.legend()
plt.show()