from src.score_heuristic import Score
from src.bubbles_left_heuristic import BubblesLeft

heuristics = {
  1: ('Score', Score),
  2: ('Number of bubbles left', BubblesLeft),
}