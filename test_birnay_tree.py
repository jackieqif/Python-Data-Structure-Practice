"""unit tests for binary_tree class."""

import unittest

import binary_tree


class Tests(unittest.TestCase):
  """test cases for binary_tree."""

  def setUp(self):
    self.tree = binary_tree.BinaryTree('root')

  def testClassInit(self):
    self.assertIsInstance(self.tree, binary_tree.BinaryTree)
    self.assertEqual(self.tree.root, 'root')
    self.assertEqual(self.tree._left, None)
    self.assertEqual(self.tree._right, None)

  def testGetRoot(self):
    self.assertEqual(self.tree.GetRoot(), 'root')

  def testGetLeft(self):
    self.assertEqual(self.tree.GetLeft(), None)

  def testGetRight(self):
    self.assertEqual(self.tree.GetRight(), None)

  def testSetRoot(self):
    self.tree.SetRoot('New Root')
    self.assertEqual(self.tree.GetRoot(), 'New Root')

  def testSetLeft(self):
    self.tree.SetLeft(binary_tree.BinaryTree('new_left'))
    self.assertEqual(self.tree._left.root, 'new_left')
    self.assertRaises(TypeError, self.tree.SetLeft('Left Root'))

  def testSetRight(self):
    self.tree.SetRight(binary_tree.BinaryTree('new_right'))
    self.assertIsInstance(self.tree._right, binary_tree.BinaryTree)

  def testAddLeft(self):
    self.tree.AddLeft('Left Root')
    self.tree.AddLeft('Inserted Left')
    self.assertIsInstance(self.tree._left, binary_tree.BinaryTree)
    self.assertEqual(self.tree._left.root, 'Inserted Left')
    self.assertEqual(self.tree._left._left.root, 'Left Root')


if __name__ == '__main__':
  unittest.main()
