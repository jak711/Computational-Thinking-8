from utils import *

# Section 1 - setup
set_background("hauntedhouse")

# TODO - create at least two variables and set their starting value. ex: cookies = 0
ghosts = 0
graveyard = 0

# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -250,200)
m1.hideturtle()
m1.color("red")

m2 = create_sprite("alien", -250,150)
m2.hideturtle()
m2.color("red")

# Section 2 - controls
# TODO - define an action. ex: def my_control()
def spawn_ghost():
    global ghosts
    ghosts += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    g1=create_sprite("ghost",x,y)
    time.sleep(0.1)
    g1.hideturtle()

window.onkeypress(spawn_ghost, "space")
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
def buy_graveyard():
    global graveyard, ghosts
    if ghosts >= 10:
        ghosts -= 10
        graveyard += 1
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        g2=create_sprite("old-creepy-graveyard-on-stormy-winter-day-in-black",x,y)
        time.sleep(0.6)
        g2.hideturtle()
window.onkeypress(buy_graveyard,"g")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    if i % 100 == 0:
        ghosts += graveyard
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    m1.clear()
    m1.write(f"Current ghosts {ghosts}",font = ("Arial", 30, "normal"))

    m2.clear()
    m2.write(f"Current graveyards {graveyard}",font = ("Arial", 30, "normal"))
    time.sleep(0.01)
    window.update()