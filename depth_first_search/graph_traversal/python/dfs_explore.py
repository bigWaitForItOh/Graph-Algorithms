##################################################################################################
#Recursive Implementation of Depth First Search Traversal for Adjacency List Graph
#Time Complexity: O (V+E)
##################################################################################################

def dfs_traverse (graph, source, traversal, visited):
	for neighbour in graph [source]:
		if (not neighbour in visited):
			traversal.append (neighbour);
			visited.add (neighbour);
			dfs_traverse (graph, neighbour, traversal, visited);

def dfs_explore (graph, source):
	traversal = [source];
	visited = set ([source]);

	dfs_traverse (graph, source, traversal, visited);
	return (traversal);

if (__name__ == '__main__'):
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
	print (dfs_explore (graph, 'A'));