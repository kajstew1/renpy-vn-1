# The script of the game goes in this file.





# The game starts here.
label splashscreen:
    scene black 
    with Pause(1)
    show mytext "Dr. Psilicon Presents......" with dissolve
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    # show mytext "The Back Story" with dissolve
    # with Pause(2)

    # hide mytext with dissolve
    # with Pause(1)

    return
    
label splashscreen2:
    scene black
    with Pause(1)
    show mytext "You find yourself waking up on a crash ship."
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    # show mytext "So Start your journey now!"
    # with Pause(2)

    # hide mytext with dissolve
    # with Pause(1)

    jump xxxxx

# start of the game
label start:
    
    # Display a message and show an alert box when a button is clicked
    # jump splashscreen2
    
    #show bg_crashsite with dissolve
    scene bg_crashsite with dissolve

    "Person Enters World, wake up on crash ship?"
 
    jump crash_fork


label crash_fork:
    scene bg_fork with dissolve
    
    # terrorlightz.c "Which way do you want to go?"
    #show screen evt_choose_path
   
    menu: 
        "Choose a path."
        "Left..." if (persistent.path_to_outskirts_taken == False or persistent.path_to_tavern_taken == False):
            #show screen evt_choose_path
            #call screen evt_choose_route with dissolve
            $ persistent.path_to_town_taken = True
            jump path_town_fork
        "Right..." if persistent.path_to_hut_taken == False:
            #show screen evt_choose_path 
            #call screen evt_choose_route with dissolve
            $ persistent.path_to_hut_taken = True
            jump path_hut
        "No thank you!": 
            return
    
    
    return

label path_hut:
    #show bg_tavern with dissolve
    hide screen evt_choose_path
    scene bg_hut with dissolve

    show terrorlightz_talking at left
    
    terrorlightz.c "Come inside to meet me."

    jump hut_meet_terrorlightz
    

label hut_meet_terrorlightz:
    scene bg_insidehut with dissolve

    show terrorlightz_talking at right
    
    terrorlightz.c "Some text meeting terrorlightz."

    jump hut_forage

label hut_forage:
    scene bg_hut with dissolve

    show terrorlightz_talking at right

    terrorlightz.c "Some text foraging."

    jump hut_remember

label hut_remember:
    scene bg_hut with dissolve

    show terrorlightz_talking at right

    terrorlightz.c "Some text remembering eating mushrooms on a way spaceship."

    jump game_over


label path_town_fork:
    scene bg_town with dissolve
    
    # terrorlightz.c "Which way do you want to go?"
    #show screen evt_choose_path
    menu: 
        "Choose a path."
        "Town..." if persistent.path_to_outskirts_taken == False:
            #show screen evt_cthoose_path
            #call screen evt_choose_route with dissolve
            $ persistent.path_to_outskirts_taken = True
            jump path_town_outskirts
        "Tavern..." if persistent.path_to_tavern_taken == False:
            #show screen evt_choose_path 
            #call screen evt_choose_route with dissolve
            $ persistent.path_to_tavern_taken = True
            jump path_tavern
       
    


label path_town_outskirts:
    #show bg_tavern with dissolve
    #call screen bg_hut
    hide screen evt_choose_path
    scene bg_townoutskirts with dissolve
    
    show mysteryspacewoman at left

    "Hi. Could I get directions?"
    #mysteryspacewoman.c "some text"

    jump town_alley


label town_alley:
    scene bg_townalley with dissolve

    show terrorlightztalking at right

    terrorlightz.c "Following a girl to a dark alley."

    jump game_over




label path_tavern:
    #show bg_tavern with dissolve
    hide screen evt_choose_path

    call screen tavern_nav
    
    jump tavern_drink



label path_tavern_alt:
    # to unlock 3d perspectives
    camera:
        perspective True

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    hide screen evt_choose_path

    #scene bg_tavern
    call screen tavern_nav

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show drp casual neutral at left

    drpsilicon.c "You've created a new Ren'Py game."

    show  gnome casual neutral at right with dissolve

    gnome.c "Hi I am a gnome"

    drpsilicon.c "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label game_over:
    menu: 
        "You have died.  Would you like to restart?"
        "Yes":
            jump start
        "No":
            return

label placeholder:
    jump start


label variable1: 
    hide screen evt_choose_char
    $ player_name = renpy.input("what would you like to name your character?") 

    scene black
    n "Synopsis: You, as the protagonist, are a high school student who is struggling with English class. One day, while cleaning out the school library, they discover a mysterious book that seems to be missing some pages. As they begin to read the book, they are transported into the story and must find the missing pages in order to return to their own world."
    jump bAct1
    

label variable2: 
    hide screen evt_choose_char
    $ player_name = renpy.input("what would you like to name your character?") 
    
    scene black
    n "Synopsis: You, as the protagonist, are a high school student who is struggling with English class. One day, while cleaning out the school library, they discover a mysterious book that seems to be missing some pages. As they begin to read the book, they are transported into the story and must find the missing pages in order to return to their own world."
    jump gAct1
