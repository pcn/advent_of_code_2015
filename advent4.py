from hashlib import md5
from functools import partial
import binascii
from itertools import takewhile, count, repeat

prefix = "bgvyzdsv"

def does_not_match(number, plen):
    s = prefix + str(number)
    h = md5(s)
    result = binascii.hexlify(h.digest())
    if result[0:plen] == "".join(repeat("0", plen)):
        return False
    return True

def match5(number):
    return does_not_match(number, 5)

def match6(number):
    return does_not_match(number, 6)

print len(list(takewhile(match5, count())))

print len(list(takewhile(match6, count())))

match5(254575)
