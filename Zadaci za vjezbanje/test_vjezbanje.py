'''
class Queue:
    def __init__(self):
        self.items = []
        self.size = 0
    
    def enqueue(self, item):
        self.size = self.size + 1
        return self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            self.size = self.size - 1
            return self.items.pop(0)
    
    def is_empty(self):
        return self.size == 0

    def first(self):
        if not self.is_empty():
            return self.items[0]
    
    def get_queue(self):
        return self.items

    def __len__(self):
        return self.size
    def peek(self):
        if len(self.items) > 0:
             return self.items[0].value

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    def _insert(self, data, current_node):
        if data < current_node.value:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.value:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, '')
        elif traversal_type == 'levelorder':
            return self.levelorder_print(self.root, '')
        else:
            return 'Invalid traversal type'

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + '->')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '->')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + '->')
        return traversal        

    def levelorder_print(self, start, traversal):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ''
        while len(queue) > 0:
            traversal += str(queue.peek()) + '->'
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def find(self, data):
        is_found = False
        if self.root:
            is_found = self._find(data, self.root)
            
            return is_found
        else:
            return None

    def _find(self, data, current_node):
        if data == current_node.value:
            return True
        if data > current_node.value and current_node.right:
            return self._find(data, current_node.right)
        if data < current_node.value and current_node.left:
            return self._find(data, current_node.left)

    def min_val_node(self, node):
        current = node
        while current.left :
            current = current.left
        return current
    def min(self):
        if self.root:
            return self.min_val_node(self.root)

#6 vjezbe, 57:32'

    def delete_node(self, current, data):
        if current is None:
            return current
        if data < current.value:
            current.left = self.delete_node(current.left, data)
        elif data > current.value:
            current.right = self.delete_node(current.right, data)
        else:
            if current.left is None:
                temp = current.right
                current = None
                return temp
            elif current.right is None:
                temp = current.left
                current = None
                return temp
            
            temp = self.min_val_node(current.right)
            current.value = temp.value
            current.right = self.delete_node(current.right, temp.value)
        return current

    def _size(self, current):
        if current is None:
            return 0
        else:
            return self._size(current.left) + self._size(current.right) +1
    def size(self):
        return self._size(self.root)

    def _get_num_leaf(self, current):
        if not current:
            return 0
        else: 
            if not current.left and not current.right:
                return 1
            else:
                return self._get_num_leaf(current.left) + self._get_num_leaf(current.right)
    def get_num_leaf(self):
        return self._get_num_leaf(self.root)
#odraditi stampanje lef elemenata
    

bin_tree = BinaryTree(6)
bin_tree.insert(3)
bin_tree.insert(7)
bin_tree.insert(2)
bin_tree.insert(5)
bin_tree.insert(9)

#print(bin_tree.print_tree('preorder'))
#print(bin_tree.print_tree('inorder'))
#print(bin_tree.print_tree('postorder'))
print(bin_tree.print_tree('levelorder'))
#print(bin_tree.find(10))
#print(bin_tree.min_val_node(bin_tree.root).value)
print('****')
#bin_tree.delete_node(bin_tree.root, 6)
print(bin_tree.get_num_leaf())
'''
'''
def is_sorted(l):
    if l == sorted(l):
        return True
    else:
        return False

print(is_sorted(['c','b']))
a = ['b', 'a', 'c']
#print(a.sort())
'''
print('a1' > 'a2')