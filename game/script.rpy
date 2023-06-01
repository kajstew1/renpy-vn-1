# The script of the game goes in this file.





# The game starts here.
label splashscreen:
    scene black 
    with Pause(1)
    show mytext "Dr. Psilicon Presents......" with dissolve
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    show mytext "The Back Story" with dissolve
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    return
    
label splashscreen2:
    scene black
    with Pause(1)
    show mytext "You find yourself waking up on a crash ship."
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    show mytext "So Start your journey now!"
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    jump path

# start of the game
label start:
    
    # Display a message and show an alert box when a button is clicked
    jump splashscreen2
    
label path:
    #show bg_tavern with dissolve
    call screen tavern_nav
    

label placeholder:
    scene bg_tavern with dissolve
    menu: 
        "Left...":
            show screen evt_choose_char 
            call screen evt_choose_route with dissolve
        "Right...":
            show screen evt_choose_char 
            call screen evt_choose_route with dissolve
        "No thank you!": 
            return

    drpsilicon.c "Placeholder jump."
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


label tavern:
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

    drpsilicon.c "You've created a new Ren'Py game."

    show  gnome casual neutral at right with dissolve

    gnome.c "Hi I am a gnome"

    drpsilicon.c "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
