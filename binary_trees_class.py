

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
        """Returns list of strings, width, height, and horizontal coordinate of the root. this is 
           a utility function that gets used by the <display()> method for building pretty stdout 
           visualization of the binary tree. """

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

        # Two children exist.
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



