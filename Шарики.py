import pygame
from random import randrange


class Board:
    def __init__(self, n_cols, n_rows):
        self.width = n_cols
        self.height = n_rows
        self.board = board1
        self.cell_size = cell_size

    def render(self):
        for x in range(self.width):
            for y in range(self.height):
                if board1[x][y] == 0:
                    pygame.draw.rect(screen, pygame.Color('White'), (x * self.cell_size, y * self.cell_size,
                                                                     self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, pygame.Color('green'), (x * self.cell_size, y * self.cell_size,
                                                                     self.cell_size, self.cell_size), 1)


size = width, height = 500, 500
screen = pygame.display.set_mode(size)
cell_size = 20
n_cols = width // cell_size
n_rows = height // cell_size
board1 = [[0] * n_cols for _ in range(n_rows)]
board = Board(n_cols, n_rows)
board.render()

hero_cords = [0, 0]

first_circle = True
all_circles = []
radius = 10
circles = 20
for circle in range(circles):
    all_circles.append([randrange(10, 490), randrange(10, 490), randrange(1, 5)])
s = 1
pr = 25
pygame.time.set_timer(pr, 10)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pr:

            screen.fill((0, 0, 0))
            board.render()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if hero_cords[0] > 0:
                        hero_cords[0] -= cell_size
                        board1[hero_cords[0] // cell_size][hero_cords[1] // cell_size] = 1
                elif event.key == pygame.K_RIGHT:
                    if hero_cords[0] < 500:
                        hero_cords[0] += cell_size
                        board1[hero_cords[0] // cell_size][hero_cords[1] // cell_size] = 1
                elif event.key == pygame.K_UP:
                    if hero_cords[1] > 0:
                        hero_cords[1] -= cell_size
                        board1[hero_cords[0] // cell_size][hero_cords[1] // cell_size] = 1
                elif event.key == pygame.K_DOWN:
                    if hero_cords[1] < 500:
                        hero_cords[1] += cell_size
                        board1[hero_cords[0] // cell_size][hero_cords[1] // cell_size] = 1

            for i in range(len(all_circles)):

                pygame.draw.circle(screen, pygame.Color('white'), (all_circles[i][0], all_circles[i][1]), radius)
                cords_x, cords_y = all_circles[i][0], all_circles[i][1]

                while cords_x == all_circles[i][0] and cords_y == all_circles[i][1]:
                    # Пока коорд не изменятся, цикл продолжит выполняться

                    if all_circles[i][2] == 1:

                        if all_circles[i][0] > radius and all_circles[i][1] > radius:
                            all_circles[i][0] -= s
                            all_circles[i][1] -= s

                        elif all_circles[i][0] <= radius:
                            all_circles[i][2] = 3

                        else:
                            all_circles[i][2] = 2

                    elif all_circles[i][2] == 2:

                        if all_circles[i][0] > radius and all_circles[i][1] < height - radius:
                            all_circles[i][0] -= s
                            all_circles[i][1] += s

                        elif all_circles[i][0] <= radius:
                            all_circles[i][2] = 4

                        else:
                            all_circles[i][2] = 1

                    elif all_circles[i][2] == 3:

                        if all_circles[i][0] < width - radius and all_circles[i][1] > radius:
                            all_circles[i][0] += s
                            all_circles[i][1] -= s

                        elif all_circles[i][0] >= width - radius:
                            all_circles[i][2] = 1

                        else:
                            all_circles[i][2] = 4

                    elif all_circles[i][2] == 4:

                        if all_circles[i][0] < width - radius and all_circles[i][1] < height - radius:
                            all_circles[i][0] += s
                            all_circles[i][1] += s

                        elif all_circles[i][0] >= width - radius:
                            all_circles[i][2] = 2

                        else:
                            all_circles[i][2] = 3

    pygame.display.flip()