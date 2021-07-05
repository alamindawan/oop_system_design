class Node:
    def __init__(self, value):
        self.next = None
        self.val = value

class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(item) for item in vals)}]"

obj = SingleLinkList()
obj.add('A')
obj.add('B')
print(obj)