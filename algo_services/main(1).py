# Самостоятельно инициализировать объекта класса Граф из файла algo_services/src/graph.py
# Реализация ниже использует локальный файл graph.py из того же каталога.

from graph import Graph

def build_sample_graph() -> Graph:
    g = Graph()
    # Пример: небольшой неориентированный граф
    g.add_edge("A", "B", 3)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 5)
    g.add_edge("C", "D", 1)
    return g

if __name__ == "__main__":
    graph = build_sample_graph()

    print("Вершины:", graph.get_vertices())
    print("Ребра:", graph.get_edges(directed=False))

    print()
    print("Список смежности:")
    print(graph.to_adjacency_text())

    print()
    print("DOT-представление (можно сохранить в .dot и отрендерить Graphviz):")
    print(graph.to_dot(directed=False))
