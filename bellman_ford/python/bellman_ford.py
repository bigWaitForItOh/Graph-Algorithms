###########################################################################################################################
#IMPLEMENTATION OF Bellman-Ford Single Source Shortest Path Algorithm for weighted, directed graphs with edges allowed to be of positive or negative weight. Yeilds shortest path lengths from source to every other vertex.
#Time Complexity: O (V.E), V = number of vertices, E = Number of edges
###########################################################################################################################
def bellman_ford (graph, source):
	dists = { node : 0 if node == source else float ('inf') for node in list (graph) };
	
	for i in range (len (graph) - 1):
		for src in graph:
			for dest in graph [src]:
				if (dists [dest [0]] > (dists [src] + dest [1])):
					dists [dest [0]] = dists [src] + dest [1];
	for src in graph:
		for dest in graph [src]:
			if (dists [dest [0]] > (dists [src] + dest [1])):
				return ([]);
	return (dists);

#EXAMPLE OF A GRAPH
#REPRESENTED BY A DICTIONARY, WHERE A KEY REPRESENTS THE NODE FROM WHICH THE EDGE STARTS. A key's value is a set of Tuples. The first element of each tuple is the Node the edge reaches. The second element is the weight of the edge. The list contains 1 tuple for every neighbour the KEY has.
#EXAMPLE: A is connected to B with weight 2 and C with weight 3 and X & Y are unreachable Vertices

graph = {
	'A' : set ([ ('B', -1), ('C', 4) ]),
	'B' : set ([ ('C', 3), ('D', 2), ('E', 2) ]),
	'C' : set ([]),
	'D' : set ([ ('B', 2), ('C',5) ]),
	'E' : set ([ ('D', -3) ])
};

#sampe call to bellman_ford ();
dists = bellman_ford (graph, 'A');
for node in dists: print (node, dists [node]);
