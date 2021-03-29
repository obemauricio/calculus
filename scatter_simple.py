#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 17:17:00 2021

@author: obe
"""

import matplotlib.pyplot as plt
import random
import numpy as np

x1 = random.sample(range(0, 100), 10)
y1 = random.sample(range(0,100), 10)
print(x1, y1)

coeffs = np.polyfit(x1, y1, 1)
m = coeffs[0]
const = coeffs[1]
print(m, const)
fun_lin = (x1 * m) + const
plt.plot(x1, fun_lin)

plt.scatter(x1, y1, label='Datos 1', color='red')

plt.title('Scatter')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.legend()
plt.show()