# Section 1 - Your code
from utils import *
player_name = input("What is your name?    ")

set_background("All_Gizah_Pyramids")

s1 = create_sprite("spruite", -200, 0)
s2 = create_sprite("images", 200, 0)

s1.color("white")
s2.color("pink")
time.sleep(5)

s1.write("Hi john not quite my tempo",font = ("Arial", 20, "normal"))
window.update()
time.sleep(4)

s1.clear()
window.update()
time.sleep(1)

s2.write("hey cranberry sprite",font = ("cursive", 20, "normal"),align= "left")
window.update()
time.sleep(3)

s2.clear()
window.update()
time.sleep(1)

s1.write(f"I'm looking for my pookie wookie bear {player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(4)

s1.clear()
s1.write("but like wanna play fortnite?",font = ("arial", 20, "normal"))
window.update()
time.sleep(3)

s1.clear()
s2.write("oh yeah cranberry sprite",font = ("cursive", 20, "normal"),align= "left")
window.update()
time.sleep(2)
######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()