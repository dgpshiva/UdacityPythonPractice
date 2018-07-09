"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position <= 0:
            return None
        else:
            current = self.head
            if self.head:
                for i in range(1, position+1):
                    if i == position:
                        return current
                    current = current.next
                    if current == None:
                        return None
            else:
                return None


    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        if position <= 0:
            pass
        else:
            if position == 1:
                new_element.next = self.head
                self.head = new_element
            else:
                current = self.head
                if self.head:
                    for i in range(1, position-1):
                        current = current.next
                        if current == None:
                            return
                    new_element.next = current.next
                    current.next = new_element


    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if self.head:
            if current.value == value:
                self.head = current.next
            else:
                while current.next != None and current.next.value != value:
                    current = current.next
                if current.next != None:
                    current.next = current.next.next


    def display(self):
        current = self.head
        if self.head:
            print current.value
            while current.next:
                current = current.next
                print current.value

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

#ll.display()

# Test insert
ll.insert(e4, 3)
#ll.display()
# Should print 4 now
print ll.get_position(3).value

# Test delete
#ll.display()
ll.delete(1)
#ll.display()
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value