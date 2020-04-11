#!/bin/python3

import helpers as pmat

# ----------------------------------------------
def hourglassSum(arr):
    arr = pmat.str_to_mat(arr) ########################### REMOVE IN SITE

    def shablon(base_i, base_j):
        return [
            arr[base_i][base_j],
            arr[base_i][base_j + 1],
            arr[base_i][base_j + 2],
            arr[base_i + 1][base_j + 1],
            arr[base_i + 2][base_j],
            arr[base_i + 2][base_j + 1],
            arr[base_i + 2][base_j + 2],
        ]
    sums = []
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            sums.append(sum(shablon(i, j)))
    return max(sums)

# ----------------------------------------------
arr = '''
-9 -9 -9  1 1 1 1 
 0 -9  0  4 3 2 2
-9 -9 -9  1 1 1 3
-9 -9 -9  1 1 1 4
-9 -9 -9  1 2 3 -15
 0  0  8  6 6 0 2
 0  0  0 -2 0 0 1
 0  0  1  2 4 0 -1
'''

print(hourglassSum(arr))
