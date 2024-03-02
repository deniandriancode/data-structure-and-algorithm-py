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

    def append(self, data):
        """Insert data at the end of linked list"""
        node = Node(data)
        o_head = self.head
        while True:
            if self.head == None:
                self.head = node
                break
            elif self.head.next == None:
                self.head.next = node
                self.head = o_head
                break

            self.head = self.head.next


    def insert(self, data, index): # this is more challanging than I thought
        """Insert data at index"""
        if index > self.__len__() or index < 0:
            raise IndexError("index out of bound")

        i = 0
        o_head = self.head
        prev_node = None

        while True:
            if index == i and index == 0:
                node = Node(data)
                node.next = self.head
                self.head = node
                break
            elif index == i:
                node = Node(data)
                prev_node.next = node
                node.next = self.head
                self.head = o_head
                break

            prev_node = self.head
            self.head = self.head.next
            i += 1

    def search(self, data):
        """Return index of first occurence, else return -1"""
        i = 0
        tmp_node = self.head
        while tmp_node != None:
            if tmp_node.data == data:
                return i
            
            tmp_node = tmp_node.next
            i += 1

        return -1

    def delete(self, index):
        """Delete item at index"""
        if index < 0 or index >= self.__len__():
            raise IndexError("index out of bound")
        if index == 0:
            self.head = self.head.next
            return
        
        o_head = self.head
        prev_node = None
        i = 0
        while self.head != None:
            if i == index:
                prev_node.next = self.head.next
                self.head = o_head
                return
            
            prev_node = self.head
            self.head = self.head.next
            i += 1

    def get(self, index):
        """Get item at index from linked list"""
        i = 0
        tmp = self.head
        while tmp != None:
            if i == index:
                return tmp

            i += 1
            tmp = tmp.next

        return None

    def reverse(self):
        """Return a new reversed linked list"""
        rev = self
        head = self.head

        curr = head
        prev = None
        next = None

        while curr != None:
            next = curr.next
            curr.next = prev # here we got the rotation, that's pretty cool
            prev = curr
            curr = next

        head = prev
        rev.head = head
        return rev

    def reverse_rec(self, head):
        """Reverse linked list using recursion""" # duh
        if head == None or head.next == None:
            return head

        revs = self.reverse_rec(head.next)

        head.next.next = head # here we got the rotation
        head.next = None # bro how is this thing even work!?

        return revs

    def __len__(self):
        i = 0
        o_head = self.head
        while o_head != None:
            i += 1
            o_head = o_head.next
            
        return i

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
    l = LinkedList()
    l.insert(1, 0)
    l.append(6)
    l.append(5)
    l.append(7)
    # print(l)

    l.append(100)
    print(l)

    # print(l.size)
    l.insert(9, 4)
    print(l)

    # print(l.search(59))
    # print(len(l))

    # l.delete(6) # error
    l.delete(0)
    print(l)

    rev = l.reverse_rec(l.head)
    print(rev)
