# perfil.py
from GS2_PCP_2025.competencia import Competencia

class Perfil:
    def __init__(self, nome):
        self.nome = nome
        self.competencias = {}  # dict: nome_competencia -> nível (0 a 10)

    def adicionar_competencia(self, competencia: Competencia, nivel: int):
        self.competencias[competencia.nome] = nivel

    def exibir_perfil(self):
        print(f"\nPerfil de {self.nome}:")
        for comp, nivel in self.competencias.items():
            print(f"  - {comp}: {nivel}/10")
