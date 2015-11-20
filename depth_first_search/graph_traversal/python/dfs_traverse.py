#####################################################################################################################################
#IMPLEMENTATION OF Depth First Search Graph Traversal Algorithm - Explores the entire Graph startng from the origin node
#NOTE: The program output may differ on multiple runs for the same graph (thought the different outputs will all be correct).
#      The reason for this is that we are using set () to represent neighbouring nodes of a particular node inside the graph.
#      Python sets do not necessarily store the nodes in the order in which they exist in the list.
#      If you want consistency in the traversal, implement a graph without the set (), like shown in example graph_no_set
#####################################################################################################################################

stack = [];
def dfs_traverse (graph, origin, path):
	if (origin in stack or origin in path):
		return;

	stack.append (origin);
	path.append (origin);
	for neighbour in graph [origin]:
		dfs_traverse (graph, neighbour, path);
	stack.pop ();

'''
#EXAMPLE OF A GRAPH WITHOUT set () of neighbours
#REPRESENTED BY A DICTIONARY, WHERE A KEY REPRESENTS THE NODE FROM WHICH THE EDGE STARTS. The corresponding value is a LIST of nodes the KEY node is neighbors with.
graph_no_set = {
		'A' : ['B', 'S'],
		'B' : ['A'],
		'C' : ['D', 'E', 'F', 'S'],
		'D' : ['C'],
		'E' : ['C', 'H'],
		'F' : ['C', 'G'],
		'G' : ['F', 'H', 'S'],
		'H' : ['E', 'G'],
		'I' : [],
		'S' : ['A', 'C', 'G']
};
'''

#EXAMPLE OF A GRAPH WITH set () of neighbours
#REPRESENTED BY A DICTIONARY, WHERE A KEY REPRESENTS THE NODE FROM WHICH THE EDGE STARTS. The corresponding value is a SET of nodes the KEY node is neighbors with.

graph = {
		'A' : set (['B', 'S']),
		'B' : set (['A']),
		'C' : set (['D', 'E', 'F', 'S']),
		'D' : set (['C']),
		'E' : set (['C', 'H']),
		'F' : set (['C', 'G']),
		'G' : set (['F', 'H', 'S']),
		'H' : set (['E', 'G']),
		'I' : set ([]),
		'S' : set (['A', 'C', 'G'])
};

#SAMPLE CALL TO THE FUNCTION
#'A' is the node from which we start the exploration - notice that Node 'I' never appears in the returned list of explored nodes since it is isolated
path = [];
dfs_traverse (graph, 'A', path);
print (path);

