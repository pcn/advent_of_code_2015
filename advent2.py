#!/usr/bin/env python


# Get the data via:
# curl -b session=<session> -s http://adventofcode.com/day/2/input > /tmp/advent_day2

def yield_input():
    with open("/tmp/advent_day2", "r") as in_:
        for line in in_:
            yield [ int(i) for i in line.split('x') ]

def ribbon_length(sides):
    ss = sorted(sides)
    min_c = (ss[0] * 2) + (ss[1] * 2)
    bow = reduce(lambda x, y: x * y, sides)
    return min_c + bow

sum([ribbon_length(l) for l in yield_input()])
