
import heapq
from typing import Callable, List, Optional, Set, Tuple

from main.algoritmos.utils_busca import reconstruir_caminho
from main.mapa import vizinhos
from main.no import No

Ponto = Tuple[int, int]

HeuristicaFn = Callable[[Ponto, Ponto], float]

CalcFFn = Callable[[float, float], float]

RetornoBusca = Tuple[Optional[List[Ponto]], Optional[int], int, int]


def busca_best_first(
    mapa,
    origem: Ponto,
    destino: Ponto,
    heuristica_fn: HeuristicaFn,
    calc_f_fn: CalcFFn,
) -> RetornoBusca:

    n = len(mapa)
    borda: List[No] = []
    visitados: Set[Ponto] = set()
    estados_gerados = 0
    estados_visitados = 0

    h_ini = heuristica_fn(origem, destino)
    f_ini = calc_f_fn(0, h_ini)
    no_inicial = No(f=f_ini, g=0, h=h_ini, pos=origem, pai=None)

    heapq.heappush(borda, no_inicial)
    estados_gerados += 1

    while borda:
        atual = heapq.heappop(borda)

        if atual.pos in visitados:
            continue

        visitados.add(atual.pos)
        estados_visitados += 1

        if atual.pos == destino:
            caminho = reconstruir_caminho(atual)
            return caminho, int(atual.g), estados_gerados, estados_visitados

        for v in vizinhos(atual.pos, mapa, n):
            if v not in visitados:
                custo_aresta = mapa[v[0]][v[1]]
                novo_g = atual.g + custo_aresta
                novo_h = heuristica_fn(v, destino)
                novo_f = calc_f_fn(novo_g, novo_h)

                novo_no = No(f=novo_f, g=novo_g, h=novo_h, pos=v, pai=atual)
                heapq.heappush(borda, novo_no)
                estados_gerados += 1

    return None, None, estados_gerados, estados_visitados
