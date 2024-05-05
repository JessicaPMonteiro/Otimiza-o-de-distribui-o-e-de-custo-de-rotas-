# -*- coding: utf-8 -*-
"""API_6-Otimização.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a59w5v8soPoX8YIn3lETJdUFYjoeU2Kb
"""

!pip install pulp
from pulp import *

capacidades = [90000000, 56000000, 90000000]

demandas = [5973721, 1778080, 5958798, 896173, 3241494, 3244827, 12738726, 6792503, 7471374, 2098730, 7295028, 1350774, 1439856, 3977784, 3666906, 271034, 1272373, 569236, 1589336, 5063433, 10686204, 2495205, 1753764, 20427048, 7828763, 5788209, 11836544, 6145143, 13860432, 3482379, 4084642, 10839219, 1336988, 1898750, 14197671, 1716192, 827342, 2539443, 1789064, 973767, 5304924, 838856, 8150094, 678417, 3600095, 3522678, 3675315, 1310374, 1761137, 4402893, 1331761]

custos = [
         [0.565885317460317, 0.514546777777777, 0.436219444444444, 0.471928428184281, 0.507578907290571, 0.55688588835212, 0.529495222222222, 0.554305800376647, 0.433270013164823, 0.717840896239751, 0.37443014499837, 0.793698480392157, 0.77019875, 0.717517142857142, 0.838820103540414, 0.846754098484848, 0.820852083333333, 0.840651446330589, 0.696220282747956, 0.735111111111111, 0.772314814814814, 0.695549928586431, 0.749944444444444, 0.715572748210395, 0.638239999999999, 0.70239181856809, 0.724912018841345, 0.728051204276146, 0.748644444444444, 0.763937727272727, 0.69938869557057, 0.688097525252525, 0.675307638888888, 0.687558184693232, 0.69523351196856, 0.0, 0.0, 0.0, 0.880125555555555, 0.976172337256149, 0.91888351603994, 0.910791665046971, 0.986811540102389, 0.635977875608272, 0.640323156149977, 0.6455140625, 0.282929309600862, 0.285691827111984, 0.302230888888888, 0.356160923410677, 0.421230888888888],
         [0.0, 0.0, 0.0, 0.0, 0.261781252123683, 0.0, 0.0, 0.26426782475158, 0.272099053497942, 0.29769584233978, 0.26691471329046, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.287117708333333 ,0.247116666666666, 0.30014414330218, 0.272387407407407, 0.312135739171374, 0.326399616593567, 0.435734268670309, 0.292742712364105, 0.346254722222222, 0.59854,0.272621679340937, 0.272517245478036, 0.480926304347826, 0.466511720457219, 0.461646922453703, 0.556988518518518, 0.611559020496224, 0.576341914735591, 0.569364872004357, 0.611120099740674, 0.0, 0.0, 0.0, 0.686131041666666, 0.720368539076376, 0.613698333333333, 0.683380865611929, 0.619190555555555],
         [0.426126661464835, 0.380956409022659, 0.376658154935039, 0.40414004969191, 0.407479660240322, 0.374513005407291, 0.431393662215628, 0.371297022014213, 0.479187413926499, 0.285763912678421, 0.561697973966118, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.291277265258215, 0.283728148148148, 0.269506944444444, 0.291433138474295, 0.253963749999999, 0.292163148148148, 0.274617916666666, 0.286542682051282, 0.214776999999999, 0.310358866698367, 0.273383541666666, 0.296390634920634, 0.282618208469055, 0.274100808080808, 0.279591296296296, 0.293892130801687, 0.297450513844515, 0.7204556131062, 0.705420815752461, 0.701328907339073, 0.0, 0.0, 0.0, 0.0, 0.0, 0.477560164499605, 0.488251748888888, 0.47474808080808, 0.89613621031746, 0.961990165306549, 1.05462972222222, 1.01535053485461, 1.10046666666666],
         ]

num_fabricas = len(capacidades)
num_produtos = len(demandas)

producao = LpProblem('Producao', LpMinimize)

x = {(i, j): LpVariable(f'x{i}_{j}', lowBound=0, cat=LpInteger) for i in range(1, num_fabricas + 1) for j in range(1, num_produtos + 1) if (i, j) not in [(1, 36), (1, 37),(1, 38), (2, 1), (2, 2), (2, 3), (2, 4), (2, 6), (2, 7), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (2, 19), (2, 20), (2, 21), (2, 22), (2, 23), (2, 44), (2, 45), (2, 46), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16), (3, 17), (3, 18), (3, 39), (3, 40), (3, 41), (3,42), (3, 43)]}

producao += lpSum(custos[i-1][j-1] * x[i, j] for i in range(1, num_fabricas + 1) for j in range(1, num_produtos + 1) if (i, j) not in [(1, 36), (1, 37),(1, 38), (2, 1), (2, 2), (2, 3), (2, 4), (2, 6), (2, 7), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (2, 19), (2, 20), (2, 21), (2, 22), (2, 23), (2, 44), (2, 45), (2, 46), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16), (3, 17), (3, 18), (3, 39), (3, 40), (3, 41), (3,42), (3, 43)])

for i in range(1, num_fabricas + 1):
    producao += lpSum(x[i, j] for j in range(1, num_produtos + 1) if (i, j) not in [(1, 36), (1, 37),(1, 38), (2, 1), (2, 2), (2, 3), (2, 4), (2, 6), (2, 7), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (2, 19), (2, 20), (2, 21), (2, 22), (2, 23), (2, 44), (2, 45), (2, 46), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16), (3, 17), (3, 18), (3, 39), (3, 40), (3, 41), (3,42), (3, 43)]) <= capacidades[i - 1]

for j in range(1, num_produtos + 1):
    producao += lpSum(x[i, j] for i in range(1, num_fabricas + 1) if (i, j) not in [(1, 36), (1, 37),(1, 38), (2, 1), (2, 2), (2, 3), (2, 4), (2, 6), (2, 7), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (2, 19), (2, 20), (2, 21), (2, 22), (2, 23), (2, 44), (2, 45), (2, 46), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16), (3, 17), (3, 18), (3, 39), (3, 40), (3, 41), (3,42), (3, 43)]) == demandas[j - 1]

producao

producao.solve()

print("Quantidade a ser produzida:", LpStatus[producao.status])
for v in producao.variables():
    print(f"{v.name} = {v.varValue}")

print("Custo Total = ", value(producao.objective))