"""Implementation of Linked List data structure in Python.

The following implement a singly linked list, to find other types
of linked list, see another files in this directory.

This code includes a list of operations that can be perform on
linked list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"[data: {self.data}, next: {self.next}]"

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        """Insert data at the beginning of linked list"""
        ndata = Node(data)
        ndata.next = self.head
        self.head = ndata

    # man there are a lot of operations to implement, let's call it a day for now

    def __repr__(self):
        s = ""
        tmp_head = self.head
        while tmp_head != None:
            s += f"{tmp_head.data}"
            if tmp_head.next != None:
                s += " -> "
            tmp_head = tmp_head.next
                
        return s

    
if __name__ == "__main__":
    n1 = Node(4)
    n2 = Node(6)
    n3 = Node(7)

    n1.next = n2
    n2.next = n3

    l = LinkedList()
    l.head = n1
    print(l)

    l.push(100)
    print(l)
