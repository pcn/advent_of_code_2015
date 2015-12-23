from collections import namedtuple
from functools import partial

Point = namedtuple('Point', ['x', 'y'])

master_grid = [ [off for x in range(1000)] for y in range(1000)]

on  = 1
off = 0


def str_to_pt(pt):
    x, y = pt.split(',')
    return Point(int(x), int(y))


def read_line(s, grid):
    line = s.split(" ")
    if s.startswith("turn on"):
        start = str_to_pt(line[2])
        end   = str_to_pt(line[4])
        turn_on_area(start, end, grid)
    elif s.startswith("turn off"):
        start = str_to_pt(line[2])
        end   = str_to_pt(line[4])
        turn_off_area(start, end, grid)
    elif s.startswith("toggle"):
        start = str_to_pt(line[1])
        end   = str_to_pt(line[3])
        toggle_area(start, end, grid)
    else:
        raise ValueError, "Can't figure out the {}".format(s)


def turn_on_area(start, end, grid):
    """start and end are pairs of coordinates that define an area"""
    for pt in yield_area(start, end, grid):
        grid[pt.x][pt.y] = on


def turn_off_area(start, end, grid):
    """start and end are pairs of coordinates that define an area"""
    for pt in yield_area(start, end, grid):
        grid[pt.x][pt.y] = off


def toggle_area(start, end, grid):
    """start and end are pairs of coordinates that define an area"""
    for pt in yield_area(start, end, grid):
        if grid[pt.x][pt.y] == off:
            grid[pt.x][pt.y] = on
        else:
            grid[pt.x][pt.y] = off

def yield_area(start, end, grid):
    """Start and end are points"""
    for row in range(start.x, end.x+1):
        for col in range(start.y, end.y+1):
            yield Point(row, col)

def yield_input():
    with open("/Users/peter.norton/advent/2015/advent_day6", "r") as in_:
        for line in in_:
            yield line.rstrip()

for line in yield_input():
    read_line(line, master_grid)

sum([sum(row) for row in master_grid])
