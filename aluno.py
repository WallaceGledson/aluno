# -*- coding: utf-8 -*-
"""Aluno.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hxH_6h4XzuBpAtf60D8a-o0_i3tK2H0u
"""

sala = []
while True:
    acao = int(input('''digite 1 para adicionar um aluno
    2 para excluir um aluno
    3 para atualizar o aluno
    4 para ver lista de alunos'''))
    if acao == 1:
        aluno = input('informe o nome do aluno')
        sala.append(aluno)
    elif acao == 2:
        aluno = input('informe o aluno que deseja excluir! ')
        if aluno in sala:
            aluno_x = sala.index(aluno)
            sala.pop(aluno_x)
            print(f'{aluno} excluido(a) com sucesso.')
        else:
            print('o aluno nao esta cadastrado.')
    elif acao == 3:
        aluno = input('informe o nome do aluno que desejar atualizar')
        if aluno in sala:
            aluno_x = sala.index(aluno)
            sala.pop(aluno_x)
            aluno = input('informe o nome do aluno')
            sala.insert(aluno_x,aluno)
            print(f'{aluno} foi adicionado com sucesso.')
            sala.sort()
        else:
            print('o aluno nao esta cadastrado')
    elif acao == 4:
                print(sala)
    elif acao == 5:
        break 
    else:
        print('opcao invalida')