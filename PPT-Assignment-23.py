#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Answer1:

def calculateDepth(preorder):
    stack = []
    depth = 0

    for char in preorder:
        if char == 'n':
            stack.append(char)
            depth += 1
        elif char == 'l':
            depth -= 1

    return depth


preorder = "nlnll"
depth = calculateDepth(preorder)
print(depth)


# In[14]:


preorder = "nlnnlll"
depth = calculateDepth(preorder)
print(depth)


# In[15]:


#Answer 2:

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def leftView(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    left_view = []

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            current_node = queue.popleft()

            # Add the leftmost node of each level to the left view list
            if i == 0:
                left_view.append(current_node.val)

            # Add the left and right children of the current node to the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return left_view

# Example usage
root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(1)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)

result = leftView(root)
print(*result)


# In[16]:


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)
root.left.right.right.right = TreeNode(6)

result = leftView(root)
print(*result)


# In[17]:


#Answer 3:

def rightView(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    right_view = []

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            current_node = queue.popleft()

            # Update the rightmost node at each level
            if i == level_size - 1:
                right_view.append(current_node.val)

            # Add the left and right children of the current node to the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return right_view

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(8)

result = rightView(root)
print(*result)


# In[18]:


root = TreeNode(1)
root.left = TreeNode(8)
root.left.left = TreeNode(7)

result = rightView(root)
print(*result)


# In[19]:


#answer 4:

def bottomView(root):
    if root is None:
        return []

    queue = deque()
    queue.append((root, 0))  # Node and its horizontal distance
    bottom_view = {}
    min_hd = max_hd = 0

    while queue:
        current_node, hd = queue.popleft()

        # Update the bottom view dictionary with the current node for its horizontal distance
        bottom_view[hd] = current_node.val

        # Update the minimum and maximum horizontal distance
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        # Add the left and right children of the current node to the queue
        if current_node.left:
            queue.append((current_node.left, hd - 1))
        if current_node.right:
            queue.append((current_node.right, hd + 1))

    # Create the bottom view list using the bottom view dictionary
    bottom_view_list = [bottom_view[hd] for hd in range(min_hd, max_hd + 1)]

    return bottom_view_list


root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)
root.right.right = TreeNode(25)

result = bottomView(root)
print(*result)


# In[20]:


root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(25)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)

result = bottomView(root)
print(*result)


# In[ ]:




