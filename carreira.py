# carreira.py

class Carreira:
    def __init__(self, nome, requisitos):
        # requisitos: dict com {competencia: nível mínimo}
        self.nome = nome
        self.requisitos = requisitos

    def compatibilidade(self, perfil):
        total = 0
        for comp, nivel_min in self.requisitos.items():
            nivel_usuario = perfil.competencias.get(comp, 0)
            total += min(nivel_usuario / nivel_min, 1)  # limita a 1
        return (total / len(self.requisitos)) * 100

    def recomendar(self, perfil):
        score = self.compatibilidade(perfil)
        if score >= 75:
            return f" {self.nome} — Alta compatibilidade ({score:.1f}%)"
        elif score >= 50:
            return f" {self.nome} — Compatibilidade moderada ({score:.1f}%)"
        else:
            return f"{self.nome} — Baixa compatibilidade ({score:.1f}%)"
