import chess

class ChessBoard:
    def __init__(self):
        self.board = chess.Board()

    def display_board(self):
        print(self.board)

    def make_move(self, move_str):
        try:
            move = self.board.parse_san(move_str)
            if move in self.board.legal_moves:
                self.board.push(move)
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid move format. Please use e2 e4 format.")

    def display_result(self):
        print("Game Over!")
        print("Final board state:")
        print(self.board)
        print("Result:", self.board.result())
