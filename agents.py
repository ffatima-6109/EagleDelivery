from collections import deque
import heapq
from itertools import count


class SearchResult:
    def __init__(self, path, expanded):
        self.path = path
        self.expanded = expanded


def reconstruct_path(parents, goal):
    path = []
    state = goal
    while state is not None:
        path.append(state)
        state = parents[state]
    path.reverse()
    return path


def bfs(campus, start, goal):
    frontier = deque([start])
    parents = {start: None}
    expanded = 0
    while frontier:
        state = frontier.popleft()
        if state == goal:
            return SearchResult(reconstruct_path(parents, goal), expanded)
        expanded += 1
        for action, successor in campus.neighbors(state):
            if successor not in parents:
                parents[successor] = state
                frontier.append(successor)
    return SearchResult(None, expanded)



def manhattan(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])




def astar(campus, start, goal):
    if start == goal:
        return SearchResult([start], 0)

    frontier = []
    order = count()

    heapq.heappush(
        frontier, (manhattan(start, goal), next(order), 0, start)
    )

    best_cost = {start: 0}
    parents = {start: None}
    expanded = 0

    while frontier:
        f, _, g, state = heapq.heappop(frontier)

        if g != best_cost[state]:
            continue

        if state == goal:
            return SearchResult(
                reconstruct_path(parents, goal), expanded
            )

        expanded += 1

        for action, successor in campus.neighbors(state):
            new_cost = g + 1

            if new_cost < best_cost.get(successor, float("inf")):
                best_cost[successor] = new_cost
                parents[successor] = state

                priority = new_cost + manhattan(successor, goal)

                heapq.heappush(
                    frontier,
                    (priority, next(order), new_cost, successor)
                )

    return SearchResult(None, expanded)




def epsilon_greedy(q_values, state, actions, epsilon, rng):
    if rng.random() < epsilon:
        return rng.choice(actions)

    best_value = max(
        q_values.get((state, action), 0.0)
        for action in actions
    )

    best_actions = [
        action for action in actions
        if q_values.get((state, action), 0.0) == best_value
    ]

    return rng.choice(best_actions)



def q_learning_update(q_values, state, action, reward,
                      next_state, actions, alpha, gamma, terminal):

    old_value = q_values.get((state, action), 0.0)

    if terminal:
        target = reward
    else:
        next_best = max(
            q_values.get((next_state, a), 0.0)
            for a in actions
        )
        target = reward + gamma * next_best

    new_value = old_value + alpha * (target - old_value)

    q_values[(state, action)] = new_value

