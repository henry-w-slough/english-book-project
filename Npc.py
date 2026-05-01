from slankpy.Objects import KinematicObject
from slankpy.Input import MouseInput
from slankpy.UI import Label
import pygame


class Npc(KinematicObject.KinematicObject):
    def __init__(self, width: int, height: int, *groups:pygame.sprite.Group) -> None:
        super().__init__(width, height, *groups)

        self.animation_delay = 0
        self.animation_frame = 0

        self.animation_state = "idle"

        self.dialogue = {
            0: "This is text 1",
            1: "This is text 2",
            2: "This is text 3",
            3: "This is text 4",
            4: "This is text 5",
        }

        self.is_active = False
    
    def update(self) -> None:

        self.animation_delay += 1
        if self.animation_delay >= 15:
            self.animation_frame += 1
            self.animation_delay = 0
        if self.animation_frame >= 4:
            self.animation_frame = 0

        self.set_sprite(self.animation_state, self.animation_frame)
        
        if MouseInput.is_mouse_over_object(self):
            self.animation_state = "hovered"
            if MouseInput.is_mouse_clicked(0):
                self.is_active = True
        else:
            self.animation_state = "idle"