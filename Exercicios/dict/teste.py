from collections import namedtuple

Turma = namedtuple("Turma", "Nome Sobrenome Idade")

aluno_teste = input().split(" ")
aluno = Turma(*aluno_teste)

print(aluno)