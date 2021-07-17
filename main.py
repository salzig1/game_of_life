"""https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life"""

import pygame as pg
import random
from decorator import count_calls
from visulation import graph
pg.init()

# general
FPS = 130
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 800
SCREEN_COLOR = (125, 57, 71)

# game rules
ROWS = 30
CELL_COLOR = (37, 31, 161)

# data collection
cell_count = []
remaining_cells = []
runs = 0

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
grid = [[random.choice([1, 0]) for _ in range(ROWS)] for _ in range(ROWS)]

clock = pg.time.Clock()

myfont = pg.font.SysFont('Comic Sans MS', 25)

def main():
    """Main loop"""

    global runs

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            # restart button
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (x >= 13 and x <= 13 + 100
                        and y >= 110 and y <= 110 + 40):
                    restart()


        clock.tick(FPS)
        screen.fill(SCREEN_COLOR)

        cells = draw_cells_and_grid()
        gui(cells)
        update_cells()

        # TODO: find way to find out if no cells spawn

        # stop if simulation is over
        if len(cell_count) > 3:
            if cell_count[-1] == cell_count[-2] == cell_count[-3] == cell_count[-4]:

                runs += 1

                # collect data
                remaining_perc = 100 / cell_count[0] * cell_count[-1]
                remaining_cells.append(remaining_perc)

                restart()

        pg.display.flip()


def gui(cells):
    global runs

    # run counter
    textsurface = myfont.render("Runned Simulations: " + str(runs), False, (0, 0, 0))
    screen.blit(textsurface, (535, 0))

    # generation counter
    textsurface = myfont.render("Generations: " + str(count_calls.call_count), False, (0, 0, 0))
    screen.blit(textsurface, (10, 0))

    # alive cells counter
    textsurface = myfont.render("Alive cells: " + str(cells), False, (0, 0, 0))
    screen.blit(textsurface, (10, 50))
    cell_count.append(cells)

    # restart button
    s = pg.Surface((100, 40))
    s.set_alpha(130)
    s.fill((255, 0, 0))
    screen.blit(s, (10, 110))

    textsurface = myfont.render("Restart", False, (0, 0, 0))
    screen.blit(textsurface, (13, 110))


def restart():
    global grid

    cell_count.clear()
    count_calls.call_count = 0
    grid.clear()
    grid = [[random.choice([1, 0]) for _ in range(ROWS)] for _ in range(ROWS)]


def draw_cells_and_grid():
    """Draws living cells, returns
       number of alive cells"""

    alive_cells, x, y = 0, 0, 0
    cell_size = SCREEN_WIDTH / ROWS
    for i in range(ROWS):
        for j in range(ROWS):
            # draw if alive
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
    # graph(count_calls.call_count, cell_count)
    graph(runs, remaining_cells)
