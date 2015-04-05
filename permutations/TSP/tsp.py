# TSP Exact Undirected Solver
#  
# 
#
# For algorithms class, Spring 2015
# By Marshall Ehlinger

import math

def permuteRoutes(cityList):
	uniqueRouteCount = long(math.factorial(len(cityList) - 1) / 2)
	print "Number of unique routes: " + str(uniqueRouteCount)
	routeList = []
	routeList.append(cityList)

	for i in range(0, uniqueRouteCount - 1):
		# -1 in above range is initial route permutation
		routeList.append(lexPermute(routeList[i]))

	return routeList

def lexPermute(route):
	# Finds the next route in lexicographic order
	#
	# If array p has two consecutive elements in increasing order,
    # Find the largest index i so that p[i]< p[i+1] 

	p = list(route)

	for i in range (len(p) - 2, -1, -1):
		if p[i] < p[i+1]:

			# Find the largest index j so that p[i]< p[j]
			for k in range (len(p) - 1, i, -1):
				if p[k] > p[i]:
					j = k
					break

			# Swap p[i] and p[j]
			temp = p[i]
			p[i] = p[j]
			p[j] = temp

			# Reverse the order of  p[i+1] all the way up to p[n]
			for g in range(i+1, int(math.ceil((len(p) + (i+1)) / 2))):
				temp = p[len(p) - (g-i)]
				p[len(p) - (g-i)] = p[g]
				p[g] = temp

			return p


def getArrayFromCSV(filename):
	# Returns a two-dimensional array of data from comma-seperated text file,
	# formatted as a 2-dimensional adjacency matrix, to a 2D list of lists
	with open(filename,"r") as csv:
		dataList = csv.read().splitlines()
	for i in range(0, len(dataList)):
		dataList[i] = dataList[i].split(",")
		for j in range(0, len(dataList[i])):
			dataList[i][j].rstrip()
			dataList[i][j] = int(dataList[i][j])
	return dataList


########
# TEST #
########
adjacencyMatrix = getArrayFromCSV("tests/6.txt")
routes = permuteRoutes(adjacencyMatrix[0])