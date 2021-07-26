class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
            else data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
         else:
            self.data = data

    def printSelf(self):
        # Your code goes here
      if self.left:
         self.left.printSelf()
      return self.value
      if self.right:
         self.right.printSelf()
        
    def search(self, find_val):
        # Your code goes here
      if lkpval < self.data:
         if self.left is None:
            return str(lkpval)+" Not Found"
         return self.left.findval(lkpval)
       else if lkpval > self.data:
            if self.right is None:
               return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

