#!venv/bin/python3
# -*- coding: utf8 -*-

import os
import itertools
from typing import *

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


def drawer(image: str, sleep_time: float = 0.15) -> None:
    os.system('clear')
    image = colored(f"{image}", "magenta", attrs=["bold"])
    os.system(f'echo "{image}"')
    os.system(f'sleep {sleep_time}')


def plotter(dots: BoardType, grid_size: int = 10) -> None:
    image = ''
    for colomn in range(-grid_size, grid_size + 1):
        for row in range(grid_size, -(grid_size + 1), -1):
            image += '*' if (colomn, row) in dots else ' '
        image += '\n'
    drawer(image)


if __name__ == '__main__':
    data = {(0, 0), (-1, 1), (1, -1), (0, 0), (-1, -1), (1, 1), (0, 0), (0, 1), (0, -1), (-1, 0), (0, 0), (1, 0)}

    while data:
        data = advance(data)
        plotter(data)