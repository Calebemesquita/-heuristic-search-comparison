
import random
from typing import List, Optional, Tuple

from main.algoritmos.best_first_search import HeuristicaFn, Ponto, RetornoBusca
from main.mapa import vizinhos


def sde_gulosa_deterministica(
    mapa,
    origem: Ponto,
    destino: Ponto,
    heuristica_fn: HeuristicaFn,
) -> RetornoBusca:


    n = len(mapa)
    atual_pos: Ponto = origem
    atual_h: float = heuristica_fn(origem, destino)
    atual_g: float = 0
    caminho: List[Ponto] = [origem]

    estados_gerados = 1
    estados_visitados = 0

    while atual_pos != destino:
        estados_visitados += 1
        melhorou = False

        for v in vizinhos(atual_pos, mapa, n):
            estados_gerados += 1
            v_h = heuristica_fn(v, destino)

            if v_h < atual_h:
                atual_g += mapa[v[0]][v[1]]
                atual_h = v_h
                atual_pos = v
                caminho.append(v)
                melhorou = True
                break

        if not melhorou:
            return None, None, estados_gerados, estados_visitados

    return caminho, int(atual_g), estados_gerados, estados_visitados


def sde_maior_aclive(
    mapa,
    origem: Ponto,
    destino: Ponto,
    heuristica_fn: HeuristicaFn,
) -> RetornoBusca:


    n = len(mapa)
    atual_pos: Ponto = origem
    atual_h: float = heuristica_fn(origem, destino)
    atual_g: float = 0
    caminho: List[Ponto] = [origem]

    estados_gerados = 1
    estados_visitados = 0

    while atual_pos != destino:
        estados_visitados += 1
        melhor_v: Optional[Ponto] = None
        melhor_h: float = atual_h

        for v in vizinhos(atual_pos, mapa, n):
            estados_gerados += 1
            v_h = heuristica_fn(v, destino)

            if v_h < melhor_h:
                melhor_h = v_h
                melhor_v = v

        if melhor_v is None:
            return None, None, estados_gerados, estados_visitados

        atual_g += mapa[melhor_v[0]][melhor_v[1]]
        atual_h = melhor_h
        atual_pos = melhor_v
        caminho.append(melhor_v)

    return caminho, int(atual_g), estados_gerados, estados_visitados


def sde_gulosa_estocastica(
    mapa,
    origem: Ponto,
    destino: Ponto,
    heuristica_fn: HeuristicaFn,
    rng: random.Random,
) -> RetornoBusca:

    n = len(mapa)
    atual_pos: Ponto = origem
    atual_h: float = heuristica_fn(origem, destino)
    atual_g: float = 0
    caminho: List[Ponto] = [origem]

    estados_gerados = 1
    estados_visitados = 0

    while atual_pos != destino:
        estados_visitados += 1
        melhores_vizinhos: List[Tuple[Ponto, float]] = []

        for v in vizinhos(atual_pos, mapa, n):
            estados_gerados += 1
            v_h = heuristica_fn(v, destino)

            if v_h < atual_h:
                melhores_vizinhos.append((v, v_h))

        if not melhores_vizinhos:
            return None, None, estados_gerados, estados_visitados

        melhor_v, melhor_h = rng.choice(melhores_vizinhos)

        atual_g += mapa[melhor_v[0]][melhor_v[1]]
        atual_h = melhor_h
        atual_pos = melhor_v
        caminho.append(melhor_v)

    return caminho, int(atual_g), estados_gerados, estados_visitados
