"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
		# the node we want to return
		result_node = None
		# to keep track of the node in the main tree
		current_node = node
		# create a set of all nodes
		all_nodes = get_all_nodes(current_node)


	def get_all_nodes(self, current_node):
		all_nodes = set()
		while current_node not in all_nodes:
			# visit all it's neighbours
			for neighbor_node in current_node.neighbours:
				all_nodes.add(neighbor_node)
		
		
		