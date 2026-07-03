
from main.algoritmos.best_first_search import (
    FuncHeristic,
    Ponto,
    SearchReturn,
    busca_best_first,
)


def busca_gulosa(
    mapa,
    origem: Ponto,
    destino: Ponto,
    heuristica_fn: FuncHeristic,
) -> SearchReturn:


    return busca_best_first(
        mapa,
        origem,
        destino,
        heuristica_fn,
        calc_f_fn=lambda g, h: h,
    )
