from math import sqrt
# from path_pygame import scrub
# from path_pygame import scramble
import time


def log_(log):
    f = open("position_log.txt", "a")
    f.write(log)
    f.close()


class GridMatrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rects = []
        self.current = {}
        self.goal = {}

    def create_rects(self):
        dim_x = self.width // 20
        dim_y = self.height // 20
        for n in range(0, dim_x):
            for m in range(0, dim_y):
                self.rects.append({
                    'coord': [n, m],
                    'grid': [0 + (n * 20), 0 + (m * 20), 20, 20],
                    'screen': None,
                    'color': None,
                    'fill': 1,
                    'wall': 0,
                    'cost': 0
                })
        return self.rects


def find_nine(current_pos, rectal_dict, position_list):
    current_list = []
    goal = {}
    scores = []

    for box in rectal_dict:
        if box['coord'] == position_list[1]:
            goal = box

    def wall_check(wall_num):
        if wall_num['wall'] != 1:
            wall_num['cost'] = -1
            return wall_num
        else:
            wall_num['cost'] = 1000
            return wall_num

    def get_current_recs(recs_list, pos, dest_list):
        a, b = (pos[0] - 1, pos[1] - 1)

        for i in range(0, 3):
            for j in range(0, 3):
                for box in recs_list:
                    if box['coord'] == [a + j, b + i]:
                        dest_list.append(box)

    def score(recs_obj1, recs_obj2):
        y, z = (recs_obj1['grid'][0], recs_obj1['grid'][1])
        n, m = (recs_obj2['grid'][0], recs_obj2['grid'][1])

        if sqrt((n - y) ** 2 + (m - z) ** 2) <= 20:
            recs_obj1['cost'] = -1

        return [[recs_obj1['grid'][0] // 20, recs_obj1['grid'][1] // 20],
                recs_obj1['cost'] + (sqrt((n - y) ** 2 + (m - z) ** 2)/100)
                ]

    get_current_recs(rectal_dict, current_pos, current_list)

    checks = {"box_one": current_list[1],
              "box_three": current_list[3],
              "box_five": current_list[5],
              "box_seven": current_list[-2]
              }

    for recs in current_list:
        if recs:
            wall_check(recs)

    for _ in checks:
        for coords in position_list:
            if checks[_]['coord'] == coords:
                for obj in rectal_dict:
                    if obj['coord'] == checks[_]['coord']:
                        obj['cost'] += 0.1

        scores.append(score(checks[_], goal))

    winner = scores[0]
    time.sleep(0.08)
    for num in scores:
        if num[1] <= winner[1]:
            winner = num

    log_(f"---- step ----\n"
         f'Scores: {"".join([str(i) for i in scores])}\n'
         f"Current: {position_list[0]}\n"
         f"Goal: {position_list[1]}\n"
         f"Win: {winner[0]}\n"
         f"Win Score: {winner[1]}\n")
    return winner[0]
