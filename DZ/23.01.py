from collections import deque


class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v

    def __str__(self):
        return f"k: {self.k}, v: {self.v}"


class MyDict:
    def __init__(self):
        self.lst = [None for _ in range(10)]
        self.size = 0

    def add(self, k, v):
        index: int = hash(k) % len(self.lst)

        if self.lst[index] is None:
            self.lst[index] = Node(k=k, v=v)
            return

        if isinstance(self.lst[index], deque):
            for item in self.lst[index]:
                if item.k == k:
                    item.v = v
                    return
            self.lst[index].append(Node(k=k, v=v))
            return

        if self.lst[index].k == k:
            self.lst[index].v = v
            return

        temp_lst = deque()
        temp_lst.append(self.lst[index])
        temp_lst.append(Node(k=k, v=v))
        self.lst[index] = temp_lst

    def __str__(self):

        return str(self.lst)

    def get(self, v):
        return (self.lst[v])

    def pop(self, v):
        print((self.lst.pop(v)))
        empty= None
        self.lst.append(empty)
    def clear(self):
        self.lst.clear()
        self.lst = [None for _ in range(10)]



d = {}
d = MyDict()
