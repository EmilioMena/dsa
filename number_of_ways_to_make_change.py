"""
Given an array of distinct positive integers representing coin denominations and a single non-negative integer 'n' representing a target amount of money, write a function that returns that number of ways to make change for that target amount using the given coin denominations

Note that unlimited amount of coins is at your disposal

Sample input
n = 6, denoms = [1,5]

Sample output

2 // 1x1 + 1x5 and 6x1
"""

def numberOfWaysToMakeChange(n, denoms):

	num_ways_at = [0]*(n+1)
	num_ways_at[0] = 1

	for denom in denoms:
		for i in range(len(num_ways_at)):
			if denom <= i:
				num_ways_at[i] += num_ways_at[i-denom]

	return num_ways_at[-1]
