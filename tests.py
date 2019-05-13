#Standard python library imports
import unittest

#Local imports
from binary_trees_class import Node
import binary_tree_methods as btm


class TestTreeMethods(unittest.TestCase):
    
    def setUp(self):
        self.arr01=[7,2,34,55,6,7,8,6,5,3,32,4,5,6,6,3,5,6,778,34]
        self.arr02=[18,34,56,12,4,6,88,9,5,67,77,101,234,1,2,3,6,34,35,2,5]
        self.tree01=btm.build_tree_from_array(self.arr01)
        self.tree02=btm.build_tree_from_array(self.arr02)
        self.tree01.display()
        self.tree02.display()

    def test_size_method(self):
        self.assertEqual(btm.size(self.tree01),11)
        self.assertEqual(btm.size(self.tree02),17)


    def test_deepest_left_leaf(self):
        self.assertEqual(btm.deepest_left_leaf(self.tree01),None)
        self.assertEqual(btm.deepest_left_lead(self.tree02),5)

if __name__=='__main__':

    suite=unittest.defaultTestLoader.loadTestsFromTestCase(TestTreeMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)    
    arr01=[7,2,34,55,6,7,8,6,5,3,32,4,5,6,6,3,5,6,778,34]
    arr02=[18,34,56,12,4,6,88,9,5,67,77,101,234,1,2,3,6,34,35,2,5]
    tree01=btm.build_tree_from_array(arr01)
    tree02=btm.build_tree_from_array(arr02)
    tree01.display()
    tree02.display()
    print(btm.deepest_left_leaf(tree01))
    print(btm.deepest_left_leaf(tree02).data)
    print(btm.size(tree02))
