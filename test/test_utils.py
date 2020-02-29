import src.utils as utils
from src.bubble import Bubble
from src.bubble_types import BubbleTypes

class TestUtils:
  
  def test_create_empty_board(self):
    board = utils.create_empty_board(6,5)

    bubble = Bubble(BubbleTypes.Empty)

    for i in range(len(board)):
      for j in range(len(board[i])):
        assert board[i][j] == bubble
        assert len(board[i]) == 5

    assert len(board) == 6