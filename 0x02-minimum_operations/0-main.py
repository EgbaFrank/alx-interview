#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 37
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = -1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 0
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = -10
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 24
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 10000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

