import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(num=title, figsize=(8, 5))  # Використання заголовка як назви фігури
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()


def depth_first_search(root):
    stack = [root]
    visited = []
    colors = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            colors.append(generate_color(len(visited)))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return visited, colors


def breadth_first_search(root):
    queue = [root]
    visited = []
    colors = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            colors.append(generate_color(len(visited)))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return visited, colors


def generate_color(index):
    r = min(255, index * 15)
    g = min(255, 128 + index * 5)
    b = 255 - min(255, index * 10)
    return f'#{r:02X}{g:02X}{b:02X}'


# Створення бінарного дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація обходу в глибину (DFS)
dfs_visited, dfs_colors = depth_first_search(root)
for node, color in zip(dfs_visited, dfs_colors):
    node.color = color
draw_tree(root, "Обхід в глибину (DFS)")

# Візуалізація обходу в ширину (BFS)
# Потрібно відновити дерево для чистоти візуалізації
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

bfs_visited, bfs_colors = breadth_first_search(root)
for node, color in zip(bfs_visited, bfs_colors):
    node.color = color
draw_tree(root, "Обхід в ширину (BFS)")