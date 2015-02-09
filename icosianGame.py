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
