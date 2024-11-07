#!/usr/bin/env python3
""" Exibi relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala 
que frequentam cada uma das atividades.
"""

__version__ = "0.1.0"

# Dados 
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia","Joana", "Carlos","Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Identificar melhor usando tuplas dentro da lista e labels
atividades = [
    ("Ingles",aula_ingles), 
    ("Música",aula_musica), 
    ("Dança", aula_danca),
]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades: # interação vai rodar para cada tipo de aula (
                              # ingles, musica, dança)
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 50)
# sala1 que tem interse├º├úo com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    print("Sala1", atividade_sala1)
    print("Sala2", atividade_sala2)
    print()
    print("#" * 50)
            

