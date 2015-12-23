# See and say game

def count_initial_repeats(s):
    """Given a string of digits, take the first digit.
    Iterate over the list, and count how many copies of the first digit (if any) were found following it.
    Return a tuple of the number found, and how many times it was found.
    """
    this_number = s[0]
    count = 1
    for next_ch in s[1:]:
        if next_ch != this_number:
            break
        count += 1
    return (count, this_number,)


def see_say(number):
    number_str = str(number)
    result_list = list()
    pos = 0
    while pos < len(number_str):
        count, this_number_str = count_initial_repeats(number_str[pos:])
        pos += count
        result_list.append(str(count))
        result_list.append(this_number_str)
    return "".join(result_list)

def part1():
    puzzle_input = "1113222113"
    prior = puzzle_input
    for _ in range(40):
        prior = see_say(prior)
    return len(prior)

def part2():
    puzzle_input = "1113222113"
    prior = puzzle_input
    for _ in range(50):
        prior = see_say(prior)
    return len(prior)
