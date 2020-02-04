import pygame
from random import randrange


class Board:
    def __init__(self, n_cols, n_rows):
        self.width = n_cols
        self.height = n_rows
        self.board = board1
        self.cell_size = cell_size
        self.hero_x = 0
        self.hero_y = 0
        self.flag = 0
        self.new_path = False
        self.my_path = []

    def render(self):
        for x in range(self.width):
            for y in range(self.height):
                if board1[y][x] == 1:
                    pygame.draw.rect(screen, pygame.Color('Green'), (x * self.cell_size, y * self.cell_size,
                                                                     self.cell_size, self.cell_size))
                if board1[y][x] == 2:
                    pygame.draw.rect(screen, pygame.Color('Red'), (x * self.cell_size, y * self.cell_size,
                                                                   self.cell_size, self.cell_size))

        pygame.draw.rect(screen, pygame.Color('Blue'), (self.hero_x * self.cell_size, self.hero_y * self.cell_size,
                                                        self.cell_size, self.cell_size))


def clear_my_path():
    for smth in board.my_path:
        board1[smth[0]][smth[1]] = 0
    board.hero_x = 0
    board.hero_y = 0
    board.flag = 0
    board.new_path = False
    board.my_path = []


def death():
    board.hero_x = 0
    board.hero_y = 0
    board.flag = 0
    board1 = [[0] * n_cols for _ in range(n_rows)]
    board1[0][0] = 1


def idk():
    print("начинаем закраску")
    for smth in board.my_path:
        board1[smth[0]][smth[1]] = 1
        if smth[2] == 1:
            if board1[smth[0] + 1][smth[1]] == 0:
                board1[smth[0] + 1][smth[1]] = 4
        elif smth[2] == 2:
            if board1[smth[0] - 1][smth[1]] == 0:
                board1[smth[0] - 1][smth[1]] = 4
        elif smth[2] == 3:
            if board1[smth[0]][smth[1] - 1] == 0:
                board1[smth[0]][smth[1] - 1] = 4
        elif smth[2] == 4:
            if board1[smth[0]][smth[1] + 1] == 0:
                board1[smth[0]][smth[1] + 1] = 4
    for xxxx in board1:
        print(xxxx)

    flag_in_class = False
    cells_0 = 0
    cells_4 = 0

    while not flag_in_class:
        cells = 0
        for y in range(n_rows):
            for x in range(n_cols):
                cells += check_cells(y, x)
        if cells == 0:
            flag_in_class = True

    for y in range(n_rows):
        for x in range(n_cols):
            if board1[y][x] == 4:
                cells_4 += 1
            elif board1[y][x] == 0:
                cells_0 += 1
    if cells_0 >= cells_4:
        for y in range(n_rows):
            for x in range(n_cols):
                if board1[y][x] == 4:
                    board1[y][x] = 1
    else:
        for y in range(n_rows):
            for x in range(n_cols):
                if board1[y][x] == 0:
                    board1[y][x] = 1
                elif board1[y][x] == 4:
                    board1[y][x] = 0


def check_cells(n_row, n_col):
    cells = 0
    if board1[n_row][n_col] == 4:
        if board1[n_row - 1][n_col - 1] == 0:
            cells += 1
            board1[n_row - 1][n_col - 1] = 4
        if board1[n_row - 1][n_col] == 0:
            cells += 1
            board1[n_row - 1][n_col] = 4
        if board1[n_row - 1][n_col + 1] == 0:
            cells += 1
            board1[n_row - 1][n_col + 1] = 4

        if board1[n_row][n_col - 1] == 0:
            cells += 1
            board1[n_row][n_col - 1] = 4
        if board1[n_row][n_col + 1] == 0:
            cells += 1
            board1[n_row][n_col + 1] = 4

        if board1[n_row + 1][n_col - 1] == 0:
            cells += 1
            board1[n_row + 1][n_col - 1] = 4
        if board1[n_row + 1][n_col] == 0:
            cells += 1
            board1[n_row + 1][n_col] = 4
        if board1[n_row + 1][n_col + 1] == 0:
            cells += 1
            board1[n_row + 1][n_col + 1] = 4
    return cells


