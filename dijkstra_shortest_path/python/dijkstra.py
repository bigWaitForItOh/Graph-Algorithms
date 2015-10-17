###########################################################################################################################
#IMPLEMENTATION OF Dijkstra's Shortest Path Algorithm on a weighted, directed graph.
###########################################################################################################################

from heapq import heapify, heappush, heappop;

def dijkstra (graph, start, target):
	queue, current_node = [], (0, start, [start]);

	heapify (queue);
	heappush (queue, current_node);
	while (not current_node [1] == target):
		try:
			current_node = heappop (queue);
		except Exception as e:
			return (-1, []);

		for neighbour in graph [current_node [1]]:
			heappush (queue, (current_node [0] + neighbour [1], neighbour [0], current_node [2] + [neighbour [0]]));
	return (current_node [0], current_node [2]);

#EXAMPLE OF A GRAPH
#REPRESENTED BY A DICTIONARY, WHERE A KEY REPRESENTS THE NODE FROM WHICH THE EDGE STARTS. A key's value is a list of Tuples. The first element of each tuple is the Node the edge reaches. The second element is the weight of the edge. The list contains 1 tuple for every neighbour the KEY has.
#EXAMPLE: A is connected to B with weight 2 and C with weight 3.
graph = {
	'A': [ ('B', 2), ('C', 3) ],
	'B': [ ('C', 3), ('D', 5), ('E', 8) ],
	'C': [ ('D', 6) ],
	'D': [ ('E', 8), ('F',6) ],
	'E': [ ('F', 6) ],
	'F': []
};

#SAMPLE CALL TO THE FUNCTION
print (dijkstra (graph, 'A', 'F'));
