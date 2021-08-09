"""
algoexpert DP

Write a functino that takes in an array of positive integers and returns the max sum of non-adjacent elements in the array

If the input array is empty, the function should return 0
"""

## O(n) time, O(n) space
def maxSubsetSumNoAdjacent(array):
	if len(array) == 0:
		return 0
	if len(array) == 1:
		return array[0]

	max_at_index = [0]*len(array)
	max_at_index[0] = array[0]
	max_at_index[1] = max(array[1], array[0])

	for i in range(2, len(array)):
		max_at_index[i] = max(array[i] + max_at_index[i-2], max_at_index[i-1])

	return max_at_index[-1]


# cut down space to O(1)

def maxSubsetSumNoAdjacent(array):
	if len(array) == 0:
		return 0
	if len(array) == 1:
		return array[0]

	two_away = array[0]
	one_away = max(array[1], array[0])

	for i in range(2, len(array)):
		current = max(array[i] + two_away, one_away)
		two_away = one_away
		one_away = current

	return one_away
