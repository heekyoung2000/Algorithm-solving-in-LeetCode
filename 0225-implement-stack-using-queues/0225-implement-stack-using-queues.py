class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next
        
        
class MyStack:

    def __init__(self):
        self.top_node = None
    

    def push(self, x: int) -> None:
        self.top_node = Node(x,self.top_node)
        

    def pop(self) -> int:
        if self.top_node is None:
            return None
        node = self.top_node
        self.top_node = self.top_node.next
        
        return node.item

    def top(self) -> int:
        if self.top_node is None:
            return None
        node = self.top_node
        
        return node.item
        
    def empty(self) -> bool:
        return self.top_node is None
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()