###########################################################################################################################
#Find the Center Node of an Undirected, Unweighted Tree
#Returns the centre node(s) of the given tree and maximum distance from the centre node(s)
#Time Complexity: O (N)
###########################################################################################################################

def tree_centre (tree_orig):
	tree = tree_orig.copy ();
	queue, limit = [i for i in tree if len (tree [i]) == 1], 1 if (len (tree) % 2) else 2;
	dist = 0;

	while (len (tree) > limit):
		extension = [];
		for i in range (len (queue)):
			current = queue.pop (0);
			parent = tree [current].pop ();

			tree [parent].discard (current);
			del tree [current];
			if (len (tree [parent]) == 1): extension.append (parent);

		dist += 1;
		queue += extension;

	return (queue, dist);

#Sample Tree #1
#Undirected, unweighted tree represented by a dictionary where: Key=>Source Vertex, Value=>List of its neighbour vertices.
#Note: If there is an edge between A and B, then Key (A) must contain B in its list of neighbours and Key (B) must contain A in its list of neighbours (to represent the undirected relationship).
'''
tree = {
	1 : set ([2]),
	2 : set ([1, 3]),
	3 : set ([2, 4]),
	4 : set ([3, 5]),
	5 : set ([4, 6]),
	6 : set ([5])
};
'''

#Sample Tree #2 - A more complicated tree
tree = {
	1 : set ([2]),
	2 : set ([1, 3, 4, 5]),
	3 : set ([2, 6]),
	4 : set ([2, 7]),
	5 : set ([2, 8, 13]),
	6 : set ([3]),
	7 : set ([4]),
	8 : set ([5, 9]),
	9 : set ([8, 11]),
	10 : set ([11]),
	11 : set ([9, 10, 12]),
	12 : set ([11]),
	13 : set ([5, 14]),
	14 : set ([13])
};

#Sample call to tree_centre - Pass as argument a tree. Returns a 2-tuple as result. First element is a list containing either 1 Vertex (if |V| = Odd) or 2 Vertices (if |V| = Even); |V| = number of vertices in the tree
c_nodes, c_dist = tree_centre (tree);
print (c_nodes, c_dist);
