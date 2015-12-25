# Model reindeer motion as a list of distance per second, with each second being one element in the array.
from itertools import cycle
from collections import namedtuple

Reindeer = namedtuple('Reindeer', ("name", "velocity", "runtime", "downtime"))

def read_data():
    reindeer = dict()
    for line in open('advent_day14', 'r').readlines():
        name, _, _, velocity, _, _, runtime, _, _, _, _, _, _, downtime, _ = line.split()
        reindeer[name] = Reindeer(name, int(velocity), int(runtime), int(downtime))
    return reindeer



def test_data():
    data = ["Comet can fly 14 km/s for 10 seconds, but then must rest for 127 secondso",
            "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."]
    return data

def yield_reindeer_position(reindeer):
    reindeer_actions = [ reindeer.velocity for _ in range(reindeer.runtime) ]
    reindeer_actions.extend([0 for _ in range(reindeer.downtime)])
    delta = cycle(reindeer_actions)
    while True:
        yield delta.next()


def race_at_x_time(reindeer, time):
    """time in seconds"""
    y = yield_reindeer_position(reindeer)
    distance = 0
    for _ in xrange(time):
        distance += y.next()
    return distance

def part1():
    data = read_data()
    time = 2503
    return max([race_at_x_time(r, time) for r in data.values()])

def part2():
    data = read_data()
    time = 2503
