##########################################################################################################################
#Implementation of Lowest Common Ancestor in a BINARY TREE
#Time Complexity : O (N)
#where N is the number of Nodes in the Binary Tree
#The algorithm assumes that both the query nodes exist in the Binary Tree
##########################################################################################################################

class Node (object):
	def __init__ (self, key, left, right):
		self.key = key;
		self.left = left;
		self.right = right;

###### LCA DEFINITION ######
def lca_bt (root, x, y):
	if (root == None):
		return (None);
	if (root.key == x):
		return (root.key);
	if (root.key == y):
		return (root.key);

	left = lca_bt (root.left, x, y);
	right = lca_bt (root.right, x, y);

	if (left and right):
		return (root.key);
	if (left):
		return (left);
	if (right):
		return (right);

	return (None);

if (__name__ == '__main__'):
	#Below is the construction of the Binary Tree, which is also a Binary Search Tree (same as the one used in lca_bst.py) but it is being treated as a Binary Tree
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

	print (lca_bt (root, 25, 55));
	print (lca_bt (root, 53, 64));
	print (lca_bt (root, 42, 55));
	print (lca_bt (root, 21, 11));
