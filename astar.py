import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance from start node
        self.h = 0  # Heuristic estimate of distance to goal node
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.position == other.position

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    closed_set = set()
    open_set = [Node(start)]
    heapq.heapify(open_set)

    while open_set:
        current_node = heapq.heappop(open_set)
        closed_set.add(current_node.position)

        if current_node.position == goal:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            path.reverse()
            return path

        for neighbor in get_neighbors(grid, current_node.position, rows, cols):
            if neighbor in closed_set:
                continue

            new_g = current_node.g + 1
            neighbor_node = Node(neighbor, current_node)

            if neighbor_node in open_set:
                if new_g >= neighbor_node.g:
                    continue

            neighbor_node.g = new_g
            neighbor_node.h = manhattan_distance(neighbor_node.position, goal)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            heapq.heappush(open_set, neighbor_node)

    return None

def get_neighbors(grid, position, rows, cols):
    x, y = position
    neighbors = []

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < cols and 0 <= new_y < rows and grid[new_y][new_x] != 1:
            neighbors.append((new_x, new_y))

    return neighbors

def manhattan_distance(position1, position2):
    x1, y1 = position1
    x2, y2 = position2

    return abs(x1 - x2) + abs(y1 - y2)

def get_user_input(grid):
    rows, cols = len(grid), len(grid[0])

    def get_position_input(prompt):
        while True:
            try:
                user_input = input(prompt)
                y, x = map(int, user_input.split(','))
                if 0 <= x < cols and 0 <= y < rows and grid[y][x] != 1:
                    return x, y
                else:
                    print("Invalid input. Please enter a valid position.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a comma.")

    # Display grid with row and column indices
    print("   " + "  ".join(str(i) for i in range(cols)))
    for i, row in enumerate(grid):
        print(f"{i}: {row}")

    start = get_position_input("Enter the start position (row, column): ")
    goal = get_position_input("Enter the goal position (row, column): ")

    return start, goal

grid = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

start, goal = get_user_input(grid)

path = astar(grid, start, goal)
print(f"Path found: {path}")
