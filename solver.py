#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    # split first line
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        # With each Item: index value and weight
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight

    # need to make a dynamic programming array for knapsack
    W = capacity
    n = len(items)
    
    # [[0] * cols] * rows
    # cols is weight while rows is items
    arr = [ [0 for x in range(W+1)] for x in range(n+1) ]

    for i in range(n+1): # items
        for w in range(W+1): # weight
            if i == 0 or w == 0:
                # base case
                arr[i][w] = 0
            elif items[i-1].weight <= w:
                arr[i][w] = max( items[i-1].value + arr[i-1][w- items[i-1].weight], arr[i-1][w])
            else:
                # when the item weight is more than the knapsack, the current is equal to the previous
                arr[i][w] = arr[i-1][w]

    print("test " + str(W) + " and " + str(n) )
    for i in range(n+1): # items is the rows
        print(arr[i])
    print()

    # trace back to find which items got selected
    #       weights weights weights
    # items
    # items

    # starts at the bottom, them move up items
    rIndex = len(arr) - 1
    cIndex = len(arr[0]) - 1 

    while rIndex > 0 and cIndex > 0: 
        cPrev = cIndex - 1
        # if value of previous index is different than curent index
        # the current index item is taken
        if arr[rIndex][cPrev] != arr[rIndex][cIndex] :

            # the column equals to minus that item weight
            cIndex -= items[i-1].weight

            # add that item to list of chosen items
            taken[rIndex] = 1

            # add that item weight into total weight
            weight += items[i-1].weight
        
        rIndex-=1

    value = arr[ len(arr)-1 ][ len(arr[0]) -1 ]
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

