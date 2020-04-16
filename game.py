#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import csv
import itertools
from functools import reduce
from typing import Tuple, Set, Iterator

from termcolor import colored

CellType = Tuple[int, int]
BoardType = Set[CellType]


def neighbor_dots(point: CellType) -> Iterator[CellType]:
    x, y = point
    for x_bias, y_bias in itertools.product(range(-1, 2), repeat=2):
        if any((x_bias, y_bias)):
            yield x + x_bias, y + y_bias


def advance(board: BoardType) -> BoardType:
    new_state = set()
    board_with_neighbors = board | set(itertools.chain(*map(neighbor_dots, board)))
    for point in board_with_neighbors:
        count = sum((neighbor in board) for neighbor in neighbor_dots(point))
        if count == 3 or (count == 2 and point in board):
            new_state.add(point)

    return new_state


def drawer(image: str, sleep_time: float = 0.3) -> None:
    os.system('clear')
    image = colored(f"{image}", "magenta", attrs=["bold"])
    os.system(f'echo "{image}"')
    os.system(f'sleep {sleep_time}')


def plotter(dots: BoardType, grid_size: int = 8, terminal_size: CellType = (80, 24)) -> None:
    image = ''
    for colomn in range(-grid_size, grid_size + 1):
        for row in range(grid_size, -(grid_size + 1), -1):
            image += '*' if (colomn, row) in dots else ' '
        image += '\n'

    image = image.split('\n')
    centre_x, centre_y = map(lambda x: int(x/2), terminal_size)
    bias_x = centre_x - len(image[0]) // 2
    centre = reduce(lambda image, line: image + (' ' * bias_x + line + '\n'), image, '')

    bias_y = centre_y - len(image) // 2
    drawer(''.join(['\n'*bias_y, centre, '\n'*(bias_y-2)]))


if __name__ == '__main__':
    data = set()
    with open('data/pulsar.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            x, y = map(lambda pos: int(pos), row.values())
            data.add((x, y))

    while data:
        data = advance(data)
        plotter(data)
