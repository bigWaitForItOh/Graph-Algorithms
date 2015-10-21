#####################################################################################################################################
#IMPLEMENTATION OF Breadth First Search Shortest Path Algorihtm - Returns the first (i.e. the shortest) path found between the start
#and the end node in an unweighted (or weighted with all edges having the same weight) graph.
#If the start and end nodes are not connected, the function raises an IndexError Exception signalling that no path exists between
#them.
#####################################################################################################################################

def bfs_shortest_path (graph, start, end):
	queue, traversal, backtrace, path = [start], [None], {start : None}, [];
	while (not traversal [-1] == end):
		try:
			traversal.append (queue.pop (0));
		except Exception as e:
			raise e;

		for next_node in graph [traversal [-1]]:
			if (not (next_node in queue or next_node in traversal)):
				queue.append (next_node);
				backtrace [next_node] = traversal [-1];

	while (not end == None):
		path = [end] + path;
		end = backtrace [end];

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
print (bfs_shortest_path (graph, 'A', 'G'));
