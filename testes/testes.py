import unittest
import numpy as np
import random

from main.heuristicas import distanciaManhattan
from main.algoritmos.a_estrela import a_estrela
from main.algoritmos.busca_gulosa import busca_gulosa
from main.algoritmos.subida_encosta import sde_maior_aclive, sde_gulosa_estocastica

class TestAlgoritmosBusca(unittest.TestCase):

    def setUp(self):
        self.mapa_limpo = np.full((5, 5), 3)
        self.origem = (0, 0)
        self.destino = (4, 4)

 
        self.mapa_armadilha = np.array([
            [3, 3, 3, 3, -1],
            [3, -1, -1, -1, -1],
            [3, 3, 3, 3, 3],
            [3, -1, -1, -1, 3],
            [3, 3, 3, 3, 3]
        ])

    def test_a_estrela_mapa_limpo(self):
        caminho, custo, gerados, visitados = a_estrela(
            self.mapa_limpo, self.origem, self.destino, distanciaManhattan
        )
        self.assertIsNotNone(caminho, "A* deve encontrar um caminho em mapa limpo")
        
        self.assertEqual(custo, 24, "O custo ótimo no grid 5x5 limpo (peso 3) deve ser 24")
        self.assertEqual(caminho[-1], self.destino, "O último nó do caminho deve ser o destino")

    def test_subida_encosta_otimo_local(self):
        caminho, custo, gerados, visitados = sde_maior_aclive(
            self.mapa_armadilha, self.origem, self.destino, distanciaManhattan
        )
        self.assertIsNone(caminho, "Subida de Encosta deve falhar (retornar None) ao cair num ótimo local")
        self.assertIsNone(custo)
        self.assertGreater(visitados, 0, "O algoritmo deve ter visitado alguns nós antes de travar")

    def test_a_estrela_supera_armadilha(self):
        caminho, custo, gerados, visitados = a_estrela(
            self.mapa_armadilha, self.origem, self.destino, distanciaManhattan
        )
        self.assertIsNotNone(caminho, "A* não pode ficar preso em ótimo local")
        self.assertEqual(caminho[-1], self.destino)

    def test_subida_encosta_estocastica(self):
        rng = random.Random(42) 
        caminho, custo, gerados, visitados = sde_gulosa_estocastica(
            self.mapa_limpo, self.origem, self.destino, distanciaManhattan, rng
        )
        self.assertIsNotNone(caminho, "SDE Estocástica deve resolver um mapa limpo")
        self.assertEqual(caminho[-1], self.destino)

if __name__ == '__main__':
    unittest.main()