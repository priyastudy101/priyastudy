#!/usr/bin/python

def find_majority(nums):
    d = {}
    c = 0
    for x in nums:
        if x not in d:
           d[x] = 1
        else:
           d[x] += 1
    return sorted(d.items(), key =lambda item: item[1] , reverse=True)[0][0]

print find_majority([6,5,5])
