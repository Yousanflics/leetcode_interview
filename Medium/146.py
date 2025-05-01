# LRU cache

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # self 是一定要写的
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    
    def put(self, key:int, val: int) -> None:
        # 这里的 self 也是
        # 如果已经在 cache 中就要调整，放到最前面来
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = val
        if len(self.cache) > self.cap:
            # last = False 意味着从头部也就是最早插入的 key 开始 pop
            self.cache.popitem(last=False)


### 双向链表的实现，实现 LRU

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCacheN:
    def __init__(self, capacity):
        self.cache = {} # 哈希表
        self.cap = capacity

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    # 添加节点到链表尾部（变成最新的）
    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
    
    # 删除任意节点
    def _remove(self, node):
        prev = node.pre
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _move_to_end(self, node):
        self._remove(node)
        self._add(node) 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_end(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_end(node)
        else:
            if len(self.cache) >= self.cap:
                lruNode = self.head.next
                self._remove(lruNode)
                del self.cache[lruNode.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)

