#!/usr/bin/env python

from collections import namedtuple, defaultdict
import sys
import copy

Route = namedtuple('Route', ['distance', 'start', 'end'])

def yield_input():
    with open("/Users/peter.norton/advent/2015/advent_day9", "r") as in_:
        for line in in_:
            yield line.rstrip()


simpler = ["London to Dublin = 464",
            "London to Belfast = 518",
            "Dublin to Belfast = 141",]
def yield_simpler_input():
    for i in simpler:
        yield i


def plausible_route(r_dict, start, end):
    """Check to see if a particular route is valid.

    r_dict has to have forward and reverse paths.
    """
    # rev_r_dict = defaultdict(list)
    # for k, v in r_dict.items():
    #     for dest in v:
    #        rev_r_dict[dest].append(k)
    for route in r_dict[start]:
        if route.end == end:
            return True
    # for route in rev_r_dict[start]:
    #     if route.end == end:
    #        return True
    return False

def traverse(r_dict, route):
    """recurse through the r_dict, creating a new route list for each """
    all_paths = list()

    if len(route) > 0:
        starting_positions = [route[-1]]
    else:
        starting_positions = r_dict.keys()

    for starting_point in starting_positions:
        destinations = [r.end for r in r_dict[starting_point]]
        target = None
        for target in [t for t in destinations if t not in route ]:
            next_route = copy.copy(route)
            next_route.append(target)
            result = traverse(r_dict, next_route)
            all_paths.extend(result)
        if target is None:
            return [route]
    return all_paths

def build_legs():
    """Builds a forward and reverse lookup table for current location->next steps"""
    legs = defaultdict(list)
    for line in yield_input():
        (start, _, end, _, distance) = line.split()
        legs[start].append(Route( int(distance), start, end))
        legs[end].append(Route(int(distance), end, start))
    return legs

def get_distance(start, end, legs):
    """calculates the distances in a path, indexerrors on invalid paths.
    I'm not clear on whether there can be a path that is keyed on both
    the start and the end with different distances (that'd probably be a
    bug in the data) but... just in case, I'm selecting the min distance.
    """
    invalid_route = (sys.maxint, 0, 0)
    forward_route = [r for r in legs[start] if r.start in (start, end) and r.end in (start, end)]
    backward_route =  [r for r in legs[end] if r.start in (start, end) and r.end in (start, end)]
    forward_route.append(invalid_route)
    backward_route.append(invalid_route)
    least_distance = min(min(forward_route), min(backward_route))
    if least_distance == invalid_route:
        raise IndexError, "Invalid Route"
    return least_distance.distance

def total_route_distance(route_list, legs):
    """route_list: a list of city names
    legs: a dictionary containing the start city: legs mapping


    raises indexerror from get_distance if the mapping doesn't exist in the
    legs dictionary
    """
    total_distance = 0
    for location in range(len(route_list) - 1):
        total_distance += get_distance(route_list[location], route_list[location+1], legs)
    return total_distance

def distances():
    """part 1"""
    # build a dicationary of key: [list of route]
    legs = build_legs()

    all_path_list = traverse(legs, [])
    distances = list()
    longest_path_len = max([len(pth) for pth in all_path_list])
    longest_paths= set([tuple(pth) for pth in all_path_list if len(pth) == longest_path_len])
    for path in longest_paths:
        try:
            # print "Trying path {}".format(path)
            d = total_route_distance(path, legs)
            distances.append((d, path,))
        except IndexError:
            # If there is an invalid path, discard the path
            print "Invalid path: {}".format(path)
    return distances

def part1():
    d = distances()
    return min(d)

def part2():
    d = distances()
    return max(d)
