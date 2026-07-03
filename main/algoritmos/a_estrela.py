"""
A* (A-estrela): busca best-first onde f(n) = g(n) + h(n).

Este módulo agora é apenas um wrapper fino sobre o motor genérico em
`best_first_search.py`, injetando a estratégia de cálculo de f(n)
característica do A* (custo acumulado + heurística).
"""
from main.algoritmos.best_first_search import (
    FuncHeristic,
    Ponto,
    SearchReturn,
    busca_best_first,
)


def a_estrela(
    mapa,
    origem: Ponto,
    destino: Ponto,
    heuristica_fn: FuncHeristic,
) -> SearchReturn:
    """
    Executa A* sobre o mapa, do ponto de origem ao destino.

    Returns:
        RetornoBusca: (caminho, custo_total, estados_gerados, estados_visitados)
    """
    return busca_best_first(
        mapa,
        origem,
        destino,
        heuristica_fn,
        calc_f_fn=lambda g, h: g + h,
    )
