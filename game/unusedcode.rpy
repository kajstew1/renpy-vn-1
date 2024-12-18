
label set_customization_name_vars:
    #$ quick_menu = False
    #$ _skipping = False #disable skip
    $ player_name = [player_name]
    show screen enterName
    $ renpy.pause(hard=False) #we are using this to stop the the game, but unfortunately skip and auto will ignore this so that's why we disabled skip and auto
#    $ player_name = renpy.input("what would you like to name your character?") 
    $ player_name = player_name.strip()
    "Player name [player_name]"

    jump path_char_customization
    


label set_customization_name_vars1:
    #your text
#    "Now, what is my name?"
    #these things I added for preparation
    #$ quick_menu = False
    #$ _skipping = False #disable skip
    $ player_name = ""
    show screen enterName #you do this when you want to show the screen
    $ _preferences.afm_enable = False #turn off auto
    $ renpy.pause(hard=False) #we are using this to stop the the game, but unfortunately skip and auto will ignore this so that's why we disabled skip and auto


#now we create the label continue to jump here after we decide the name
label enter_name_continue:
    $ player_name = player_name.strip()#this removes spaces at the end

    if player_name == "":
        $ player_name = player_name_default #here you type a name, that will be used, if the player types nothing

    hide screen enterName

    $ quick_menu = True
    $ _skipping = True
    #and now you can continue the game.
    
label path_choose_char:
    scene black 
    show img_customization with dissolve
#    show ccl cc_breathing at right
    
    $LongNVLText(narrator, (
    '''\
Hello.Hello.Hello.Hello.Hello.Hello.Hello.Hello.
    '''
    ))

    narrator  "Hi Hi Hi Hi Hi Hi Hi Hi "

    $LongNVLText(mysteryspacewoman.c, (
    '''\
Yo Yo Yo Yo Yo Yo Yo Yo Yo Yo Yo Yo Yo Yo.”
    '''
    ))

    show screen evt_choose_char_txtbox 
    call screen evt_choose_char_images with dissolve



#    menu: 
#        "Would you like to choose your character?"
#        "Ok...":
#            show screen evt_choose_char_txtbox 
#            call screen evt_choose_char_images with dissolve
#        "No thank you!": 
#            return
#    jump path_choose_pronoun



label path_chose_char1: 
    scene black 
    hide screen evt_choose_char_txtbox
    show img_customization
    $ player_name = renpy.input("what would you like to name your character?") 
    $ player_name = player_name.strip()


#    scene black
#    $LongNVLText(narrator, (
#    '''\
#Synopsis: You, as the protagonist, are a high school student who is struggling with English class. One day, while cleaning out the school library, they discover a mysterious book that seems to be missing some pages. As they begin to read the book, they are transported into the story and must find the missing pages in order to return to their own world.
#    '''
#    ))
    jump path_choose_pronoun
    

label path_chose_char2: 
    scene black 
    hide screen evt_choose_char_txtbox
    show img_customization 
    $ player_name = renpy.input("what would you like to name your character?") 
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "[player_name_default]"

    
#    scene black
#    $LongNVLText(narrator, (
#    '''\
#Synopsis: You, as the protagonist, are a high school student who is struggling with English class. One day, while cleaning out the school library, they discover a mysterious book that seems to be missing some pages. As they begin to read the book, they are transported into the story and must find the missing pages in order to return to their own world.
#    '''
#    ))
    jump path_choose_pronoun

label path_choose_pronoun:
#    scene black

    #narrator "Now, let's see an example of how this works. I'm going to call up the pronoun menu."

    call pronounselection # This calls a choice menu to select pronouns.

    narrator "Good, you selected pronouns! You chose [selectedpronouns!t], right?"

    narrator "(You can change pronouns if you want by selecting Prefs > Pronouns > Select Pronouns.)"

    #narrator "To show a set of specific pronouns, you can use the following code after replacing the # with the correct number:\n\n{color=#7f7fff}[[pronounlist[[#]!t]{/color}"

    #narrator "For example, if you wanted to display [pronounlist[0]!t], since that is #0 in the list in pronountool.rpy, you would use the following code:\n\n{color=#7f7fff}[[pronounlist[[0]!t\]{/color}"
    jump path_crash_site


# not currently used
label splashscreen2:
    scene main_menu_background
    show drp_logo
    
    show screen main_menu

    #show drp_motions dr_p_breathing
    #show mytext "What name would you like to use?"
    # $ player_name = renpy.input("What is your name?")
    # $ player_name = player_name.strip()

    # if player_name == "":
    #     $ player_name="[player_name_default]"


    # show mytext "So Start your journey now!"
    # with Pause(2)

    # hide mytext with dissolve
    # with Pause(1)

    jump path_crash_site
    #return
