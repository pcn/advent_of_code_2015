#!/usr/bin/env python


def yield_input():
    with open("/Users/peter.norton/advent/2015/advent_day8", "r") as in_:
        for line in in_:
            yield line.rstrip()

def part1():
    literal_len = 0
    read_len = 0

    for line in yield_input():
        literal_len += len(line)
        read_len += len(eval(line))
    return literal_len - read_len


def fatten(st):
    new_st = "\\\\".join(st.split("\\"))
    newer_st = '\\"'.join(new_st.split('"'))
    return '"{}"'.format(newer_st)

def part2():
    literal_len = 0
    fat_len = 0

    for line in yield_input():
        literal_len += len(line)
        fat_len += len(fatten(line))
    return fat_len - literal_len
