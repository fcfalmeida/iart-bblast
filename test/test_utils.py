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

  def test_are_adjacent(self):
    matrix = [
      [0,0,0,0,0],
      [1,0,0,2,1],
      [0,0,1,0,0],
      [1,1,0,3,0]
    ]

    assert utils.are_adjacent(matrix, 1, 0, 3, 0)
    assert utils.are_adjacent(matrix, 3, 1, 3, 3)
    assert utils.are_adjacent(matrix, 1, 3, 1, 4)
    assert utils.are_adjacent(matrix, 1, 0, 1, 2)
    assert utils.are_adjacent(matrix, 3, 3, 1, 3)
    assert not utils.are_adjacent(matrix, 0, 1, 2, 2)
    assert not utils.are_adjacent(matrix, 1, 0, 1, 4)
    assert not utils.are_adjacent(matrix, 1, 1, 1, 1)