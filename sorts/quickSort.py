# QuickSort in Python 2.7
# By Marshall Ehlinger
# For 2015 Analysis of Algorithms class
# Written as a protype for C code

import random

def quickSort(array, lo, hi):
	if lo < hi:
		pivot = partition(array, lo, hi)
		quickSort(array, lo, pivot-1)
		quickSort(array, pivot+1, hi)

	

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
array = [65, 4, 5, 61, 12, 232, 123123, 12, 10, 7, 99]
#print partition(array, 0, len(array))
quickSort(array, 0, len(array)-1)
print array