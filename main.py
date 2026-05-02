from slankpy.Screen import Screen
from slankpy.Camera import Camera
from slankpy.Map import MapLoader
from slankpy.UI import Label
from slankpy.Input import MouseInput
import Player
import Npc
import pygame
import random


screen = Screen.Screen(800, 800)
screen.add_layer("passable")
screen.add_layer("collides")
screen.add_layer("npcs")
screen.add_layer("players")
screen.add_layer("ui")
screen.set_fill_color((125, 104, 18))


player = Player.Player(40, 40, screen.layers["collides"], screen.layers["players"])
player.set_position(500, 500)
camera = Camera.Camera(player)
camera.set_zoom(2)


map_data = MapLoader.load_map("assets/map.tmj")
trim = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Floors", "Walls", "Path"])
floor = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Trim", "Walls", "Path"])
walls = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Floors", "Trim", "Path"])
path = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Floors", "Trim", "Walls"])

screen.layers["passable"].add(path)
screen.layers["collides"].add(walls)
screen.layers["passable"].add(floor)
screen.layers["collides"].add(trim)



attendee = Npc.Npc(40, 40, screen.layers["npcs"], screen.layers["collides"])
attendee.sprite.add_sprites("assets/npc/idle.png", "idle", 4, 1)
attendee.sprite.add_sprites("assets/npc/hovered.png", "hovered", 4, 1)
attendee.set_position(350, 250)
attendee.dialogue = {
    0: "Well hello stranger, you come far?",
    1: "Fuel pumps are self-serve after six, my policy.",
    2: "I've been working this station long before your time.",
    3: "It was my father in-law's, before he passed some time ago.",
    4: "A man just came in here, he had a mighty strange haircut.",
    5: "If you want to talk to him, he's down the right.",
}


anton = Npc.Npc(40, 40, screen.layers["npcs"], screen.layers["collides"])
anton.sprite.add_sprites("assets/npc/idle.png", "idle", 4, 1)
anton.sprite.add_sprites("assets/npc/hovered.png", "hovered", 4, 1)
anton.set_position(850, 220)
anton.dialogue = {
    0: "Hello friendo... I'm Anton...",
    1: "Seems we've been destined to meet here...",
    2: "See this coin? It's here in my hand...",
    3: "It's travelled 30 long years to get here... just for you...",
    4: "Well... I have some business to attend too...",
    5: "Godspeed... friendo...",
}



tom_bell = Npc.Npc(40, 40, screen.layers["npcs"], screen.layers["collides"])
tom_bell.sprite.add_sprites("assets/npc/idle.png", "idle", 4, 1)
tom_bell.sprite.add_sprites("assets/npc/hovered.png", "hovered", 4, 1)
tom_bell.set_position(220, 320)
tom_bell.dialogue = {
    0: "Hello friendo...",
    1: "Seems we've been destined to meet here...",
    2: "See this coin? It's here in my hand...",
    3: "It's travelled 30 long years to get here... just for you...",
    4: "Well... I have some business to attend too...",
    5: "Godspeed... friendo...",
}



carla_jean = Npc.Npc(40, 40, screen.layers["npcs"], screen.layers["collides"])
carla_jean.sprite.add_sprites("assets/npc/idle.png", "idle", 4, 1)
carla_jean.sprite.add_sprites("assets/npc/hovered.png", "hovered", 4, 1)
carla_jean.set_position(760, 350)
carla_jean.dialogue = {
    0: "Hello friendo...",
    1: "Seems we've been destined to meet here...",
    2: "See this coin? It's here in my hand...",
    3: "It's travelled 30 long years to get here... just for you...",
    4: "Well... I have some business to attend too...",
    5: "Godspeed... friendo...",
}



llewelyn = Npc.Npc(40, 40, screen.layers["npcs"], screen.layers["collides"])
llewelyn.sprite.add_sprites("assets/npc/idle.png", "idle", 4, 1)
llewelyn.sprite.add_sprites("assets/npc/hovered.png", "hovered", 4, 1)
llewelyn.set_position(300, 440)
llewelyn.dialogue = {
    0: "Hello friendo...",
    1: "Seems we've been destined to meet here...",
    2: "See this coin? It's here in my hand...",
    3: "It's travelled 30 long years to get here... just for you...",
    4: "Well... I have some business to attend too...",
    5: "Godspeed... friendo...",
}


text_box = Label.Label(screen.width, screen.height//4, "assets/font.ttf", screen.layers["ui"])
text_box.viewport_y = screen.height - text_box.rect.height
text_box.set_background_color((0, 0, 0, 0))

dialogue_event = 0

previous_input = pygame.mouse.get_pressed()

running = True
while running:

    screen.set_caption(f"{screen.clock.get_fps()}")


    mouse_input = pygame.mouse.get_pressed()
    
    if mouse_input[0]:

        if MouseInput.is_mouse_over_object(attendee) and dialogue_event == 0:
            attendee.active = True
            dialogue_event = 1 
        if MouseInput.is_mouse_over_object(anton) and dialogue_event == 0:
            anton.active = True
            dialogue_event = 1 

        if dialogue_event > 0 and not previous_input[0]:
            if dialogue_event == len(attendee.dialogue) + 1:
                text_box.set_background_color((0, 0, 0, 0))
                player.speed = 3
                dialogue_event = 0
                text_box.set_text("")
                attendee.active = False
                anton.active = False
            else:
                text_box.set_background_color((0, 0, 0, 200))
                player.speed = 0
                if attendee.active:
                    text_box.set_text(attendee.dialogue[dialogue_event - 1])
                if anton.active:
                    text_box.set_text(anton.dialogue[dialogue_event - 1])
                dialogue_event += 1

    previous_input = mouse_input


    if screen.has_quit():
        running = False


    camera.apply_offset(screen.layers["players"], screen.layers["collides"], screen.layers["passable"], screen.layers["npcs"])
    screen.visible_layer = camera.cull_layers(*screen.layers.values())
    screen.update()