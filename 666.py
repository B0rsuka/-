# Різниця по горизонталі між поточною та наступною клітинами
dx = current_cell.x - next_cell.x
# Різниця по вертикалі між поточною та наступною клітинами
dy = current_cell.y - next_cell.y

# Видаляємо ліву стіну у поточної клітини та праву стіну у наступної клітини
if dx == 1:
    current_cell.walls['left'] = False
    next_cell.walls['right'] = False
# Видаляємо праву стіну у поточної клітини та ліву стіну у наступної клітини
if dx == -1:
    current_cell.walls['right'] = False
    next_cell.walls['left'] = False
# Видаляємо верхню стіну у поточної клітини та нижню стіну у наступної клітини
if dy == 1:
    current_cell.walls['top'] = False
    next_cell.walls['bottom'] = False
# Видаляємо нижню стіну у поточної клітини та верхню стіну у наступної клітини
if dy == -1:
    current_cell.walls['bottom'] = False
    next_cell.walls['top'] = False

# Якщо координати парні, це клітинка, а не стіна
if x % 2 == 0 and y % 2 == 0:
    return False
# Якщо координати непарні, це вертикальна або горизонтальна стіна
if x % 2 == 1 and y % 2 == 1:
    return True

# Якщо координати парні, перевіряємо, чи є стіна знизу від поточної клітини
if x % 2 == 0:
    grid_x = x // 2
    grid_y = (y - 1) // 2
    return grid_cell[grid_x + grid_y * cols].walls['bottom']
# Якщо координати непарні, перевіряємо, чи є стіна справа від поточної клітини
else:
    grid_x = (x - 1) // 2
    grid_y = y // 2
    return grid_cell[grid_x + grid_y * cols].walls['right']

# Створення сітки клітин лабіринту
grid_cell = [Cell(x, y) for y in range(rows) for x in range(cols)]
# Починаємо з першої клітини
current_cell = grid_cell[0]
# Позначаємо її як відвідану
current_cell.visited = True
# Ініціалізуємо стек для відстеження шляху
stack = []

# Перевіряємо сусідів поточної клітини та створюємо лабіринт
while True:
    next_cell = current_cell.check_neighbours()
    if next_cell:
        # Позначаємо наступну клітину як відвідану
        next_cell.visited = True
        # Видаляємо стіни між поточною і наступною клітинами
        remove_walls(current_cell, next_cell)
        # Переходимо до наступної клітини
        current_cell = next_cell
        # Додаємо її до стеку
        stack.append(current_cell)
    elif stack:
        # Якщо немає доступних сусідів, повертаємося до попередньої клітини
        current_cell = stack.pop()
    else:
        # Якщо стек порожній, завершуємо виконання
        break

# Створення списку стін для відображення лабіринту
return [check_wall(grid_cell, x, y) for y in range(rows * 2 - 1) for x in range(cols * 2 - 1)]