import src.utils as utils
from src.board import Board
from src.bubble_types import BubbleTypes
from src.bubble import Bubble
from src.game_state import GameState
from src.game_results import GameResults
from copy import deepcopy

def read_op():
  op = input('Select an option: ')
  print()
  return int(op)

def print_header(game_state):
    print('=' * 37)
    print('Touches left: ', game_state.touches_left, ' | Score: ', game_state.score)
    print('=' * 37)
    print()

def game_loop(game_state):
  while game_state.result == None:
    print_header(game_state)
    utils.print_board(game_state.board)
    
    player_input = input('Touch row,col: ').split(',')
    row = int(player_input[0])
    col = int(player_input[1])
    
    print()

    game_state.update_board(row, col)

  print_header(game_state)
  utils.print_board(game_state.board)

  if game_state.result == GameResults.Win:
    print('**** You Won! ****')
  else:
    print('**** You Lost! ****')

  print()

def levels_menu():
  levels = utils.list_levels()

  for level in levels:
    print(level, ' - Level ', level)

  op = read_op()
  selected_level = levels[op]

  return selected_level

def play():
  selected_level = levels_menu()

  board_matrix, max_touches = utils.read_level_file(selected_level)
  board = Board(board_matrix)

  game_state = GameState(board, max_touches)

  game_loop(game_state)

def solve():
  pass

def print_options(options_dict):
  for op in options_dict:
    option = options_dict.get(op)
    print(option[0])

def main_menu():
  options = {
    1: ['1 - Play', play],
    2: ['2 - Solve', solve]
  }

  print_options(options)

  op = read_op()

  func = options.get(op, lambda: 'Invalid Option')[1]
  return func()

def main_loop():
  while True:
    main_menu()

main_loop()