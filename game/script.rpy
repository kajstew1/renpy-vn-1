# The script of the game goes in this file.

# put in a separate classes file 
init python:
    class Actor:
        def __init__(self, character, name):
            self.c = character
            self.name = name

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define drp =  Actor(Character("Dr. Psilicon", who_color="ffff00", what_color="#5e1f1f"), "Dr. Psilicon")

define gnome = Actor(Character("Gnome"), "Gnome")

image drp casual neutral = "drp_casual_neutral.png"
image drp casual talking = "drp_casual_talking.png"
image gnome casual neutral = "gnome_casual_neutral.png"

# The game starts here.

label start:

    # to unlock 3d perspectives
    camera:
        perspective True

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_tavern

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show drp casual neutral at left

    drp.c "You've created a new Ren'Py game."

    show  gnome casual neutral at right with dissolve

    gnome.c "Hi I am a gnome"

    drp.c "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
