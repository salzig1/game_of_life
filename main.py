import pygame as pg
import random
from decorator import count_calls
from visulation import graph
pg.init()

# general
FPS = 10
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 800
SCREEN_COLOR = (125, 57, 71)

# game rules
ROWS = 300
CELL_COLOR = (37, 31, 161)

# data collection
cell_count = []

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
grid = [[random.choice([1, 0]) for _ in range(ROWS)] for _ in range(ROWS)]

clock = pg.time.Clock()

myfont = pg.font.SysFont('Comic Sans MS', 30)

def main():
    """Main loop"""

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        clock.tick(FPS)
        screen.fill(SCREEN_COLOR)

        cells = draw_cells_and_grid()
        update_cells()

        # generation counter
        textsurface = myfont.render("Generations: " + str(count_calls.call_count), False, (0, 0, 0))
        screen.blit(textsurface,(10, 0))

        # alive cells counter
        textsurface = myfont.render("Alive cells: " + str(cells), False, (0, 0, 0))
        screen.blit(textsurface, (10, 50))
        cell_count.append(cells)

        # TODO: if no more cells --> break
        if count_calls.call_count == 400:
            run = False

        pg.display.flip()


def draw_cells_and_grid():
    """Draws living cells, returns
       number of alive cells"""

    alive_cells, x, y = 0, 0, 0
    cell_size = SCREEN_WIDTH / ROWS
    for i in range(ROWS):
        for j in range(ROWS):
            if grid[i][j]:
                pg.draw.rect(screen, CELL_COLOR, (x, y, cell_size, cell_size))
                alive_cells += 1
            x += cell_size
        x = 0
        y += cell_size

    return alive_cells



@count_calls
def update_cells():
    """Updates wether cell dies or stays alive
       after simple rules:
    """

    # temporary copy of grid
    temp = [list(i) for i in grid]
    for i in range(ROWS):
        for j in range(ROWS):

            # calculates amount of neighbours
            total = calculate_neighbours(i, j, temp)

            # rules
            if total == 3 and temp[i][j] == 0:
                grid[i][j] = 1
            elif (total < 2 or total > 3) and temp[i][j] == 1:
                grid[i][j] = 0
            else:
                grid[i][j] = temp[i][j]


def calculate_neighbours(i, j, temp):
    """Calculates neighbours of cell"""

    total = 0
    for n in range(-1, 2, 1):
        for m in range(-1, 2, 1):

            # if cell is at the edges
            if i+n < 0 or i+n > ROWS-1 or j+m < 0 or j+m > ROWS-1:
                total += 0
            else:
                total += temp[i+n][j+m]

    # so the cell itself doesnt get count as neighbour
    if temp[i][j] == 1:
        total -= 1

    return total


if __name__ == "__main__":
    main()
    graph(count_calls.call_count, cell_count)