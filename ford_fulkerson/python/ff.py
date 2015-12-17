#################################################################################################################
#Ford Fulkerson Max Flow Min Cut Algorithm
#################################################################################################################

import copy;

def bottleneck (graph, path):
	min_flow = float ('inf');

	for i in range (len (path) - 1):
		for neighbours in graph [path [i]]:
			if (neighbours [0] == path [i + 1] and neighbours [1] < min_flow):
				min_flow = neighbours [1];
				break;
	return (min_flow);

def bfs_path (graph, source, dest):
	path, current = [], None;
	backtrace, queue, visited = {source : None}, [source], set ();

	while (not current == dest):
		current = queue.pop (0);
		visited.add (current);

		for neighbour in graph [current]:
			if (not (neighbour [0] in visited or neighbour [0] in queue)):
				queue.append (neighbour [0]);
				backtrace [neighbour [0]] = current;

	while (current):
		path = [current] + path;
		current = backtrace [current];

	return (path, bottleneck (graph, path));

def zero_out (graph):
	for node in graph:
		for neighbour in graph [node]:
			neighbour [1] = 0;

def change_flow (graph, flow_net, path, min_flow):
	for i in range (len (path) - 1):
		pass;
		#LOGIC FOR MANIPULATING GRAPH & NETWORK FLOW
	
def max_flow (graph, source, sink):
	graph = copy.copy (graph);
	flow_net = copy.copy (graph);
	path, min_flow = bfs_path (graph, source);

	zero_out (flow_net);
	while (path):
		change_flow (graph, flow_net, path, min_flow);
		path, min_flow = bfs_path (graph, source, sink);

	return (flow_net);

graph = {
	'S' : [['A', 9], ['B', 9]],
	'A' : [['B', 10], ['C', 8]],
	'B' : [['C', 1], ['D', 3]],
	'C' : [['T', 10]],
	'D' : [['C', 8], ['T', 7]],
	'T' : []
};
max_flow_network = max_flow (graph, 'S', 'T');
#print (max_flow (graph, 'S', 'T'));
