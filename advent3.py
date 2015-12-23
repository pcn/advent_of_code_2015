# curl -b session=<session cookie> -s http://adventofcode.com/day/3/input > /tmp/advent_day3
from collections import defaultdict
from functools import partial
from itertools import islice
directions = {
    "^" : lambda c: (c[0], c[1]+1,),
    "<" : lambda c: (c[0]-1, c[1],),
    ">" : lambda c: (c[0]+1, c[1],),
    "v" : lambda c: (c[0], c[1]-1,)
    }

def yield_input():
    with open("/tmp/advent_day3", "r") as in_:
        for line in in_:
            for ch in line:
                yield ch

def do_next(collection, cur_pos, next_move):
    new_pos = directions[next_move](cur_pos)
    collection[new_pos] += 1
    return new_pos

def part_1():
    coll = defaultdict(int)
    coll[(0,0,)] = 1
    p = partial(do_next, coll)
    reduce(p, yield_input(), (0,0))
    return len(coll)



def part_2():
    coll = defaultdict(int)
    coll[(0,0,)] = 1

    p = partial(do_next, coll)

    res1 = reduce(p, islice(yield_input(), 0, None, 2), (0,0))
    res2 = reduce(p, islice(yield_input(), 1, None, 2), (0,0))
    return len(coll)
