import math
from typing import Tuple

def dist_euclidiana(p1: Tuple[int, int], p2: Tuple[int, int], fator: float = 1.0) -> float:
    dist = math.floor(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))
    return dist * fator

def dist_manhattan(p1: Tuple[int, int], p2: Tuple[int, int], fator: float = 1.0) -> float:
    dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return float(dist * fator)