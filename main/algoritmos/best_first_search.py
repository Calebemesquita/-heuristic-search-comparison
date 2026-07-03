
import heapq
from typing import Callable, List, Optional, Set, Tuple

from main.algoritmos.utils_busca import reconstruir_caminho
from main.mapa import vizinhos
from main.no import No

Ponto = Tuple[int, int]
FuncHeristic = Callable[[Ponto, Ponto], float]
FuncTotalCost = Callable[[float, float], float]
SearchReturn = Tuple[Optional[List[Ponto]], Optional[int], int, int]


def busca_best_first(mapa, origem: Ponto, destino: Ponto, heuristica_fn: FuncHeristic, calc_f_fn: FuncTotalCost,) -> SearchReturn:
    n = len(mapa)
    bord: List[No] = []
    visited: Set[Ponto] = set()
    estados_gerados = 0
    states_visited = 0

    init_heuristic = heuristica_fn(origem, destino)
    final_heuristic = calc_f_fn(0, init_heuristic)
    node_init = No(f=final_heuristic, g=0, h=init_heuristic, pos=origem, pai=None)

    heapq.heappush(bord, node_init)
    estados_gerados += 1

    while bord:
        current_node = heapq.heappop(bord)

        if current_node.pos in visited:
            continue

        visited.add(current_node.pos)
        states_visited += 1

        if current_node.pos == destino:
            current_path = reconstruir_caminho(current_node)
            return current_path, int(current_node.g), estados_gerados, states_visited

        for neighbor_cord in vizinhos(current_node.pos, mapa, n):
            if neighbor_cord not in visited:
                
                custo_passo_terreno = mapa[neighbor_cord[0]][neighbor_cord[1]]
                
                total_cost = current_node.g + custo_passo_terreno
                estimated_distance = heuristica_fn(neighbor_cord, destino)
                absolute_priority = calc_f_fn(total_cost, estimated_distance)

                new_neighbor_node = No( f=absolute_priority,  g=total_cost,  h=estimated_distance,  pos=neighbor_cord,  pai=current_node)
                
                heapq.heappush(bord, new_neighbor_node)
                estados_gerados += 1

    return None, None, estados_gerados, states_visited
