init python:
    class Actor:
        def __init__(self, character, name):
            self.c = character
            self.name = name


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define drpsilicon =  Actor(Character("Dr. Psilicon", who_color="ffff00", what_color="#5e1f1f"), "Dr. Psilicon")

define gnome = Actor(Character("Gnome", who_color="#c00606"), "Gnome")

define terrorlytz = Actor(Character("Terrorlytz", color="#460beb"), "Terrorlytz")



# backgrounds 
image bg_tavern  = "backgrounds/tavern/bg_tavern.png"

image bg_choose_path = "bg_tavern"



image drp casual neutral = "drp_casual_neutral.png"
image drp casual talking = "drp_casual_talking.png"
image gnome casual neutral = "gnome_casual_neutral.png"

image mytext = ParameterizedText(style="something")

style something:
    outlines [(3, "#000", 0, 0 )]
    xalign 0.5
    yalign 0.5
    
