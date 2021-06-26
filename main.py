#  -*- coding:utf-8 -*-
import math
import random
import os
import time
import pygame

# mouse click event
def mouseClik(pos, pixel_size, colorflag):
    x, y = pos
    x = x - x % pixel_size
    y = y - y % pixel_size
    idx_x = int(x / pixel_size)
    idx_y = int(y / pixel_size)
    # if cell_nowstate[idx_x][idx_y] == 0:
    if colorflag:
        pygame.draw.rect(screen, WHITE, [x, y, pixel_size, pixel_size])
        cell_nowstate[idx_x][idx_y] = 1
    else:
        pygame.draw.rect(screen, BLACK, [x, y, pixel_size, pixel_size])
        cell_nowstate[idx_x][idx_y] = 0
    pygame.display.update()

def initScreen(sizex, sizey, pixel_size):
    screen.fill(GREY)

    # menu
    pygame.draw.line(screen, WHITE, [0, sizey], [sizex,sizey], 1)

    # play icon
    pygame.draw.rect(screen, WHITE, [10, sizey + 10, 50, 50])
    pygame.draw.polygon(screen, BLACK, [[20, sizey + 20], [20, sizey + 50], [50, sizey + 35]])

    # recover icon
    pygame.draw.rect(screen, WHITE, [70, sizey + 10, 50, 50])
    pygame.draw.circle(screen, BLACK, [95, sizey + 35], 20)
    pygame.draw.circle(screen, WHITE, [95, sizey + 35], 15)
    pygame.draw.rect(screen, WHITE, [90, sizey + 10, 15, 20])
    pygame.draw.polygon(screen, BLACK, [[94, sizey + 21], [105, sizey + 15], [105, sizey + 30]])

    # screenshot icon
    pygame.draw.rect(screen, WHITE, [130, sizey + 10, 50, 50])
    pygame.draw.circle(screen, BLACK, [155, sizey + 35], 15)

    # import icon
    pygame.draw.rect(screen, WHITE, [190, sizey + 10, 50, 50])
    pygame.draw.polygon(screen, BLACK, [[215, sizey + 20], [200, sizey + 35], [230, sizey + 35]])
    pygame.draw.line(screen, BLACK, [195, sizey + 15], [235, sizey + 15], 3)
    pygame.draw.line(screen, BLACK, [215, sizey + 35], [215, sizey + 55], 10)

    pygame.display.flip()


def CellNeighbourState(x, y, scale_x, scale_y):
    neighbour_state = 0
    for i in range(3):
        for j in range(3):
            ii = i
            jj = j
            if x + ii > scale_x or x + ii < 1 or y + jj > scale_y or y + jj < 1:
                continue
            # edge continuous
            # if (x == scale_x - 1 and i == 2):
            #     ii = -scale_x + 2
            # if (y == scale_y - 1 and j == 2):
            #     jj = -scale_y + 2
            neighbour_state += cell_nowstate[x + ii - 1][y + jj - 1]
    neighbour_state -= cell_nowstate[x][y]
    return neighbour_state

def UpdateWorld(scale_x, scale_y, pixel_size):
    for i in range(scale_x):
        for j in range(scale_y):
            neighbour_state = CellNeighbourState(i, j, scale_x, scale_y)
            if neighbour_state == 3:
                cell_nextstate[i][j] = 1
            elif neighbour_state == 2:
                cell_nextstate[i][j] = cell_nowstate[i][j]
            else:
                cell_nextstate[i][j] = 0

    for i in range(scale_x):
        for j in range(scale_y):
            cell_nowstate[i][j] = cell_nextstate[i][j]
            if cell_nowstate[i][j] == 1:
                pygame.draw.rect(screen, WHITE, [i * pixel_size, j * pixel_size, pixel_size, pixel_size])
            if cell_nowstate[i][j] == 0:
                pygame.draw.rect(screen, BLACK, [i * pixel_size, j * pixel_size, pixel_size, pixel_size])
    pygame.display.update()

def SwitchPauseAndPlay(play_flag):
    if play_flag == 0:
        play_flag = 1
        # pause icon
        pygame.draw.rect(screen, WHITE, [10, sizey + 10, 50, 50])
        pygame.draw.rect(screen, BLACK, [20, sizey + 20, 10, 30])
        pygame.draw.rect(screen, BLACK, [40, sizey + 20, 10, 30])

    elif play_flag == 1:
        play_flag = 0
        # play icon
        pygame.draw.rect(screen, WHITE, [10, sizey + 10, 50, 50])
        pygame.draw.polygon(screen, BLACK, [[20, sizey + 20], [20, sizey + 50], [50, sizey + 35]])

    pygame.display.update()
    return play_flag

def SwitchRecover():
    for i in range(len(cell_nowstate)):
        for j in range(len(cell_nowstate[i])):
            cell_nowstate[i][j] = 0
            cell_nextstate[i][j] = 0
    pygame.draw.rect(screen, BLACK, [0, 0, sizex, sizey])
    pygame.display.update()

