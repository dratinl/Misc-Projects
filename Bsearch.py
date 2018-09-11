import requests
import itertools

def bin_search(arr, n, k):
	# Accepts a sorted list of integers 'arr' and beforms a binary search for the value 'k' based
	# on the size of the list 'n'. Returns the index of the found key if it exists in the array or a 
	# '-1' otherwise
	L = 0
	R = n - 1
	while (L < R):
		mid = (L + R)/2
		if k > arr[mid]:
			L = mid + 1
		else: 
			R = mid
	if L != len(arr) and arr[L] == k:
		return L
	else:
		return -1

# reads in input file from 'input.txt' in the format: 
# number of test cases
# size of array
# array
# key
# continuing from size of array for the remainder of the test cases 
with open("input.txt","r") as f:
	lines = f.readlines()
	lines = [i.strip() for i in lines]
result = []
test_amt = int(lines.pop(0))
while (test_amt > 0) :
	array_size = int(lines.pop(0))
	temp_arr = lines.pop(0)
	arr = [int(s) for s in temp_arr.split(' ')]
	key = int(lines.pop(0))
	test_amt -= 1
	result.append(bin_search(arr, array_size, key))
print result
