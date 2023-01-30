
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
def printInorder(root): 
  
    if root: 
        printInorder(root.left) 
        # then print the data of node 
        print(root.val), 
        # now recur on right child 
        printInorder(root.right) 
  
def printPostorder(root): 
    if root: 
        # First recur on left child 
        printPostorder(root.left) 
        # the recur on right child 
        printPostorder(root.right) 
        # now print the data of node 
        print(root.val), 
  
def printPreorder(root): 
    if root: 
        # First print the data of node 
        print(root.val), 
        # Then recur on left child 
        printPreorder(root.left) 
        # Finally recur on right child 
        printPreorder(root.right) 
  
# Driver code 
root = Node(8) 
root.left      = Node(3)  
root.left.left  = Node(1)
root.left.right  = Node(6)
root.left.right.left  = Node(4)
root.left.right.right  = Node(7)
root.right     = Node(10)
root.right.left  = Node(14)
root.right.left.left  = Node(13)

print ("Preorder:")
printPreorder(root) 
  
print ("\nInorder:")
printInorder(root) 
  
print ("\nPostorder:")
printPostorder(root) 