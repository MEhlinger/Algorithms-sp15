# MergeSort in Python 2.7
# By Marshall Ehlinger
# For 2015 Analysis of Algorithms class
# Implemented top-down

import math

def mergeSort(a):
	if len(a) <= 1:
		return a 	# if length of the list is 1, it is sorted, and ready to be re-merged
	else:
		midpoint = len(a) / 2
		left = mergeSort(a[:midpoint])
		right = mergeSort(a[midpoint:])

		return merge(left, right)

def merge(left, right):
	li = 0
	ri = 0
	di = 0 # left source array, right source array, and destination array iterators
	dest = [""] * (len(right) + len(left)) 

	# Fill in the return/result list 'dest' with the smallest value between left and right until either left or right is empty
	while (li < len(left) and ri < len(right)):
		if left[li] < right[ri]:
			dest[di] = left[li]
			li += 1
		else:
			dest[di] = right[ri]
			ri += 1
		di += 1 	# track leading edge of dest(ination array) contents  

	# Now that either left or right is empty, check to see if each is empty, and if not, tack it all on.
	# Both are already sorted because the recursive, bottom-up merging/sorting process
	while li < len(left):
		dest[di] = left[li]
		li += 1
		di += 1

	while ri < len(right):
		dest[di] = right[ri]
		ri += 1
		di += 1

	return dest

########
# TEST #
########
a = [4, 5, 12, 213, 22, 98, 11, 4, 74, 35, 2, 7, 6]
print mergeSort(a)
