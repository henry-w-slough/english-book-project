from slankpy.Screen import Screen


screen = Screen.Screen(800, 800)
screen.set_caption("No Country for Old Men - English Project")
screen.set_fill_color((200, 200, 200))



running = True
while running:

    if screen.has_quit():
        running = False


    screen.update()