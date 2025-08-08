init python:
    
    class Actor:
        def __init__(self, character, name):
            self.c = character
            self.name = name

    seen_labels = Set([])

    # not currently used
    def _shake_function(trans, st, at, dt=.5, dist=64):
        #dt is duration timebase, dist is maximum shake distance in pixel
        if st <= dt: 
            trans.xoffset = int((dt-st)*dist*(.5-renpy.random.random())*2)
            trans.yoffset = int((dt-st)*dist*(.5-renpy.random.random())*2)
            return 1.0/60
        else:
            return None
           
    # not currently used
    def eyewarp(x):
        return x**1.33

    vpunch = Move((0, 40), (0, -40), .10, bounce=True, repeat=True, delay=.275)

    #eye_open = ImageDissolve("bg_crashsite", 1.5, ramplen=128, reverse=False, time_warp=eyewarp)
    #eye_shut = ImageDissolve("backgrounds/eyeopen.png", 1.5, ramplen=128, reverse=True, time_warp=eyewarp)

    #eyeopen = ImageDissolve("bg_crashsite", 1.5, 100)
    #eyeclose = ImageDissolve("backgrounds/eyeopen.png", 1.5, 100, reverse=True)

    # used to define Live2D images
    def MyLive2D(*args, fallback=Placeholder(text="no live2d"), **kwargs):
        if renpy.has_live2d():
            return Live2D(*args, **kwargs)
        else:
            return fallback

    renpy.register_shader("custom.black_transparent", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
    """, fragment_300="""
        vec4 color = texture2D(tex0, v_tex_coord);
        
        /* Calculate brightness of the pixel */
        float brightness = (color.r + color.g + color.b) / 3.0;
        
        /* Create a smooth transition from transparent to opaque */
        float threshold = 0.1; /* Adjust this value as needed */
        
        if (brightness < threshold) {
            /* Make dark pixels transparent */
            gl_FragColor = vec4(color.rgb, 0.0);
        } else {
            /* Keep original color and alpha */
            gl_FragColor = color;
        }
    """)


init -100:

    # used to resize the main menu buttons
    transform buttonZoom:
        zoom .7

    transform smoke_drift:
        alpha 0.0
        parallel:
            ease 2.0 alpha 0.3
            ease 2.0 alpha 0.0
        parallel:
            ypos 0.5
            linear 4.0 ypos 0.0
        parallel:
            xpos 0.5
            ease 4.0 xpos 0.48 + 0.04 * renpy.random.random()

    #image smoke_particle:
        # Create a circular shape using Transform
        # Transform("images/smoke_particle.png", size=(20, 20))
        # Make it semi-transparent gray
        # matrixcolor ColorizeMatrix("#808080", "#808080")
        # alpha 0.3
        # Add some blur for softness
        # blur 3.0

    image smoke_effect1:
        Fixed(
            SnowBlossom("images/smoke_particle.png", 
                count=15,        # Number of particles
                border=350,       # Border around the screen
                xspeed=(-2, 20),  # Horizontal drift speed range
                yspeed=(-30, -20), # Upward speed range
                start=0,         # Start immediately
                horizontal=False, # Vertical movement
            )
        )

    image smoke_effect2:
        Fixed(
            SnowBlossom("images/smoke_particle.png", 
                count=12,        # Number of particles
                border=350,       # Border around the screen
                xspeed=(-20, 2),  # Horizontal drift speed range
                yspeed=(-20, -20), # Upward speed range
                start=20,         # Start immediately
                horizontal=False, # Vertical movement
            )
        )

    image smoke_effect3:
        Fixed(
            SnowBlossom("images/smoke_particle.png", 
                count=10,        # Number of particles
                border=350,       # Border around the screen
                xspeed=(-20, 2),  # Horizontal drift speed range
                yspeed=(-20, -20), # Upward speed range
                start=40,         # Start immediately
                horizontal=False, # Vertical movement
            )
        )
    #image snow1 = Fixed(SnowBlossom("images/smoke_particle.png", 50, xspeed=(20, 50), yspeed=(100, 200), start=50))
    #image snow2 = Fixed(SnowBlossom("gui/smoke_particle.png", 50, xspeed=(20, 50), yspeed=(100, 200), start=50))

    transform my_shake:
        parallel:
            easein 0.2 xoffset 0 yoffset 30
            easeout 0.2 xoffset 0 yoffset -30
            #linear 0.1 xoffset 0 yoffset 10
            #linear 0.1 xoffset 0 yoffset -15
            #linear 0.1 xoffset 0 yoffset 0
            repeat 30
        parallel:
            linear 10 zoom 1.5


    # called from Scene 2b while taking the right path
    transform my_running:
        parallel:
            easein 0.2 xoffset 0 yoffset 30
            easeout 0.2 xoffset 0 yoffset -30
            #linear 0.1 xoffset 0 yoffset 10
            #linear 0.1 xoffset 0 yoffset -15
            #linear 0.1 xoffset 0 yoffset 0
            repeat
        parallel:
            linear 10 zoom 1.5
        parallel:
            # take 1.3 seconds to move right edge of the image against the right edge of the screen
            linear 1.3 xalign 0.9 yalign 0.9

    transform my_bump:
        easein 0.2 xoffset 0 yoffset 100
        easeout 0.2 xoffset 0 yoffset -120
        #linear 0.1 xoffset 0 yoffset 10
        #linear 0.1 xoffset 0 yoffset -15
        #linear 0.1 xoffset 0 yoffset 0
        #repeat 10

    # Called from Scene 2h
    transform my_walking:
        parallel:
            easein 0.4 xoffset 0 yoffset 30
            easeout 0.4 xoffset 0 yoffset -30
            #linear 0.1 xoffset 0 yoffset 10
            #linear 0.1 xoffset 0 yoffset -15
            #linear 0.1 xoffset 0 yoffset 0
            repeat
        parallel:
            linear 10 zoom 1.5
        #parallel:
            #easein 4.0 crop (860, 430, 860, 600)

    
    transform shake_and_fade:
        parallel:
            yoffset 0
            ease 0.15 yoffset 8 
            ease 0.15 yoffset -8
            ease 0.15 yoffset 6
            ease 0.15 yoffset -6
            ease 0.15 yoffset 0
        repeat
        parallel:
            alpha 1.0
            ease 1.0 alpha 0.5 
            ease 1.0 alpha 1.0
        repeat
   
    
    transform my_float:
        parallel:
            yoffset 0
            ease .7 yoffset -15  # Move up 10 pixels over 1.5 seconds
            ease .7 yoffset 0    # Move back down over 1.5 seconds
            repeat               # Loop the animation
               

    # called from Scene 4 while returning to the spaceship
    transform str_walking:
        parallel:
            easein 0.6 xoffset 0 yoffset 30
            easeout 0.6 xoffset 0 yoffset -30
            #linear 0.1 xoffset 0 yoffset 15
            #linear 0.1 xoffset 0 yoffset -20
            #linear 0.1 xoffset 0 yoffset 0
            repeat
        parallel:
            linear 10 zoom 1.15
        #parallel:
            #easein 4.0 crop (860, 430, 860, 600)

    # called from Scene 4 while returning to the spaceship and Scene 2h
    transform slow_walking:
        parallel:
            easein 0.7 xoffset 0 yoffset 30
            easeout 0.7 xoffset 0 yoffset -30
            #linear 0.1 xoffset 0 yoffset 10
            #linear 0.1 xoffset 0 yoffset -15
            #linear 0.1 xoffset 0 yoffset 0
            repeat
        parallel:
            linear 10 zoom 1.5
        #parallel:
            #easein 4.0 crop (860, 430, 860, 600)
            
    # A jogging motion that's faster than walking but not as intense as running
    transform my_jogging:
        parallel:
            easein 0.3 xoffset 0 yoffset 35
            easeout 0.3 xoffset 0 yoffset -35
            repeat
        parallel:
            linear 8 zoom 1.5
        parallel:
            linear 0.6 xalign 0.5 yalign 0.5
            
    # Simulates walking into the background with focus maintained at pixel 1200,800
    transform my_walking_focused:
        subpixel True
        # Set the anchor point to the focus coordinates (1200,800 in 1920x1080)
        anchor (0.625, 0.741)  # 1200/1920, 800/1080
        # Position the image so the focus point is centered
        pos (0.625, 0.741)
        parallel:
            # Natural walking gait with realistic timing
            block:
                linear 0.4 yoffset 15
                ease 0.4 yoffset -15
                repeat
            time 30.0  # Start slowing down before zoom completes
            # Gradually reduce the walking motion
            easein 0.4 xoffset 0 yoffset 20
            easeout 0.4 xoffset 0 yoffset -20
            easein 0.5 xoffset 0 yoffset 10
            easeout 0.5 xoffset 0 yoffset -10
            easein 0.6 xoffset 0 yoffset 5
            easeout 0.6 xoffset 0 yoffset 0  # Gently come to rest
        parallel:
            # Enhanced zoom effect to simulate walking deeper into the background
            zoom 1.0
            linear 60 zoom 5.0  # Zoom continues for full 30 seconds
        parallel:
            # Movement toward the focus point
            linear 60 pos (0.5, 0.5)  # Move to center of screen

    # called from Scene 2h
    transform basic_fade:
        on show:
            alpha 0.0
            linear 3.0 alpha 1.0
        on hide:
            alpha 1.0
            linear 10.0 alpha 0.0
  
    transform basic_fade_out:
        alpha 1.0
        linear 1.0 alpha 0.0

    transform basic_fade_in:
        alpha 0.0
        linear 1.0 alpha 1.0

    transform exitright:
        linear 3.0 xpos 1.5 xzoom -1.0

    
    # called from Scene 2g
    transform abstract_scene: 
        subpixel True 
        parallel:
            xpos 0 
            linear 1.41 xpos 15 
            linear 1.58 xpos 0 
            linear 1.69 xpos 15 
            linear 1.69 xpos 0 
        parallel:
            xzoom 1.0 yzoom 1.0 zoom 1.0 
            linear 0.01 xzoom 1.0 yzoom 1.0 zoom 1.0 
        parallel:
            blur 2.0 
            linear 0.85 blur 2.0 
            linear 0.46 blur 10.0 
            linear 0.37 blur 2.0 
            linear 1.63 blur 2.0 
            linear 0.34 blur 15.0 
            linear 0.33 blur 2.0 
            linear 1.16 blur 2.0 
            linear 0.38 blur 15.0 
            linear 0.33 blur 2.0
        repeat
    #with Pause(6.47)



# variables
default persistent.is_new_game = True
default persistent.path_variables_set = False
default persistent.path_to_hut_taken = False
default persistent.path_to_town_taken = False
default persistent.path_to_outskirts_taken = False
default persistent.path_to_tavern_taken = False

# to disable chosen paths
define config.menu_include_disabled = True


# Transitions between Scenes 2e/2f 3a/3b (closing and opening eye)
define in_eye_fast = ImageDissolve("images/eye.png", 1.0)
define out_eye_fast = ImageDissolve("images/eye.png", 1.0, reverse=True)
define in_eye = ImageDissolve("images/eye.png", 6.0)
define out_eye = ImageDissolve("images/eye.png", 6.0, reverse=True)

image black:
    Solid("#000")
image white:
    Solid("#FFF")


# Define your speedline images
image speedline1_transparent:
    "images/output_frame1.png"
    shader "custom.black_transparent"
image speedline2_transparent:
    "images/output_frame2.png"
    shader "custom.black_transparent"
image speedline3_transparent:
    "images/output_frame3.png"
    shader "custom.black_transparent"
image speedline4_transparent:
    "images/output_frame4.png"
    shader "custom.black_transparent"

# Create the animation with transparent background
image speedline_animation:
    shader "custom.black_transparent"  # Apply shader to all frames
    "speedline1_transparent"
    pause 0.1
    "speedline2_transparent" 
    pause 0.1
    "speedline3_transparent"
    pause 0.1
    "speedline4_transparent"
    pause 0.1
    repeat


image main_menu_background = "gui/main_menu.png"
default show_main = False

image img_cockpit = im.Scale("backgrounds/bg_cockpit.jpg", 1920, 1080)

image img_customization = im.Scale("backgrounds/bg_customization.jpg", 1920, 1080)

#image drp_logo = im.Scale("Drpsilicon_logo.png", 1920, 1080)
image drp_logo: 
    xalign 0.5
    yalign 0.1
    im.Scale("Drpsilicon_logo.png", 960, 540)

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

# Important fixes for issues seen
# added to prevent the flashing of the narrator namebox/textbox during pause transitions
# https://lemmasoft.renai.us/forums/viewtopic.php?t=46790
default preferences.show_empty_window = False


# Declare characters used by this game. The color argument colorizes the
# name of the character.

default player_name_default = "Charlie"
define player = Character("[player_name]")
default player_name = player_name_default
default p_player_name_input = VariableInputValue("player_name", default=False)


# Set up for the Live2D protagonist side character (protl)
#   Set layers for the protl side character so stays behind dialogue
#     make a whole new layer for the char for the side character.
define config.layers = [ 'master', 'transient','screens','character', 'overlay' ] 

#tag it so every protl image is automatically place on the 'character' layer. 
#  to place behind the dialogue window
define config.tag_layer = {'protl':'character'}  

# clear it so the char will disappear when enter game screen, otherwise he will awkwardly stay there
define config.menu_clear_layers = ['character'] 

image protl = MyLive2D("images/protagonist_motions", default_fade=0.0, top=0.0, base=1.0, height=1.0, loop=True, fallback="protagonist breathing")




define narrator = Character ("[player_name]") #, what_slow_cps=0, what_font="fontfile_name.ttf")
define narrator_none = Character (None)  #  # called from Scene 2g
define narrator_nvl = Character (None, kind=nvl) #, what_slow_cps=0, what_font="fontfile_name.ttf")


#introduced in Scene 2f
define terrorlightz = Actor(Character("Terrorlightz", color="#E26EFF"), "Terrorlightz")

image tll = MyLive2D("images/terrorlightz_motions", default_fade=0.0, top=0.0, base=1.0, height=1.0, loop=True, fallback="terrorlightz talking")



#introduced in Scene 3b seems to be the protl side character
define drpsilicon =  Actor(Character("Dr. Psilicon", color="#8ac924"), "Dr. Psilicon")

image drp_motions = MyLive2D("images/dr_p_motions", default_fade=0.0, loop=True, fallback="dr_p casual talking")
image drpl = MyLive2D("images/dr_p_motions", default_fade=0.0, top=0.0, base=1.0, height=1.0, loop=True, fallback="drp casual talking")


# introduced in Scene 3c
define commercialcris = Actor(Character("Commercial Cris", color="#fc424b"), "Commercial Cris")

image ccl = MyLive2D("images/cc_motions", default_fade=0.0, top=0.0, base=1.0, height=1.0, loop=True, fallback="commercialcris talking")



# introduced in Scene 3c2
define mysteryspacewoman = Actor(Character("Mystery Space Woman", color="#FCA4C5"), "Mystery Space Woman")

image mswl = MyLive2D("images/myst_s_woman_motions", default_fade=0.0, top=0.0, base=1.0, height=1.0, loop=True, fallback="mysteryspacewoman talking")




define char = Character('Me', image="charimage")
image side charimage = MyLive2D("images/myst_s_woman_motions/myst_s_woman_motions.model3.json", loop=True, fallback="mysteryspacewoman talking")

define sidenarrator = Character (None, image="narrator_img")
image side narrator_img = MyLive2D("images/protagonist_motions/protagonist_motions.model3.json", loop=True, zoom=1.0, fallback="side_protagonist_neutral")
#image side narrator_img = Live2D("images/protagonist_motions/protagonist_motions.model3.json", loop=True, motions="protag_breathing", zoom=.1)
#image side narrator_img = "side_protagonist_neutral"


define belvania = Character("Belvania", color="#82efd2")







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


image growl = "Effects/growl.png"
image roar = "Effects/roar.png"
image smash = "Effects/smash.png"


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
