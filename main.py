import pygame as pg
import random
import time

WIDTH = 800
HEIGTH = 800
screen = pg.display.set_mode((WIDTH, HEIGTH))

ROWS = 400
grid = [[random.choice([1, 0]) for _ in range(ROWS)] for _ in range(ROWS)]


clock = pg.time.Clock()

def main():
    run = True


    while run:
        clock.tick(10)
        screen.fill((255, 255, 255))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        draw_cells()
        update_cells()

        pg.display.flip()


def draw_cells():
    x, y = 0, 0
    cell_width = WIDTH / ROWS

    for i in range(ROWS):
        for j in range(ROWS):
            if grid[i][j]:
                pg.draw.rect(screen, (0, 0, 0), (x, y, cell_width, cell_width))
            x += cell_width
        x = 0
        y += cell_width

def update_cells():
    temp = [list(i) for i in grid]

    for i in range(ROWS):
        for j in range(ROWS):
            total = calculate_neighbors(i, j, temp)

            # life conditions
            if total == 3 and temp[i][j] == 0:
                grid[i][j] = 1
            elif (total < 2 or total > 3) and temp[i][j] == 1:
                grid[i][j] = 0
            else:
                grid[i][j] = temp[i][j]








def calculate_neighbors(i, j, temp):
    total = 0
    for n in range(-1, 2, 1):
        for m in range(-1, 2, 1):
            if i+n < 0 or i+n > ROWS-1 or j+m < 0 or j+m > ROWS-1:
                total += 0
            else:
                total += temp[i+n][j+m]

    if temp[i][j] == 1:
        total -= 1



    return total







if __name__ == "__main__":
    main()