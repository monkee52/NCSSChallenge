# Enter your code for "Graph nOOde" here.
class Node:
  def __init__(self, id, label):
    self.id = id
    self.label = label
    self.neighbours = []
  def __str__(self):
    return "(%d: %s)" % (self.id, self.label)
  def add_neighbour(self, neighbour, label):
    self.neighbours.append((label, neighbour))
  def get_neighbours(self, label):
    o = []
    
    if (label == None):
      for i in self.neighbours:
        o.append(i[1])
    else:
      for i in self.neighbours:
        if (i[0] == label):
          o.append(i[1])
    
    return o
  def degree(self, label):
    if (label == None):
      return len(self.neighbours)
    
    o = 0
    
    for i in self.neighbours:
      if (i[0] == label):
        o += 1
    
    return o
  def has_neighbour(self, node, label):
    for i in self.neighbours:
      if ((label == None or label == i[0]) and i[1] == node):
        return True
    
    return False
