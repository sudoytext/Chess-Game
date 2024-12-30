import chess.engine

class ChessEngine:
    def __init__(self, board):
        self.board = board

    def make_engine_move(self):
        print("\nEngine is thinking...")
        with chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish") as engine:
            result = engine.play(self.board, chess.engine.Limit(time=2.0))
            self.board.push(result.move)
            print(f"Engine played: {result.move}")
