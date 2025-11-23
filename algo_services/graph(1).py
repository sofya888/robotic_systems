# Добавить логгирование каждого действия log()

from typing import Any, Dict, List, Tuple, Optional

class Graph:
    def __init__(self) -> None:
        """
        Инициализация пустого графа.
        Граф представлен в виде словаря, где:
        - ключи: вершины графа,
        - значения: словари соседей с весами ребер
        """
        self.graph: Dict[Any, Dict[Any, float]] = {}
        self._logs: List[str] = []
        self.log("Инициализирован пустой граф")

    # ====== Служебное логгирование ======
    def log(self, message: str) -> None:
        """
        Простое логгирование действий над графом.
        """
        entry = f"[Graph] {message}"
        self._logs.append(entry)
        print(entry)

    def get_logs(self) -> List[str]:
        """Возвращает копию накопленных логов."""
        return list(self._logs)

    # ====== Основные операции над графом ======
    def add_vertex(self, vertex: Any) -> None:
        """
        Добавление вершины в граф.
        Параметры:
             vertex: название вершины (строка или число)
        """
        if vertex not in self.graph:
            self.graph[vertex] = {}
            self.log(f"Добавлена вершина: {vertex}")
        else:
            self.log(f"Вершина уже существует: {vertex}")

    def add_edge(self, vertex1: Any, vertex2: Any, weight: float = 1, directed: bool = False) -> None:
        """
        Добавление ребра между двумя вершинами.
        Параметры: 
             vertex1: первая вершина
             vertex2: вторая вершина
             weight: вес ребра (по умолчанию 1)
             directed: ориентированность ребра, по умолчанию False
        """
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1][vertex2] = weight  # nested dictionary

        if not directed:
            self.graph[vertex2][vertex1] = weight

        self.log(f"Добавлено ребро: {vertex1} {'->' if directed else '<->'} {vertex2} (вес={weight})")

    def remove_edge(self, vertex1: Any, vertex2: Any, directed: bool = False) -> None:
        """
        Удаление ребра между двумя вершинами.
        Параметры: 
            vertex1: первая вершина,
            vertex2: вторая вершина,
            directed: ориентированность (по умолчанию False)
        """
        removed = False

        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            # исправлено: обращение к словарю по правильным ключам
            del self.graph[vertex1][vertex2]
            removed = True

        # Если граф неориентированный — удаляем обратное ребро
        if not directed and vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            del self.graph[vertex2][vertex1]
            removed = True

        if removed:
            self.log(f"Удалено ребро: {vertex1} {'->' if directed else '<->'} {vertex2}")
        else:
            self.log(f"Ребро не найдено и не удалено: {vertex1} - {vertex2} (directed={directed})")

    def get_vertices(self) -> List[Any]:
        """
        Получаем список всех вершин графа.
        Возвращает: 
            list: список вершин
        """
        vertices = list(self.graph.keys())
        self.log(f"Получены вершины: {vertices}")
        return vertices

    def get_edges(self, directed: bool = False) -> List[Tuple[Any, Any, float]]:
        """
        Получение списка ребер. Переделано на обход через while.
        Для неориентированного графа дубли исключаются.
        """
        edges: List[Tuple[Any, Any, float]] = []
        visited = set()

        vertices = list(self.graph.keys())
        i = 0
        while i < len(vertices):
            v1 = vertices[i]
            neighbors_items = list(self.graph[v1].items())
            j = 0
            while j < len(neighbors_items):
                v2, weight = neighbors_items[j]
                if directed:
                    edges.append((v1, v2, weight))
                else:
                    key = tuple(sorted((v1, v2)))
                    if key not in visited:
                        edges.append((v1, v2, weight))
                        visited.add(key)
                j += 1
            i += 1

        self.log(f"Получены ребра (directed={directed}): {edges}")
        return edges

    def get_neighbors(self, vertex: Any) -> Dict[Any, float]:
        """
        Получение соседей вершины.
        Параметры: 
            vertex : вершина, для которой ищем соседей
        Возвращаем: 
            dict: словарь соседей с весами ребер
        """
        neighbors = dict(self.graph.get(vertex, {}))
        self.log(f"Соседи вершины {vertex}: {neighbors}")
        return neighbors
    
    def get_weight(self, vertex1: Any, vertex2: Any) -> Optional[float]:
        """
        Получение веса ребра между двумя вершинами.
        Параметры:
            vertex1: первая вершина
            vertex2: вторая вершина
        Возвращаем:
            number: вес ребра или None, если ребра нет
        """
        w = self.graph.get(vertex1, {}).get(vertex2)
        self.log(f"Вес ребра {vertex1} -> {vertex2}: {w}")
        return w

    def is_connected(self, vertex1: Any, vertex2: Any) -> bool:
        """
        Проверка наличия ребра между двумя вершинами
        Параметры:
            vertex1: первая вершина
            vertex2: вторая вершина
        Возвращаем:
            bool: True, если есть ребро, иначе False
        """
        connected = vertex2 in self.graph.get(vertex1, {})
        self.log(f"Проверка связности {vertex1} -> {vertex2}: {connected}")
        return connected
    
    def __str__(self) -> str:
        """
        Строковое представление графа
        """
        result = "Graph:\n"
        for vertex in self.graph:
            result += f"{vertex}: {self.graph[vertex]}\n"
        return result

    def __contains__(self, vertex: Any) -> bool:
        """
        Проверка наличия вершины в графе.
        """
        present = vertex in self.graph
        self.log(f"Проверка наличия вершины {vertex}: {present}")
        return present

    # ====== Визуализация / экспорт ======
    def to_adjacency_text(self) -> str:
        """
        Возвращает человекочитаемое представление списка смежности.
        """
        lines: List[str] = []
        for v, nbrs in self.graph.items():
            parts = [f"{n}({w})" for n, w in nbrs.items()]
            lines.append(f"{v}: " + ", ".join(parts) if parts else f"{v}: ∅")
        text = "\n".join(lines)
        self.log("Сформировано текстовое представление списка смежности")
        return text

    def to_dot(self, directed: bool = False) -> str:
        """
        Генерирует строку в формате Graphviz DOT.
        Для неориентированного графа ребра не дублируются.
        """
        gtype = "digraph" if directed else "graph"
        connector = "->" if directed else "--"
        lines: List[str] = [f"{gtype} G {{"]

        # Вершины
        for v in self.graph.keys():
            lines.append(f'    "{v}";')

        # Ребра
        visited = set()
        for v1, nbrs in self.graph.items():
            for v2, w in nbrs.items():
                if directed:
                    lines.append(f'    "{v1}" {connector} "{v2}" [label="{w}"];')
                else:
                    key = tuple(sorted((v1, v2)))
                    if key in visited:
                        continue
                    visited.add(key)
                    lines.append(f'    "{v1}" {connector} "{v2}" [label="{w}"];')

        lines.append("}")
        dot = "\n".join(lines)
        self.log(f"Сгенерирован DOT (directed={directed})")
        return dot
