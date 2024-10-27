import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Якщо граф неорієнтований

    def dijkstra(self, start):
        # Відстані до всіх вершин (попередньо невідомі)
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0  # Відстань до початкової вершини = 0

        # Бінарна купа (піраміда) для вибору вершини з найменшою відстанню
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Пропускаємо оброблені вершини
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Оновлюємо відстань, якщо знайдено коротший шлях
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Приклад використання
graph = Graph()

# Додаємо ребра до графа
graph.add_edge('A', 'B', 1)  # Ребро між A і B з вагою 1
graph.add_edge('A', 'C', 4)  # Ребро між A і C з вагою 4
graph.add_edge('B', 'C', 2)  # Ребро між B і C з вагою 2
graph.add_edge('B', 'D', 5)  # Ребро між B і D з вагою 5
graph.add_edge('C', 'D', 1)  # Ребро між C і D з вагою 1
graph.add_edge('D', 'E', 3)  # Ребро між D і E з вагою 3

# Визначаємо початкову вершину для алгоритму Дейкстри
start_vertex = 'A'

# Обчислюємо найкоротші шляхи від початкової вершини
shortest_paths = graph.dijkstra(start_vertex)

# Виводимо результати
print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"Вершина {vertex}: {distance}")