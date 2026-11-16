from graph import Graph
from bfs import BFS


class WordLadder:
    def __init__(self, filename):
        self.filename = filename
        self.g = self.build_graph()

    def build_graph(self):
        d = {}  # { "_ATS": ["CATS", "MATS", ...], ... }
        g = Graph()

        with open(self.filename, 'r') as wfile:
            words = wfile.read().split()
        words_set = set(words)

        for word in words:
            g.add_vertex(word)
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i + 1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]

        # 1. zamiana litery: łączymy słowa w obrębie kubełka
        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.add_edge(word1, word2)

        # 2. usunięcie / wstawienie litery:
        # jeśli po skreśleniu jednej litery ze słowa dostajemy legalne słowo, to słowa łączy krawędź w obie strony
        for word in words:
            for i in range(len(word)):
                shorter = word[:i] + word[i + 1:]
                if shorter in words_set:
                    g.add_edge(word, shorter)  # usunięcie litery
                    g.add_edge(shorter, word)  # wstawienie litery

        return g

    def describe(self, a, b):
        """Opisuje operację zamieniającą słowo a w słowo b."""
        if len(a) == len(b):
            for i in range(len(a)):
                if a[i] != b[i]:
                    return f"{a} -> {b}: replace '{a[i]}' at index {i} with '{b[i]}'"
        elif len(b) == len(a) + 1:
            for i in range(len(b)):
                if b[:i] + b[i + 1:] == a:
                    return f"{a} -> {b}: add '{b[i]}' at index {i}"
        else:
            for i in range(len(a)):
                if a[:i] + a[i + 1:] == b:
                    return f"{a} -> {b}: remove '{a[i]}' at index {i}"

    def shortest_path(self, word1, word2):
        if word1 not in self.g or word2 not in self.g:
            raise ValueError("Słowa muszą być legalne.")

        bfs = BFS(self.g)
        bfs.bfs(word1)
        path = bfs.traverse(word2)

        # traverse przy braku ścieżki zwraca [word2]
        if path[0] != word1:
            raise ValueError(f"Nie da się przekształcić {word1} w {word2}.")
        return path

    def print_operations(self, word1, word2):
        path = self.shortest_path(word1, word2)
        for i in range(len(path) - 1):
            print(self.describe(path[i], path[i + 1]))


if __name__ == "__main__":
    w_ladder = WordLadder("collins2015.txt")
    w_ladder.print_operations("RIGHT", "WRONG")