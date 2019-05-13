import random

def size(root): 
    '''
    Compute the total number of nodes in a tree.
    '''
    if root is None: 
        return 0 
    else: 
        return (size(root.left) + 1 + size(root.right))

def is_balanced(root):
    '''
    Method for determining if a binary tree is balanced.

    A binary tree is balanced if:
        - it's empty
        - the left sub tree is balanced
        - the right subtree is balanced
        - the difference in depth between left and right is <=1

    Parameters:
    ____________
    root : the node object, below which the definition of 'balanced' will be applied.    
    '''
    if root is None: 
        return True
    return is_balanced(root.right) and is_balanced(root.left) and abs(get_height(root.left) - get_height(root.right)) <= 1              

def get_height(root):
    '''
    Returns the maxium depth of the tree. 

    Parameters:
    ___________
    root : the node object, below which maximum depth will be calculated.  
    '''
    if root is None: 
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))    


def build_tree(n,min_num,max_num,start=None):
    '''
    Method for building and populating a binary tree.  

    Parameters:
    ___________
    n : int 
        the number of integers you want to populate the tree with. 
    min_num : int 
        the smallest number available to the random number generator.
    max_num : int 
        the largest number available to the random number generator.
    start : int, optional
        the value to appear at the stump of the tree.            
    '''
    if start:
        initial=start
    else:
        initial=random.randint(min_num,max_num)
    root=Node(initial)
    for _ in range(n-1):
        root.insert(random.randint(min_num,max_num))
    return root    


 
        
               
    


def inorderTraversal(root):
    '''
    Return an array of tree elements using inorder traversal.  
    Left-->Root-->Right
    '''
    res = []
    if root:
        res = inorderTraversal(root.left)
        res.append(root.data)
        res = res + inorderTraversal(root.right)
    return res


def postorderTraversal(root):
    '''
    Returns an array of tree elements using post order traversal.  
    Post order is often used to delete tree elements
    Left-->Right-->Root
    '''
    res=[]
    if root:
        res=postorderTraversal(root.left)
        res = res + postorderTraversal(root.right)
        res.append(root.data)
    
    return res  

def preorderTraversal(root):
    '''
    Returns an array of tree elements using pre order traversal.  
    Pre order is often used to copy a tree
    Root-->Left-->Right
    '''
    res=[]
    if root:
        res.append(root.data)
        res = res + preorderTraversal(root.left)
        res = res + preorderTraversal(root.right)
         
    return res    


def balance_tree(array):
    '''
    Balances an unbalanced binary tree in O(n) time from the inorder traversal
    stored in an array
    steps:
        - Take inorder traversal of existing tree and store in array.
        - Find value at mid point of this array.  
        - create new binary tree using this midpoint as root node.
    '''
    if not array:
        return None
    
    midpoint=len(array)//2
    new_root=Node(array[midpoint])
    new_root.left=balance_tree(array[:midpoint])
    new_root.right=balance_tree(array[midpoint+1:])
    return new_root

'''
# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 


print ("Height of tree is %d" %(maxDepth(root)))
'''

def getLeafCount(node): 
    '''
    Count the number of leaf nodes in a tree
    '''
    if node is None: 
        return 0 
    if(node.left is None and node.right is None): 
        return 1 
    else: 
        return getLeafCount(node.left) + getLeafCount(node.right) 
    
    

def _deepestLeftLeafUtil(root, lvl, maxlvl, isLeft): 
    '''
    # A utility function to find deepest leaf node. 
    # lvl:  level of current node. 
    # maxlvl: pointer to the deepest left leaf node found so far 
    # isLeft: A bool indicate that this node is left child 
    # of its parent 
    # resPtr: Pointer to the result 
    '''
      
    # Base CAse 
    if root is None: 
        return
  
    # Update result if this node is left leaf and its  
    # level is more than the max level of the current result 
    if(isLeft is True): 
        if (root.left == None and root.right == None): 
            if lvl > maxlvl[0] :  
                _deepestLeftLeafUtil.resPtr = root  
                maxlvl[0] = lvl  
                return
  
    # Recur for left and right subtrees 
    _deepestLeftLeafUtil(root.left, lvl+1, maxlvl, True) 
    _deepestLeftLeafUtil(root.right, lvl+1, maxlvl, False) 
  
# A wrapper for left and right subtree 
def deepestLeftLeaf(root): 
    '''
    Used with the above utility function to calculate deepest LEFT leaf
    '''
    maxlvl = [0] 
    _deepestLeftLeafUtil.resPtr = None
    _deepestLeftLeafUtil(root, 0, maxlvl, False) 
    return _deepestLeftLeafUtil.resPtr     


def printRoute(stack, root): 
    '''
    Print all routes down a binary tree
    '''
    if root == None: 
        return
          
    # append this node to the path array 
    stack.append(root.data) 
    if(root.left == None and root.right == None): 
          
        # print out all of its  
        # root - to - leaf 
        print(' '.join([str(i) for i in stack])) 
          
    # otherwise try both subtrees 
    printRoute(stack, root.left) 
    printRoute(stack, root.right) 
    stack.pop() 
    




if __name__=='__main__':

    tree=build_tree(40,0,100)
    tree.display()
    print(tree.size(tree))
    print(tree.is_balanced(tree))
            