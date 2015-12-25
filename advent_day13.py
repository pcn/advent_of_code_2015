from itertools import permutations
from collections import defaultdict

class Guest(object):
    def __init__(self, name):
        self.name = name
        self.feelings = defaultdict(int)


def test_data():
    return ["Alice would gain 54 happiness units by sitting next to Bob.",
            "Alice would lose 79 happiness units by sitting next to Carol.",
            "Alice would lose 2 happiness units by sitting next to David.",
            "Bob would gain 83 happiness units by sitting next to Alice.",
            "Bob would lose 7 happiness units by sitting next to Carol.",
            "Bob would lose 63 happiness units by sitting next to David.",
            "Carol would lose 62 happiness units by sitting next to Alice.",
            "Carol would gain 60 happiness units by sitting next to Bob.",
            "Carol would gain 55 happiness units by sitting next to David.",
            "David would gain 46 happiness units by sitting next to Alice.",
            "David would lose 7 happiness units by sitting next to Bob.",
            "David would gain 41 happiness units by sitting next to Carol.",]

def yield_data():
    data = open("advent_day13")
    for line in data:
        yield line


def parse_data(data):
    ppl = dict()
    for line in data:
        (name, _, op, count, _, _, _, _, _, _, other_name) = line.split()
        other_name = other_name[:-1] # Remove the trailing "."
        if name not in ppl.keys():
            ppl[name] = Guest(name)
        if op == 'gain':
            ppl[name].feelings[other_name] = int(count)
        else:
            ppl[name].feelings[other_name] = (- int(count))
    return ppl

def compute_happiness(people, arrangement):
    total_happiness = 0
    def get_neighbors(name):
        left = arrangement.index(name) - 1
        if arrangement.index(name) == (len(arrangement) - 1):
            right = 0
        else:
            right = arrangement.index(name) + 1
        return (arrangement[left], arrangement[right],)

    for name in arrangement:
        (left, right) = get_neighbors(name)
        total_happiness += people[name].feelings[left]
        total_happiness += people[name].feelings[right]
    return (total_happiness, arrangement)

def part1():
    data = parse_data(yield_data())
    return max([ compute_happiness(data, arrangement)
                 for arrangement in permutations(data.keys())])



def part2():
    data = parse_data(yield_data())
    data["me"] = Guest("me")
    return max([ compute_happiness(data, arrangement)
                 for arrangement in permutations(data.keys())])
