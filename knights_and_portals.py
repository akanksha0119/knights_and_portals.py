

from collections import deque
from typing import List, Tuple

def bfs(grid: List[List[int]], start: Tuple[int, int]) -> List[List[int]]:
    """
    Perform BFS to compute shortest distances from start cell to all others.

    Args:
        grid: 2D list of 0s (empty) and 1s (blocked)
        start: (x, y) coordinate

    Returns:
        2D list of distances from start
    """
    n, m = len(grid), len(grid[0])
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    queue = deque([start])
    dist[start[0]][start[1]] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    return dist

def shortest_path_with_portal(grid: List[List[int]]) -> int:
    """
    Find shortest path from top-left to bottom-right with one teleport.

    Args:
        grid: 2D list representing the grid

    Returns:
        Integer representing shortest path length or -1 if unreachable
    """
    n, m = len(grid), len(grid[0])

    if grid[0][0] == 1 or grid[n-1][m-1] == 1:
        return -1

    start_dist = bfs(grid, (0, 0))
    end_dist = bfs(grid, (n - 1, m - 1))

    result = start_dist[n-1][m-1] if start_dist[n-1][m-1] != -1 else float('inf')

    empty_cells = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 0]

    for (x1, y1) in empty_cells:
        for (x2, y2) in empty_cells:
            if (x1, y1) != (x2, y2):
                if start_dist[x1][y1] != -1 and end_dist[x2][y2] != -1:
                    result = min(result, start_dist[x1][y1] + 1 + end_dist[x2][y2])

    return result if result != float('inf') else -1


def run_tests():
    """
    Run sample test cases
    """
    print("=== Knights and Portals: Sample Test Cases ===\n")

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
        for row in test["grid"]:
            print(" ", row)
        print(f"Expected: {test['expected']}, Got: {result}")
        print("Result:", "✅ Passed\n" if result == test["expected"] else "❌ Failed\n")

if __name__ == "__main__":
    run_tests()

