import json
from functools import partial

def sum_values(ob):
    """json doesn't allow for numeric object keys"""
    if isinstance(ob, list):
        return sum([sum_values(o) for o in ob])
    elif isinstance(ob, dict):
        return sum([sum_values(o) for o in ob.values()])
    elif isinstance(ob, int):
        return ob
    else:
        return 0


def get_data():
    data = json.load(open("advent_day12"))
    return data

def get_data_filtered():
    def red_filter(jd):
        if "red" in jd.values():
            return {}
        return jd
    data = json.load(open("advent_day12"), object_hook=red_filter)
    return data


def part1():
    return sum_values(get_data())

def part2():
    return sum_values(get_data_filtered())
