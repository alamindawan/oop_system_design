class Node:
   def __init__(self, value):
       self.next = None
       self.prev = None
       self.val = value

class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        node = Node(val)

        if self.head is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"


obj = DoubleLinkList()
obj.add(10)
obj.add(100)
obj.add(1000)
print(obj)
obj.remove(100)
print(obj)


