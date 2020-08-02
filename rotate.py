#!python

import math
import itertools

EMPTY_SEAT = {"empty": "self-reflection"}

def split_by_two(group):
    sub_groups = {}
    i = 0
    x = 0
    for member, room in group.items():
        if (even(i)):
            sub_groups[x] = {member: room}
        else:
            sub_groups[x] = {**sub_groups[x], **{member: room}}
            x+= 1
        i+= 1
    return sub_groups


def sort_non_overlapping(combinations):

    for blubb in combinations:
        pass
    return sorted_combinations

def even(number):
    return (number % 2) == 0

def odd(number):
    return (number % 2) != 0

def make_even_numbered_group(group):
    length = len(group)
    if odd(length):
        return {**group, **EMPTY_SEAT}
    else:
        return group

def rotate(splitted_group):
    pass

members = {
    "a": "blubb",
    "b": "john",
    "c": "doe",
    "d": "foo",
    "e": "bar",
    }

print("members {}".format(members))
length = len(members)
group = make_even_numbered_group(members)
print("group {}".format(group))
print("")


splitted_groups = split_by_two(group)
print (splitted_groups)

rotate(splitted_group)

# combinations = list(itertools.combinations(group, 2))
# print("All unique pairing combinations:")
# print(combinations)

# for pair in combinations:
#     print("{}".format(pair))

# for pair in combinations:
#     print("{}".format(pair))
#     print("Rooms: Either <<{}>> or <<{}>>".format(total[pair[0]], total[pair[1]]))
    # print()


# import sys
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))
# try:
#     total = int(sys.argv[1])
#     part = int(sys.argv[2])
# except ValueError as e:
#     print("args need to be castable to int - using defaults...")
# except BaseException as e:
#     print("no args - using defaults...")
