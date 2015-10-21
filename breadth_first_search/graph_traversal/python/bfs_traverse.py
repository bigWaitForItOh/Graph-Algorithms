#####################################################################################################################################
#IMPLEMENTATION OF Breadth First Search Graph Traversal Algorithm - Explores the entire Graph startng from the given origin
#####################################################################################################################################

def bfs_traverse (graph, origin):
	queue, path = [origin], [];
	while (queue):
		path.append (queue.pop (0));
		for next_node in graph [path [-1]]:
			if (not (next_node in queue or next_node in path)):
				queue.append (next_node);
	return (path);

#EXAMPLE OF A GRAPH
#REPRESENTED BY A DICTIONARY, WHERE A KEY REPRESENTS THE NODE FROM WHICH THE EDGE STARTS. The corresponding value is a set of nodes the KEY node is neighbors with.
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
print (bfs_traverse (graph, 'A'));
