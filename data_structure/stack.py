from double_link_list import DoubleLinkList
class Stack():
    def __init__(self):
        self.__list = DoubleLinkList()

    def push_item(self, value):
        return self.__list.add(value)

    def pop_item(self):
        return self.__list.r

    def __str__(self):
        return self.__list.__str__()
obj = Stack()
obj.push_item(300)
obj.push_item(400)
print(obj)
