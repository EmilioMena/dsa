"""
Given an array of positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, write a function that returns the smallest number of coins needed to make change for (to sum up to) that target amount using the given coin denominations.

Note that you have access to an unlimited amount of coins. 
In other words, if the denominations are [1, 5, 10] , you have access to an unlimited amount of 1 s, 5 s, and 10 s.

If it's impossible to make change for the target amount, return -1 .
"""

def minNumberOfCoinsForChange(n, denoms):
	min_ways = [float('inf')] * (n+1)
	min_ways[0] = 0 # min number of ways to make 0 coins is 0

	for i in range(len(min_ways)):
		for denom in denoms:
			if i >= denom:
				rem = i-denom
				min_ways[i] = min(min_ways[i], 1+min_ways[rem])


	return -1 if min_ways[-1] == float('inf') else min_ways[-1]
