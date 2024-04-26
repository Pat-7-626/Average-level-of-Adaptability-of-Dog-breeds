from collections import defaultdict, deque


class UndirectedGraph:
    """
    an undirected graph
    """

    def __init__(self, adj_v_list: list):
        """

        :param adj_v_list: [(a, b), (c, d), ...] where
        a and b are adjacent vertices and c and d are adjacent vertices.
        """
        self.__graph = defaultdict(list)
        for v, w in adj_v_list:
            self.__graph[v].append(w)
            self.__graph[w].append(v)

    @property
    def graph(self) -> dict:
        """

        :return: self.__graph: dict
        """
        return self.__graph

    def breadth_first_search(self, s: str) -> dict:
        """

        :param s: starting vertex: str
        :return: distance: dict
        """
        distance = {}
        marked = set()
        queue = deque()

        for v in self.graph:
            distance[v] = float("inf")
        distance[s] = 0
        queue.append((None, s))

        while queue:
            p, v = queue.popleft()
            if v not in marked:
                marked.add(v)
                if p:
                    distance[v] = distance[p] + 1
                for w in self.graph[v]:
                    queue.append((v, w))

        return distance

    def shortest_distance(self, s: str, f: str) -> str:
        """

        :param s: starting vertex: str
        :param f: stopping vertex: str
        :return: result: str
        """
        distance = self.breadth_first_search(s)

        if f in distance:
            if distance[f] == float('inf'):
                result = f"There is no path from {s} to {f}."
            else:
                result = (f"The shortest path from {s} to {f} is "
                          f"{distance[f]} step(s).")
        else:
            result = f"There is no path from {s} to {f}."

        return result


# Example (Use the real dataset when solving the problem.)

Dog = UndirectedGraph([('Labrador', 'Poodle'),
                       ('Labrador', 'German Shepherd'),
                       ('Poodle', 'Bulldog'),
                       ('Bulldog', 'Golden Retriever'),
                       ('Chihuahua', 'Golden Retriever'),
                       ('Samoyed', 'Japanese Spitz'),
                       ('Bulldog', 'Chihuahua'),
                       ('Labrador', 'Golden Retriever'),
                       ('German Shepherd', 'Japanese Spitz')])

print(Dog.shortest_distance('Golden Retriever', 'Labrador'))
print(Dog.shortest_distance('Golden Retriever', 'Poodle'))
print(Dog.shortest_distance('Samoyed', 'Labrador'))
