class Player:
    def __init__(self):
        pass

    def get_player_move(self):
        move = input("Enter your move (e.g., e2 e4) or type 'quit' to exit: ")
        return move.lower()
