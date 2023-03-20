from board import Board


class Game:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.board = Board()
        self.turn = self.p1

    def play(self):
        x = input(fr"{self.turn.name} enter a place: ")
        while True:

            # while not self.board.make_move(self.turn, x):
            while True:
                try:
                    self.board.make_move(self.turn, int(x))
                    break
                except IndexError:
                    x = input("try another place")
                    # self.board.make_move(self.turn, x)
            print(self.board)
            if self.turn == self.p1:
                self.turn = self.p2
            else:
                self.turn = self.p1
            if self.board.is_winner(self.p1.marker) or self.board.is_winner(self.p2.marker):
                if self.board.is_winner(self.p1.marker):
                    print(f"{self.p1.name} is win 😍")
                else:
                    print(f"{self.p2.name} is win 😍")
                break
            if self.board.is_draw():
                print("draw")
                break
            x = input(f"{self.turn.name} enter a place")

        # not  and not self.board.is_winner(
        # self.p2.marker) and not s:
