import numpy as np
from cvxopt import matrix, solvers

c = matrix(
    [1.4, 5.1, 1.3, 5.1, 1.4, 5.1, 1.3, 5.1]
)

# G = matrix(
#     [
#         [    -1,     -1,      0,      0,  0,  0,  0,  0],
#         [     0,      0,     -1,     -1,  0,  0,  0,  0],
#         [     0,      0,      0,      0, -1, -1,  0,  0],
#         [     0,      0,      0,      0,  0,  0, -1, -1],
#         [     1,      0,      1,      0,  0,  0,  0,  0],
#         [  10/7,      0,   10/7,      0,  1,  0,  1,  0],
#         [10/7+1,      0, 10/7+1,      0,  1,  0,  1,  0],
#         [     0,      1,      0,      1,  0,  0,  0,  0],
#         [     0,   10/7,      0,   10/7,  0,  1,  0,  1],
#         [     0, 10/7+1,      0, 10/7+1,  0,  1,  0,  1],
#         [1,0,0,0,0,0,0,0],
#         [0,1,0,0,0,0,0,0],
#         [0,0,1,0,0,0,0,0],
#         [0,0,0,1,0,0,0,0],
#         [0,0,0,0,1,0,0,0],
#         [0,0,0,0,0,1,0,0],
#         [0,0,0,0,0,0,1,0],
#         [0,0,0,0,0,0,0,1],
#     ],
#     tc='d'
# )

G = matrix(
    [
        [      1,       1,       0,       0,   0,   0,   0,   0],
        [      0,       0,       1,       1,   0,   0,   0,   0],
        [      0,       0,       0,       0,   1,   1,   0,   0],
        [      0,       0,       0,       0,   0,   0,   1,   1],
        [     -1,       0,      -1,       0,   0,   0,   0,   0],
        [  -10/7,       0,   -10/7,       0,  -1,   0,  -1,   0],
        [-10/7-1,       0, -10/7-1,       0,  -1,   0,  -1,   0],
        [      0,      -1,       0,      -1,   0,   0,   0,   0],
        [      0,   -10/7,       0,   -10/7,   0,  -1,   0,  -1],
        [      0, -10/7-1,       0, -10/7-1,   0,  -1,   0,  -1],
        [-1,0,0,0,0,0,0,0],
        [0,-1,0,0,0,0,0,0],
        [0,0,-1,0,0,0,0,0],
        [0,0,0,-1,0,0,0,0],
        [0,0,0,0,-1,0,0,0],
        [0,0,0,0,0,-1,0,0],
        [0,0,0,0,0,0,-1,0],
        [0,0,0,0,0,0,0,-1],
    ],
    tc='d'
)

h = matrix(
        [2300, 5000, 4400, 5800, 3000, 2300, 6100, 2200, 6700, 9300, 0,0,0,0,0,0,0,0 ], 
        tc='d'
    )

# не работает
# if len(G) != len(h):
#     raise BaseException('len(G):', len(G), 'len(h):', len(h))
# for row in G:
#     if len(row) == len(c):
#         raise BaseException("row:", row, "c:", c)

solution = solvers.lp(c, G.T, h, solver='glpk')
print('Status:', solution['status'])
print('Objective :', solution['primal objective'])
print('x = \n', solution['x'], sep='')
