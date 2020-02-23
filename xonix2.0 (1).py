import pygame
from random import randrange

CELL_TYPE_PATH = 2


class Hero:
    hero_cords_x = 0
    hero_cords_y = 0
    
    def __init__(self):
        self.rest_lives = 3
        self.text_lives = 'жизней: ' + str(self.rest_lives)
        self.new_path = False
        self.my_path = []


class Board:
    def __init__(self, n_cols, n_rows):
        self.width = n_cols
        self.height = n_rows
        self.board = board1
        self.cell_size = cell_size
        self.flag = 0      
        self.lvl = 1
        self.text_lvl = str(self.lvl) + ' lvl'
        self.font = pygame.font.Font(None, 20)
        self.text = self.font.render(self.text_lvl, True, pygame.Color("red"))

    def render(self):
        for x in range(self.width):
            for y in range(self.height):
                if board1[y][x] == 1:
                    pygame.draw.rect(screen, pygame.Color('Green'), (x * self.cell_size, y * self.cell_size,
                                                                     self.cell_size, self.cell_size))
                if board1[y][x] == 2:
                    pygame.draw.rect(screen, pygame.Color('Red'), (x * self.cell_size, y * self.cell_size,
                                                                   self.cell_size, self.cell_size))

        pygame.draw.rect(screen, pygame.Color('Blue'), (Hero.hero_cords_x * self.cell_size, Hero.hero_cords_y * self.cell_size,
                                                        self.cell_size, self.cell_size))


