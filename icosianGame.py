# The Icosian Game


def buildIcosian(ring, edges):
	if ring == 5:
		# Build empty set of vertices, each with three edges initially set to 0
		for i in range (0, 20):
			edges.append([0, 0, 0])


	for i in range (ring - 5, ring):
		if ring == 5:
			if i + 5 == ring:
				edges[i][0] = i + 4
			else:
				edges[i][0] = i - 1
			if i + 1 == ring:
				edges[i][1] = i - 4
			else:
				edges[i][1] = i + 1
			edges[i][2] = i + 5
		elif ring == 10:
			if i + 1 == ring:
				edges[i][0] = i + 1
			else:
				edges[i][0] = i + 6
			edges[i][1] = i + 5
			edges[i][2] = i - 5
		elif ring == 15:
			if i + 5 == ring:
				edges[i][0] = i - 1
			else:
				edges[i][0] = i - 6
			edges[i][1] = i - 5
			edges[i][2] = i + 5
		else:
			if i + 5 == ring:
				edges[i][0] = i + 4
			else:
				edges[i][0] = i - 1
			if i + 1 == ring:
				edges[i][1] = i - 4
			else:
				edges[i][1] = i + 1
			edges[i][2] = i - 5
	if ring != 20:
		buildIcosian(ring+5, edges)

	return edges


def hamiltonianPath(graph):
	startNode = graph[0]
	path = [0]	# Path begins with the start node, 0
	nextNode(path, graph, startNode, False) # Recursively builds and checks a tree
	return "Finished."


def nextNode(path, graph, goalNeighbors, finishedBool):
	if not (finishedBool):
		if (path[len(path)-1] in goalNeighbors) and (len(path) == len(graph)):
			finishedBool = True
			printFullPath(path)
		neighborSet = graph[path[len(path) - 1]]
		for neighbor in neighborSet:
			if neighbor not in path:
				path.append(neighbor) 
				nextNode(path, graph, goalNeighbors, finishedBool)
			if neighbor == path[len(path) - 1]:
				path.pop()
	

def printFullPath(path):
	print str(path) + " back to -> " + str(path[0])



#####################################################
# The test itself! Blam-o!
edges = []
icosian = buildIcosian(5, edges)
print hamiltonianPath(icosian)
######################################################
