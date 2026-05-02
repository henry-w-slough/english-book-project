from slankpy.Screen import Screen
from slankpy.Camera import Camera
from slankpy.Map import MapLoader
from slankpy.UI import Label
from slankpy.Input import MouseInput
import Player
import Npc
import pygame


screen = Screen.Screen(800, 800)
screen.add_layer("passable")
screen.add_layer("collides1")
screen.add_layer("npcs")
screen.add_layer("collides2")
screen.add_layer("players")
screen.add_layer("ui")
screen.set_fill_color((125, 104, 18))
pygame.display.set_icon(pygame.image.load("assets/no-country-for-old-men.webp"))
screen.set_caption("No Country for Old Men - Game")


map_data = MapLoader.load_map("assets/map.tmj")
trim = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Floors", "Walls", "Path", "Furniture"])
floor = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Trim", "Walls", "Path", "Furniture"])
walls = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Floors", "Trim", "Path", "Furniture"])
path = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Floors", "Trim", "Walls", "Furniture"])
furniture = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Floors", "Trim", "Walls", "Path"])

screen.layers["passable"].add(path)
screen.layers["collides1"].add(walls)
screen.layers["passable"].add(floor)
screen.layers["collides1"].add(trim)
screen.layers["collides2"].add(furniture)



attendee = Npc.Npc(40, 40, screen.layers["npcs"], screen.layers["collides1"])
attendee.sprite.add_sprites("assets/npc/attendee/idle.png", "idle", 4, 1)
attendee.sprite.add_sprites("assets/npc/attendee/hovered.png", "hovered", 4, 1)
attendee.set_position(350, 220)
attendee.dialogue = {
    0: "Well hello stranger, you come far?",
    1: "I'm the attendee at this here gas station.",
    2: "I've been working this station long before your time.",
    3: "It was my father in-law's, before he passed some time ago.",
    4: "A man just came in here, he had a mighty strange haircut.",
    5: "If you want to talk to him, he's down the right.",
}


anton = Npc.Npc(40, 40, screen.layers["npcs"], screen.layers["collides1"])
anton.sprite.add_sprites("assets/npc/anton/idle.png", "idle", 4, 1)
anton.sprite.add_sprites("assets/npc/anton/hovered.png", "hovered", 4, 1)
anton.set_position(850, 220)
anton.dialogue = {
    0: "Hello friendo... I'm Anton...",
    1: "Seems we've been destined to meet here...",
    2: "See this coin? It's here in my hand...",
    3: "It's travelled 30 long years to get here... just for you...",
    4: "Well... I have some business to attend too...",
    5: "Godspeed... friendo...",
}



tom_bell = Npc.Npc(40, 40, screen.layers["npcs"], screen.layers["collides1"])
tom_bell.sprite.add_sprites("assets/npc/tom_bell/idle.png", "idle", 4, 1)
tom_bell.sprite.add_sprites("assets/npc/tom_bell/hovered.png", "hovered", 4, 1)
tom_bell.set_position(220, 320)
tom_bell.dialogue = {
    0: "Hey there partner, I'm Tom Bell, the sheriff.",
    1: "Been tracking down a criminal said to be around here.",
    2: "It's said he kills for pleasure, like sport.",
    3: "I found a car ablaze some days back, said to be his doing.",
    4: "Sometimes I feel the modern day is aging too fast for me.",
    5: "But anyway, be safe out there."
}



carla_jean = Npc.Npc(40, 40, screen.layers["npcs"], screen.layers["collides1"])
carla_jean.sprite.add_sprites("assets/npc/carla_jean/idle.png", "idle", 4, 1)
carla_jean.sprite.add_sprites("assets/npc/carla_jean/hovered.png", "hovered", 4, 1)
carla_jean.set_position(950, 350)
carla_jean.dialogue = {
    0: "Hello there, I'm Carla Jean.",
    1: "My husband Llewelyn is somewhere `round here.",
    2: "He's been gone for some days, won't even tell me what he's up to.",
    3: "He came home yesterday with a briefcase and a gun, no explanation.",
    4: "I sure hope my husband is safe...",
    5: "Anyway, see you around.",
}



llewelyn = Npc.Npc(40, 40, screen.layers["npcs"], screen.layers["collides1"])
llewelyn.sprite.add_sprites("assets/npc/llewelyn/idle.png", "idle", 4, 1)
llewelyn.sprite.add_sprites("assets/npc/llewelyn/hovered.png", "hovered", 4, 1)
llewelyn.set_position(300, 440)
llewelyn.dialogue = {
    0: "Hello. Name is Llewelyn.",
    1: "My business? Surviving best describes it.",
    2: "I found a briefcase full of money.",
    3: "Been on the run ever since, keeping my family safe.",
    4: "Killer been hired to come after me, not sure of his name.",
    5: "Keep yourself safe, friend.",
}


text_box = Label.Label(screen.width, screen.height//4, "assets/font.ttf", screen.layers["ui"])
text_box.viewport_y = screen.height - text_box.rect.height
text_box.set_background_color((0, 0, 0, 0))

dialogue_event = 0

previous_input = pygame.mouse.get_pressed()


player = Player.Player(40, 40, pygame.sprite.Group(screen.layers["collides1"], screen.layers["collides2"]), screen.layers["players"])
player.set_position(500, 500)
camera = Camera.Camera(player)
camera.set_zoom(2.5)


running = True
while running:


    mouse_input = pygame.mouse.get_pressed()
    
    if mouse_input[0]:

        print(dialogue_event)

        if MouseInput.is_mouse_over_object(attendee) and dialogue_event == 0:
            attendee.active = True
            dialogue_event = 1 
        if MouseInput.is_mouse_over_object(anton) and dialogue_event == 0:
            anton.active = True
            dialogue_event = 1 
        if MouseInput.is_mouse_over_object(carla_jean) and dialogue_event == 0:
            carla_jean.active = True
            dialogue_event = 1 
        if MouseInput.is_mouse_over_object(tom_bell) and dialogue_event == 0:
            tom_bell.active = True
            dialogue_event = 1 
        if MouseInput.is_mouse_over_object(llewelyn) and dialogue_event == 0:
            llewelyn.active = True
            dialogue_event = 1 

        if dialogue_event > 0 and not previous_input[0]:
            if dialogue_event == len(attendee.dialogue) + 1:
                text_box.set_background_color((0, 0, 0, 0))
                player.speed = 3
                dialogue_event = 0
                text_box.set_text("")
                attendee.active = False
                anton.active = False
                tom_bell.active = False
                carla_jean.active = False
                llewelyn.active = False
            else:
                text_box.set_background_color((0, 0, 0, 200))
                player.speed = 0
                if attendee.active:
                    text_box.set_text(attendee.dialogue[dialogue_event - 1])
                if anton.active:
                    text_box.set_text(anton.dialogue[dialogue_event - 1])
                if tom_bell.active:
                    text_box.set_text(tom_bell.dialogue[dialogue_event - 1])
                if carla_jean.active:
                    text_box.set_text(carla_jean.dialogue[dialogue_event - 1])
                if llewelyn.active:
                    text_box.set_text(llewelyn.dialogue[dialogue_event - 1])
                dialogue_event += 1

    previous_input = mouse_input


    if screen.has_quit():
        running = False


    camera.apply_offset(screen.layers["players"], screen.layers["collides1"], screen.layers["collides2"], screen.layers["passable"], screen.layers["npcs"])
    screen.visible_layer = camera.cull_layers(*screen.layers.values())
    screen.update()