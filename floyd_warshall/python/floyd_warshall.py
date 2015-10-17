#IMPLEMENTATION OF FLOYD-WARSHALL ALL PAIRS SHORTEST PATH ALGORITHM
#Yields Shortest Path Lengths in a Weighted Directed Graph with no loops and multiple edges 
#THE graph IS AN n X n MATRIX, WHERE n = NUMBER OF NODES
	#graph [i] [j] = W if the weight of the edge from Node i to j = W
	#graph [i] [j] = infinite if there is no direct edge from i to j (to assign infinite to a value, use: float ('inf') )
	#graph [i] [j] = 0 if i = j (, i.e., no self loops allowed)

def floyd_warshall (graph):
	nodes = len (graph);
	for k in range (nodes):
		for j in range (nodes):
			for i in range (nodes):
				if (graph [i] [k] + graph [k] [j] < graph [i] [j]):
					graph [i] [j] = graph [i] [k] + graph [k] [j];
	return (graph);

#USAGE:
#once a graph matrix has been retreived from floyd_warshall (), we use graph [i] [j] to find the shortest distance between node i & node j
#EXAMPLE:
graph = [
		[0, float ('inf'), float ('inf'), 4, 2],
		[float ('inf'), 0, float ('inf'), float ('inf'), float ('inf')],
		[2, 3, 0, float ('inf'), float ('inf')],
		[0, 5, float ('inf'), 0, float ('inf')],
		[float ('inf'), 1, 7, 6, 0]
];

#RETRIEVE THE SHORTEST PATH DISTANCES
distances = floyd_warshall (graph);
#PRINT SHORTEST DISTANCE BETWEEN NODE 0 AND NODE 1
print (distances [0] [1]);
