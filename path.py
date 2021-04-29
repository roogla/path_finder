from random import randint
from grid import *
from utility import *
import pygame
import os

n, m = (100, 100)
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{n},  {m}"


def draw_grid():
    for _ in rect_list:
        pygame.draw.rect(_['screen'], _['color'], _['grid'], _['fill'])


def return_index(recs_list, check):
    a, b = check
    for rec in recs_list:
        if rec.get('coord') == [a, b]:
            return recs_list.index(rec)


def rect_detection(point_pos, color=None, fill=None):
    a, b = point_pos[0] // 20, point_pos[1] // 20
    if color is None:
        color = colors['red']

    for g in rect_list:
        if g.get('coord') == [a, b]:
            g.update(color=color)
            if fill is None:
                g.update(fill=0)
            else:
                g.update(fill=1)


# sets all rect objects back to default screen, color, and fill
def rect_scrub(new_list):
    for rect_obj in new_list:
        rect_obj.update(screen=screen, color=colors['black'], fill=1)
    return new_list


# sets random rects to be walls based on the size of the grid
def rect_scramble(scram_list):
    rand = randint(len(scram_list) // 6, len(scram_list) // 4)
    for x in range(rand):
        a, b = (randint(0, 29), randint(0, 29))
        for _ in scram_list:
            if _.get('coord') == [a, b]:
                _.update(fill=0, wall=1)


# set global declarations and init variables
pygame.init()
colors = {
    'white': [255, 255, 255],
    'black': [0, 0, 0],
    'red': [255, 0, 0],
    'red2': [235, 64, 52],
    'green': [134, 168, 109]
}
start_grid = GridMatrix(600, 600)
pygame.display.set_caption("A* path finder")
screen = pygame.display.set_mode([start_grid.width, start_grid.height])
rect_list = rect_scrub(start_grid.create_rects())

if __name__ == '__main__':
    rect_scramble(rect_list)
    clock = pygame.time.Clock()
    running = True
    switch = [False for _ in range(3)]
    point_holder = []

    while running:
        pointer_pos = pygame.mouse.get_pos()
        screen.fill(colors['white'])
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                rect_detection(pointer_pos, colors['red'])
                point_holder.append([int(pointer_pos[0] // 20), int(pointer_pos[1] // 20)])

                if not switch[0]:
                    switch[0] = True
                elif switch[0]:
                    switch[1] = True

        if switch[0] and switch[1]:
            if point_holder[0] == point_holder[1]:
                pygame.display.update()
                rect_scrub(rect_list)
                rect_scramble(rect_list)
                point_holder = []
                switch = [False for _ in range(3)]
            else:
                for points in point_holder:
                    rect_detection((points[0] * 20, points[1] * 20), colors['green'])

                point_holder.append(point_holder[0])
                rect_detection((point_holder[0][0] * 20, point_holder[0][1] * 20), colors['black'], 1)
                point_holder[0] = find_nine(point_holder[0], rect_list, point_holder)
                rect_detection((point_holder[0][0] * 20, point_holder[0][1] * 20), colors['red'])
                rect_detection((point_holder[1][0] * 20, point_holder[1][1] * 20), colors['red'])
                pygame.display.set_caption(f"{point_holder[0]}")

        pygame.display.update()
        clock.tick(30)
pygame.quit()
