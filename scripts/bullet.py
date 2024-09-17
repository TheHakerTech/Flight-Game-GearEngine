from gear.engine import *

class Bullet(Script):
    def on_ready(self):
        self.node: Node2D = self.node
        self.player: Node2D = self.tree.get_node("player")
        self.node.transform = Vector2D(self.player.transform.x + 1, self.player.transform.y)
        self.speed = 3
    
    def physic_process(self):
        if self.node.transform.y > 1:
            self.node.translate(0, -self.speed)
        else:
            self.tree.del_node("bullet")