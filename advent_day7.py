from collections import namedtuple

wire_mask = 2**16 - 1

gates = {
    'AND'      : lambda x, y: (x & y) & wire_mask,
    'OR'       : lambda x, y: (x | y) & wire_mask,
    'LSHIFT'   : lambda x, y: (x << y) & wire_mask,
    'RSHIFT'   : lambda x, y: (x >> y) & wire_mask,
    'IDENTITY' : lambda x: x & wire_mask,
    'NOT'      : lambda x: (~ x) & wire_mask,
}

Gate = namedtuple('Gate', ['operation', 'first_input', 'second_input'])
WIRES = dict()
class Wire(object):
    """A wire, as defined by the challenge"""
    def __init__(self, name, gate):
        """
        Name of the wire, the gate, and the names of the outputs.

        Also contains the input values for those gates that it would operate on when propogated
        """
        self.name      = name
        self.gate      = gate
        self.value     = None

    def operate(self):
        def is_number(x):
            try:
                int(x)
                return True
            except ValueError: # not an int
                return False
        def resolve_input(x):
            if is_number(x):
                return int(x)
            return WIRES[x].operate()
        op = self.gate.operation
        if not self.value:
            if op in ('IDENTITY', 'NOT'):
                first_number = resolve_input(self.gate.first_input)
                self.value = gates[op](first_number)
            if op in ('AND', 'OR', 'LSHIFT', 'RSHIFT'):
                first_number = resolve_input(self.gate.first_input)
                second_number = resolve_input(self.gate.second_input)
                self.value = gates[op](first_number, second_number)
        return self.value

def parse_input_line(line):
    l = line.split()
    name = l[-1]
    if l[1] == '->': # direct value
        WIRES[name] = Wire(name, Gate('IDENTITY', l[0], None))
    elif l[0] == 'NOT':
        WIRES[name] = Wire(name, Gate('NOT', l[1], None))
    else: # AND, OR
        WIRES[name] = Wire(name, Gate(l[1], l[0], l[2]))



def test():
    """
For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456"""
    data = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""".splitlines()

    expected_results = {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123,
        'y': 456
    }

    for d in data:
        parse_input_line(d)
    result = dict()
    for k in WIRES.keys():
        result[k] = WIRES[k].operate()
    return result == expected_results

def yield_input():
    with open("/Users/peter.norton/advent/2015/advent_day7", "r") as in_:
        for line in in_:
            yield line.rstrip()

def part1():
    for line in yield_input():
        parse_input_line(line)

    return WIRES['a'].operate()

def part2():
    result = part1()
    global WIRES
    WIRES = dict()
    for line in yield_input():
        parse_input_line(line)

    parse_input_line("{} -> b".format(result))
    return WIRES['a'].operate()
