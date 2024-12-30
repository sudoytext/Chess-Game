from game import board, player, engine

def main():
    print("Welcome to the Chess Game!")
    board_instance = board.ChessBoard()
    player_instance = player.Player()

    while not board_instance.board.is_game_over():
        print("\nCurrent board state:")
        board_instance.display_board()

        move = player_instance.get_player_move()
        if move == 'quit':
            print("Thanks for playing!")
            break

        board_instance.make_move(move)

        if not board_instance.board.is_game_over():
            engine_instance = engine.ChessEngine(board_instance.board)
            engine_instance.make_engine_move()

    board_instance.display_result()

if __name__ == "__main__":
    main()
