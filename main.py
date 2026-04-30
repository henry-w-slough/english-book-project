from slankpy.Screen import Screen
from slankpy.Camera import Camera
from slankpy.Map import MapLoader
import Player


screen = Screen.Screen(800, 800)
screen.set_caption("No Country for Old Men - English Project")
screen.add_layer("tiles")
screen.add_layer("players")


player = Player.Player(40, 40, screen.layers["players"])
player.set_position(400, 400)
camera = Camera.Camera(player)
camera.set_zoom(2)


map_data = MapLoader.load_map("assets/untitled.tmj")
map = MapLoader.map_to_group(map_data, "assets/tileset.png", "tiles", 5, 5)
screen.layers["tiles"].add(map)


running = True
while running:

    screen.set_caption(f"{screen.clock.get_fps()}")


    if screen.has_quit():
        running = False


    player.check_collision(screen.layers["tiles"])


    camera.apply_offset(*screen.layers.values())
    screen.visible_layer = camera.cull_layers(*screen.layers.values())
    screen.update()