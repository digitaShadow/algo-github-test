"""
ALGO-Python-Test

14th June, 2021
Last Edited By: QASIM ALI

"""



import json
import random

# -> (dict, dict, dict, dict,)

def parse_commands_func():
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    parse_commands = []

    [parse_commands.append(row.copy()) if 'function' in row and row['function'] == 'parse' else False for row in data]

    # OLD CODE
    # for row in data:
    #     if 'function' in row and row['function'] == 'parse':
    #         parse_commands.append(row.copy())
    # print("parse_commands: " + format(parse_commands))
    return parse_commands

def copy_commands_func():
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    copy_commands = []

    [copy_commands.append(row.copy()) if 'function' in row and row['function'] == 'copy' else False for row in data]

    # OLD CODE
    # for row in data:
    #     if 'function' in row and row['function'] == 'copy':
    #         copy_commands.append(row.copy())
    # print("copy_commands: " + format(copy_commands))
    return copy_commands

def two_lists():
    functional_commands = []
    counter = 0

    # [functional_commands.append(new_row) for row in parse_commands]
    parse_commands = parse_commands_func()
    copy_commands = copy_commands_func()
    for row in parse_commands:
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'parse'
        new_row['_counter'] = counter
        functional_commands.append(new_row)

    counter = 0
    for row in copy_commands:
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'copy'
        new_row['_counter'] = counter
        functional_commands.append(new_row)
    print("functional_commands: " + format(functional_commands))
    return functional_commands


def random_sampling_func():
    random_commands = []
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
        random_commands = random.sample(data, 2)
    print("random_commands: "+ format(random_commands))
    return random_commands

def main():
    # NOTE: Get all the parse commands

    parse  = parse_commands_func()
    print("parse_commands: " + format(parse))

    # NOTE: Get all the copy commands
    copy = copy_commands_func()
    print("copy_commands: " + format(copy))

    # NOTE: Put the two lists together and say which list it came from as well as the item number for that list
    lists = two_lists()

    # NOTE: Get random sampling of data
    random = random_sampling_func()

    return parse, copy, lists, random


if __name__ == '__main__':
    # parse_commands, copy_commands, functional_commands, random_commands = main()
    parse, copy, lists, random  = main()

    assert parse == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert lists == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random) == 2

    # OLD CODE

    # print(parse)
    # assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    # assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    # assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    # assert len(random_commands) == 2
