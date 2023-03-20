class Board:
    def __init__(self):
        self.arr = [' '] * 9

    def __str__(self):
        res = ""
        for i in range(len(self.arr)):
            res += self.arr[i] + '|'
            if i == 2 or i == 5:
                res += '\n'
        return res

    def is_winner(self, marker):
        for i in range(0, 8, 3):
            if self.arr[i] == self.arr[i + 1] == self.arr[i + 2] == marker:
                return True
        for i in range(0, 3):
            if self.arr[i] == self.arr[i + 3] == self.arr[i + 6] == marker:
                return True
        if self.arr[0] == self.arr[4] == self.arr[8] == marker:
            return True
        if self.arr[2] == self.arr[4] == self.arr[6] == marker:
            return True
        return False

    def is_draw(self):
        if ' ' not in self.arr:
            return True
        else:
            return False
        # cnt=0
        # for i in self.arr:
        #     if i!=' ':
        #         cnt+=1
        # if cnt==9:
        #     print("draw")

    def make_move(self, player, place):
        if (self.arr[int(place)] == ' '):
            self.arr[int(place)] = player.marker
            self.is_winner(player.marker)
            if not self.is_winner(player.marker):
                self.is_draw()
            return True
        else:
            raise IndexError("the place is full")
