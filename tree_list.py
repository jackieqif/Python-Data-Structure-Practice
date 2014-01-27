"""Tree data structure using list (of list)."""


def makeTree(obj):
    return [obj, [], []]


def getRootVal(tree):
    return tree[0]


def getRightChild(tree):
    return tree[2]


def getLeftChild(tree):
    return tree[1]


def setLeftChild(tree, left):
    original = tree[1]
    if len(original) > 0:
        tree[1] = makeTree(left)
        tree[1][1] = original
    else:
        tree[1] = makeTree(left)


def setRightChild(tree, right):
    original = tree[2]
    if len(original) > 0:
        tree[2] = makeTree(right)
        tree[2][2] = original
    else:
        tree[2] = makeTree(right)


def buildTree():
    tree = makeTree('a')
    setLeftChild(tree, 'b')
    setRightChild(tree, 'c')
    setRightChild(getLeftChild(tree), 'd')
    setLeftChild(getRightChild(tree), 'e')
    setRightChild(getRightChild(tree), 'f')
    return tree

ttree = buildTree()
