#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 17:51:08 2021

@author: obe
"""

import matplotlib.pyplot as plt
import random

stocks = random.sample(range(0, 20), 5)
apple = random.sample(range(0, 30), 5)
BTC = random.sample(range(0, 40), 5)
tesla = random.sample(range(0, 70), 5)

division = random.choices([30,60,20,10,80,15,35,45], k=4)
print(division)

activities = ['stock', 'apple', 'BTC', 'tesla']
color = ['red', 'purple', 'blue', 'orange']
#configurar las caracteristicas del grafico
plt.pie(division, labels=activities, colors=color, startangle=90, shadow= True, explode=(0.1,0,0,0), autopct='½1.1f½½')
plt.title('Pie graph')
plt.show

