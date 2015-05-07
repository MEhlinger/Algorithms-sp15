# TSP Exact (Undirected) Solver
#  
#
# For algorithms class, Spring 2015
# By Marshall Ehlinger

import math

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

			# Reverse the order of  p[i+1] all the way up to p[numCities]
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

def letterToNumber(letter):
	# Converts a one-char string to it's alphabetical index (0-indexed)
	return ord(letter) - 97

def progressBar(routeNum, numRoutes, loadingBarAsterisks, percentComplete):
	# PROGRESS BAR PRINT LOGIC
	if routeNum % loadingBarAsterisks == 0:
		print(str(percentComplete) + "% complete, at route " + str(routeNum) + "/" + str(numRoutes))
		return 10 	# Return the amount of percent to add to percentComplete 
	return 0 # Only count by percent increment defined in above return statement

def sumRouteCost(numCities, adjacencyMatrix, route, minCost):
	routeCost = 0
	route.append(route[0])

	for i in range(0, numCities):
		routeCost += adjacencyMatrix[letterToNumber(route[i])][letterToNumber(route[i+1])]
		if (routeCost > minCost):
			return float('inf')
	return routeCost + adjacencyMatrix[letterToNumber(route[0])][letterToNumber(route[numCities])]


def tspSolveExact(inputPathStr):
	adjacencyMatrix = getArrayFromCSV(inputPathStr)

	cityNames = []
	for i in range(0, len(adjacencyMatrix[0])):
		cityNames.append(chr(i+97))
		adjacencyMatrix[i][i] = 0 # Adjust all nodes' distance to self to "0"

	numRoutes = int(math.ceil(math.factorial(len(cityNames) - 1) / 2))
	print("Number of unique routes: " + str(numRoutes))

	loadingBarAsterisks = math.floor(numRoutes / 10)

	minCost = float("inf")
	shortestRoute = []
	numCities = len(cityNames)

	routeNum = 0
	percentComplete = 0
	route = list(cityNames)

	for i in range(0, numRoutes):

		percentComplete += progressBar(routeNum, numRoutes, loadingBarAsterisks, percentComplete)
		routeNum += 1

		
		routeCost = sumRouteCost(numCities, adjacencyMatrix, route, minCost)

		if routeCost < minCost:
			shortestRoute = list(route)
			minCost = routeCost

		# Get next route/permutation, removing the return trip to the starting city before permuting
		route.pop()
		route = list(lexPermute(route))



	print("Shortest Route : " + str(shortestRoute))
	print("Cost of Shortest Route : " + str(minCost))


########
# MAIN #
########
tspSolveExact("tests/10.txt")