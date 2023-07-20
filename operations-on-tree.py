from collections import defaultdict

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = defaultdict(set)
        self.children = defaultdict(list)

        for i, p in enumerate(parent):
            if p != -1:
                self.children[p].append(i)

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False

        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked and self.locked[num] == user:
            self.locked.pop(num, None)
            return True

        return False

    def upgrade(self, num: int, user: int) -> bool:
        def has_locked_descendant(node):
            for child in self.children[node]:
                if child in self.locked or has_locked_descendant(child):
                    return True
            return False

        def has_locked_ancestor(node):
            while node != -1:
                if node in self.locked:
                    return True
                node = self.parent[node]
            return False

        if num in self.locked:
            return False

        if has_locked_ancestor(num) or not has_locked_descendant(num):
            return False

        def unlock_descendants(node):
            for child in self.children[node]:
                if child in self.locked:
                    self.locked.pop(child)
                unlock_descendants(child)

        unlock_descendants(num)
        self.locked[num] = user
        return True