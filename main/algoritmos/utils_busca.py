
from typing import List, Optional, Tuple

from main.no import No


def reconstruir_caminho(no_final: No) -> List[Tuple[int, int]]:
    caminho: List[Tuple[int, int]] = []
    curr: Optional[No] = no_final

    while curr:
        caminho.append(curr.pos)
        curr = curr.pai

    return caminho[::-1]
