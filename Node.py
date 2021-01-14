class Node:
    def __init__(self, value, _next=None, prev=None):
        self.value = value
        self.next = _next
        self.prev = prev

    def __repr__(self):
        return f"{self.value!r}"

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.value < other.value

        return self.value < other

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.value > other.value

        return self.value > other

    def __str__(self):
        return str(self.value)
