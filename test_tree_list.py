"""test cases for tree_list module."""


import unittest
from tree_list import *


class tests(unittest.TestCase):
  """test cases."""
  def test_makeTree(self):
    self.assertEqual(makeTree('a'), ['a', [], []])

if __name__ == '__main__':
  unittest.main()
