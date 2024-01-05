# Створення кліткового автомата на Python.
# Використаємо бібліотеку matplotlib для візуалізації кліткового автомата.
# Клітковий автомат - "Життя" (Game of Life):
# Цей код створює візуалізацію кліткового автомата "Життя"
# з випадковою початковою конфігурацією.
# Можна змінювати сітки,
# ймовірність живих кліток при початковій ініціалізації та іншими параметрами.


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Розмір сітки
rows, cols = 30, 30

# Ініціалізація випадкового стану кліток
grid = np.random.choice([0, 1], size=(rows, cols), p=[0.7, 0.3])

# Функція для виконання кроку в клітковому автоматі "Життя"
def update(frameNum, img, grid, rows, cols):
    newGrid = grid.copy()
    for i in range(rows):
        for j in range(cols):
            # Обчислення кількості живих сусідів
            total = int((grid[i, (j-1)%cols] + grid[i, (j+1)%cols] +
                         grid[(i-1)%rows, j] + grid[(i+1)%rows, j] +
                         grid[(i-1)%rows, (j-1)%cols] + grid[(i-1)%rows, (j+1)%cols] +
                         grid[(i+1)%rows, (j-1)%cols] + grid[(i+1)%rows, (j+1)%cols])/255)
            # Правила гри "Життя"
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    # Оновлення гри
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

# Створення візуалізації
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, rows, cols),
                              frames=10, interval=500)

plt.show()