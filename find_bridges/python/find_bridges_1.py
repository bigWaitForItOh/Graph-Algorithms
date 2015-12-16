##################################################################################################################################
#Program to find Bridges in a simple, unweighted, undirected graph.
#Time Complexity: O (E*(V + E))
#E = number of edges, V = number of Nodes
#For each edge in the graph, it removes the edge and explores the new graph using Breadth First Search to check if the graph is still connected.
#It then inserts the removed edge back into the graph
##################################################################################################################################

def is_connected (graph):
	queue, visited = [list (graph.keys ()) [0]], set ();
	current = None;

	while (queue):
		current = queue.pop ();
		visited.add (current);

		for neighbour in graph [current]:
			if (not (neighbour in visited or neighbour in queue)):
				queue.append (neighbour);

	return (len (graph) == len (visited));

def find_bridges (graph):
	bridges = set ();
	for node in graph:
		for neighbour in graph [node]:
			graph [node].remove (neighbour);
			graph [neighbour].remove (node);

			if (not is_connected (graph)):
				bridges.add ( (node, neighbour) );

			graph [node].add (neighbour);
			graph [neighbour].add (node);
	return (bridges);

graph = {
	'A' : set (['B','C']),
	'B' : set (['A','C']),
	'C' : set (['A','B','D','F']),
	'D' : set (['C','E']),
	'E' : set (['D']),
	'F' : set (['C'])
};

print (find_bridges (graph));
