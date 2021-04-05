# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# https://shimo.im/docs/UdY2UUKtliYXmk8t/read

visited = set()
def dfs(node, visited):
    if node in visited: # terminator
        # already visited
    	return

    visited.add(node)

    # process current node here.
	# ...
	for next_node in node.children():
        if next_node not in visited:
            dfs(next_node, visited)

# 非递归
def DFS(self, tree):
    if tree.root is None:
        return []

    visited, stack = [], [tree.root]

    while stack:
        node = stack.pop()
        visited.add(node)

        process (node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)

    # other processing work 
    # ...