def SwitchScreenShot():
    text = pygame.font.SysFont("C:/Windows/Fonts/simhei.ttf", 20)
    text_fmt = text.render("screenshot saved!", False, (255, 255, 255))
    screen.blit(text_fmt, (10, sizey + 60))
    pygame.display.update()
    print("screenshot saved!")

    rect = pygame.Rect(0, 0, sizex, sizey)
    sub = screen.subsurface(rect)
    pygame.image.save(sub, "screenshot.jpg")

def SwitchImport(scale_x, scale_y):
    print("import data!")
    row = 0
    with open('out.txt') as f:
        for line in f:
            for col in range(int(len(line) / 2)):
                if (line[col * 2 ] == "1"):
                    cell_nowstate[col][row] = 1
                else:
                    cell_nowstate[col][row] = 0
            row += 1

    for i in range(scale_x):
        for j in range(scale_y):
            if cell_nowstate[i][j] == 1:
                pygame.draw.rect(screen, WHITE, [i * pixel_size, j * pixel_size, pixel_size, pixel_size])
            if cell_nowstate[i][j] == 0:
                pygame.draw.rect(screen, BLACK, [i * pixel_size, j * pixel_size, pixel_size, pixel_size])
    pygame.display.update()

def ScreenRecord():
    text = pygame.font.SysFont("C:/Windows/Fonts/simhei.ttf", 20)
    text_fmt = text.render("screenshots saved!", False, (255, 255, 255))
    screen.blit(text_fmt, (10, sizey + 60))
    pygame.display.update()
    print("screenshot saved!")

    rect = pygame.Rect(0, 0, sizex, sizey)
    sub = screen.subsurface(rect)
    print(path_screenshots + "ss_" + str(ss_cnt) + "_" +
          time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".jpg")
    cv2.imwrite(path_screenshots + "ss_" + str(ss_cnt) + "_" +
                time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".jpg", im_rd)
    pygame.image.save(sub, "screenshot.jpg")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (20, 20, 20)

size = [800, 600]
sizex = size[0]
sizey = size[1]
menu_height = 80
pixel_size = 10

play_flag = 0
mouse_click_flag = 0
temp_x0 = -pixel_size
temp_y0 = -pixel_size

pygame.init()
pygame.font.init()
pygame.display.set_caption("test")
screen = pygame.display.set_mode([sizex, sizey + menu_height])

cell_nowstate = [[0] * int(sizey / pixel_size) for i in range(int(sizex / pixel_size))]
cell_nextstate = [[0] * int(sizey / pixel_size) for i in range(int(sizex / pixel_size))]
print(int(sizex / pixel_size), int(sizey / pixel_size))

done = False
clock = pygame.time.Clock()
initScreenflag = True
mouse_cell_add = 0

mRunning = True
while mRunning:
    mouse_pressed = pygame.mouse.get_pressed(3)
    if mouse_pressed[0]:
        if pygame.mouse.get_pos()[1] < sizey:
            temp_x, temp_y = pygame.mouse.get_pos()
            if temp_x0 < temp_x < (temp_x0 + pixel_size) and temp_y0 < temp_y < (temp_y0 + pixel_size) and mouse_cell_add == 1:
                pass
            else:
                mouse_cell_add = 1
                temp_x0 = temp_x - temp_x % pixel_size
                temp_y0 = temp_y - temp_y % pixel_size
                mouseClik(pygame.mouse.get_pos(), pixel_size, 1)
    elif mouse_pressed[2]:
        if pygame.mouse.get_pos()[1] < sizey:
            temp_x, temp_y = pygame.mouse.get_pos()
            if temp_x0 < temp_x < (temp_x0 + pixel_size) and temp_y0 < temp_y < (temp_y0 + pixel_size) and mouse_cell_add == 0:
                pass
            else:
                mouse_cell_add = 0
                temp_x0 = temp_x - temp_x % pixel_size
                temp_y0 = temp_y - temp_y % pixel_size
                mouseClik(pygame.mouse.get_pos(), pixel_size, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # mouse click event
            # pause and play
            if (sizey + 50) > pygame.mouse.get_pos()[1] > (sizey + 10) and 60 > pygame.mouse.get_pos()[0] > 10:
                play_flag = SwitchPauseAndPlay(play_flag)

            # recover
            if (sizey + 50) > pygame.mouse.get_pos()[1] > (sizey + 10) and 120 > pygame.mouse.get_pos()[0] > 70:
                SwitchRecover()

            # screenshot
            if (sizey + 50) > pygame.mouse.get_pos()[1] > (sizey + 10) and 180 > pygame.mouse.get_pos()[0] > 130:
                SwitchScreenShot()

            # import data
            if (sizey + 50) > pygame.mouse.get_pos()[1] > (sizey + 10) and 240 > pygame.mouse.get_pos()[0] > 190:
                SwitchImport(int(sizex / pixel_size), int(sizey / pixel_size))



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                UpdateWorld(int(sizex / pixel_size), int(sizey / pixel_size), pixel_size)
    if play_flag:
        UpdateWorld(int(sizex / pixel_size), int(sizey / pixel_size), pixel_size)
        time.sleep(0.2)

    if initScreenflag:
        initScreen(sizex, sizey, pixel_size)
    initScreenflag = False
pygame.quit()

