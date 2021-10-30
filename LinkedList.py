from collections.abc import Iterable
from typing import Optional
from Node import Node
import copy


class DoublyLinkedList:

    def __init__(self, value=None, *, iterable=True, return_nodes=False):
        """
        :param value: value to add to the linked list, if iterable loop through and each piece of data unless iterable
        is set to False
        :param iterable: set this to False if initializing using an iterable and you want it to be stored in one node
        :type iterable: Boolean
        :param return_nodes: set this to True if you want to return the Nodes instead of the value
        :type return_nodes: Boolean
        """
        self.head = self.last = self.current = None
        self.return_nodes = return_nodes
        self.len = 0
        if value:
            if iterable:
                self.extend(value)
            else:
                self.add(value)

    def add(self, obj) -> None:
        """Add an item to the list"""
        last = Node(obj, prev=self.last)
        if self.head is None:
            self.head = last
        if self.last is not None:
            self.last.next = last
        self.last = last
        self.len += 1

    def append(self, obj) -> None:
        """Append an object to the linked list"""
        self.add(obj)

    def index(self, obj, start: int = 0, end: int = None) -> Optional[int]:
        """:returns: the first index of the value in the list, None if not found"""
        end = end or self.len
        if start > end or start > self.len - 1 or end < 1:
            return None

        index = 0
        head = self.head
        while head is not None:
            if head.value == obj:
                return index
            index += 1
            head = head.next
        return None

    def get(self, index: int) -> Node:
        """:returns: the node from the index"""
        count = 0
        obj = self.head
        index = index if index >= 0 else self.len + index

        if index == self.len - 1:
            return self.last

        if index < 0 or index > self.len - 1:
            raise IndexError("list index out of range")

        while True:
            if count == index:
                return obj
            obj = obj.next
            count += 1

    def count(self, obj) -> int:
        """:returns: the number of times the object appears in the list"""
        count = 0
        item = self.head
        while item is not None:
            if item.value == obj:
                count += 1
            item = item.next
        return count

    def clear(self) -> None:
        """Remove all items from the list"""
        self.head = None
        self.len = 0

    def copy(self):
        """:returns: a copy of the list"""
        new_list = DoublyLinkedList(return_nodes=self.return_nodes)
        item = self.head
        while item is not None:
            new_list.add(item)
            item = item.next
        return new_list

    def pop(self, index: int = None):
        """Remove an item from the index and return it"""
        if self.head is None:
            raise IndexError("pop from empty Linked List")

        if index is None or index == self.len - 1 or index == -1:
            item = self.last
            if self.last.prev is None:
                self.head = None
            else:
                self.last.prev.next = None
            self.last = self.last.prev

        elif index == 0 or index == -self.len:
            item = self.head
            self.head = self.current = self.head.next
        else:
            item = obj = self.get(index)
            obj.prev.next = obj.next
        self.len -= 1
        return item.value

    def reverse(self) -> None:
        """Reverses the list"""
        curr = self.head
        new_list = DoublyLinkedList(return_nodes=self.return_nodes)
        while curr is not None:
            new_list.insert(0, curr)
            curr = curr.next
        self.clear()
        self.extend(new_list)

    def insert(self, obj, index: int) -> None:
        """Insert an object at a specified index"""
        if isinstance(obj, Node):
            obj = obj.value
        if index == 0:
            self.add(obj)
            return
        if index == self.len:
            self.append(obj)
            return
        node = self.get(index)
        prev = node.prev
        new = Node(obj, node, prev)
        prev.next, node.previous = new, new
        self.len += 1

    def extend(self, iterable: Iterable) -> None:
        """Extend list by adding elements from an iterable."""
        if isinstance(iterable, DoublyLinkedList):
            if self.len > 0:
                self.head.next = iterable.head
            else:
                self.head = iterable.head
            self.len += iterable.__len__()
        else:
            for item in iterable:
                self.append(item)

    def __len__(self) -> int:
        """:returns: len(self)."""
        return self.len

    def __repr__(self) -> str:
        """:returns: repr(self)"""
        return f"Linked List Object Containing: [{', '.join(str(i) for i in self)}]"

    def remove(self, obj) -> None:
        """:returns: first occurrence of value."""
        if self.head.data == obj:
            self.head = self.head.next
            self.current = self.head
        else:
            item = self.head
            while item is not None:
                if item.data == obj:
                    item.prev.next = item.next
                    if item.next is None:
                        self.last = self.last.prev
                    break
                item = item.next
            else:
                return
        self.len -= 1

    def sort(self, *, key=None, reverse: bool = False) -> None:
        """Sort in place."""
        if key is None:
            new = DoublyLinkedList(sorted(self.copy(), reverse=reverse), return_nodes=self.return_nodes)
        else:
            new = DoublyLinkedList(sorted(self.copy(), key=key, reverse=reverse), return_nodes=self.return_nodes)
        self.clear()
        self.extend(new)

    def __iter__(self) -> None:
        """Implement iter(self)"""
        item = self.head
        if self.return_nodes:
            while item is not None:
                yield item
                item = item.next
        else:
            while item is not None:
                yield item.value
                item = item.next

    def __add__(self, other):
        """:returns: self + other."""
        old = DoublyLinkedList(self.copy(), return_nodes=self.return_nodes)
        self.extend(other)
        new = self.copy()
        self.clear()
        self.extend(old)
        return new

    def __deepcopy__(self, memo={}):

        lst = DoublyLinkedList()
        item = self.head
        while item is not None:
            lst.append(copy.deepcopy(item.value))
            item = item.next
        return lst

    def __radd__(self, other):
        """:returns: other + self"""
        old = DoublyLinkedList(self.copy(), return_nodes=self.return_nodes)
        self.clear()
        self.extend(other)
        self.extend(old)
        new = self.copy()
        self.clear()
        self.extend(old)
        return new

    def __mul__(self, other):
        """:returns: self * other"""
        new_list = DoublyLinkedList(return_nodes=self.return_nodes)
        for i in range(abs(other)):
            new_list.extend(self.copy())

        if other < 0:
            new_list.reverse()

        return new_list

    def __contains__(self, item) -> bool:
        """:returns: item in self."""
        for node in self:
            if node == item or node.data == item:
                return True
        return False

    def __gt__(self, other) -> bool:
        """:returns: self > other"""
        if not isinstance(other, (list, DoublyLinkedList)):
            raise TypeError(f"'>' not supported between instances of 'DoublyLinkedList' and '{type(other).__name__}'")

        for x, y in zip(self, other):
            if x > y:
                return True
            else:
                return False

        return self.len > len(other)

    def __lt__(self, other) -> bool:
        """:return self < other """
        if not isinstance(other, (list, DoublyLinkedList)):
            raise TypeError(f"'<' not supported between instances of 'DoublyLinkedList' and '{type(other).__name__}'")

        for x, y in zip(self, other):
            if x < y:
                return True
            else:
                return False

        return self.len < len(other)

    def __ge__(self, other) -> bool:
        """:returns: self >= other"""
        if not isinstance(other, (list, DoublyLinkedList)):
            raise TypeError(f"'>=' not supported between instances of 'DoublyLinkedList' and '{type(other).__name__}'")

        for x, y in zip(self, other):
            if x < y:
                return False

        return self.len >= len(other)

    def __le__(self, other) -> bool:
        """:returns: self <= other"""
        if not isinstance(other, (list, DoublyLinkedList)):
            raise TypeError(f"'<=' not supported between instances of 'DoublyLinkedList' and '{type(other).__name__}'")

        for x, y in zip(self, other):
            if x > y:
                return False

        return self.len <= len(other)

    def __eq__(self, other) -> bool:
        """:returns: self == other."""

        if isinstance(other, Iterable) and self.len == len(other):
            if other in self and self in other:
                return True
            for a, b in zip(self, other):
                if a != b:
                    return False
            return True
        return False

    def __ne__(self, other) -> bool:
        """:returns: self != other"""
        return not self.__eq__(other)

    def __bool__(self) -> bool:
        """:returns: bool(self)"""
        return self.head is not None

    def __getitem__(self, item):
        """:returns: x.__getitem__(y) <==> x[y]."""
        if isinstance(item, int):
            return self.get(item)
        elif isinstance(item, slice):
            start = item.start or 0
            stop = item.stop or self.len
            step = item.step or 1
            if not all(isinstance(int, i) for i in (start, stop, step)):
                raise TypeError("only type 'int' is acceptable")
            if start < 0:
                start = self.len + start
            if stop < 0:
                stop = self.len + stop
            if step < 0:
                rev = True
                step = -step
            else:
                rev = False
            lst = DoublyLinkedList()
            for i, x in enumerate(self):
                if start <= i < stop and (i + start) % step == 0:
                    lst.append(x)
            if rev:
                return reversed(lst)
            return lst
        else:
            raise TypeError('Invalid index type given (accepted indexes: int, slice)')

    def __setitem__(self, key, value):
        """Set self[key] to value"""
        if not isinstance(key, int):
            raise TypeError('list indices must be integers or slices, not str')
        self.get(key).value = value

    def __delitem__(self, key):
        """Delete self[key]"""
        if not isinstance(key, int):
            raise TypeError('list indices must be integers or slices, not str')
        self.pop(key)

    def __reversed__(self):
        """:returns: reversed(self)."""
        new_list = DoublyLinkedList(self.copy(), return_nodes=self.return_nodes)
        new_list.reverse()
        return new_list

    def __next__(self):
        """Implement next(iter)"""
        if self.current is None or self.head is None:
            raise StopIteration

        current = self.current
        self.current = self.current.next
        return current.data
