# GS2_PCP_2025
# 🧭 Sistema de Orientação de Carreiras

Um sistema simples em **Python orientado a objetos** desenvolvido para analisar competências profissionais e recomendar carreiras adequadas ao perfil do usuário. O projeto simula uma ferramenta inteligente de orientação de carreiras, conectando lógica de programação ao desenvolvimento humano e profissional.

---

## 📌 **Descrição do Projeto**

Este sistema solicita ao usuário que avalie suas competências (de 0 a 10). Com base nessas informações, ele calcula a compatibilidade entre o perfil e diferentes carreiras do futuro, retornando recomendações personalizadas.

O projeto foi criado para treinar conceitos fundamentais de Python, incluindo:

* Classes e objetos (POO)
* Listas, dicionários e tuplas
* Funções e condicionais
* Módulos organizados
* Interação em linha de comando (CLI)

---

## 🚀 **Como Executar o Projeto**

### **1. Clonar o repositório:**

```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
```

### **2. Executar o programa principal:**

```bash
python app.py
```

### **3. Siga as instruções na tela:**

* Digite seu nome
* Avalie cada competência com notas entre **0 e 10**
* Receba sua análise de compatibilidade com diversas carreiras

Não é necessária nenhuma biblioteca externa — apenas Python instalado.

---

## 📁 **Estrutura de Arquivos**

```
📦 Projeto
├── app.py               # Arquivo principal (executável)
├── perfil.py            # Classe Perfil
├── competencia.py       # Classe Competencia
├── carreira.py          # Classe Carreira
└── README.md            # Documento atual
```

---

## 🧱 **Arquitetura das Classes**

### **🔹 Classe Competencia** (`competencia.py`)

Representa uma competência técnica ou comportamental.

* Atributos: `nome`, `tipo`

### **🔹 Classe Perfil** (`perfil.py`)

Armazena o nome do usuário e suas competências avaliadas.

* Métodos:

  * `adicionar_competencia()`
  * `exibir_perfil()`

### **🔹 Classe Carreira** (`carreira.py`)

Contém o nome da carreira e seus requisitos mínimos.

* Métodos:

  * `compatibilidade()` → retorna % de adequação
  * `recomendar()` → retorna texto de recomendação

### **🔹 Arquivo Principal** (`app.py`)

* Coleta entradas do usuário
* Cria perfil
* Avalia compatibilidade com carreiras
* Exibe recomendações

---

## 📊 **Demonstração (Exemplo de Saída)**

```
=== Sistema de Orientação de Carreiras ===
Digite seu nome: João

Avalie suas competências de 0 a 10:
Lógica: 9
Criatividade: 6
Colaboração: 5
Adaptabilidade: 7
Comunicação: 8

--- Seu perfil ---
  - Lógica: 9/10
  - Criatividade: 6/10
  - Colaboração: 5/10
  - Adaptabilidade: 7/10
  - Comunicação: 8/10

--- Recomendações de Carreira ---
 Engenheiro de Software — Alta compatibilidade (83.3%)
 Designer de Produto — Baixa compatibilidade (41.6%)
 Gestor de Projetos — Compatibilidade moderada (66.6%)
 Cientista de Dados — Alta compatibilidade (87.5%)
```

---


## 📌 **Autor**

Projeto desenvolvido por **Massayoshi Bando Fogaca e Silva**.

Caso tenha dúvidas ou queira adicionar novas funcionalidades, fique à vontade para abrir *issues* ou enviar *pull requests*! 🚀
