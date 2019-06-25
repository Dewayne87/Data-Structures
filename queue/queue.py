class Node:
  def __init__(self,value,next_node= None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self,node):
    self.next_node = node

class LinkedList:
  def __init__(self,head=None,tail=None):
    self.head = head
    self.tail = tail

  def add_to_head(self,node):
    newNode = Node(node)
    if self.head == None:
      self.head = newNode
      self.tail = self.head
    else:
      newNode.set_next_node(self.head)
      self.head = newNode

  def add_to_tail(self,node):
    newNode = Node(node)
    if self.head == None:
      self.head = newNode
      self.tail = self.head
    else:
      self.tail.set_next_node(newNode)
      self.tail = newNode

  def remove_from_head(self):
    value = None
    if self.head == None:
      value = None
    elif self.head == self.tail:
      value = self.head.get_value()
      self.head = None
      self.tail = None
    else:
      value = self.head.get_value()
      self.head = self.head.get_next_node()
    return value
    
class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    self.size += 1
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    if self.size == 0:
      return None
    else:
      self.size -= 1
      return self.storage.remove_from_head()
      
    
  def len(self):
    return self.size

