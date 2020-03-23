from src.score_heuristic import Score
from src.bubbles_left_heuristic import BubblesLeft
from src.total_sum_heuristic import TotalSum

heuristics = {
  1: ('Score', Score),
  2: ('Number of bubbles left', BubblesLeft),
  3: ('Total Sum', TotalSum)
}