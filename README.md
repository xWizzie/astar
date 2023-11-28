# A* Pathfinding Algorithm

## Overview

This repository contains a Python implementation of the A* algorithm for pathfinding in a 2D grid environment. The algorithm is capable of finding the shortest path from a start position to a goal position while considering obstacles in the grid.

## Contents

- [A* Algorithm Implementation](#a-algorithm-implementation)
- [How to Use](#how-to-use)
- [Input Grid Format](#input-grid-format)
- [User Input](#user-input)
- [Example Usage](#example-usage)

## A* Algorithm Implementation

The A* algorithm is implemented in Python using a priority queue to efficiently manage the set of nodes to be explored. The heuristic used for estimating the remaining cost is the Manhattan distance.

The code includes modular functions for getting neighbors, calculating distances, and obtaining user input for start and goal positions.

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/xWizzie/astar.git
    ```

2. Navigate to the project directory:

    ```bash
    cd astar
    ```

3. Run the Python script:

    ```bash
    python astar.py
    ```

## Input Grid Format

The input grid is a 2D matrix represented by a list of lists. The values in the grid can be either 0 (free space) or 1 (obstacle). The user is prompted to input the start and goal positions on this grid.

Example Grid:

```python
grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
```

## User Input

The user is prompted to enter the start and goal positions. The grid is displayed with row and column indices to aid in making informed choices.

## Example Usage

```
from astar_pathfinding import astar, get_user_input

grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

start, goal = get_user_input(grid)

path = astar(grid, start, goal)
print(f"Path found: {path}")
```
