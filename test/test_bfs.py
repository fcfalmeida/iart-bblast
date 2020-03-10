from src.bfs import BFS
from src.game_state import GameState
from src.game_results import GameResults
from src.board import Board

def simulate_game(game_state, solution):
  for move in solution:
    move_row, move_col = move
    game_state.update_board(move_row, move_col)

  assert game_state.result == GameResults.Win

class TestBFS:
  def test_bfs_level_7(self):
    board = Board([
      [0,0,0,0,0], 
      [0,1,0,1,0], 
      [1,2,1,2,1], 
      [0,2,0,2,0],
      [0,1,0,1,0],
      [0,0,0,0,0]
    ])

    game_state = GameState(board, 2)
    
    solution = BFS.execute(game_state)

    simulate_game(game_state, solution)

  def test_bfs_level_12(self):
    board = Board([
      [1,4,3,1,2], 
      [1,0,3,1,4], 
      [1,1,3,4,4], 
      [2,2,1,2,1],
      [2,2,1,0,3],
      [0,0,1,2,1]
    ])

    game_state = GameState(board, 1)
    
    solution = BFS.execute(game_state)

    simulate_game(game_state, solution)

  def test_bfs_level_16(self):
    board = Board([
      [2,4,4,1,1], 
      [2,2,2,0,4], 
      [0,4,2,2,2], 
      [1,1,1,3,1],
      [1,4,0,1,4],
      [4,0,3,2,0]
    ])

    game_state = GameState(board, 2)
    
    solution = BFS.execute(game_state)

    simulate_game(game_state, solution)

  def test_bfs_level_17(self):
    board = Board([
      [0,4,3,2,2], 
      [1,2,2,2,1], 
      [1,2,2,2,2], 
      [0,3,1,1,3],
      [3,2,0,2,0],
      [2,4,2,2,0]
    ])

    game_state = GameState(board, 2)
    
    solution = BFS.execute(game_state)

    simulate_game(game_state, solution)

  def test_bfs_level_26(self):
    board = Board([
      [1,1,1,1,1], 
      [4,2,3,1,2], 
      [2,1,4,1,2], 
      [3,0,1,3,0],
      [2,1,0,4,3],
      [0,3,2,3,1]
    ])

    game_state = GameState(board, 3)
    
    solution = BFS.execute(game_state)

    simulate_game(game_state, solution)