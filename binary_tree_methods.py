
#Standard python library imports
import random

#Local imports
from binary_trees_class import Node

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


def build_tree_from_array(arr):
    if arr:
        root=Node(arr.pop(0))
        for _ in range(len(arr)):
            root.insert(arr.pop(0))
        return root


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


def inorder_traversal(root):
    '''
    Return an array of tree elements using inorder traversal.  
    In-order traversal = Left-->Root-->Right
    '''
    res = []
    if root:
        res = inorder_traversal(root.left)
        res.append(root.data)
        res = res + inorder_traversal(root.right)
    return res


def postorder_traversal(root):
    '''
    Returns an array of tree elements using post order traversal.  
    Post order is often used to delete tree elements.
    Post-order traversal = Left-->Right-->Root
    '''
    res=[]
    if root:
        res=postorder_traversal(root.left)
        res = res + postorder_traversal(root.right)
        res.append(root.data)
    
    return res  

def preorder_traversal(root):
    '''
    Returns an array of tree elements using pre order traversal.  
    Pre order is often used to copy a tree
    Pre-order traversal = Root-->Left-->Right
    '''
    res=[]
    if root:
        res.append(root.data)
        res = res + preorder_traversal(root.left)
        res = res + preorder_traversal(root.right)
         
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


def get_leaf_count(node): 
    '''
    Count the number of leaf nodes in a tree.

    Parameters:
    ___________
    node : object
        a binary tree object
    '''
    if node is None: 
        return 0 
    if(node.left is None and node.right is None): 
        return 1 
    else: 
        return get_leaf_count(node.left) + get_leaf_count(node.right) 
    
    
def _deepest_left_leaf_util(root, level, max_level, is_left): 
    '''
    A utility function to find deepest leaf node. 

    Parameters:
    ___________

    level : int 
        level of current node. 
    max_level : object 
        pointer to the deepest left leaf node found so far. 
    is_left : bool 
        indicates that this node is left child of its parent or not.
    result_pointer : object 
        Pointer to the result. 
    '''
      
    # Base Case 
    if root is None: 
        return
  
    # Update result if this node is left leaf and its  
    # level is more than the max level of the current result 
    if(is_left is True): 
        if (root.left == None and root.right == None): 
            if level > max_level[0] :  
                _deepest_left_leaf_util.result_pointer = root  
                max_level[0] = level  
                return
  
    # Recur for left and right subtrees 
    _deepest_left_leaf_util(root.left, level+1, max_level, True) 
    _deepest_left_leaf_util(root.right, level+1, max_level, False) 
  

def deepest_left_leaf(root): 
    '''
    Used with the above utility function to calculate deepest LEFT leaf
    '''
    max_level = [0] 
    _deepest_left_leaf_util.result_pointer = None
    _deepest_left_leaf_util(root, 0, max_level, False) 
    return _deepest_left_leaf_util.result_pointer  


def print_route(stack, root): 
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
    print_route(stack, root.left) 
    print_route(stack, root.right) 
    stack.pop() 
    




if __name__=='__main__':

    

    
    tree01=build_tree_from_array(arr)
    tree01.display()
    tree=build_tree(40,0,100)
    tree.display()
    print(size(tree))
    print(is_balanced(tree))
    print(deepest_left_leaf(tree).data)
            