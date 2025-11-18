# app.py
from perfil import Perfil
from competencia import Competencia
from carreira import Carreira

def main():
    print("=== Sistema de Orientação de Carreiras ===")

    nome = input("Digite seu nome: ")
    perfil = Perfil(nome)

    # Define competências possíveis
    competencias_disponiveis = [
        Competencia("Lógica", "técnica"),
        Competencia("Criatividade", "comportamental"),
        Competencia("Colaboração", "comportamental"),
        Competencia("Adaptabilidade", "comportamental"),
        Competencia("Comunicação", "comportamental")
    ]

    print("\nAvalie suas competências de 0 a 10:")
    for c in competencias_disponiveis:
        while True:
            try:
                nivel = int(input(f"{c.nome}: "))
                if 0 <= nivel <= 10:
                    perfil.adicionar_competencia(c, nivel)
                    break
                else:
                    print("Digite um número entre 0 e 10.")
            except ValueError:
                print("Valor inválido. Digite um número.")

    # Define carreiras e seus requisitos
    carreiras = [
        Carreira("Engenheiro de Software", {"Lógica": 8, "Colaboração": 6, "Adaptabilidade": 6}),
        Carreira("Designer de Produto", {"Criatividade": 8, "Comunicação": 7, "Colaboração": 6}),
        Carreira("Gestor de Projetos", {"Comunicação": 8, "Adaptabilidade": 7, "Colaboração": 8}),
        Carreira("Cientista de Dados", {"Lógica": 9, "Adaptabilidade": 7, "Criatividade": 5})
    ]

    print("\n--- Seu perfil ---")
    perfil.exibir_perfil()

    print("\n--- Recomendações de Carreira ---")
    for c in carreiras:
        print(c.recomendar(perfil))

    print("\nObrigado por usar o sistema! 🚀")

if __name__ == "__main__":
    main()
