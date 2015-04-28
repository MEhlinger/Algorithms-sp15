# Inter Quartile Range Finder
# by Marshall Ehlinger
# For Spring 2015 Analysis of Algorithms exam

# INPUT: a list of numerical values
# OUTPUT: The IQR-- the difference between the 7th percentile value and the 25th

import math

def IQR(array):
	hi = len(array)
	lo = 0

	q1 = int(math.ceil((hi - 1) / 4))
	q2 = int(math.ceil(q1 * 3))
	print q1, q2
	q1Val = -1
	q2Val = -1
	q1Found = False
	q2Found = False

	for i in range(lo, hi):
		fulcrum = partition(array, lo, hi-1)
		if fulcrum == q1:
			q1Val = array[fulcrum]
			q1Found = True
		if fulcrum == q2:
			q2Val = array[fulcrum]
			q2Found = True
		if fulcrum <= q1:
			lo = fulcrum
		if fulcrum >= q2:
			hi = fulcrum
	if q1Val == -1:
		q1Val = array[q1]
	if q2Val == -1:
		q2Val = array[q2]

	print q1Val
	print q2Val
	return q2Val - q1Val


def partition(array, lo, hi):
	pivot = array[hi]
	for i in range(lo, hi):
		if array[i] <= pivot:
			swap(array, i, lo)
			lo += 1
	swap(array, lo, hi)
	return lo # return the 'centerpoint'/wall

def swap(a, first, second):
	temp = a[first]
	a[first] = a[second]
	a[second] = temp


########
# TEST #
########
a = [100, 1, 25, 75]
print IQR(a)