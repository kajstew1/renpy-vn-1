init python:
    class Actor:
        def __init__(self, character, name):
            self.c = character
            self.name = name

    #persistent.__dict__['_chosen'] = {}

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character (None) #, what_slow_cps=0, what_font="fontfile_name.ttf")

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
    

init -50 python:
    def LongNVLText(talker, text):
        text = text.strip()
        splittedText = []

        maxPageLength = 199 # 947Max. number of chars per page
        
        while (len(text) > maxPageLength):
            foundBlankPosition = text.rfind(' ', 0, maxPageLength + 1)
        
            if (foundBlankPosition < 0):
                foundBlankPosition = maxPageLength + 1 # If no blank present then print all you get
                
                
            subText = text[0:foundBlankPosition + 1]
                
            splittedText.append(subText)
                
            text = text[foundBlankPosition:].strip()
            
        if (len(text) > 0):
            splittedText.append(text) # Print all remaining text
        
        totalTextPages = len(splittedText)
        currentPage = 0
        
        for printText in splittedText:
            currentPage = currentPage + 1

            if (len(printText) > 0): # Only print something if there is something to print
                talker(printText)
            
                if (currentPage < totalTextPages): # New page!
                    nvl_clear()

