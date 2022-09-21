import Consts
import random

trash_array = [[]]
max_trash_count = 2

def add_trash():
    for i in range(Consts.TURTLE_AMOUNT):
        if count_trash_in_row(i) < max_trash_count and i.index(Consts.TRASH) < 3:
            pass


def get_random_trash():
    return Consts.TRASHES_LIST[random.randint(0, 2)]

def count_trash_in_row(row):
    count = 0
    for i in row:
        if i == Consts.TRASH:
            count += 1
    return count


def get_trash():
    return trash_array


def increase_difficulty():
    global max_trash_count
    max_trash_count += 1