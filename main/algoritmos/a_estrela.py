
from main.algoritmos.bfs import (FuncHeristic,Ponto,SearchReturn,BFS,)


def a_estrela( mapa, origem: Ponto, destino: Ponto, heuristica_fn: FuncHeristic,) -> SearchReturn:
    return BFS( mapa, origem, destino, heuristica_fn, calc_f_fn=lambda g, h: g + h,)