class Circle:
    def __init__(self):
        self.circles = 1
        self.all_circles = []

    def move_circle(self):
        pygame.draw.circle(screen, pygame.Color('white'), (self.all_circles[i][0] * cell_size,
                                                           self.all_circles[i][1] * cell_size), radius)
        # cords_x, cords_y = self.all_circles[i][0], self.all_circles[i][1]

        flag_ok = False
        flag_1 = True
        flag_2 = True
        flag_3 = True
        flag_4 = True

        # Пока коорд не изменятся, цикл продолжит выполняться
        while not flag_ok:

            # влево вверх
            if self.all_circles[i][2] == 1:

                # можно подвинуться
                if board1[self.all_circles[i][1] - 1][self.all_circles[i][0] - 1] != 1 and \
                        board1[self.all_circles[i][1] - 1][self.all_circles[i][0]] != 1 and \
                        board1[self.all_circles[i][1]][self.all_circles[i][0] - 1] != 1:
                    # врезались в путь героя
                    if board1[self.all_circles[i][1] - 1][self.all_circles[i][0] - 1] == 2 or \
                            board1[self.all_circles[i][1] - 1][self.all_circles[i][0]] == 2 or \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] - 1] == 2:
                        sound1.play()
                        running = clear_my_path()
                    self.all_circles[i][0] -= 1
                    self.all_circles[i][1] -= 1
                    flag_ok = True
                else:
                    # меняем направление
                    flag_1 = False
                    # зашли в угол или наткнулись на угол
                    if board1[self.all_circles[i][1] - 1][self.all_circles[i][0] - 1] == 1 and \
                            board1[self.all_circles[i][1] - 1][self.all_circles[i][0]] == 1 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] - 1] == 1 or \
                            board1[self.all_circles[i][1] - 1][self.all_circles[i][0] - 1] == 1 and \
                            board1[self.all_circles[i][1] - 1][self.all_circles[i][0]] == 0 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] - 1] == 0:
                        if flag_4:
                            self.all_circles[i][2] = 4
                        elif flag_2:
                            self.all_circles[i][2] = 2
                        elif flag_3:
                            self.all_circles[i][2] = 3
                        else:
                            flag_ok = True

                    # земля только слева
                    elif board1[self.all_circles[i][1]][self.all_circles[i][0] - 1] == 1 and \
                            board1[self.all_circles[i][1] - 1][self.all_circles[i][0]] == 0:
                        if flag_3:
                            self.all_circles[i][2] = 3
                        elif flag_2:
                            self.all_circles[i][2] = 2
                        elif flag_4:
                            self.all_circles[i][2] = 4
                        else:
                            flag_ok = True

                    # земля только сверху
                    elif board1[self.all_circles[i][1] - 1][self.all_circles[i][0]] == 1 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] - 1] == 0:
                        if flag_2:
                            self.all_circles[i][2] = 2
                        elif flag_3:
                            self.all_circles[i][2] = 3
                        elif flag_4:
                            self.all_circles[i][2] = 4
                        else:
                            flag_ok = True
                    else:
                        if flag_2:
                            self.all_circles[i][2] = 2
                        elif flag_3:
                            self.all_circles[i][2] = 3
                        elif flag_4:
                            self.all_circles[i][2] = 4
                        else:
                            flag_ok = True

            # влево вниз
            elif self.all_circles[i][2] == 2:

                # можно подвинуться
                if board1[self.all_circles[i][1] + 1][self.all_circles[i][0] - 1] != 1 and \
                        board1[self.all_circles[i][1] + 1][self.all_circles[i][0]] != 1 and \
                        board1[self.all_circles[i][1]][self.all_circles[i][0] - 1] != 1:
                    # врезались в героя
                    if board1[self.all_circles[i][1] + 1][self.all_circles[i][0] - 1] == 2 or \
                            board1[self.all_circles[i][1] + 1][self.all_circles[i][0]] == 2 or \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] - 1] == 2:
                        sound1.play()
                        running = clear_my_path()
                    self.all_circles[i][0] -= 1
                    self.all_circles[i][1] += 1
                    flag_ok = True
                else:
                    # меняем направлние
                    flag_2 = False
                    # зашли в угол  или наткнулись на угол
                    if board1[self.all_circles[i][1] + 1][self.all_circles[i][0] - 1] == 1 and \
                            board1[self.all_circles[i][1] + 1][self.all_circles[i][0]] == 1 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] - 1] == 1 or \
                            board1[self.all_circles[i][1] + 1][self.all_circles[i][0] - 1] == 1 and \
                            board1[self.all_circles[i][1] + 1][self.all_circles[i][0]] == 0 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] - 1] == 0:
                        if flag_3:
                            self.all_circles[i][2] = 3
                        elif flag_1:
                            self.all_circles[i][2] = 1
                        elif flag_4:
                            self.all_circles[i][2] = 4
                        else:
                            flag_ok = True

                    # земля только слева
                    elif board1[self.all_circles[i][1]][self.all_circles[i][0] - 1] == 1 and \
                            board1[self.all_circles[i][1] + 1][self.all_circles[i][0]] == 0:
                        if flag_4:
                            self.all_circles[i][2] = 4
                        elif flag_1:
                            self.all_circles[i][2] = 1
                        elif flag_3:
                            self.all_circles[i][2] = 3
                        else:
                            flag_ok = True

                    # земля только снизу
                    elif board1[self.all_circles[i][1] + 1][self.all_circles[i][0]] == 1 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] - 1] == 0:
                        if flag_1:
                            self.all_circles[i][2] = 1
                        elif flag_3:
                            self.all_circles[i][2] = 3
                        elif flag_4:
                            self.all_circles[i][2] = 4
                        else:
                            flag_ok = True
                    else:
                        if flag_1:
                            self.all_circles[i][2] = 1
                        elif flag_3:
                            self.all_circles[i][2] = 3
                        elif flag_4:
                            self.all_circles[i][2] = 4
                        else:
                            flag_ok = True
            # вправо вверх
            elif self.all_circles[i][2] == 3:

                # можно подвинуться
                if board1[self.all_circles[i][1] - 1][self.all_circles[i][0] + 1] != 1 and \
                        board1[self.all_circles[i][1] - 1][self.all_circles[i][0]] != 1 and \
                        board1[self.all_circles[i][1]][self.all_circles[i][0] + 1] != 1:
                    # врезались в героя
                    if board1[self.all_circles[i][1] - 1][self.all_circles[i][0] + 1] == 2 or \
                            board1[self.all_circles[i][1] - 1][self.all_circles[i][0]] == 2 or \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] + 1] == 2:
                        sound1.play()
                        running = clear_my_path()
                    self.all_circles[i][0] += 1
                    self.all_circles[i][1] -= 1
                    flag_ok = True
                else:
                    # меняем напрваление
                    flag_3 = False
                    # зашли в угол  или наткнулись на угол
                    if board1[self.all_circles[i][1] - 1][self.all_circles[i][0] + 1] == 1 and \
                            board1[self.all_circles[i][1] - 1][self.all_circles[i][0]] == 1 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] + 1] == 1 or \
                            board1[self.all_circles[i][1] - 1][self.all_circles[i][0] + 1] == 1 and \
                            board1[self.all_circles[i][1] - 1][self.all_circles[i][0]] == 0 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] + 1] == 0:
                        if flag_2:
                            self.all_circles[i][2] = 2
                        elif flag_1:
                            self.all_circles[i][2] = 1
                        elif flag_4:
                            self.all_circles[i][2] = 4
                        else:
                            flag_ok = True

                    # земля только справа
                    elif board1[self.all_circles[i][1] - 1][self.all_circles[i][0]] == 0 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] + 1] == 1:
                        if flag_1:
                            self.all_circles[i][2] = 1
                        elif flag_2:
                            self.all_circles[i][2] = 2
                        elif flag_4:
                            self.all_circles[i][2] = 4
                        else:
                            flag_ok = True

                    # земля только сверху
                    elif board1[self.all_circles[i][1] - 1][self.all_circles[i][0]] == 1 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] + 1] == 0:
                        if flag_4:
                            self.all_circles[i][2] = 4
                        elif flag_1:
                            self.all_circles[i][2] = 1
                        elif flag_2:
                            self.all_circles[i][2] = 2
                        else:
                            flag_ok = True
                    else:
                        if flag_4:
                            self.all_circles[i][2] = 4
                        elif flag_1:
                            self.all_circles[i][2] = 1
                        elif flag_2:
                            self.all_circles[i][2] = 2
                        else:
                            flag_ok = True
            # вправр вниз
            elif self.all_circles[i][2] == 4:

                # можно подвинуться
                if board1[self.all_circles[i][1] + 1][self.all_circles[i][0] + 1] != 1 and \
                        board1[self.all_circles[i][1] + 1][self.all_circles[i][0]] != 1 and \
                        board1[self.all_circles[i][1]][self.all_circles[i][0] + 1] != 1:
                    # врезались в героя
                    if board1[self.all_circles[i][1] + 1][self.all_circles[i][0] + 1] == 2 or \
                            board1[self.all_circles[i][1] + 1][self.all_circles[i][0]] == 2 or \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] + 1] == 2:
                        sound1.play()
                        running = clear_my_path()
                    self.all_circles[i][0] += 1
                    self.all_circles[i][1] += 1
                    flag_ok = True
                else:
                    # меняем направление
                    flag_4 = False
                    # зашли в угол или наткнулись на угол
                    if board1[self.all_circles[i][1] + 1][self.all_circles[i][0] + 1] == 1 and \
                            board1[self.all_circles[i][1] + 1][self.all_circles[i][0]] == 1 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] + 1] == 1 or \
                            board1[self.all_circles[i][1] + 1][self.all_circles[i][0] + 1] == 1 and \
                            board1[self.all_circles[i][1] + 1][self.all_circles[i][0]] == 0 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] + 1] == 0:
                        if flag_1:
                            self.all_circles[i][2] = 1
                        elif flag_2:
                            self.all_circles[i][2] = 2
                        elif flag_3:
                            self.all_circles[i][2] = 3
                        else:
                            flag_ok = True

                    # земля только справа
                    elif board1[self.all_circles[i][1]][self.all_circles[i][0] + 1] == 1 and \
                            board1[self.all_circles[i][1] + 1][self.all_circles[i][0]] == 0:
                        if flag_2:
                            self.all_circles[i][2] = 2
                        elif flag_1:
                            self.all_circles[i][2] = 1
                        elif flag_3:
                            self.all_circles[i][2] = 3
                        else:
                            flag_ok = True

                    # земля только снизу
                    elif board1[self.all_circles[i][1] + 1][self.all_circles[i][0]] == 1 and \
                            board1[self.all_circles[i][1]][self.all_circles[i][0] + 1] == 0:
                        if flag_3:
                            self.all_circles[i][2] = 3
                        elif flag_1:
                            self.all_circles[i][2] = 1
                        elif flag_2:
                            self.all_circles[i][2] = 2
                        else:
                            flag_ok = True
                    else:
                        if flag_3:
                            self.all_circles[i][2] = 3
                        elif flag_1:
                            self.all_circles[i][2] = 1
                        elif flag_2:
                            self.all_circles[i][2] = 2
                        else:
                            flag_ok = True
        

