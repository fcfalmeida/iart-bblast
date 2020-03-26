from src.bfs import BFS
from src.dfs import DFS
from src.idepth import IDepth
from src.ucs import UCS
from src.greedy_algorithm import Greedy
from src.a_star import AStar

algorithms = {
  1: ('BFS', BFS),
  2: ('DFS', DFS),
  3: ('UCS', UCS),
  4: ('IDepth', IDepth),
  5: ('Greedy', Greedy),
  6: ('A*', AStar)
}