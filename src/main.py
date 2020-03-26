import time
import src.utils as utils
from src.board import Board
from src.bubble_types import BubbleTypes
from src.bubble import Bubble
from src.game_state import GameState
from src.game_results import GameResults
from src.algorithms import algorithms
from src.heuristics import heuristics
from src.a_star_heuristics import aStarHeuristics


def read_op():
    op = input("Select an option: ")
    print()
    return int(op)


def print_header(game_state):
    print("=" * 37)
    print("Touches left: ", game_state.touches_left, " | Score: ",
          game_state.score)
    print("=" * 37)
    print()


def game_loop(game_state):
    while game_state.result == None:
        print_header(game_state)
        utils.print_board(game_state.board)

        player_input = input("Touch row,col: ").split(",")
        row = int(player_input[0])
        col = int(player_input[1])

        print()

        game_state.update_board(row, col)

    print_header(game_state)
    utils.print_board(game_state.board)

    if game_state.result == GameResults.Win:
        print("**** You Won! ****")
    else:
        print("**** You Lost! ****")

    print()


def levels_menu():
    levels = utils.list_levels()

    print("**** Level ****")

    for level in levels:
        print(level, " - Level ", level, sep="")

    op = read_op()
    selected_level = levels[op]

    return selected_level


def algorithms_menu():
    print("**** Algorithm ****")

    for alg_key in algorithms:
        algorithm = algorithms[alg_key]
        print(alg_key, " - ", algorithm[0])

    heuristic = None
    op = read_op()
    if op == 5:
        heuristic = heuristic_menu()
    if op == 6:
        heuristic = a_star_heuristic_menu()
    selected_algorithm = algorithms[op][1]

    return selected_algorithm, heuristic


def play():
    selected_level = levels_menu()

    board_matrix, max_touches = utils.read_level_file(selected_level)
    board = Board(board_matrix)

    game_state = GameState(board, max_touches)

    game_loop(game_state)


def solve():
    selected_level = levels_menu()
    algorithm, heuristic = algorithms_menu()

    board_matrix, max_touches = utils.read_level_file(selected_level)
    board = Board(board_matrix)

    game_state = GameState(board, max_touches)

    print_header(game_state)
    utils.print_board(game_state.board)

    start_time = time.time()
    solution = algorithm.execute(game_state, heuristic)
    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    for move in solution:
        move_row, move_col = move
        game_state.update_board(move_row, move_col)
        print("Move: [", move_row, ",", move_col, "]")
        print_header(game_state)
        utils.print_board(game_state.board)

    if game_state.result == GameResults.Win:
        print("**** You Won! ****")
    else:
        print("**** You Lost! ****")

    print("\nSolved in ", total_time, " seconds", sep="")
    print()


def print_options(options_dict):
    for op in options_dict:
        option = options_dict.get(op)
        print(option[0])


def main_menu():
    options = {1: ["1 - Play", play], 2: ["2 - Solve", solve]}

    print_options(options)

    op = read_op()

    func = options.get(op, lambda: "Invalid Option")[1]
    return func()


def main_loop():
    while True:
        main_menu()


def heuristic_menu():
    print("**** Heuristic ****")

    for heur_key in heuristics:
        heuristic = heuristics[heur_key]
        print(heur_key, " - ", heuristic[0])

    op = read_op()
    selected_heuristic = heuristics[op][1]

    return selected_heuristic


def a_star_heuristic_menu():
    print("**** Heuristic ****")

    for heur_key in aStarHeuristics:
        heuristic = aStarHeuristics[heur_key]
        print(heur_key, " - ", heuristic[0])

    op = read_op()
    selected_heuristic = aStarHeuristics[op][1]

    return selected_heuristic


main_loop()
