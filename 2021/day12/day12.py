from collections import defaultdict


def _traverse(graph, cur, visited):
    if cur == "end":
        return 1

    s = 0

    for neighbor in graph[cur]:
        if neighbor.islower() and neighbor in visited:
            continue

        s += _traverse(graph, neighbor, visited.union({neighbor}))

    return s


def traverse(graph):
    return _traverse(graph, "start", {"start"})


def _traverse_v2(graph, cur, visited):
    if cur == "end":
        return 1

    if cur == "start" and visited[cur] == 2:
        return 0

    s = 0

    max_small_visits = max([v for k, v in visited.items() if k.islower()])

    for neighbor in graph[cur]:
        if neighbor.islower() and visited[neighbor] > 0 and max_small_visits == 2:
            continue

        visited[neighbor] += 1
        s += _traverse_v2(graph, neighbor, visited)
        visited[neighbor] -= 1

    return s


def traverse_v2(graph):
    visited = defaultdict(int)
    visited["start"] += 1
    return _traverse_v2(graph, "start", visited)


def main():
    graph = defaultdict(list)

    with open("input.txt", "r") as fp:
        for line in fp:
            n1, n2 = line.strip().split("-")
            graph[n1].append(n2)
            graph[n2].append(n1)

    print(traverse(graph))
    print(traverse_v2(graph))


if __name__ == "__main__":
    main()
