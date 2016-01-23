###########################################################################################################
#Find Height of a Binary Search Tree
#Inspiration: https://www.hackerrank.com/contests/30-days-of-code/challenges/day-22-binary-search-trees
#Time Complexity of getHeight (): O (N)
#where N is the number of Nodes in the BST. We visit each node exactly once.
###########################################################################################################

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            cur=Node(data)
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if (root == None):
            return (0);

        height, stack = 0, [(root, 1)];
        while (stack):
            cNode, cLevel = stack.pop ();
            if (cLevel > height):
                height = cLevel;

            if (cNode.left):
                stack.append ( (cNode.left, cLevel + 1) );
            if (cNode.right):
                stack.append ( (cNode.right, cLevel + 1) );

        return (height);

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)