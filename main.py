from player import Player
from game import Game

p1 = Player(input("wat's your name? "), 'x')
p2 = Player(input("wat's your name? "), 'o')
g = Game(p1, p2)
g.play()
