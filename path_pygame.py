import pygame
from random import randint
from grid import *
from bolt_on import *

# first github capture - files downloaded and this comment is my first tracked comit
# it's nice to be coding again.

commit = True

def draw_grid():
    for y in rect_list:
        pygame.draw.rect(y['screen'], y['color'], y['grid'], y['fill'])


def change_list(x, y, color=None, fill=None):
    if color is None:
        color = colors['red']

    for g in rect_list:
        if g['coord'] == [x, y]:
            g['color'] = color
            if fill is None:
                g['fill'] = 0
            else:
                g['fill'] = 1


def square_detection(point_pos, color=None, fill=None):
    a, b = point_pos
    change_list(a // 20, b // 20, color, fill)


def scrub(new_list):
    for rect_obj in new_list:
        rect_obj['screen'] = screen
        rect_obj['color'] = colors['black']
        rect_obj['fill'] = 1
    return new_list


def scramble(scram_list):
    rando = randint(len(scram_list) // 6, len(scram_list) // 4)
    for x in range(rando):
        a = randint(0, 24)
        b = randint(0, 24)
        for y in scram_list:
            if y['coord'] == [a, b]:
                y['fill'] = 0
                y['wall'] = 1


# set global declarations and init variables
pygame.init()
colors = {
    'white': [255, 255, 255],
    'black': [0, 0, 0],
    'red': [255, 0, 0],
    'red2': [235, 64, 52],
    'green': [134, 168, 109]
}
start_grid = GridMatrix(500, 500)
pygame.display.set_caption("A* path finder")
screen = pygame.display.set_mode([start_grid.width, start_grid.height])
rect_list = scrub(start_grid.create_rects())

if __name__ == '__main__':
    scramble(rect_list)
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
                square_detection(pointer_pos, colors['red'])
                point_holder.append([pointer_pos[0] // 20, pointer_pos[1] // 20])
                if switch[0]:
                    switch[1] = True
                else:
                    switch[0] = True

        if switch[0] and switch[1]:
            if point_holder[0] == point_holder[1]:
                scrub(rect_list)
                scramble(rect_list)
                point_holder = []
                switch = [False for _ in range(3)]
            else:
                point_holder.append(point_holder[0])
                square_detection((point_holder[0][0] * 20, point_holder[0][1] * 20), colors['black'], 1)
                point_holder[0] = find_nine(point_holder[0], rect_list, point_holder)
                square_detection((point_holder[0][0] * 20, point_holder[0][1] * 20), colors['red'])

            for n in rect_list:
                for m in rect_list:
                    if n['color'] == colors['red'] and m['color'] == colors['red']:
                        pygame.draw.line(
                            screen, (0, 0, 0), in_line(n['coord']), in_line(m['coord']), 2
                        )

        pygame.display.update()
        clock.tick(30)
pygame.quit()
