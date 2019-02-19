#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from collections import namedtuple
sys.setrecursionlimit(10001)
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []
    weights=[]
    values=[]
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
        weights+=[int(parts[1])]
        values+=[int(parts[0])]

    """
    def knapSack(W, wt, val, n):
        K = [[0 for x in range(W+1)] for x in range(n+1)]
        sel=[[[] for x in range(W+1)] for x in range(n+1)]
        # Build table K[][] in bottom up manner
        for i in range(n+1):
            for w in range(W+1):
                if i==0 or w==0:
                    K[i][w] = 0
                elif wt[i-1] <= w:
                    if val[i-1] + K[i-1][w-wt[i-1]] <= K[i-1][w]:
                        K[i][w] = K[i-1][w]
                        sel[i][w] = sel[i-1][w]+[0]
                    else:
                        K[i][w] = val[i-1] + K[i-1][w-wt[i-1]]
                        sel[i][w] = sel[i-1][w]+[1]
                else:
                    K[i][w] = K[i-1][w]
                    sel[i][w] = sel[i-1][w]+[0]

        return (K[n][W],sel[n][W])
    value,taken=knapSack(capacity, weights, values, item_count)

    """
    taken=[0]*item_count

    def knap(k,n):
        if k==0 or n==0:
            return 0
        elif weights[n-1]>k:
            taken[n-1]=0
            return knap(k,n-1)
        else:
            if values[n-1]+knap(k-weights[n-1],n-1)>=knap(k,n-1):
                taken[n-1]=1
                return values[n-1]+knap(k-weights[n-1],n-1)
            else:
                taken[n-1]=0
                return knap(k,n-1)

    value=knap(capacity,item_count)

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
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
        file_location='data/ks_30_0'
        #file_location='data/ks_lecture_dp_2'
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
