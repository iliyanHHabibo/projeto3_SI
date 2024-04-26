from csp import *


def getCoords(variable):
    """
    Convert a variable name in the format 'V_row_col' to a tuple of integers (row, col).
    
    Args:
    - variable (str): The variable identifier in the format 'V_row_col'.
    
    Returns:
    - tuple: A tuple containing two integers (row, col).
    """
    # Strip the prefix 'V_' and split by '_'
    parts = variable[2:].split('_')
    # Convert split parts to integers
    row, col = map(int, parts)
    return (row, col)
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
def sort_key(k):
    parts = k.split('_')
    return (int(parts[1]), int(parts[2]))

def CSP_numberlink(puzzle):
    height = len(puzzle)
    width = len(puzzle[0])
    domain = {}
    numbers = set()
    # Dominio
    # Inicializar domínios e identificar números
    for i in range(height):
        for j in range(width):
            var = f'V_{j}_{i}'
            if puzzle[i][j] != '.':
                numbers.add(int(puzzle[i][j]))
            domain[var] = []

    # Configurar domínios para células finais e não finais
    for i in range(height):
        for j in range(width):
            var = f'V_{j}_{i}'
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
    def sortable_key(key):
      parts = key.split('_')
      return tuple(int(part) for part in parts[1:])
    def get_grid_dimensions(grid):
        """Return the dimensions of the grid as a tuple (number of rows, number of columns)."""
        if not grid:  # Check if the grid is empty
            return (0, 0)
        number_of_rows = len(grid)
        number_of_columns = len(grid[0]) if grid[0] else 0  # Check the first row for number of columns
        return (number_of_rows, number_of_columns)

    def setup_neighbors(m, n):
        """Setup neighbors for a Numberlink puzzle grid of size n x m using V_col_row format for variables
        and return them in the format 'X: Y Z; Y: Z; ...' without repeating neighbors."""
        neighbors_dict = {}
        for row in range(n):
            for col in range(m):
                cell = f"V_{col}_{row}"
                neighbors = []
                # Determine neighbors and add to the list
                # if the cell is a number dont add any neighbors that are numbers
                if type(puzzle[row][col])== int :
                    if row > 0:  # Neighbor to the up
                        if type(puzzle[row-1][col])!=int:
                            neighbors.append(f"V_{col}_{row - 1}")
                   
                    if row < n - 1:  # Neighbor to the down
                        if type(puzzle[row+1][col])!=int:
                            neighbors.append(f"V_{col}_{row + 1}")
                    if col > 0:  # Neighbor to the left
                        if type(puzzle[row][col-1])!=int:
                            neighbors.append(f"V_{col - 1}_{row}")
                    if col < m - 1:  # Neighbor to the right
                        if type(puzzle[row][col+1])!=int:
                            neighbors.append(f"V_{col + 1}_{row}")
                    # Assign the list of neighbors to the cell variable in the dictionary
                    neighbors_dict[cell] = neighbors
                    continue
                    
                if row > 0:  # Neighbor to the up
                    neighbors.append(f"V_{col}_{row - 1}")
                if row < n - 1:  # Neighbor to the down
                    neighbors.append(f"V_{col}_{row + 1}")
                if col > 0:  # Neighbor to the left
                    neighbors.append(f"V_{col - 1}_{row}")
                if col < m - 1:  # Neighbor to the right
                    neighbors.append(f"V_{col + 1}_{row}")
                # Assign the list of neighbors to the cell variable in the dictionary
                neighbors_dict[cell] = neighbors
                
        sorted_dict = {k: neighbors_dict[k] for k in sorted(neighbors_dict.keys(), key=sort_key)}
        sorted_data = {key: sorted(value, key=sortable_key) for key, value in sorted_dict.items()}
   
        
        return sorted_data





 
    grid_dimension=get_grid_dimensions(puzzle)
    neighbors =  setup_neighbors(grid_dimension[0], grid_dimension[1])
    #restrictions
    def constraints(var1, value1, var2, value2):
        """Path Continuity Constraint, Unique Paths Constraint, Number Matching Constraint,Grid Boundary Constraint"""
        #caminhos nunca se cruzam
        if value1[1] != value2[1]:
            return False
        
        #Cells labeled with numbers should only connect to cells with the same number
        if value1[1] != value2[1]:
            return False
        #The path must be continuous and maintain connectivity based on the allowed directions (up, down, left, right). 
        # This might involve specifying allowed "pipe" shapes or directions that can be placed in each cell to ensure continuity.
        #finais
        if value2[0] == 's':
            coords = getCoords(var2)
            coordsSouth = (coords[0], coords[1]+1)
            if getCoords(var1) != coordsSouth:
                return False
       
    
        if value2[0] == 'n':
            coords = getCoords(var2)
            coordsNorth = (coords[0], coords[1]-1)
            if getCoords(var1) != coordsNorth:
                return False
        if value2[0] == 'w':
            coords = getCoords(var2)
            coordsWest = (coords[0]-1, coords[1])
            if getCoords(var1) != coordsWest:
                return False
        if value2[0] == 'e':
            coords = getCoords(var2)
            coordsEast = (coords[0]+1, coords[1])
            if getCoords(var1) != coordsEast:
                return False
        #não finais
        if value2[0] == 'ns':
            coords = getCoords(var2)
            coordsNorth = (coords[0], coords[1]-1)
            coordsSouth = (coords[0], coords[1]+1)
            if getCoords(var1) != coordsNorth and getCoords(var1) != coordsSouth:
                return False
        if value2[0] == 'we':
            coords = getCoords(var2)
            coordsWest = (coords[0]-1, coords[1])
            coordsEast = (coords[0]+1, coords[1])
            if getCoords(var1) != coordsWest and getCoords(var1) != coordsEast:
                return False
        if value2[0] == 'ne':
            coords = getCoords(var2)
            coordsNorth = (coords[0], coords[1]-1)
            coordsEast = (coords[0]+1, coords[1])
            if getCoords(var1) != coordsNorth and getCoords(var1) != coordsEast:
                return False
        if value2[0] == 'nw':
            coords = getCoords(var2)
            coordsNorth = (coords[0], coords[1]-1)
            coordsWest = (coords[0]-1, coords[1])
            if getCoords(var1) != coordsNorth and getCoords(var1) != coordsWest:
                return False
        if value2[0] == 'se':
            coords = getCoords(var2)
            coordsSouth = (coords[0], coords[1]+1)
            coordsEast = (coords[0]+1, coords[1])
            if getCoords(var1) != coordsSouth and getCoords(var1) != coordsEast:
                return False
        if value2[0] == 'sw':
            coords = getCoords(var2)
            coordsSouth = (coords[0], coords[1]+1)
            coordsWest = (coords[0]-1, coords[1])
            if getCoords(var1) != coordsSouth and getCoords(var1) != coordsWest:
                return False
        return True
    
    return CSP(variaveis, domain, neighbors, constraints)


        


try:
    puzzle=[['.','.','.','.','.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.', 3 ,'.','.'],
        ['.','.','.','.','.','.'],
        ['.','.','.','.', 2 ,'.'],
        [ 2 , 1 , 3 ,'.','.', 1 ]]
    p = CSP_numberlink(puzzle)
    z=AC3(p)
    for v in sorted(p.variables):
        print(v,':',sorted(z.curr_domains[v]))
except Exception as e:
    print(repr(e))