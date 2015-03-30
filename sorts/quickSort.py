# QuickSort in Python 2.7
# By Marshall Ehlinger
# For 2015 Analysis of Algorithms class
# Written as a protype for C code


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
# MAIN #
########
def main():
	with open("sorts.txt", "r") as data:
		array = data.readlines()
	array = array[0].split(",")
	for i in range (0, len(array)):
		array[i] = int(array[i])
	quickSort(array, 0, len(array)-1)
	print array

########
# TEST #
########	
main()