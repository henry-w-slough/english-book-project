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


text_box = Label.Label(screen.width, screen.height//4, "", screen.layers["ui"])
text_box.set_background_color((0, 0, 0, 100))
text_box.viewport_y = screen.height - text_box.rect.height

dialogue_event = 0

previous_input = pygame.mouse.get_pressed()

running = True
while running:

    screen.set_caption(f"{screen.clock.get_fps()}")


    mouse_input = pygame.mouse.get_pressed()
    if attendee.is_active:
        if dialogue_event == 0:
            continue
    else:
        player.speed = 3
        text_box.set_background_color((0, 0, 0, 255))

    previous_input = mouse_input


    if screen.has_quit():
        running = False


    camera.apply_offset(screen.layers["players"], screen.layers["collides"], screen.layers["passable"], screen.layers["npcs"])
    screen.visible_layer = camera.cull_layers(*screen.layers.values())
    screen.update()