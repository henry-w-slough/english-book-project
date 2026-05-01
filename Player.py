from slankpy.Objects import KinematicObject
from slankpy.Input import KeyboardInput

import pygame
import random


class Player(KinematicObject.KinematicObject):
    def __init__(self, width: int, height: int, *groups:pygame.sprite.Group) -> None:
        super().__init__(width, height, *groups)

        self.speed = 3
        
        self.sprite.add_sprites("assets/player/walk_forward.png", "walk_forward", 4, 1)
        self.sprite.add_sprites("assets/player/walk_backward.png", "walk_backward", 4, 1)
        self.sprite.add_sprites("assets/player/walk_left.png", "walk_left", 4, 1)
        self.sprite.add_sprites("assets/player/walk_right.png", "walk_right", 4, 1)

        self.set_sprite("walk_forward", 0)

        self.direction = "forward"

        self.animation_frame = 0
        self.animation_delay = 0

    def update(self) -> None:
        
        move_x = KeyboardInput.get_input_vector(pygame.K_a, pygame.K_d)
        move_y = KeyboardInput.get_input_vector(pygame.K_w, pygame.K_s)

        self.add_position(move_x*self.speed, move_y*self.speed)

        if move_x > 0:
            self.direction = "right" 
        if move_x < 0:
            self.direction = "left"
        if move_y > 0:
            self.direction = "forward" 
        if move_y < 0:
            self.direction = "backward"

        if move_x != 0 or move_y != 0:
            self.animation_delay += 1
            if self.animation_delay >= 15:
                self.animation_frame += 1
                self.animation_delay = 0
            if self.animation_frame >= 4:
                self.animation_frame = 0
        else:
            self.animation_frame = 0

        self.set_sprite(f"walk_{self.direction}", self.animation_frame)


    def check_collision(self, *layers:pygame.sprite.Group) -> None:
        
        for layer in layers:
            
            hits = self.collision.check_mask(layer)

            if not hits:
                continue

            self.collision.resolve_mask(layer)

            