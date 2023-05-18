import random

MAX_NUM = 1_000_000
L = 500
l = 460
COUNT = 5
NUM_AFTER_POINTS = 10**COUNT


def model(allLength, minLength):
    pointC = random.randint(0, allLength * NUM_AFTER_POINTS) / NUM_AFTER_POINTS
    return pointC >= minLength


def solve(allLength, minLength):
    return 1 - minLength / allLength


print(solve(L, l))
