from slankpy.Screen import Screen
from slankpy.Camera import Camera
from slankpy.Map import MapLoader
import Player
import Npc


screen = Screen.Screen(800, 800)
screen.add_layer("tiles")
screen.add_layer("npcs")
screen.add_layer("players")
screen.set_fill_color((125, 104, 18))


player = Player.Player(40, 40, screen.layers["players"])
player.set_position(400, 400)
camera = Camera.Camera(player)
camera.set_zoom(2)


map_data = MapLoader.load_map("assets/map.tmj")
trim = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Floors", "Walls", "Path"])
floor = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Trim", "Walls", "Path"])
walls = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Floors", "Trim", "Path"])
path = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5, ["Floors", "Trim", "Walls"])

screen.layers["tiles"].add(path)
screen.layers["tiles"].add(walls)
screen.layers["tiles"].add(floor)
screen.layers["tiles"].add(trim)


attendee = Npc.Npc(40, 40, screen.layers["npcs"])
attendee.sprite.add_sprites("assets/npc/idle.png", "idle", 4, 1)
attendee.set_position(400, 400)


running = True
while running:

    screen.set_caption(f"{screen.clock.get_fps()}")


    if screen.has_quit():
        running = False


    player.check_collision(screen.layers["tiles"])


    camera.apply_offset(*screen.layers.values())
    screen.visible_layer = camera.cull_layers(*screen.layers.values())
    screen.update()