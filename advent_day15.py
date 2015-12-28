from collections import namedtuple, OrderedDict
from itertools import permutations, product

Ingredient = namedtuple('Ingredient', ["name", "capacity", "durability", "flavor", "texture", "calories"])
qualities = ('capacity', 'durability', 'flavor', 'texture', 'calories')


test_data = ["Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
             "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"]


def get_data():
    data = OrderedDict()
    # for line in test_data:
    for line in open("advent_day15", 'r').readlines():
        name, rest = line.split(':')
        capacity, durability, flavor, texture, calories = [int(i.split()[1]) for i in rest.split(",")]
        data[name] = Ingredient(name, capacity, durability, flavor, texture, calories)
    return data


def yield_subset_sum(target, the_len):
    for y in product(range(target+1), repeat=the_len):
        if sum(y) == target:
            yield y

def subset_sum(numbers, target, partial, the_len):
    s = sum(partial)
    combinations = list()
    # check if the partial sum is equals to target
    if s == target:
        # print "sum(%s)=%s" % (partial, target)
        return [partial]
    if s >= target:
        return []  # if we reach the number why bother to continue
    if len(partial) >= the_len:
        return []

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        # subset_sum(remaining, target, partial + [n], the_len)
        combinations.extend(subset_sum(remaining, target, partial + [n], the_len))
    return [c for c in combinations if len(c) == the_len]


def special_mult(*args):
    return reduce(lambda x, y: max(x, 0) * max(y, 0), args)

def evaluate_recipe_quality(ingredients, quantities, include_calories=False):
    """When include_calories=True, target a 500 calorie recipe"""
    def evaluate_ingredient(i, q):
        return [ q * prop for prop in i[1:] ]

    quals = map(evaluate_ingredient, ingredients.values(), quantities)
    combined_quals = map(sum, zip(*quals))
    if include_calories and combined_quals[-1] != 500:
        return 0
    return reduce(special_mult, combined_quals[:-1])


def yield_recipe_quality(ingredients, include_calories=False):
    """This is for part 1, it doesn't count calories"""
    # for target in subset_sum(range(100), 100, [], len(ingredients)):
    for target in yield_subset_sum(100, len(ingredients)):
        for c in permutations(target):
            quality = evaluate_recipe_quality(ingredients, c, include_calories)
            if quality > 0:
                yield quality

def part1():
    data = get_data()
    def yield_results():
        for cmb in  yield_recipe_quality(data):
            yield cmb

    return max(yield_results())

def part2():
    data = get_data()
    def yield_results():
        for cmb in  yield_recipe_quality(data, True):
            yield cmb

    return max(yield_results())
