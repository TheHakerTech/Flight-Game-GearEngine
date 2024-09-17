from gear.engine import *
from gear.process import _input
from gear.utils.matrix_generator import Image
from scripts.bullet import Bullet
from threading import Timer

class PlayerMovement(Script):
    def on_ready(self):
        # Get nodes
        self.player: Node2D = self.node
        self.sprite: Sprite2D = self.tree.get_node("player/sprite")
        # Init vars
        self.loop: Loop = self.tree.loop
        self.screen: Screen = self.loop.screen
        self.PLAYER_START_POS = Vector2D(0, 10)
        self.speed = 1
        self.can_shoot = True
        self.player.transform = self.PLAYER_START_POS
    
    def physic_process(self):
        if _input.keys["right"]:
            if self.player.transform.x < self.screen.width - len(self.sprite.matrix.elements[0]):
                self.player.transform.x += self.speed

        if _input.keys["left"]:
            if self.player.transform.x > 0:
                self.player.transform.x -= self.speed
        
        if _input.keys["up"] and self.can_shoot:
            bullet = Node2D(
                "bullet",
                0, 0,
                nodes=[
                    Sprite2D(
                        "sprite",
                        0, 0,
                        scripts=[
                            Bullet()
                        ],
                        matrix=Image("sprites/bullet.png")
                    )
                ]
            )
            self.tree.add_child(bullet)
            self.can_shoot = False
            can_shoot_timer = Timer(1, self.shoot_timer)
            can_shoot_timer.start()

        if _input.keys["esc"]:
            raise KeyboardInterrupt()
    
    def shoot_timer(self): self.can_shoot = True