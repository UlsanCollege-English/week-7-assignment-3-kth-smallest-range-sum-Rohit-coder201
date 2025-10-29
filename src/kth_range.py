class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    """Insert key into BST, reject duplicates."""
    if root is None:
        return Node(key)
    if key == root.key:
        return root
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def kth_smallest(root, k):
    """Return k-th smallest key (1-indexed). Raise IndexError if k > total nodes."""
    stack = []
    cur = root
    count = 0

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        count += 1
        if count == k:
            return cur.key

        cur = cur.right

    raise IndexError("k is out of bounds for the tree size")


def range_sum_bst(root, low, high):
    """Return sum of node keys within [low, high]."""
    if root is None:
        return 0

    total = 0
    if low <= root.key <= high:
        total += root.key
    if root.key > low:
        total += range_sum_bst(root.left, low, high)
    if root.key < high:
        total += range_sum_bst(root.right, low, high)

    return total
