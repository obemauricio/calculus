#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:50:15 2021

@author: obe
"""

import matplotlib.pyplot as plt
import random

#definiendo los datos
date = random.sample(range(0,1000), 100)
bins = list(range(0,100, 10))
print(date, bins)
#configurar las caracteristicas del grafico
plt.hist(date, bins, histtype='bar', rwidth=0.8, color='red')
#definir titulos y nombres de ejes
plt.title('Histograma')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
#mostrar figura
plt.show()