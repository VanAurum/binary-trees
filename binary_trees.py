#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 08:27:44 2019

@author: vanaurum
"""
import random
import sys
import time



class Node:
    """This class is a full implementation of a binary tree with methods for executing a wide variety 
       of binary tree operations.

       Attributes:
       ___________
       data : int, str
            The value that exists at this node of the tree.  eg. tree=Node(4) initializes a tree with 
            a stump integer value of 4.
    """

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data == data:
            return
        elif self.data < data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else: # self.data > data
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)


    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child exists.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child exists.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child exists.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def build_tree(n,min_num,max_num,start=None):
    if start:
        initial=start
    else:
        initial=random.randint(min_num,max_num)
    root=Node(initial)
    for _ in range(n-1):
        root.insert(random.randint(min_num,max_num))
    return root    


def is_balanced(root):
    '''
    A binary tree is balanced if:
        - it's empty
        - the left sub tree is balanced
        - the right subtree is balanced
        - the difference in depth between left and right is <=1
    '''
    if root is None: 
        return True
    return is_balanced(root.right) and is_balanced(root.left) and abs(get_height(root.left) - get_height(root.right)) <= 1   
        
               
def get_height(root):
    '''
    Return the maxium depth of the tree
    '''
    if root is None: 
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))        


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
    
    

def size(node): 
    '''
    Compute the total number of nodes in a tree
    '''
    if node is None: 
        return 0 
    else: 
        return (size(node.left)+ 1 + size(node.right))     