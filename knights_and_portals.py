

from collections import deque
from typing import List, Tuple


def bfs(grid: List[List[int]], start: Tuple[int, int]) -> List[List[int]]:
    """
    Perform BFS to find shortest distance from start to all reachable cells.

    Args:
        grid: 2D grid of 0s and 1s
        start: starting coordinate (x, y)

    Returns:
        2D list of distances
    """
    n, m = len(grid), len(grid[0])
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    q.append(start)
    dist[start[0]][start[1]] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return dist


def shortest_path_with_portal(grid: List[List[int]]) -> int:
    """
    Finds the shortest path from top-left to bottom-right using one optional teleport.

    Args:
        grid: 2D grid of 0s (open) and 1s (walls)

    Returns:
        Integer: minimum steps to reach (n-1, m-1) or -1 if not reachable.
    """
    n, m = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
        return -1

    start_dist = bfs(grid, (0, 0))
    end_dist = bfs(grid, (n - 1, m - 1))

    # Direct path without teleport
    min_dist = start_dist[n - 1][m - 1] if start_dist[n - 1][m - 1] != -1 else float('inf')

    # Find shortest teleport-enhanced path
    empty_cells = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 0]

    for (x1, y1) in empty_cells:
        for (x2, y2) in empty_cells:
            if (x1, y1) == (x2, y2):
                continue
            if start_dist[x1][y1] != -1 and end_dist[x2][y2] != -1:
                min_dist = min(min_dist, start_dist[x1][y1] + 1 + end_dist[x2][y2])

    return min_dist if min_dist != float('inf') else -1


def run_tests():
    """
    Run test cases to validate the algorithm.
    """
    print("=== KNIGHTS AND PORTALS TESTS ===\n")

    test_cases = [
        {
            "grid": [
                [0, 0, 0],
                [1, 1, 0],
                [0, 0, 0]
            ],
            "expected": 4
        },
        {
            "grid": [
                [0, 1],
                [1, 0]
            ],
            "expected": 2
        },
        {
            "grid": [
                [0, 1, 1],
                [1, 1, 1],
                [1, 1, 0]
            ],
            "expected": -1
        },
        {
            "grid": [
                [0, 0],
                [0, 0]
            ],
            "expected": 2
        },
        {
            "grid": [
                [1, 0],
                [0, 0]
            ],
            "expected": -1
        }
    ]

    for idx, test in enumerate(test_cases, 1):
        result = shortest_path_with_portal(test["grid"])
        print(f"Test Case {idx}:")
        print("Input Grid:")
        for row in test["grid"]:
            print(" ", row)
        print(f"Expected Output: {test['expected']}")
        print(f"Your Output    : {result}")
        print("Test", "Passed\n" if result == test["expected"] else "Failed\n")


if __name__ == "__main__":
    run_tests()
