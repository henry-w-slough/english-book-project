from slankpy.Objects import KinematicObject
from slankpy.Input import MouseInput
import pygame


class Npc(KinematicObject.KinematicObject):
    def __init__(self, width: int, height: int, *groups:pygame.sprite.Group) -> None:
        super().__init__(width, height, *groups)

        self.animation_delay = 0
        self.animation_frame = 0
    
    def update(self) -> None:


        self.animation_delay += 1
        if self.animation_delay >= 15:
            self.animation_frame += 1
            self.animation_delay = 0
        if self.animation_frame >= 4:
            self.animation_frame = 0

        self.set_sprite("idle", self.animation_frame)
        
        if MouseInput.is_mouse_over_object(self):
            print('asdd')