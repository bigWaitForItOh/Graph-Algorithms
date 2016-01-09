##########################################################################################################################
#Implementation of Lowest Common Ancestor in a BINARY SEARCH TREE, assuming that the 2 nodes provided exist in the tree
#Time Complexity : O (log (N))
##########################################################################################################################

class Node (object):
	def __init__ (self, key, left, right):
		self.key = key;
		self.left = left;
		self.right = right;

###### LCA DEFINITION ######
def lca_bst (root, x, y):
	if (max(x,y) < root.key):
		return (lca_bst (root.left, x, y));
	if (min (x,y) > root.key):
		return (lca_bst (root.right, x, y));

	return (root.key);


if (__name__ == '__main__'):
	p = Node (64, None, None);
	o = Node (62, None, None);
	m = Node (70, None, None);
	l = Node (63, o, p);
	k = Node (65, l, m);
	j = Node (42, None, None);
	h = Node (55, None, None);
	g = Node (46, j, None);
	f = Node (25, None, None);
	e = Node (53, g, h);
	d = Node (16, None, f);
	c = Node (74, k, None);
	b = Node (41, d, e);
	root = Node (60, b, c);

	print (lca_bst (root, 25, 55));
	print (lca_bst (root, 53, 64));
	print (lca_bst (root, 42, 55));
	print (lca_bst (root, 21, 11));