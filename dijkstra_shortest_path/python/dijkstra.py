###########################################################################################################################
#IMPLEMENTATION OF Dijkstra's Shortest Path Algorithm for weighted, directed graphs. Yields shortest path LENGTHS from
#source to every other vertex (needs to be modified to include path information).
###########################################################################################################################

#takes the graph (described below) and the source vertex as arguments and returns a dictionary which contains all the vertices and their corresponding shortest path lengths
def dijkstra (graph, start):
	spt_set, dists = set (), { node : 0 if node == start else float ('inf') for node in list (graph) };

	while (not spt_set == set (list (graph))):
		nearest = (None, float ('inf'));
		for node in dists:
			if (nearest [1] > dists [node] and spt_set.isdisjoint ([node])):
				nearest = (node, dists [node]);
		spt_set.add (nearest [0]);

		for node in graph [nearest [0]]:
			if (dists [node [0]] > (nearest [1] + node [1])):
				dists [node [0]] = nearest [1] + node [1];
	return (dists);

#EXAMPLE OF A GRAPH
#REPRESENTED BY A DICTIONARY, WHERE A KEY REPRESENTS THE NODE FROM WHICH THE EDGE STARTS. A key's value is a set of Tuples. The first element of each tuple is the Node the edge reaches. The second element is the weight of the edge. The list contains 1 tuple for every neighbour the KEY has.
#EXAMPLE: A is connected to B with weight 2 and C with weight 3.
graph = {
	'A': set ([ ('B', 2), ('C', 3) ]),
	'B': set ([ ('C', 3), ('D', 5), ('E', 8) ]),
	'C': set ([ ('D', 6) ]),
	'D': set ([ ('E', 8), ('F',6) ]),
	'E': set ([ ('F', 6) ]),
	'F': set ([])
};

#SAMPLE CALL TO THE FUNCTION
dists = dijkstra (graph, 'A');
print ('Distances from A to all nodes are: ');
for i in x: print (i, x [i]);
