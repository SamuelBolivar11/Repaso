"""
5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
·
·
·
·
"""

print('Ingresa el primer numero')
numero1 = int(input())

for i in range(1,11):
    print(f'{numero1} X {i} = {numero1 * i}')
