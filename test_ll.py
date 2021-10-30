from LinkedList import DoublyLinkedList

ll = DoublyLinkedList()
ll.add(2)
print(ll)

ll.append((4, 5, 6))
print(ll)
print(ll[1])

ll[0] = [2, 14]  # ll.__setitem__(0, [2, 14])
print(ll)

del ll[1]  # ll.__delitem__(1)
print(ll)

ll2 = DoublyLinkedList()
ll2.add("abc")

print(ll + ll2)
print(ll2 + ll)
