init python:
    class Actor:
        def __init__(self, character, name):
            self.c = character
            self.name = name


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define drpsilicon =  Actor(Character("Dr. Psilicon", who_color="ffff00", what_color="#8ac924"), "Dr. Psilicon")

#define gnome = Actor(Character("Gnome", who_color="#c00606"), "Gnome")

define terrorlightz = Actor(Character("Terrorlightz", color="#460beb"), "Terrorlightz")

define commercialcris = Actor(Character("Commercial Cris", color="#460beb"), "Commercial Cris")

define mysteryspacewoman = Actor(Character("Mystery Space Woman", color="#460beb"), "Mystery Space Woman")


# backgrounds 
#image bg_tavern  = "backgrounds/tavern/bg_tavern.png"

#image bg_choose_path = "bg_tavern"


# images
image drp casual neutral = "drp_casual_neutral.png"
image drp casual talking = "drp_casual_talking.png"

image terrorlightz neutral = "terrorlightz_neutral.png"
image terrorlightz talking = "terrorlightz_talking.png"
#image gnome casual neutral = "gnome_casual_neutral.png"

image mysteryspacewoman neutral = "msw_neutral.png"
image mysteryspacewoman talking = "msw_talking.png"

image commercialcris neutral = "cc_neutral.png"
image commercialcris talking = "cc_talking.png"


# variables
default persistent.path_to_hut_taken = False
default persistent.path_to_town_taken = False
default persistent.path_to_outskirts_taken = False
default persistent.path_to_tavern_taken = False

# to disable chosen paths
#define config.menu_include_disabled = True

image mytext = ParameterizedText(style="something")
style something:
    outlines [(3, "#000", 0, 0 )]
    xalign 0.5
    yalign 0.5
    
