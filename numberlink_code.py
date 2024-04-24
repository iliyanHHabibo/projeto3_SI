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
    # Dominio
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

    #variaveis
    variaveis = domain.keys()
    #neighbors
    
    def get_grid_dimensions(grid):
        """Return the dimensions of the grid as a tuple (number of rows, number of columns)."""
        if not grid:  # Check if the grid is empty
            return (0, 0)
        number_of_rows = len(grid)
        number_of_columns = len(grid[0]) if grid[0] else 0  # Check the first row for number of columns
        return (number_of_rows, number_of_columns)

    def setup_neighbors(n, m):
        """Setup neighbors for a Numberlink puzzle grid of size n x m using V_row_col format for variables."""
        neighbors = {}
        for row in range(n):
            for col in range(m):
                # Define neighbors as a list of variable names in V_row_col format
                adjacent = []
                # Check each direction and add if within bounds, using formatted names
                if row > 0:  # Up
                    adjacent.append(f"V_{row - 1}_{col}")
                if row < n - 1:  # Down
                    adjacent.append(f"V_{row + 1}_{col}")
                if col > 0:  # Left
                    adjacent.append(f"V_{row}_{col - 1}")
                if col < m - 1:  # Right
                    adjacent.append(f"V_{row}_{col + 1}")
                # Assign the list of neighbors to the cell variable in the dictionary
                neighbors[f"V_{row}_{col}"] = adjacent
        return neighbors
    def format_neighbors_to_string(neighbors):
        """Format the neighbors dictionary into a string with the format 'A: B C D; B: C D; etc.'"""
        formatted_string = ""
        for key, values in neighbors.items():
            # Join the list of neighbors into a string separated by spaces
            neighbors_string = ' '.join(values)
            # Append the current key and its neighbors to the formatted string
            formatted_string += f"{key}: {neighbors_string}; "
        return formatted_string.strip()  # Remove the trailing space
    grid_dimension=get_grid_dimensions(puzzle)
    print(format_neighbors_to_string(setup_neighbors(grid_dimension[0],grid_dimension[1])))
    
    
    
    

#neighbours 


        
    
# Gere o domínio a partir do código CSP_numberlink
domain = CSP_numberlink(puzzle)

