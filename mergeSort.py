# MergeSort in Python 2.7
# By Marshall Ehlinger
# For 2015 Analysis of Algorithms class
# Implemented top-down

import math

def mergeSort(array):
	n = len(array)
	if (n > 1):

		mid = len(array) / 2
		b = array[:mid]
		c = array[mid:]

		b = mergeSort(b)
		c = mergeSort(c)

		print "b: " + str(b)
		print "c: " + str(c)

		return merge(b, c)
	else:
		return array


def copy(source, dest, startSourceIndex, endSourceIndex, startDestIndex, endDestIndex):
	subLen1 = endSourceIndex - startSourceIndex
	subLen2 = endDestIndex - startDestIndex 
	if (subLen1 != subLen2):
		print "Illegal copy attempt " + str(source) + "/" + str(dest) + ": unequal subarrays(" + str(subLen1) + " vs " + str(subLen2) + ")"
	else:
		for i in range(0, subLen2):
			dest[startDestIndex + i] = source[startSourceIndex + i]

def merge(sub1, sub2):
	lenSub1 = len(sub1)
	lenSub2 = len(sub2)
	newList = []
	i = 0
	j = 0
	k = 0 # Iterator variables

	while (i < lenSub1) and (j < lenSub2):
		if sub1[i] <= sub2[j]:
			newList.append(sub1[i])
			i += 1
		else:
			newList.append(sub2[j])
			j += 1
		k += 1
	if i == lenSub1:
		return newList.append(sub2[j:])
	else:
		return newList.append(sub1[i:])


########
# TEST #
########
a = [4, 5, 12, 213, 22, 98, 11, 4, 74, 35, 2, 7, 6]
mergeSort(a)
print a