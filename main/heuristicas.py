import math
from typing import Tuple

"""
# O(1) Independente do tamanho da matriz
# pitagoras, para saber distancia entre dois pontos (x1,y1) e (x2,y2) 
"""
def distanciaEuclidiana(p1: Tuple[int, int], p2: Tuple[int, int], fator: float = 1.0) -> float:
    dist = math.floor(math.hypot(p1[0]-p2[0], p1[1] -p2[1]))
    return dist * fator

""""
# O(1) Independente do tamanho da matriz
# mannhattan, vai saber distancia usnado linhas verticais e horizontais com = ∣x2​−x1​∣ + ∣y2​−y1​∣
"""
def distanciaManhattan(p1: Tuple[int, int], p2: Tuple[int, int], fator: float = 1.0) -> float:
    dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return float(dist * fator)