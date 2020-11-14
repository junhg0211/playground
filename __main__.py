from sys import argv

from basis import Game, Designer
from server import Server

if len(argv) <= 1:
    game = Game()
    game.start()
else:
    if argv[1] in {'-g', '-G', '--basis'}:
        game = Game()
        game.run()
    elif argv[1] in {'-s', '-S', '--server'}:
        server = Server()
        server.start()
    elif argv[1] in {'-d', '-D', '--designer'}:
        designer = Designer()
        designer.start()
