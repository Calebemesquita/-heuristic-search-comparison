
import random
from typing import List, Optional, Tuple

from main.algoritmos.best_first_search import HeuristicaFn, Ponto, RetornoBusca
from main.mapa import vizinhos




"""
# algoritmo de <Subida de Encosta> ou deterministica
variação: subida de encosta First Choice
Intera nos vizinhos na ordem N-L-S-O
No primeiro vizinho que Heuristica H(atual) > Hvizinho) ele se move para o vizinho
"""
def subidaEncostaFirstChoice( mapa, origem: Ponto,  destino: Ponto, heuristica_fn: HeuristicaFn,) -> RetornoBusca:
    n = len(mapa)
    current_possition: Ponto = origem
    current_heuristic: float = heuristica_fn(origem, destino)
    
    custo_acumulado: float = 0
    current_path: List[Ponto] = [origem]

    estados_gerados = 1
    estados_visitados = 0

    while current_possition != destino:
        estados_visitados += 1
        melhorou = False

        for v in vizinhos(current_possition, mapa, n):
            estados_gerados += 1
            heuristic_next_vertice = heuristica_fn(v, destino)

            if heuristic_next_vertice < current_heuristic:
                custo_acumulado += mapa[v[0]][v[1]]                     #somamos o custo do vertice que encontramos melhor
                current_heuristic = heuristic_next_vertice              #atualizamos a heuristica
                current_possition = v                                   #atualiza posicao atual
                current_path.append(v)                                  #adiciona o vertice ao caminho
                melhorou = True                                         #quebramos o loop, pois encontramos um vizinho melhor
                break

        if not melhorou:
            return None, None, estados_gerados, estados_visitados       #desiste

    return current_path, int(custo_acumulado), estados_gerados, estados_visitados






"""
# Algoritmo de <Subida de Encosta>
variação: subida de encosta Maior Aclive
Intera nos vizinhos na ordem N-L-S-O
Seleciona o vizinho dos aredores com a menor heuristica H(vizinho) < H(atual)
Se não houver vizinho melhor ele desiste
<Alpinista na Neblina> kkk
"""
def subidaEncostaMaiorAclive( mapa, origem: Ponto, destino: Ponto, heuristica_fn: HeuristicaFn, ) -> RetornoBusca:
    n = len(mapa)
    current_possition: Ponto = origem
    current_heuristic: float = heuristica_fn(origem, destino)

    custo_acumulado: float = 0
    current_path: List[Ponto] = [origem]

    estados_gerados = 1
    estados_visitados = 0

    while current_possition != destino:
        estados_visitados += 1
        best_vertice: Optional[Ponto] = None
        best_heuristic: float = current_heuristic

        for v in vizinhos(current_possition, mapa, n):
            estados_gerados += 1
            heuristic_next_vertice = heuristica_fn(v, destino)

            if heuristic_next_vertice < best_heuristic:
                best_heuristic = heuristic_next_vertice
                best_vertice = v


        if best_vertice is None:
            return None, None, estados_gerados, estados_visitados

        custo_acumulado += mapa[best_vertice[0]][best_vertice[1]]              #somamos o custo do vertice que encontramos melhor
        current_heuristic = best_heuristic                                     #atualizamos a heuristica
        current_possition = best_vertice                                       #atualiza posicao atual
        current_path.append(best_vertice)                                      #adiciona o vertice ao caminho

    return current_path, int(custo_acumulado), estados_gerados, estados_visitados



"""
# Algoritmo de <Subida de Encosta>
variação: subida de encosta Estocástica
Intera nos vizinhos na ordem N-L-S-O
Seleciona o vizinho dos aredores com a menor heuristica H(vizinho) < H(atual)
Porem, se houver mais de um vizinho melhor, ele escolhe aleatoriamente entre eles
e se não houver vizinho melhor ele desiste
"""
def subidaEncostaEstocastica(mapa, origem: Ponto, destino: Ponto, heuristica_fn: HeuristicaFn, rng: random.Random,) -> RetornoBusca:
    n = len(mapa)
    current_possition: Ponto = origem
    current_heuristic: float = heuristica_fn(origem, destino)
    custo_acumulado: float = 0
    current_path: List[Ponto] = [origem]

    estados_gerados = 1
    estados_visitados = 0

    while current_possition != destino:
        estados_visitados += 1
        melhores_vizinhos: List[Tuple[Ponto, float]] = []                   #prepara uma lista de tuplas (vizinho, heuristica) p guardar melhores vizinhos

        for v in vizinhos(current_possition, mapa, n):
            estados_gerados += 1
            heuristic_next_vertice = heuristica_fn(v, destino)

            if heuristic_next_vertice < current_heuristic:
                melhores_vizinhos.append((v, heuristic_next_vertice))

        if not melhores_vizinhos:
            return None, None, estados_gerados, estados_visitados

        best_vertice, best_heuristic = rng.choice(melhores_vizinhos)

        custo_acumulado += mapa[best_vertice[0]][best_vertice[1]]
        current_heuristic = best_heuristic
        current_possition = best_vertice
        current_path.append(best_vertice)

    return current_path, int(custo_acumulado), estados_gerados, estados_visitados
