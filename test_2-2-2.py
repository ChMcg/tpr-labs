#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.optimize import linprog
import matplotlib
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
for i in range(100, 5000, 50):
    initial_volume = i
    costs = [0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0] 
    A_ub = [
        [ 3.9,    0,     0,    0,    0,    0,     0,    0,    0,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
        [   0, -0.4,     0,    0,  3.9,    0,     0,    0,    0,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
        [   0, -0.4,     0,    0,    0, -0.4,     0,    0,  3.9,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
        [   0, -0.4,     0,    0,    0, -0.4,     0,    0,    0, -0.4,     0,    0,  3.9,    0,     0,    0,   0, 0,     0, 0],
        [   0, -0.4,     0,    0,    0, -0.4,     0,    0,    0, -0.4,     0,    0,    0, -0.4,     0,    0, 3.9, 0,     0, 0],
        [   0,    0, 1/1.6,    0,    0,    0,     0,    0,    0,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
        [   0,    0,     0, -0.1,    0,    0, 1/1.6,    0,    0,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
        [   0,    0,     0, -0.1,    0,    0,     0, -0.1,    0,    0, 1/1.6,    0,    0,    0,     0,    0,   0, 0,     0, 0],
        [   0,    0,     0, -0.1,    0,    0,     0, -0.1,    0,    0,     0, -0.1,    0,    0, 1/1.6,    0,   0, 0,     0, 0],
        [   0,    0,     0, -0.1,    0,    0,     0, -0.1,    0,    0,     0, -0.1,    0,    0,     0, -0.1,   0, 0, 1/1.6, 0],
        [   0,    0,     1,    1,    0,    0,     0,    0,    0,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
        [-0.5,    0,     0,    0,    0,    0,     1,    1,    0,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
        [   0,    0,     0,    0, -0.5,    0,     0,    0,    0,    0,     1,    1,    0,    0,     0,    0,   0, 0,     0, 0],
        [   0,    0,     0,    0,    0,    0,     0,    0, -0.5,    0,     0,    0,    0,    0,     1,    1,   0, 0,     0, 0],
        [   0,    0,     0,    0,    0,    0,     0,    0,    0,    0,     0,    0, -0.5,    0,     0,    0,   0, 0,     1, 1]
    ]
                
    b_ub = [3900, 3900, 3900, 3900, 3900, initial_volume, initial_volume, initial_volume, initial_volume, initial_volume, initial_volume, 0, 0, 0, 0] #Vector of coefficients (right part) in inequalities

    A_eq = [
        [   1,1,1,1,    0,0,0,0,    0,0,0,0,    0,0,0,0,    0,0,0,0],
        [-3.9,0,0,0,    1,1,1,1,    0,0,0,0,    0,0,0,0,    0,0,0,0],
        [   0,0,0,0, -3.9,0,0,0,    1,1,1,1,    0,0,0,0,    0,0,0,0],
        [   0,0,0,0,    0,0,0,0, -3.9,0,0,0,    1,1,1,1,    0,0,0,0],
        [   0,0,0,0,    0,0,0,0,    0,0,0,0, -3.9,0,0,0,    1,1,1,1]
    ] 
    
    b_eq = [4400, 0, 0, 0, 0] 
    ans = linprog(costs, A_ub, b_ub, A_eq, b_eq)	
    
    data_sts 	= sum(ans.x[0::4])
    data_sts_up	= sum(ans.x[1::4])
    data_stm	= sum(ans.x[3::4])
        
    objective_function_val 	= plt.scatter(initial_volume, -ans.fun, c="#FFCDD2")
    steel_to_steel 			= plt.scatter(initial_volume, data_sts, c="#80DEEA") 
    steel_to_up_steel 		= plt.scatter(initial_volume, data_sts_up, c="#B3E5FC")
    steel_to_up_machine 	= plt.scatter(initial_volume, data_stm, c="#D1C4E9")
    if i == 1000: 
        plt.legend(
            [
                'пр-во станков',
                'увеличение пр-ва стали',
                'пр-во стали',
                'увеличение пр-ва станков'
            ]
        )

plt.title('Задание 2.2.1')
ax.set_xlabel('Объём стали')
ax.set_ylabel('Значения переменных')
grid1 = plt.grid(True)
plt.show()
