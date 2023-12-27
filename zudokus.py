def print_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=" ")
        print()

def is_valid_move(sudoku, row, col, num):
    # Verificar si el número ya está en la fila o columna
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    # Verificar si el número ya está en el bloque 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[i + start_row][j + start_col] == num:
                return False

    return True

def find_empty_location(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(sudoku):
    row, col = find_empty_location(sudoku)

    # Si no hay celdas vacías, el sudoku está resuelto
    if row is None and col is None:
        return True

    # Intentar colocar números del 1 al 9 en la celda vacía
    for num in range(1, 10):
        if is_valid_move(sudoku, row, col, num):
            sudoku[row][col] = num

            # Recursivamente intentar resolver el resto del sudoku
            if solve_sudoku(sudoku):
                return True

            # Si no se puede resolver, retroceder y probar otro número
            sudoku[row][col] = 0

    # No hay solución posible desde esta configuración
    return False

# Ejemplo de sudoku para resolver (0 representa una celda vacía)

def print_sudoku(sudoku):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Línea horizontal después de cada bloque de 3 filas
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Separador vertical después de cada bloque de 3 columnas
            print(sudoku[i][j], end=" ")
        print()

# Ejemplo de sudoku para resolver (0 representa una celda vacía)
sudoku_to_solve = [
    [5, 3, 1, 1, 7, 1, 0, 1, 1],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku a resolver:")
print_sudoku(sudoku_to_solve)

if solve_sudoku(sudoku_to_solve):
    print("\nSudoku resuelto:")
    print_sudoku(sudoku_to_solve)
else:
    print("\nNo hay solución para el sudoku proporcionado.")

