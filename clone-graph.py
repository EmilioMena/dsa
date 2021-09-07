"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""

class Solution(object):
    def cloneGraph(self, node):
        return cloneGraph(node, {})

def cloneGraph(node, node_copy):
    """
    Time: O(N + M) N is number of nodes and M is number of edges
    Space: O(N) space occupied by the node_copy hash
           also O(H) where H is the height of the graph would be occupied by the recursion stack
    
    DFS. Map the visited nodes to their clone to keep track of them and avoid cycling.
    For each of the children, call the recursion
    """
    if not node:
        return None
    
    if node in node_copy:
        return node_copy[node]
    
    copy = Node(node.val)
    copy_neighbors = []
    node_copy[node] = copy
    for child in node.neighbors:
        copy_neighbors.append(cloneGraph(child, node_copy))
    copy.neighbors = copy_neighbors
    
    return copy

class Solution2(object):
    """
    similar to the first solution but postpone adding children to the copied node until all
    nodes are created
    
    O(N+M) time and O(N) space
    """

    def cloneGraph(self, node):
        return cloneGraph(node, {})

def cloneGraph(node, node_copy):
    if node and node not in node_copy:
        copy = Node(node.val)
        node_copy[node] = copy
        for child in node.neighbors:
            cloneGraph(child, node_copy)
        for child in node.neighbors:
            copy.neighbors.append(node_copy[child])
            
    return node_copy
