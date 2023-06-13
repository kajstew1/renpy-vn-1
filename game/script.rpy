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
    
    # terrorlytz.c "Which way do you want to go?"
    show screen evt_choose_path
    menu: 
        "Left...":
            #show screen evt_choose_path
            #call screen evt_choose_route with dissolve
            jump path_town_fork
        "Right...":
            #show screen evt_choose_path 
            #call screen evt_choose_route with dissolve
            jump path_hut
        "No thank you!": 
            return
    
    
    return

label path_hut:
    #show bg_tavern with dissolve
    hide screen evt_choose_path
    scene bg_hut with dissolve

    #show terrorlytztalking at left
    
    terrorlytz.c "Come inside to meet me."

    jump hut_meet_terrorlytz
    

label hut_meet_terrorlytz:
    scene bg_insidehut with dissolve

    show terrorlytztalking at right
    
    terrorlytz.c "Some text meeting terrorlytz."

    jump hut_forage

label hut_forage:
    scene bg_hut with dissolve

    show terrorlytztalking at right

    terrorlytz.c "Some text foraging."

    jump hut_remember

label hut_remember:
    scene bg_hut with dissolve

    show terrorlytztalking at right

    terrorlytz.c "Some text remembering eating mushrooms on a way spaceship."

    return


label path_town_fork:
    scene bg_town with dissolve
    
    # terrorlytz.c "Which way do you want to go?"
    show screen evt_choose_path
    menu: 
        "Town...":
            #show screen evt_choose_path
            #call screen evt_choose_route with dissolve
            jump path_town_outskirts
        "Tavern...":
            #show screen evt_choose_path 
            #call screen evt_choose_route with dissolve
            jump path_tavern
       
    


label path_town_outskirts:
    #show bg_tavern with dissolve
    #call screen bg_hut
    hide screen evt_choose_path
    scene bg_townoutskirts with dissolve
    
    show mysteryspacewoman at left

    "Hi. Could I get directions?"
    #mysteryspacewoman.c "some text"

    return


label town_alley:
    scene bg_townalley with dissolve

    show terrorlytztalking at right

    terrorlytz.c "Following a girl to a dark alley."

    return




label path_tavern_alt:
    #show bg_tavern with dissolve
    hide screen evt_choose_path

    call screen tavern_nav
    
    jump tavern_drink



label path_tavern:
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
