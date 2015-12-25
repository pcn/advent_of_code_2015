# Model reindeer motion as a list of distance per second, with each second being one element in the array.
from itertools import cycle
from collections import namedtuple

Reindeer = namedtuple('Reindeer', ("name", "velocity", "runtime", "downtime"))

def read_data():
    reindeer = dict()
    # for line in test_data():
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


def winner_at_x_time(reindeer, time):
    """time in seconds"""
    y = yield_reindeer_position(reindeer)
    distance = 0
    for _ in xrange(time):
        distance += y.next()
    return distance

def race_progress(reindeer, time):
    y = yield_reindeer_position(reindeer)
    return [ y.next() for _ in range(time) ]

def score_by_lead(reindeer_positions, time):
    rds = reindeer_positions.keys()
    reindeer_bonuses = { k: 0 for k in rds }
    # for each second, sum from 0 to second, and award a bonus to each
    # reindeer who is in the lead
    for point_in_time in range(1, time+1):
        race_status = {k: sum(reindeer_positions[k][0:point_in_time]) for k in rds}
        max_distance = max([v for v in race_status.values()])
        for key in [k for k, v in race_status.items() if v == max_distance]:
            reindeer_bonuses[key] += 1
    return reindeer_bonuses



def part1():
    data = read_data()
    time = 2503
    return max([winner_at_x_time(r, time) for r in data.values()])

def part2():
    data = read_data()
    time = 2503
    reindeer_positions = {k: race_progress(v, time) for k, v in data.items()}
    scores = score_by_lead(reindeer_positions, time)
    return scores
