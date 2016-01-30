##################################################################################################################
#Level Order Traversal of Binary Search Tree (using Queue data structure)
#Inspiration: https://www.hackerrank.com/contests/30-days-of-code/challenges/day-23-review-and-binary-trees
#Time Complexity of levelOrder (): O (N)
#where N = number of nodes in tree
##################################################################################################################

import sys
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
       	queue = [root];
       	finalString = '';

       	while (queue):
       	    current = queue.pop (0);
       	    finalString += str (current.data) + ' ';

       	    if (current.left):
       	    	queue.append (current.left);
       	    if (current.right):
       	    	queue.append (current.right);

        print (finalString);

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)