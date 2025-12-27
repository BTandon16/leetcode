class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    # Implement the LRUCache class:
    # LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    # int get(int key) Return the value of the key if the key exists, otherwise return -1.
    # void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
    # If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    # The functions get and put must each run in O(1) average time complexity.

    head = None
    tail = None

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        currNode = self.head
        while (currNode is not None):
            if (currNode.key == key):
                # UPDATING CACHE
                if (currNode == self.head or currNode == self.tail):
                    if (currNode != self.head):
                        # If currNode is only the tail, no changes needed to cache
                        return currNode.value
                    elif (currNode != self.tail):
                        # If currNode is the head but not tail, then set the next of currNode as the new head
                        currNode.next.prev = None
                        self.head = currNode.next
                    else:
                        # If currNode is both head and tail, no changes needed to cache
                        return currNode.value
                else:
                    # Remove the currNode from its position in the list
                    currNode.prev.next = currNode.next
                    currNode.next.prev = currNode.prev
                # Put currNode at the tail of the list
                self.tail.next = currNode
                currNode.prev = self.tail
                currNode.next = None
                self.tail = currNode

                return currNode.value
            else:
                currNode = currNode.next
        return -1
    
    def put(self, key: int, value: int) -> None:
        if (self.capacity == 0):
            return

        currNode = self.head
        count = 0
        while (currNode is not None):
            count += 1
            if (currNode.key == key):
                currNode.value = value
                # UPDATING CACHE
                if (currNode == self.head or currNode == self.tail):
                    if (currNode != self.head):
                        # If currNode is only the tail, no changes needed to cache
                        return currNode.value
                    elif (currNode != self.tail):
                        # If currNode is the head but not tail, then set the next of currNode as the new head
                        currNode.next.prev = None
                        self.head = currNode.next
                    else:
                        # If currNode is both head and tail, no changes needed to cache
                        return currNode.value
                else:
                    # Remove the currNode from its position in the list
                    currNode.prev.next = currNode.next
                    currNode.next.prev = currNode.prev
                # Put currNode at the tail of the list
                self.tail.next = currNode
                currNode.prev = self.tail
                currNode.next = None
                self.tail = currNode

                return
            else:
                currNode = currNode.next
        
        newNode = Node(key, value)
        # Remove the head if capacity is reached (head is least recently used)
        if (count == self.capacity):
            if (self.capacity != 1):
                self.head = self.head.next
            else:
                self.head = newNode
                self.tail = newNode
                return
        # Add the new node at the tail of the list
        if (count != 0):
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
        return

# lRUCache = LRUCache(2)
# lRUCache.put(2, 1)
# lRUCache.put(1, 1)
# lRUCache.put(2, 3)
# lRUCache.put(4, 1)
# lRUCache.get(1)
# lRUCache.get(2)