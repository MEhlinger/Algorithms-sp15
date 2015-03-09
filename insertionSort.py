# Insertion Sort
# by Marshall Ehlinger
# Written for Spring 2015 Analysis of Algorithms

a = [12, 5, 2, 6, 7, 0, 14, 2, 1, 20, 5, 19]

# i is the index of the first item in the unsorted portion of the list/array
for i in range(1, len(a)):
	j = i # j is the index of the item being checked
	while (j > 0) and (a[j-1] > a[j]):
		# While the first unsorted item is greater than the previous item (every possibility of which is in the sorted portion)
		temp = a[j]
		a[j] = a[j-1]
		a[j-1] = temp

		# Decrement j and repeat to sift unsorted item down to proper location
		j -= 1

print a
