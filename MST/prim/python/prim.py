############################################################################################################################
#Prim's Algorithm to find the minimum Spanning Tree of a simple, weighted, undirected graph using binary Heap.
#Time Complexity:
#	O (E log (V))
#E: number of edged, V : number of Nodes / Vertices
############################################################################################################################

from heapq import heapify, heappop, heappush;

#prim_mst () takes graph as argument, returns a 2-Tuple: (A, B) where A is the MST and B is the MST weight
def prim_mst (graph):
	visited, nodes = set (), set ([i for i in graph]);
	tree, tree_weight = {i : set () for i in graph}, 0;
	edge_choices = [(0, None, list (graph) [0])];

	heapify (edge_choices);
	while (nodes):
		weight, src, dest = heappop (edge_choices);
		if (src):
			tree [src].add ( (dest, weight) );
			tree [dest].add ( (src, weight) );

		nodes.remove (dest);
		visited.add (dest);
		tree_weight += weight;

		for neighbour in graph [dest]:
			if (not (neighbour [0] in visited)):
				heappush (edge_choices, (neighbour [1], dest, neighbour [0]));

	return (tree, tree_weight);

if (__name__ == '__main__'):
	graph = {
		1 : set ([(2,5),(4,8)]),
		2 : set ([(1,5),(3,10),(6,6)]),
		3 : set ([(2,10),(5,7),(6,4)]),
		4 : set ([(1,8),(6,3)]),
		5 : set ([(3,7),(6,1)]),
		6 : set ([(2,6),(3,4),(4,3),(5,1)])
	};

	mst = prim_mst (graph);
	print (mst [1]);
	for i in mst [0]: print (i, mst [0] [i]);