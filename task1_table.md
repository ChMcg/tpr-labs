#### Табличное представление задачи:


 | $a_{11}$ | $a_{12}$ | $a_{21}$ | $a_{22}$ | $b_{11}$ | $b_{12}$ | $b_{21}$ | $b_{22}$ |    $e_{11}$    |    $e_{12}$    |    $e_{21}$    |    $e_{22}$    | знак  |   h   |
 | :------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: | :------------: | :------------: | :------------: | :------------: | :---: | :---: |
 |    1     |    1     |          |          |          |          |          |          |       1        |       1        |                |                | $<=$  | 2300  |
 |          |          |    1     |    1     |          |          |          |          |                |                |       1        |       1        | $<=$  | 5000  |
 |          |          |          |          |    1     |    1     |          |          |                |                |                |                | $<=$  | 4400  |
 |          |          |          |          |          |          |    1     |    1     |                |                |                |                | $<=$  | 5800  |
 |    1     |          |    1     |          |          |          |          |          |                |                |                |                | $>=$  | 3000  |
 |          |          |          |          |    1     |          |    1     |          | $\frac{10}{7}$ |                | $\frac{10}{7}$ |                | $>=$  | 2300  |
 |    1     |          |    1     |          |    1     |          |    1     |          | $\frac{10}{7}$ |                | $\frac{10}{7}$ |                | $>=$  | 6100  |
 |          |    1     |          |    1     |          |          |          |          |                |                |                |                | $>=$  | 2200  |
 |          |          |          |          |          |    1     |          |    1     |                | $\frac{10}{7}$ |                | $\frac{10}{7}$ | $>=$  | 6700  |
 |          |    1     |          |    1     |          |    1     |          |    1     |                | $\frac{10}{7}$ |                | $\frac{10}{7}$ | $>=$  | 9300  |
 |    1     |          |          |          |          |          |          |          |                |                |                |                | $>=$  |   0   |
 |          |    1     |          |          |          |          |          |          |                |                |                |                | $>=$  |   0   |
 |          |          |    1     |          |          |          |          |          |                |                |                |                | $>=$  |   0   |
 |          |          |          |    1     |          |          |          |          |                |                |                |                | $>=$  |   0   |
 |          |          |          |          |    1     |          |          |          |                |                |                |                | $>=$  |   0   |
 |          |          |          |          |          |    1     |          |          |                |                |                |                | $>=$  |   0   |
 |          |          |          |          |          |          |    1     |          |                |                |                |                | $>=$  |   0   |
 |          |          |          |          |          |          |          |    1     |                |                |                |                | $>=$  |   0   |
 |          |          |          |          |          |          |          |          |       1        |                |                |                | $>=$  |   0   |
 |          |          |          |          |          |          |          |          |                |       1        |                |                | $>=$  |   0   |
 |          |          |          |          |          |          |          |          |                |                |       1        |                | $>=$  |   0   |
 |          |          |          |          |          |          |          |          |                |                |                |       1        | $>=$  |   0   |
  

  #### Функция цели:

  $$
    f(\vec{a}, \vec{b}) = 1,4*(a_{11} + b_{11} + e_{11}) + \\
    5,1*(a_{12} + b_{12} + e_{12}) + \\
    1,3*(a_{21} + b_{21} + e_{21}) + \\
    5,1*(a_{22} + b_{22} + e_{22})
  $$


#### Результат:

| j $\rightarrow$ | 1    | 2    |
| --------------- | ---- | ---- |
| $a_{1j}$        | 0    | 200  |
| $a_{2j}$        | 3000 | 2000 |
| $b_{1j}$        | 0    | 4100 |
| $b_{2j}$        | 3100 | 0    |

Objective : `50770.0`

#### Без замены:

| j $\rightarrow$ | 1    | 2    |
| --------------- | ---- | ---- |
| $a_{1j}$        | 0    | 1400 |
| $a_{2j}$        | 3800 | 1200 |
| $b_{1j}$        | 0    | 4400 |
| $b_{2j}$        | 2300 | 2300 |

Objective : `55360.0`