def clear_my_path():
    for smth in hero.my_path:
        board1[smth[0]][smth[1]] = 0
    Hero.hero_cords_x = 0
    Hero.hero_cords_y = 0
    board.flag = 0
    hero.new_path = False
    hero.my_path = []

    hero.rest_lives -= 1
    if hero.rest_lives <= 0:
        return False
    else:
        hero.text_lives = 'жизней: ' + str(hero.rest_lives)
        return True


def death():
    Hero.hero_cords_x = 0
    Hero.hero_cords_y = 0
    board.flag = 0
    board1 = [[0] * n_cols for _ in range(n_rows)]
    board1[0][0] = 1


def idk():
    for smth in hero.my_path:
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

    flag_in_class = False
    cells_0 = 0
    cells_4 = 0
    any_cells = 0

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
    for y in range(n_rows):
        for x in range(n_cols):
            if board1[y][x] == 1:
                any_cells += 1
    if any_cells / (n_cols * n_rows) >= 0.75:
        new_game()


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


def new_game():
    Hero.hero_cords_x = 0
    Hero.hero_cords_y = 0
    board.flag = 0

    for y in range(1, n_rows - 1):
        for x in range(1, n_cols - 1):
            board1[y][x] = 0

    cl_circle.circles += 1
    cl_circle.all_circles.append([randrange(2, n_cols - 1), randrange(2, n_rows - 1), randrange(1, 5)])

    board.lvl += 1
    board.text_lvl = str(board.lvl) + ' lvl'
    board.text = board.font.render(board.text_lvl, True, pygame.Color("red"))


