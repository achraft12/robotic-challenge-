from collections import deque

ROWS = 5
COLS = 5

START = (0, 0)
PAYLOAD = (2, 2)
GOAL = (4, 4)


def bfs(start, goal, obstacles):
    """Return the shortest path from start to goal, or None if no path exists."""
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    # Up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current = queue.popleft()

        if current == goal:
            # Rebuild the path by following parents backward
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        for dr, dc in directions:
            nr = current[0] + dr
            nc = current[1] + dc
            neighbor = (nr, nc)

            inside_grid = 0 <= nr < ROWS and 0 <= nc < COLS
            free_cell = neighbor not in obstacles
            not_visited = neighbor not in visited

            if inside_grid and free_cell and not_visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None


def print_grid(obstacles, path=None):
    """Print a simple 5x5 map."""
    path = set(path or [])

    for r in range(ROWS):
        row = []
        for c in range(COLS):
            cell = (r, c)

            if cell == START:
                symbol = "S"
            elif cell == PAYLOAD:
                symbol = "P"
            elif cell == GOAL:
                symbol = "B"
            elif cell in obstacles:
                symbol = "#"
            elif cell in path:
                symbol = "*"
            else:
                symbol = "."

            row.append(symbol)

        print(" ".join(row))

    print()


def run_mission(name, obstacles):
    print("=" * 45)
    print(name)
    print("=" * 45)

    print("Initial grid:")
    print_grid(obstacles)

    # Step 1: move from start to payload
    path_to_payload = bfs(START, PAYLOAD, obstacles)

    if path_to_payload is None:
        print("No path to the payload.")
        print("MISSION FAILED")
        return

    print("Path to payload:")
    print(path_to_payload)
    print_grid(obstacles, path_to_payload)

    has_payload = True
    print("Payload collected:", has_payload)
    print()

    # Step 2: move from payload to Point B
    path_to_goal = bfs(PAYLOAD, GOAL, obstacles)

    if path_to_goal is None:
        print("No path from the payload to Point B.")
        print("MISSION FAILED")
        return

    print("Path to Point B:")
    print(path_to_goal)
    print_grid(obstacles, path_to_goal)

    print("MISSION COMPLETE")
    print()


if __name__ == "__main__":
    # Scenario 1: at least 3 obstacles, but a valid route exists
    successful_obstacles = {
        (0, 2),
        (1, 2),
        (3, 0),
    }

    # Scenario 2: the robot can collect the payload,
    # but Point B is blocked by its two reachable neighbors.
    blocked_obstacles = {
        (0, 2),
        (1, 2),
        (3, 4),
        (4, 3),
    }

    run_mission("SCENARIO 1: VALID ROUTE", successful_obstacles)
    run_mission("SCENARIO 2: BLOCKED GOAL", blocked_obstacles)
