######################################################################################################################
#Find the Longest Path Length in an unweighted, undirected tree using Breadth First Search (Twice)
#Returns the Start Node, End Node and Length of the the longest path in the tree as a 3-Tuple
#Can be modified to include the Path Information
######################################################################################################################

#This routine returns a 2-Tuple: (The farthest Node from source Node, Length of the Path between source to Farthest)
#All edges are assumed to be of path length 1
def bfs_farthest (tree, source):
        visited, queue = [], [(source, 0)];
        while (queue):
                current = queue.pop (0);
                visited.append ( (current [0], current [1]) );

                for neighbour in tree [visited [-1] [0]]:
                        if (not (neighbour in [i [0] for i in queue] or neighbour in [i [0] for i in visited])):
                                queue.append ( (neighbour, visited [-1] [1] + 1) );

        return ( (visited [-1] [0], visited [-1] [1]) );

def longest_path (tree):
	source, path_len = bfs_farthest (tree, list (tree.keys ()) [0]);
	dest, path_len = bfs_farthest (tree, source);
	return (source, dest, path_len);

#Sample Tree - Dictionary: Key => Source Node, Value => list of Nodes which are neighbours of Source Node
#NOTE: The dictionary should reflect the undirected nature of the tree.
#eg - Node 1 is connected to 2 and 2 is also connected to 1.

tree = {
	1 : [2, 3],
	2 : [1, 4, 5],
	3 : [1, 6, 7],
	4 : [2, 8],
	5 : [2],
	6 : [3],
	7 : [3],
	8 : [4]
};

print (longest_path (tree));
