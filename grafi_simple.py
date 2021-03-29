#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:43:59 2021

@author: obe
"""

import matplotlib.pyplot as plt

a = [1, 2, 3, 4]
b = [11, 22, 33, 44]

plt.plot(a, b, color="blue", linewidth=5, label='linea')
plt.legend()
plt.show()