class Node: 
    def __init__(self, data=None, next= None):
        self.data = data 
        self.next = next
    

class LinkedList: 
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode 
        self.length = 1
        
    def insert_at_end(self, data): 
        newNode = Node(data)
        if self.head is None: 
            self.head = newNode 
            self.tail = newNode
        else: 
            self.tail.next = newNode
            self.tail = newNode 
        self.length += 1 
        return self 
        
    def remove_at_end(self):
        if self.head is None: 
            print("The linked list is empty")
            return

        temp = self.head
        pre = self.head

        while temp.next: 
            pre = temp
            temp = temp.next 
        self.tail = pre 
        self.tail.next = None
        self.length -= 1 
        
        if self.length == 0:
            self.head = None 
            self.tail = None 
        return temp

    def unshift(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return self

        new_node.next = self.head 
        self.head = new_node

        return self
    
    def shift(self):

        if self.head is None:
            print("The linked list is empty")
            return 
        
        temp = self.head 
        self.head = self.head.next
        self.length -= 1 
        
        if not self.head: 
            self.head = None 
            self.tail = None 
            print("No more element")

        temp.next = None
        return self
            
    def __repr__(self):
        current_node = self.head
        linked = ""
        while current_node:
            current_data = str(current_node.data)
            if current_node.next:
                current_data += "-->"
                linked += str(current_data) 

            else:
                linked += str(current_data)

            current_node = current_node.next

        return linked

linked = LinkedList(1)
linked.insert_at_end(2)
linked.insert_at_end(3)
for i in range(4, 11):
    linked.insert_at_end(i)
linked.remove_at_end()
linked.unshift(10)
linked.shift()

new = LinkedList(1)
new.shift()
print(linked)
print(new)