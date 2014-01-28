"""Tree data structure using Object Oriented Desgine."""


class BinaryTree(object):
  """Binary Tree Class, contains root, left child and right child."""

  def __init__(self, root_obj, left=None, right=None):
    self.root = root_obj
    self._left = left
    self._right = right

  def GetRoot(self):
    return self.root

  def GetLeft(self):
    return self._left

  def GetRight(self):
    return self._right

  def SetRoot(self, root_obj):
    self.root = root_obj

  def SetRight(self, right_tree):
    if not isinstance(right_tree, BinaryTree):
      raise TypeError('value supplied must be instance of BinaryTree')
    else:
      self._right = right_tree

  def SetLeft(self, left_tree):
    if not isinstance(left_tree, BinaryTree):
      raise TypeError('value supplied must be instance of BinaryTree')
    else:
      self._left = left_tree

  def AddLeft(self, left_root_obj):
    new_left = BinaryTree(left_root_obj)
    if self._left is None:
      self._left = new_left
    else:
      left = self._left
      self._left = new_left
      new_left.SetLeft(left)

  def AddRight(self, right_root_obj):
    new_right = BinaryTree(right_root_obj)
    if self._right is None:
      self._right = new_right
    else:
      right = self._right
      self._right = new_right
      self._right.SetRight(right)
