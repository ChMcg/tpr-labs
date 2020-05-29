#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.optimize import linprog

initial_volume = 4400
costs = [0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0] 

A_ub = [
    [ 3.9,    0,     0,    0,    0,    0,     0,    0,    0,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
    [   0, -0.4,     0,    0,  3.9,    0,     0,    0,    0,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
    [   0, -0.4,     0,    0,    0, -0.4,     0,    0,  3.9,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
    [   0, -0.4,     0,    0,    0, -0.4,     0,    0,    0, -0.4,     0,    0,  3.9,    0,     0,    0,   0, 0,     0, 0],
    [   0, -0.4,     0,    0,    0, -0.4,     0,    0,    0, -0.4,     0,    0,    0, -0.4,     0,    0, 3.9, 0,     0, 0],
    [   0,    0, 1/1.6,    0,    0,    0,     0,    0,    0,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
    [   0,    0,     0, -1/6,    0,    0, 1/1.6,    0,    0,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
    [   0,    0,     0, -1/6,    0,    0,     0, -1/6,    0,    0, 1/1.6,    0,    0,    0,     0,    0,   0, 0,     0, 0],
    [   0,    0,     0, -1/6,    0,    0,     0, -1/6,    0,    0,     0, -1/6,    0,    0, 1/1.6,    0,   0, 0,     0, 0],
    [   0,    0,     0, -1/6,    0,    0,     0, -1/6,    0,    0,     0, -1/6,    0,    0,     0, -1/6,   0, 0, 1/1.6, 0],
    [   0,    0,     1,    1,    0,    0,     0,    0,    0,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
    [-0.5,    0,     0,    0,    0,    0,     1,    1,    0,    0,     0,    0,    0,    0,     0,    0,   0, 0,     0, 0],
    [   0,    0,     0,    0, -0.5,    0,     0,    0,    0,    0,     1,    1,    0,    0,     0,    0,   0, 0,     0, 0],
    [   0,    0,     0,    0,    0,    0,     0,    0, -0.5,    0,     0,    0,    0,    0,     1,    1,   0, 0,     0, 0],
    [   0,    0,     0,    0,    0,    0,     0,    0,    0,    0,     0,    0, -0.5,    0,     0,    0,   0, 0,     1, 1]
]
    
b_ub = [3900, 3900, 3900, 3900, 3900, 1200, 1200, 1200, 1200, 1200, 1200, 0, 0, 0, 0] 

A_eq = [
    [   1,1,1,1,    0,0,0,0,    0,0,0,0,    0,0,0,0,    0,0,0,0],
    [-3.9,0,0,0,    1,1,1,1,    0,0,0,0,    0,0,0,0,    0,0,0,0],
    [   0,0,0,0, -3.9,0,0,0,    1,1,1,1,    0,0,0,0,    0,0,0,0],
    [   0,0,0,0,    0,0,0,0, -3.9,0,0,0,    1,1,1,1,    0,0,0,0],
    [   0,0,0,0,    0,0,0,0,    0,0,0,0, -3.9,0,0,0,    1,1,1,1]
] 
b_eq = [initial_volume, 0, 0, 0, 0]

ans = linprog(costs, A_ub, b_ub, A_eq, b_eq)
# print(ans)
ret = ans['x']
ret = [int(x) for x in ret]
# print(ret)
x_s     = ret[0::4]
x_s_u   = ret[1::4]
x_m     = ret[2::4]
x_m_u   = ret[3::4]
print('Производство стали:', '\n\t',              x_s)
print('Увеличение производства стали:', '\n\t',   x_s_u)
print('Производство станков:', '\n\t',            x_m)
print('Увеличение производства станков:', '\n\t', x_m_u)
