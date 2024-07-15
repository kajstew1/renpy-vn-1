init python:
    
    class Actor:
        def __init__(self, character, name):
            self.c = character
            self.name = name

    seen_labels = Set([])

    def _shake_function(trans, st, at, dt=.5, dist=64):
        #dt is duration timebase, dist is maximum shake distance in pixel
        if st <= dt: 
            trans.xoffset = int((dt-st)*dist*(.5-renpy.random.random())*2)
            trans.yoffset = int((dt-st)*dist*(.5-renpy.random.random())*2)
            return 1.0/60
        else:
            return None
           

    def eyewarp(x):
        return x**1.33

    vpunch = Move((0, 40), (0, -40), .10, bounce=True, repeat=True, delay=.275)

    #eye_open = ImageDissolve("bg_crashsite", 1.5, ramplen=128, reverse=False, time_warp=eyewarp)
    #eye_shut = ImageDissolve("backgrounds/eyeopen.png", 1.5, ramplen=128, reverse=True, time_warp=eyewarp)

    #eyeopen = ImageDissolve("bg_crashsite", 1.5, 100)
    #eyeclose = ImageDissolve("backgrounds/eyeopen.png", 1.5, 100, reverse=True)

    def MyLive2D(*args, fallback=Placeholder(text="no live2d"), **kwargs):
        if renpy.has_live2d():
            return Live2D(*args, **kwargs)
        else:
            return fallback

# variables
default persistent.path_variables_set = False
default persistent.path_to_hut_taken = False
default persistent.path_to_town_taken = False
default persistent.path_to_outskirts_taken = False
default persistent.path_to_tavern_taken = False

# to disable chosen paths
define config.menu_include_disabled = True

define in_eye_fast = ImageDissolve("images/eye.png", 1.0)
define out_eye_fast = ImageDissolve("images/eye.png", 1.0, reverse=True)
define in_eye = ImageDissolve("images/eye.png", 6.0)
define out_eye = ImageDissolve("images/eye.png", 6.0, reverse=True)

image black:
    Solid("#000")
image white:
    Solid("#FFF")


image img_cockpit = im.Scale("backgrounds/bg_cockpit.jpg", 1920, 1080)

image img_customization = im.Scale("backgrounds/bg_customization.jpg", 1920, 1080)

#choosescreen 
image boychar:
    "boy.png" 
    zoom 0.60 
 
image girlchar: 
    "girl.png" 
    zoom 0.50 
 
image boychar2: 
    "boy2.png" 
    zoom 0.50 
    
image girlchar2: 
    "girl2.png" 
    zoom 0.60 


#default she_selected = False
#default he_selected = False
#default they_selected = True
default pronoun1_selected = "they"
default pronouns = "They/Them"
default pronoun1 = "they"
default pronoun2 = "them"
default pronoun3 = "their"
default be = "are"
default screen_tooltip = ""

#selectedpronouns = pronounlist[pronoun]
# they = theylist[pronoun]
# them = themlist[pronoun]
# their = theirlist[pronoun]
# theirs = theirslist[pronoun]
# s = slist[pronoun]
# es = eslist[pronoun]
# are = arelist[pronoun]





# Declare characters used by this game. The color argument colorizes the
# name of the character.

default player_name_default = "Space Traveler"
define player = Character("[player_name]")
default player_name = player_name_default
default p_player_name_input = VariableInputValue("player_name", default=False)


image drp_motions = MyLive2D("images/dr_p_motions", default_fade=0.0, loop=True, fallback="dr_p casual talking")
    

##  Declare characters here
#define config.layers = [ 'master', 'transient','screens','character', 'overlay' ] #make a whole new layer for the char- screw side image(i never quite get it anyway)!
#define config.tag_layer = {'narrator_img':'character'}  #tag it so every cohan image is automatically place on the 'character' layer. Alternatively, you can use "onlayer" to manually put him in there every time
#define config.menu_clear_layers = ['character'] # clear it so the char will disappear when enter game screen, otherwise he will awkwardly stay there
  
#define sidenarrator1 = Character(None, image="narrator_img")


define char = Character('Me', image="charimage")
image side charimage = MyLive2D("images/myst_s_woman_motions/myst_s_woman_motions.model3.json", loop=True, fallback="mysteryspacewoman talking")

define sidenarrator = Character (None, image="narrator_img")
image side narrator_img = MyLive2D("images/protagonist_motions/protagonist_motions.model3.json", loop=True, zoom=1.0, fallback="side_protagonist_neutral")
#image side narrator_img = Live2D("images/protagonist_motions/protagonist_motions.model3.json", loop=True, motions="protag_breathing", zoom=.1)

#image side narrator_img = "side_protagonist_neutral"

image ccl = MyLive2D("images/cc_motions", default_fade=0.0, top=0.0, base=1.0, height=1.0, loop=True, fallback="commercialcris talking")
image mswl = MyLive2D("images/myst_s_woman_motions", default_fade=0.0, top=0.0, base=1.0, height=1.0, loop=True, fallback="mysteryspacewoman talking")
image protl = MyLive2D("images/protagonist_motions", default_fade=0.0, top=0.0, base=1.0, height=1.0, loop=True, fallback="protagonist talking")
image tll = MyLive2D("images/terrorlightz_motions", default_fade=0.0, top=0.0, base=1.0, height=1.0, loop=True, fallback="terrorlightz talking")
image drpl = MyLive2D("images/dr_p_motions", default_fade=0.0, top=0.0, base=1.0, height=1.0, loop=True, fallback="drp casual talking")


define narrator = Character (None) #, what_slow_cps=0, what_font="fontfile_name.ttf")
define narrator_nvl = Character (None, kind=nvl) #, what_slow_cps=0, what_font="fontfile_name.ttf")

define drpsilicon =  Actor(Character("Dr. Psilicon", who_color="9EFB65", what_color="#8ac924"), "Dr. Psilicon")

#define gnome = Actor(Character("Gnome", who_color="#c00606"), "Gnome")

define terrorlightz = Actor(Character("Terrorlightz", color="#E26EFF"), "Terrorlightz")

define commercialcris = Actor(Character("Commercial Cris", color="#D5D5D5"), "Commercial Cris")

define mysteryspacewoman = Actor(Character("Mystery Space Woman", color="#FCA4C5"), "Mystery Space Woman")


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





image mytext = ParameterizedText(style="something")
style something:
    outlines [(3, "#000", 0, 0 )]
    xalign 0.5
    yalign 0.5
    

init -50 python:
    import math

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
                talker (printText)
            
                if (currentPage < totalTextPages): # New page!
                    nvl_clear()

    def LongNVLText1(talker, text):
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
                talker (printText)
            
                if (currentPage < totalTextPages): # New page!
                    nvl_clear()

    #
    
#
