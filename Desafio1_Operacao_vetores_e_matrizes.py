'''
Desafio 1: Operações com Vetores e Matrizes

Crie dois vetores e faça as operações de soma e produto escalar.
Crie duas matrizes 2x2 e realize as operações de soma e multiplicação de matrizes.

'''

import numpy as np

# Exercício 1

print('='*140)
print('** OPERAÇÕES COM VETORES **')
print('='*140)

vetor1 = np.array([8, 4, 12])
vetor2 = np.array([9, 3, 21])

# Soma de Vetores
soma_vetores = vetor1 + vetor2
print('\nSoma de Vetores')
print('Vetor 1:', vetor1)
print('Vetor 2:', vetor2)
print('Resultado da soma:', soma_vetores)

# Produto Escalar de Vetores
produto_escalar = np.dot(vetor1, vetor2)
print('\n\nProduto Escalar')
print(f'O produto escalar dos vetores 1 e 2 é: {produto_escalar}')
print()

print('='*140)
print('** OPERAÇÕES COM MATRIZES **')
print('='*140)

A = np.array([[2,4], [6,8]])
B = np.array([[3,9], [15,21]])

# Soma de Matrizes
soma_matrizes = A + B
print('\nSoma de Matrizes')
print('Matriz A:\n', A)
print('Matriz B:\n', B)
print('Resultado da soma:\n', soma_matrizes)

#Multiplicação de matrizes
multiplicacao_matrizes = np.dot(A, B)
print('\n\nMultiplicação de matrizes')
print('Resultado da multiplicação:\n', multiplicacao_matrizes)
print()

