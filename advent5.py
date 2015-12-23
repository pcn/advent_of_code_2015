def has_doubles(s):
    for pos in range(len(s)-1):
        if s[pos] == s[pos+1]:
            return True
    return False

def has_bad_strings(s):
    bad_strings = ("ab", "cd", "pq", "xy")
    for bs in bad_strings:
        if bs in s:
            return True
    return False

def has_three_vowels(s):
    good_vowels = "aeiou"
    ithas = [x for x in tuple(s) if x in good_vowels]
    return len(ithas) >= 3

def yield_input():
    with open("/tmp/advent_day5", "r") as in_:
        for line in in_:
            yield line.rstrip()

def count_nice_strings():
    nice_strings = list()
    for line in yield_input():
        if not has_doubles(line):
            continue
        if has_bad_strings(line):
            continue
        if not has_three_vowels(line):
            continue
        nice_strings.append(line)
    return nice_strings


# part 2

from collections import defaultdict

def two_letters_appear_twice(s):
    # Find all doubles
    for pos in range(len(s)-1):
        if len(s.split(s[pos:pos+2])) > 2:
            # return s[pos:pos+2]
            return True
    return False

def letters_separated_by_one(s):
    for pos in range(len(s)-2):
        if s[pos] == s[pos+2]:
            return True
    return False

def new_count_nice_strings():
    nice_strings = list()
    for line in yield_input():
        if two_letters_appear_twice(line) is False:
            continue
        if not letters_separated_by_one(line):
            continue
        nice_strings.append(line)
    return nice_strings