def display_hearts(self):
    return self.text_lives


def change_direction(event):
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


def move_hero():
    # налево
    if board.flag == 1 and Hero.hero_cords_x >= 1 and board1[Hero.hero_cords_y][Hero.hero_cords_x - 1] != CELL_TYPE_PATH:
        Hero.hero_cords_x -= 1

    # направо
    elif board.flag == 2 and Hero.hero_cords_x < n_cols - 1 and board1[Hero.hero_cords_y][Hero.hero_cords_x + 1] != 2:
        Hero.hero_cords_x += 1

    # вверх
    elif board.flag == 3 and Hero.hero_cords_y >= 1 and board1[Hero.hero_cords_y - 1][Hero.hero_cords_x] != 2:
        Hero.hero_cords_y -= 1

    # вниз
    elif board.flag == 4 and Hero.hero_cords_y < n_rows - 1 and board1[Hero.hero_cords_y + 1][Hero.hero_cords_x] != 2:
        Hero.hero_cords_y += 1

    # встаем на воду
    if board1[Hero.hero_cords_y][Hero.hero_cords_x] == 0:
        if not hero.new_path:
            hero.new_path = True
            hero.my_path = []
        board1[Hero.hero_cords_y][Hero.hero_cords_x] = 2
        hero.my_path.append([Hero.hero_cords_y, Hero.hero_cords_x, board.flag])

    # встаем на землю
    elif board1[Hero.hero_cords_y][Hero.hero_cords_x] == 1:
        # если шли по воде
        if hero.new_path:
            idk()
            hero.new_path = False


pygame.init()

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

hero = Hero()

board = Board(n_cols, n_rows)
board.render()

cl_circle = Circle()

first_circle = True
radius = 6
for circle in range(cl_circle.circles):
    cl_circle.all_circles.append([randrange(2, n_cols-1), randrange(2, n_rows-1), randrange(1, 5)])
s = 3
pr = 25
pygame.time.set_timer(pr, 70)
pr1 = 26
pygame.time.set_timer(pr1, 220000)

# flag = 0
running = True

HEART_IMG = pygame.image.load("heart.png")
HEART_IMG = pygame.transform.scale(HEART_IMG.convert_alpha(), (30, 27))

fon_IMG = pygame.image.load("waste.png")
fon_IMG = pygame.transform.scale(fon_IMG.convert_alpha(), (480, 480))

sound1 = pygame.mixer.Sound('explos.wav')
pygame.mixer.music.load('Popcorn Original Song.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(2)

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # выбираем направление движения
            change_direction(event)

        if event.type == pr and hero.rest_lives > 0:

            screen.fill((0, 0, 0))
            board.render()
            # передвижение героя
            move_hero()

            for i in range(len(cl_circle.all_circles)):
                # передвижение шарика
                cl_circle.move_circle()
        if event.type == pr1:
            print("sound")
            pygame.mixer.music.play()
    screen.blit(board.text, (board.width * board.cell_size // 2 - 10, 0))
    if hero.rest_lives == 1:
        screen.blit(HEART_IMG, (10, 450))
    if hero.rest_lives == 2:
        screen.blit(HEART_IMG, (10, 450))
        screen.blit(HEART_IMG, (50, 450))
    if hero.rest_lives == 3:
        screen.blit(HEART_IMG, (10, 450))
        screen.blit(HEART_IMG, (50, 450))
        screen.blit(HEART_IMG, (90, 450))
    if hero.rest_lives == 0:
        screen.blit(fon_IMG, (0, 0))
    pygame.display.flip()

