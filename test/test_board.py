from src.board import Board

class TestBoard:

  def test_is_empty(self):
    board = Board()

    assert board.is_empty()