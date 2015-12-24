def incr_char(c):
    num = ord(c) + 1
    if 97 <= num and num <= 122:
        return chr(num)
    if 65 <= num and num <= 90:
        return chr(num)
    raise ValueError, "Overflowed the alphabet"

def increment_string(st):
    """With a string st, increment the letters starting from the rightmost,
    so the string "abx" would increment to "aby" then "abz", and then roll
    over to "aca"
    """
    increment_done = False
    new_st = list()
    for c in reversed(st):
        if increment_done:
            new_st.append(c)
        else:
            try:
                new_c = incr_char(c)
                new_st.append(new_c)
                increment_done = True
            except ValueError:
                if ord(c) == 90:
                    new_st.append("A")
                elif ord(c) == 122:
                    new_st.append("a")
    return "".join(reversed(new_st))



def has_increasing_run(st):
    """Has a run of 3 letters"""
    for place in range(len(st) - 2):
        try:
            next_c = incr_char(st[place])
            next_c2 = incr_char(next_c)
        except ValueError:
            # In the case of incr_char throwing this, the rule won't be satisified here
            continue
        if st[place + 1] == next_c and st[place + 2] == next_c2:
            return True
    return False

def has_no_confusing_letters(st):
    confusing_letters = 'i', 'o', 'l'
    for l in confusing_letters:
        if l in st:
            return False
    return True

def has_two_different_pairs(st):
    pairs = set()
    for pos in range(len(st) -1) :
        if st[pos] == st[pos + 1]:
            pairs.add(st[pos])
        if len(pairs) > 1:
            return True
    return False

def valid_password(pw):
    if has_increasing_run(pw) and \
        has_no_confusing_letters(pw) and \
        has_two_different_pairs(pw):
        return True
    return False

def next_password(pw):
    newpw = increment_string(pw)
    while True:
        if valid_password(newpw):
            return newpw
        else:
            newpw = increment_string(newpw)

def part1():
    return next_password("vzbxkghb")

def part2():
    return next_password(part1())
