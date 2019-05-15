# Binary Trees
This is a master class with pretty-print output that I created for people who are interested in learning about binary trees and how all the different functionality can behave!

## Method list
* __build_tree__ 
* __size__
* __is_balanced__
* __get_height__
* __build_tree_from_array__
* __inorder_traversal__
* __postorder_traversal__
* __preorder_traversal__
* __balance_tree__
* __get_leaf_count__
* __print_route__
* __get_deepest_left_leaf__

___



### build_tree
Builds a binary tree of size __n__ by drawing random numbers 
between __min_nim__ and __max_num__.  You can also specify an optiona __start__ value to be the stump node.

### Output:
```
   ________________________68___________     
  /                                     \    
  5_____                           ____95___ 
 /      \                         /         \
 4   __18___                     78_       99
/   /       \                   /   \     /  
1  13_     35_____             76  82_   98  
      \   /       \           /       \      
     17  31      42___       75      94      
                /     \                      
               40    53_                     
              /     /   \                    
             39    52  58_                   
                          \                  
                         67                  
Tree size: 24
Tree balanced? False
Deepest left leaf: 39
Tree height :8
In-order traversal:  [1, 4, 5, 13, 17, 18, 31, 35, 39, 40, 42, 52, 53, 58, 67, 68, 75, 76, 78, 82, 94, 95, 98, 99]
Post-order traversal : [1, 4, 17, 13, 31, 39, 40, 52, 67, 58, 53, 42, 35, 18, 5, 75, 76, 94, 82, 78, 98, 99, 95, 68]
Number of leafs: 9
Deepest left leaf: 39
```