size = width, height = 480, 480
screen = pygame.display.set_mode(size)
cell_size = 12
n_cols = width // cell_size
n_rows = height // cell_size

board1 = [[0] * n_cols for _ in range(n_rows)]
for q in range(n_cols):
    board1[0][q] = 1
    board1[-1][q] = 1
for z in range(n_rows):
    board1[z][0] = 1
    board1[z][-1] = 1

board = Board(n_cols, n_rows)
board.render()

# board.new_path = False
# board.my_path = []

# board.hero_x = 0
# board.hero_y = 0

first_circle = True
all_circles = []
radius = 6
circles = 5
for circle in range(circles):
    all_circles.append([randrange(2, n_cols-1), randrange(2, n_rows-1), randrange(1, 5)])
s = 3
pr = 25
pygame.time.set_timer(pr, 70)

# flag = 0
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # выбираем направление движения
            if event.key == pygame.K_LEFT:
                board.flag = 1
            elif event.key == pygame.K_RIGHT:
                board.flag = 2
            elif event.key == pygame.K_UP:
                board.flag = 3
            elif event.key == pygame.K_DOWN:
                board.flag = 4
            elif event.key == pygame.K_SPACE:
                board.flag = 0

        if event.type == pr:

            screen.fill((0, 0, 0))
            board.render()

            # налево
            if board.flag == 1 and board.hero_x >= 1 and board1[board.hero_y][board.hero_x - 1] != 2:
                board.hero_x -= 1

            # направо
            elif board.flag == 2 and board.hero_x < n_cols - 1 and board1[board.hero_y][board.hero_x + 1] != 2:
                board.hero_x += 1

            # вверх
            elif board.flag == 3 and board.hero_y >= 1 and board1[board.hero_y - 1][board.hero_x] != 2:
                board.hero_y -= 1

            # вниз
            elif board.flag == 4 and board.hero_y < n_rows - 1 and board1[board.hero_y + 1][board.hero_x] != 2:
                board.hero_y += 1

            # встаем на воду
            if board1[board.hero_y][board.hero_x] == 0:
                if not board.new_path:
                    board.new_path = True
                    board.my_path = []
                board1[board.hero_y][board.hero_x] = 2
                board.my_path.append([board.hero_y, board.hero_x, board.flag])

            # встаем на землю
            elif board1[board.hero_y][board.hero_x] == 1:
                # если шли по воде
                if board.new_path:
                   idk()
                   board.new_path = False

            try:
                for i in range(len(all_circles)):

                    pygame.draw.circle(screen, pygame.Color('white'), (all_circles[i][0] * cell_size,
                                                                       all_circles[i][1] * cell_size), radius)
                    # cords_x, cords_y = all_circles[i][0], all_circles[i][1]

                    flag_ok = False
                    flag_1 = True
                    flag_2 = True
                    flag_3 = True
                    flag_4 = True
                    # print("======", i, all_circles[i])

                    # Пока коорд не изменятся, цикл продолжит выполняться
                    while not flag_ok:

                        # print(all_circles[i][2], flag_1, flag_2, flag_3, flag_4)

                        # влево вверх
                        if all_circles[i][2] == 1:

                            # можно подвинуться
                            if board1[all_circles[i][1] - 1][all_circles[i][0] - 1] != 1 and \
                                    board1[all_circles[i][1] - 1][all_circles[i][0]] != 1 and \
                                    board1[all_circles[i][1]][all_circles[i][0] - 1] != 1:
                                # врезались в путь героя
                                if board1[all_circles[i][1] - 1][all_circles[i][0] - 1] == 2 or \
                                        board1[all_circles[i][1] - 1][all_circles[i][0]] == 2 or \
                                        board1[all_circles[i][1]][all_circles[i][0] - 1] == 2:
                                    clear_my_path()
                                all_circles[i][0] -= 1
                                all_circles[i][1] -= 1
                                flag_ok = True
                            else:
                                # print("меняем направление")
                                flag_1 = False
                                # зашли в угол или наткнулись на угол
                                if board1[all_circles[i][1] - 1][all_circles[i][0] - 1] == 1 and \
                                        board1[all_circles[i][1] - 1][all_circles[i][0]] == 1 and \
                                        board1[all_circles[i][1]][all_circles[i][0] - 1] == 1 or \
                                        board1[all_circles[i][1] - 1][all_circles[i][0] - 1] == 1 and \
                                        board1[all_circles[i][1] - 1][all_circles[i][0]] == 0 and \
                                        board1[all_circles[i][1]][all_circles[i][0] - 1] == 0:
                                    # print("1 угол")
                                    if flag_4:
                                        all_circles[i][2] = 4
                                    elif flag_2:
                                        all_circles[i][2] = 2
                                    elif flag_3:
                                        all_circles[i][2] = 3
                                    else:
                                        flag_ok = True

                                # земля только слева
                                elif board1[all_circles[i][1]][all_circles[i][0] - 1] == 1 and \
                                        board1[all_circles[i][1] - 1][all_circles[i][0]] == 0:
                                    # print("1 земля только слева")
                                    if flag_3:
                                        all_circles[i][2] = 3
                                    elif flag_2:
                                        all_circles[i][2] = 2
                                    elif flag_4:
                                        all_circles[i][2] = 4
                                    else:
                                        flag_ok = True

                                # земля только сверху
                                elif board1[all_circles[i][1] - 1][all_circles[i][0]] == 1 and \
                                        board1[all_circles[i][1]][all_circles[i][0] - 1] == 0:
                                    # print("1 земля только сверху")
                                    if flag_2:
                                        all_circles[i][2] = 2
                                    elif flag_3:
                                        all_circles[i][2] = 3
                                    elif flag_4:
                                        all_circles[i][2] = 4
                                    else:
                                        flag_ok = True
                                else:
                                    # print("1 иное")
                                    if flag_2:
                                        all_circles[i][2] = 2
                                    elif flag_3:
                                        all_circles[i][2] = 3
                                    elif flag_4:
                                        all_circles[i][2] = 4
                                    else:
                                        flag_ok = True

                        # влево вниз
                        elif all_circles[i][2] == 2:

                            # print("---------", i, all_circles[i])
                            # print("можно подвинуться")
                            # можно подвинуться
                            if board1[all_circles[i][1] + 1][all_circles[i][0] - 1] != 1 and \
                                    board1[all_circles[i][1] + 1][all_circles[i][0]] != 1 and \
                                    board1[all_circles[i][1]][all_circles[i][0] - 1] != 1:
                                # врезались в героя
                                if board1[all_circles[i][1] + 1][all_circles[i][0] - 1] == 2 or \
                                   board1[all_circles[i][1] + 1][all_circles[i][0]] == 2 or \
                                   board1[all_circles[i][1]][all_circles[i][0] - 1] == 2:
                                    clear_my_path()
                                all_circles[i][0] -= 1
                                all_circles[i][1] += 1
                                flag_ok = True
                            else:
                                # print("---------", i, all_circles[i])
                                # print(all_circles[i][2], flag_1, flag_2, flag_3, flag_4)
                                # print("меняем направление")
                                flag_2 = False
                                # зашли в угол  или наткнулись на угол
                                if board1[all_circles[i][1] + 1][all_circles[i][0] - 1] == 1 and \
                                        board1[all_circles[i][1] + 1][all_circles[i][0]] == 1 and \
                                        board1[all_circles[i][1]][all_circles[i][0] - 1] == 1 or \
                                        board1[all_circles[i][1] + 1][all_circles[i][0] - 1] == 1 and\
                                        board1[all_circles[i][1] + 1][all_circles[i][0]] == 0 and \
                                        board1[all_circles[i][1]][all_circles[i][0] - 1] == 0:
                                    # print("2 угол")
                                    if flag_3:
                                        all_circles[i][2] = 3
                                    elif flag_1:
                                        all_circles[i][2] = 1
                                    elif flag_4:
                                        all_circles[i][2] = 4
                                    else:
                                        flag_ok = True

                                # земля только слева
                                elif board1[all_circles[i][1]][all_circles[i][0] - 1] == 1 and\
                                        board1[all_circles[i][1] + 1][all_circles[i][0]] == 0:
                                    # print("2 земля только слева")
                                    if flag_4:
                                        all_circles[i][2] = 4
                                    elif flag_1:
                                        all_circles[i][2] = 1
                                    elif flag_3:
                                        all_circles[i][2] = 3
                                    else:
                                        flag_ok = True

                                # земля только снизу
                                elif board1[all_circles[i][1] + 1][all_circles[i][0]] == 1 and \
                                        board1[all_circles[i][1]][all_circles[i][0] - 1] == 0:
                                    # print("2 земля только снизу")
                                    if flag_1:
                                        all_circles[i][2] = 1
                                    elif flag_3:
                                        all_circles[i][2] = 3
                                    elif flag_4:
                                        all_circles[i][2] = 4
                                    else:
                                        flag_ok = True
                                else:
                                    # print("2 иное")
                                    if flag_1:
                                        all_circles[i][2] = 1
                                    elif flag_3:
                                        all_circles[i][2] = 3
                                    elif flag_4:
                                        all_circles[i][2] = 4
                                    else:
                                        flag_ok = True
                                # print("2 ok")
                        # вправо вверх
                        elif all_circles[i][2] == 3:

                            # можно подвинуться
                            if board1[all_circles[i][1] - 1][all_circles[i][0] + 1] != 1 and \
                                    board1[all_circles[i][1] - 1][all_circles[i][0]] != 1 and \
                                    board1[all_circles[i][1]][all_circles[i][0] + 1] != 1 :
                                # врезались в героя
                                if board1[all_circles[i][1] - 1][all_circles[i][0] + 1] == 2 or \
                                        board1[all_circles[i][1] - 1][all_circles[i][0]] == 2 or \
                                        board1[all_circles[i][1]][all_circles[i][0] + 1] == 2:
                                    clear_my_path()
                                all_circles[i][0] += 1
                                all_circles[i][1] -= 1
                                flag_ok = True
                            else:
                                # print("меняем направление")
                                flag_3 = False
                                # зашли в угол  или наткнулись на угол
                                if board1[all_circles[i][1] - 1][all_circles[i][0] + 1] == 1 and \
                                        board1[all_circles[i][1] - 1][all_circles[i][0]] == 1 and \
                                        board1[all_circles[i][1]][all_circles[i][0] + 1] == 1 or \
                                        board1[all_circles[i][1] - 1][all_circles[i][0] + 1] == 1 and \
                                        board1[all_circles[i][1] - 1][all_circles[i][0]] == 0 and \
                                        board1[all_circles[i][1]][all_circles[i][0] + 1] == 0:
                                    # print("3 угол")
                                    if flag_2:
                                        all_circles[i][2] = 2
                                    elif flag_1:
                                        all_circles[i][2] = 1
                                    elif flag_4:
                                        all_circles[i][2] = 4
                                    else:
                                        flag_ok = True

                                # земля только справа
                                elif board1[all_circles[i][1] - 1][all_circles[i][0]] == 0 and \
                                        board1[all_circles[i][1]][all_circles[i][0] + 1] == 1:
                                    # print("3 земля только справа")
                                    if flag_1:
                                        all_circles[i][2] = 1
                                    elif flag_2:
                                        all_circles[i][2] = 2
                                    elif flag_4:
                                        all_circles[i][2] = 4
                                    else:
                                        flag_ok = True

                                # земля только сверху
                                elif board1[all_circles[i][1] - 1][all_circles[i][0]] == 1 and \
                                        board1[all_circles[i][1]][all_circles[i][0] + 1] == 0:
                                    # print("3 земля только сверху")
                                    if flag_4:
                                        all_circles[i][2] = 4
                                    elif flag_1:
                                        all_circles[i][2] = 1
                                    elif flag_2:
                                        all_circles[i][2] = 2
                                    else:
                                        flag_ok = True
                                else:
                                    # print("3 иное")
                                    if flag_4:
                                        all_circles[i][2] = 4
                                    elif flag_1:
                                        all_circles[i][2] = 1
                                    elif flag_2:
                                        all_circles[i][2] = 2
                                    else:
                                        flag_ok = True
                        # вправр вниз
                        elif all_circles[i][2] == 4:

                            # можно подвинуться
                            if board1[all_circles[i][1] + 1][all_circles[i][0] + 1] != 1 and \
                                    board1[all_circles[i][1] + 1][all_circles[i][0]] != 1 and \
                                    board1[all_circles[i][1]][all_circles[i][0] + 1] != 1:
                                # print(" 4 можно подвинуться")
                                # врезались в героя
                                if board1[all_circles[i][1] + 1][all_circles[i][0] + 1] == 2 or \
                                        board1[all_circles[i][1] + 1][all_circles[i][0]] == 2 or \
                                        board1[all_circles[i][1]][all_circles[i][0] + 1] == 2:
                                    clear_my_path()
                                all_circles[i][0] += 1
                                all_circles[i][1] += 1
                                flag_ok = True
                            else:
                                # print("меняем направление")
                                flag_4 = False
                                # зашли в угол или наткнулись на угол
                                if board1[all_circles[i][1] + 1][all_circles[i][0] + 1] == 1 and \
                                        board1[all_circles[i][1] + 1][all_circles[i][0]] == 1 and \
                                        board1[all_circles[i][1]][all_circles[i][0] + 1] == 1 or \
                                        board1[all_circles[i][1] + 1][all_circles[i][0] + 1] == 1 and\
                                        board1[all_circles[i][1] + 1][all_circles[i][0]] == 0 and \
                                        board1[all_circles[i][1]][all_circles[i][0] + 1] == 0:
                                    # print("4 угол")
                                    if flag_1:
                                        all_circles[i][2] = 1
                                    elif flag_2:
                                        all_circles[i][2] = 2
                                    elif flag_3:
                                        all_circles[i][2] = 3
                                    else:
                                        flag_ok = True

                                # земля только справа
                                elif board1[all_circles[i][1]][all_circles[i][0] + 1] == 1 and \
                                        board1[all_circles[i][1] + 1][all_circles[i][0]] == 0:
                                    # print("4 земля только справа")
                                    if flag_2:
                                        all_circles[i][2] = 2
                                    elif flag_1:
                                        all_circles[i][2] = 1
                                    elif flag_3:
                                        all_circles[i][2] = 3
                                    else:
                                        flag_ok = True

                                # земля только снизу
                                elif board1[all_circles[i][1] + 1][all_circles[i][0]] == 1 and \
                                        board1[all_circles[i][1]][all_circles[i][0] + 1] == 0:
                                    # print("4 земля только снизу")
                                    if flag_3:
                                        all_circles[i][2] = 3
                                    elif flag_1:
                                        all_circles[i][2] = 1
                                    elif flag_2:
                                        all_circles[i][2] = 2
                                    else:
                                        flag_ok = True
                                else:
                                    # print("4 иное")
                                    if flag_3:
                                        all_circles[i][2] = 3
                                    elif flag_1:
                                        all_circles[i][2] = 1
                                    elif flag_2:
                                        all_circles[i][2] = 2
                                    else:
                                        flag_ok = True

                                # print("4 ok")

            except Exception as e:
                print("!!!!", e)
                print(all_circles, n_cols, n_rows)
                # for xxxx in board1:
                # print(xxxx)
                running = False

    pygame.display.flip()
