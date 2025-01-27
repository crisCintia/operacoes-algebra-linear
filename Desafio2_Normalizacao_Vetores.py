'''
Desafio 2: Crie um programa que receba um vetor e normalize seus valores, ou seja, transforme os valores para a escala de 0 a 1.

Dica: A normalização de um vetor é feita dividindo cada elemento pelo seu maior valor.
'''

import numpy as np

print('='*140)
print('** NORMALIZAÇÃO DE VETORES **')
print('='*140)

print('Para que realizemos a normalização dos vetores, por favor, insira os valores abaixo: ')

# Tratamento de erro para entradas inválidas
while True:
    try:
        vetor = np.array([
            float(input('Valor 1: ')), 
            float(input('Valor 2: ')), 
            float(input('Valor 3: '))
        ])
        break # sai do loop caso os valores forem válidos

    except ValueError:
        print('Valores incorretos, por favor tente novamente!')

# Normalização de vetores
max_valor = np.max(vetor)

if max_valor == 0:
    print('O vetor contém apenas zeros, não pode ser normalizado!')
else:
    vetor_normalizado = np.round(vetor/max_valor, 2)
    print(f'A normalização do vetor é: {vetor_normalizado}')