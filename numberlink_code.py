from csp import *

puzzle=[['.','.','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.', 3 ,'.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.','.', 2 ,'.'],
        [ 2 , 1 , 3 ,'.','.', 1 ]]

def gVar(x,y):
    return 'V_'+str(x)+'_'+str(y)
    
def puzzle_display(puzzle):
    comp=len(puzzle)
    for y in range(comp):
        for x in range(comp):
            print(puzzle[y][x],end=' ')
        print()

def puzzle_resolvido(puzzle,assignment):
    new_puzzle=puzzle.copy()
    for l in range(len(new_puzzle)):
        for c in range(len(new_puzzle[0])):
            if new_puzzle[l][c] =='.':
                new_puzzle[l][c]=assignment[gVar(c,l)][1]
    return new_puzzle

def CSP_numberlink(puzzle):
    height = len(puzzle)
    width = len(puzzle[0])
    domain = {}
    numbers = set()

    # Inicializar domínios e identificar números
    for i in range(height):
        for j in range(width):
            var = f'v_{j}_{i}'
            if puzzle[i][j] != '.':
                numbers.add(int(puzzle[i][j]))
            domain[var] = []

    # Configurar domínios para células finais e não finais
    for i in range(height):
        for j in range(width):
            var = f'v_{j}_{i}'
            if puzzle[i][j] == '.':
                # Célula não final: conexões com base na localização
                if i == 0: #primeira linha
                    if j == 0:
                        domain[var] += [('se', number) for number in numbers]
                    elif j == width-1:
                        domain[var] += [('sw', number) for number in numbers]
                    else:
                        domain[var] += [('se', number) for number in numbers] + [('sw', number) for number in numbers] + [('we', number) for number in numbers]
                elif i == height-1: #última linha
                    if j == 0:
                        domain[var] += [('ne', number) for number in numbers]
                    elif j == width-1:
                        domain[var] += [('nw', number) for number in numbers]
                    else:
                        domain[var] += [('ne', number) for number in numbers] + [('nw', number) for number in numbers] + [('we', number) for number in numbers]
                elif j == 0: #primeira coluna
                    domain[var] += [('se', number) for number in numbers] + [('ne', number) for number in numbers] + [('ns', number) for number in numbers]
                elif j == width-1: #última coluna
                    domain[var] += [('sw', number) for number in numbers] + [('nw', number) for number in numbers] + [('ns', number) for number in numbers]
                else: #células do meio
                    domain[var] += [('se', number) for number in numbers] + [('sw', number) for number in numbers] + \
                                   [('ne', number) for number in numbers] + [('nw', number) for number in numbers] + \
                                   [('ns', number) for number in numbers] + [('we', number) for number in numbers]
            else:
                num = int(puzzle[i][j])
                # Célula final: conexões diretas conforme o número
                if i == 0:
                    #check se a celula a sul está livre
                    if puzzle[i+1][j] == '.':
                        domain[var] += [('s', num)]
                if i == height-1:
                    #check se a celula a norte está livre
                    if puzzle[i-1][j] == '.':
                        domain[var] += [('n', num)]
                if j == 0:
                    #check se a celula a este está livre
                    if puzzle[i][j+1] == '.':
                        domain[var] += [('e', num)]
                if j == width-1:
                    #check se a celula a oeste está livre
                    if puzzle[i][j-1] == '.':
                        domain[var] += [('w', num)]
                if 0 < i < height - 1:
                    #check se a celula a norte e a sul estão livres
                    if puzzle[i-1][j] == '.':
                        domain[var] += [('n', num)]
                    if puzzle[i+1][j] == '.':
                        domain[var] += [('s', num)]
                if 0 < j < width - 1:
                    #check se a celula a este e oeste estão livres
                    if puzzle[i][j-1] == '.':
                        domain[var] += [('w', num)]
                    if puzzle[i][j+1] == '.':
                        domain[var] += [('e', num)]

    return domain

domain = CSP_numberlink(puzzle)
for key, value in sorted(domain.items()):
    print(f'{key}: {value}')

# Output esperado conforme fornecido
expected_output = {
    "V_0_0": [('se', 1), ('se', 2), ('se', 3)],
    "V_0_1": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('se', 1), ('se', 2), ('se', 3)],
    "V_0_2": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('se', 1), ('se', 2), ('se', 3)],
    "V_0_3": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('se', 1), ('se', 2), ('se', 3)],
    "V_0_4": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('se', 1), ('se', 2), ('se', 3)],
    "V_0_5": [('n', 2)],
    "V_1_0": [('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_1_1": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_1_2": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_1_3": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_1_4": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_1_5": [('n', 1)],
    "V_2_0": [('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_2_1": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_2_2": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_2_3": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_2_4": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_2_5": [('e', 3), ('n', 3)],
    "V_3_0": [('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_3_1": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_3_2": [('e', 3), ('n', 3), ('s', 3), ('w', 3)],
    "V_3_3": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_3_4": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_3_5": [('ne', 1), ('ne', 2), ('ne', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_4_0": [('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_4_1": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_4_2": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_4_3": [('ne', 1), ('ne', 2), ('ne', 3), ('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('se', 1), ('se', 2), ('se', 3), ('sw', 1), ('sw', 2), ('sw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_4_4": [('e', 2), ('n', 2), ('s', 2), ('w', 2)],
    "V_4_5": [('ne', 1), ('ne', 2), ('ne', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('we', 1), ('we', 2), ('we', 3)],
    "V_5_0": [('sw', 1), ('sw', 2), ('sw', 3)],
    "V_5_1": [('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('sw', 1), ('sw', 2), ('sw', 3)],
    "V_5_2": [('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('sw', 1), ('sw', 2), ('sw', 3)],
    "V_5_3": [('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('sw', 1), ('sw', 2), ('sw', 3)],
    "V_5_4": [('ns', 1), ('ns', 2), ('ns', 3), ('nw', 1), ('nw', 2), ('nw', 3), ('sw', 1), ('sw', 2), ('sw', 3)],
    "V_5_5": [('n', 1), ('w', 1)]
}

# Gere o domínio a partir do código CSP_numberlink
domain = CSP_numberlink(puzzle)



