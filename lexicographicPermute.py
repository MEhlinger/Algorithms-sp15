# Generates next permutation in lexicographic order
# Prototype for TSP problem code (will be implemented in C)
# For algorithms class, Spring 2015
# By Marshall Ehlinger

import math

def lexPermute(p):
	# If permutation array "a" (p in the code below) has two consecutive elements in increasing order,
    # Find the largest index i so that a[i]< a[i+1] 
	for i in range (len(p) - 2, -1, -1):
		if p[i] < p[i+1]:

			# Find the largest index j so that a[i]< a[j]
			for k in range (len(p) - 1, i, -1):
				if p[k] > p[i]:
					j = k
					break

			# Swap (a[i] and a[j])
			temp = p[i]
			p[i] = p[j]
			p[j] = temp

			# Reverse the order of  ai+1 all the way up to a[n]
			for g in range(i+1, int(math.ceil((len(p) + (i+1)) / 2))):
				temp = p[len(p) - (g-i)]
				p[len(p) - (g-i)] = p[g]
				p[g] = temp

			print p # Recursive print
			lexPermute(p) # Recursive call, primarily for debugging

	return p


########
# TEST #
########
perm = [1,2,3,4]
print perm
lexPermute(perm)