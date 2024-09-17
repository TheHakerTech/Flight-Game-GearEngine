from gear.engine import *
from project.nodes import Nodes

class Game:
    tree: Tree | None = None
    screen: Screen | None = None
    loop: Loop | None = None
    WIDTH = 9
    HEIGHT = 13

    @staticmethod
    def main():
        # Init tree, screen, loop
        Game.tree = Nodes.tree
        Game.screen = Screen(Game.WIDTH, Game.HEIGHT, 10)
        Game.loop = Loop(Game.tree, Game.screen)
        # Run game
        Game.loop.run()

if __name__ == "__main__":
    Game.main()