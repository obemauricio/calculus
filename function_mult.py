#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 00:03:18 2021

@author: obe
"""

from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
def f(x,y):
    return x**2 + y**2
res = 100 
x = np.linspace(-4, 4, num=res)
y = np.linspace(-4, 4, num=res)
x, y = np.meshgrid(x,y)

z = f(x,y)
surf = ax.plot_surface(x, y, z, cmap=cm.cool)

fig.colorbar(surf)
