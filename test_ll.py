from LinkedList import DoublyLinkedList

ll2 = DoublyLinkedList()
ll2.add(2)
print(ll2)

ll2.append((4, 5, 6))
print(ll2)
print(ll2[1])

ll2.__setitem__(0, [2, 14])
print(ll2)

ll2.__delitem__(1)
print(ll2)
