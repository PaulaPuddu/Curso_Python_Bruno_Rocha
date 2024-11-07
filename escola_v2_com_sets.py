#!/usr/bin/env python3
""" Exibi relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala 
que frequentam cada uma das atividades.
"""

__version__ = "0.1.2"

# Dados 
# versão de lista e sets para dicionarios

alunos = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["João", "Antonio", "Carlos", "Maria", "Isolda"],
}

atividades = {
    "Ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Musica": ["Erik", "Carlos", "Maria"],
    "Danca": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

# Função para listar alunos por atividade
for atividade, inscritos in atividades.items():
    print(f"Atividade: {atividade}")
    for sala, alunos_sala in alunos.items():
        alunos_na_atividade = set(inscritos).intersection(alunos_sala)
        if alunos_na_atividade:
            print(f"  {sala}: {', '.join(alunos_na_atividade)}")
    print()


