from src.game_state import GameState
from src.board import Board
import src.utils as utils

class TestGameState:
  
  def test_update_board_no_changes(self):
    curr_board = Board([
      [1,0,2,0], 
      [0,0,1,1], 
      [1,1,2,2], 
      [0,1,0,1]
    ])
    game_state = GameState(curr_board, 1)
    game_state.update_board(0, 1)

    assert game_state.board == curr_board

  def test_update_board_single_red_bubble(self):
    empty_board = Board()
    curr_board = Board([
      [0,0,0,0,0], 
      [0,0,0,0,0], 
      [0,0,1,0,0], 
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]
    ])

    game_state = GameState(curr_board, 1)
    game_state.update_board(2, 2)

    assert game_state.board == empty_board

  def test_update_board_multiple_red_bubbles(self):
    empty_board = Board()
    curr_board = Board([
      [1,0,1,0,1], 
      [0,0,0,0,0], 
      [1,0,1,0,1], 
      [0,0,0,0,0],
      [0,0,0,0,0],
      [1,0,1,0,1]
    ])

    game_state = GameState(curr_board, 1)
    game_state.update_board(0, 0)

    assert game_state.board == empty_board

  def test_update_board_red_green_bubbles(self):
    expected_board = Board([
      [0,0,0,0,0],
      [0,1,0,1,0],
      [1,1,0,1,1],
      [0,2,0,2,0],
      [0,1,0,1,0],
      [0,0,0,0,0]
    ])

    # level 7
    curr_board = Board([
      [0,0,0,0,0], 
      [0,1,0,1,0], 
      [1,2,1,2,1], 
      [0,2,0,2,0],
      [0,1,0,1,0],
      [0,0,0,0,0]
    ])

    game_state = GameState(curr_board, 2)
    game_state.update_board(2, 2)

    assert game_state.board == expected_board

  def test_update_board_level_12(self):
    expected_board = Board()

    curr_board = Board([
      [1,4,3,1,2], 
      [1,0,3,1,4], 
      [1,1,3,4,4], 
      [2,2,1,2,1],
      [2,2,1,0,3],
      [0,0,1,2,1]
    ])

    game_state = GameState(curr_board, 1)
    game_state.update_board(3, 2)

    assert game_state.board == expected_board

  def test_update_board_level_16(self):
    expected_board = Board([
      [1,1,1,0,0], 
      [0,0,0,0,0], 
      [0,0,0,0,0], 
      [0,0,0,0,0],
      [0,0,0,0,0],
      [1,0,0,0,0]
    ])

    curr_board = Board([
      [2,4,4,1,1], 
      [2,2,2,0,4], 
      [0,4,2,2,2], 
      [1,1,1,3,1],
      [1,4,0,1,4],
      [4,0,3,2,0]
    ])

    game_state = GameState(curr_board, 1)
    game_state.update_board(3, 2)

    assert game_state.board == expected_board

  def test_update_board_level_17(self):
    expected_board = Board([
      [0,4,3,2,2], 
      [1,2,2,2,1], 
      [1,2,1,1,2], 
      [0,2,0,0,1],
      [3,2,0,1,0],
      [2,4,1,2,0]
    ])

    curr_board = Board([
      [0,4,3,2,2], 
      [1,2,2,2,1], 
      [1,2,2,2,2], 
      [0,3,1,1,3],
      [3,2,0,2,0],
      [2,4,2,2,0]
    ])

    game_state = GameState(curr_board, 2)
    game_state.update_board(3, 3)

    assert game_state.board == expected_board

    expected_board = Board()
    game_state.update_board(4, 3)

    assert game_state.board == expected_board

  def test_update_board_level_18(self):
    expected_board = Board()

    curr_board = Board([
      [0,3,2,4,0], 
      [1,1,1,2,0], 
      [0,1,4,1,2], 
      [0,4,2,0,1],
      [1,1,1,2,2],
      [0,4,0,1,1]
    ])

    game_state = GameState(curr_board, 1)
    game_state.update_board(4, 2)

    utils.print_board(game_state.board)

    assert game_state.board == expected_board
