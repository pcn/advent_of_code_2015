from collections import namedtuple, OrderedDict
from itertools import permutations

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
    for a in args:
        if a < 0:
            return 0
    return reduce(lambda x,y: x*y, args)

def evaluate_recipe_quality(ingredients, quantities, include_calories=False):
    """When include_calories=True, target a 500 calorie recipe"""
    def evaluate_ingredient(i, q):
        try:
            rv = [ q * prop for prop in i[1:] ]
            return rv
        except TypeError as te:
            print "TypeError ingredients: {}, quantities:{}, include_calorie: {}".format(
                ingredients, quantities, include_calories)
            raise

    quals = map(evaluate_ingredient, ingredients.values(), quantities)
    combined_quals = map(sum, zip(*quals))
    if include_calories:
        if combined_quals[-1] == 500:
            return reduce(special_mult, combined_quals[:-1])
        else:
            return 0
    else:
        return reduce(special_mult, combined_quals[:-1])


def yield_recipe_quality(ingredients, include_calories=False):
    """This is for part 1, it doesn't count calories"""
    for target in subset_sum(range(100), 100, [], len(ingredients)):
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
