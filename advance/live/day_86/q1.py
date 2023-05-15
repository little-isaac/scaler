class Node:
    data = None
    next = None
    def __init__(self,data="") -> None:
        self.data = data
        self.next = None
        pass


class Stack:
    top = None
    def __init__(self) -> None:
        self.top = None
        pass
    def push(self,data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    def pop(self):
        temp = self.top
        if temp is None:
            return None
        self.top = temp.next
        return temp
    def printTop(self):
        if self.top is not None:
            print(self.top.data)
        else:
            print("None")

if __name__ == "__main__":
    stack = Stack()

    stack.printTop()
    stack.push(5)
    stack.printTop()
    stack.push(3)
    stack.printTop()
    stack.push(4)
    stack.printTop()
    print(stack.pop().data)
    stack.printTop()
    print(stack.pop().data)
    stack.printTop()
    print(stack.pop().data)
    stack.printTop()