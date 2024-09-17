from gear.engine import *
from gear.utils.matrix_generator import Image
from scripts.player_movement import PlayerMovement

class Nodes:
    tree = Tree(
        nodes=[
            Node2D(
                "player",
                0, 0,
                scripts=[
                    PlayerMovement()
                ],
                nodes=[
                    Sprite2D(
                        "sprite",
                        0, 0,
                        matrix=Image("sprites/player.png")
                    )
                ]
            )
        ]
    )