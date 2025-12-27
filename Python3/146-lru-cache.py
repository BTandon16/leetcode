# Node class for Nodes in a doubly linked list (for maintaining LRU Cache)
class Node:
    def __init__(self, key:int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    # Implement the LRUCache class:
    # The functions get and put must each run in O(1) average time complexity.

    # LRUCache(int capacity) Initialize the LRU cache with positive size capacity
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Dictionary with a key:Node pair instead of the key:value
        self.dict = dict()

        # Initialize the doubly linked list
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    # int get(int key) Return the value of the key if the key exists, otherwise return -1.
    def get(self, key: int) -> int:
        currNode = self.dict.get(key)
        # Check if the key exists
        if (currNode is None):
            return -1
        # Update cache because this key was accessed
        self.removeNode(currNode)
        self.addNode(currNode)
        return currNode.value

    # void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
    # If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        currNode = self.dict.get(key)
        # Check if the key exists
        if (currNode is not None):
            # Update the doubly linked list with the new node as most recently accessed, remove the old node
            self.removeNode(currNode)
            self.addNode(newNode)
            # Update the node in the dictionary
            self.dict[key] = newNode
        else:
            if self.capacity != len(self.dict.keys()):
                # Add node to the doubly linked list
                self.addNode(newNode)
                # Add a new dictionary key-Node pair
                self.dict[key] = newNode
            else:
                self.dict.pop(self.tail.prev.key)
                self.removeNode(self.tail.prev)

                self.addNode(newNode)
                self.dict[key] = newNode
    
    def addNode(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node: Node) -> None:
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

# lRUCache = LRUCache(2)
# lRUCache.put(2, 1)
# lRUCache.put(1, 1)
# lRUCache.put(2, 3)
# lRUCache.put(4, 1)
# lRUCache.get(1)
# lRUCache.get(2)