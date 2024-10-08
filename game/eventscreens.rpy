


screen reset_paths():
    $ persistent.path_variables_set = False
    $ persistent.path_to_hut_taken = False
    $ persistent.path_to_town_taken = False
    $ persistent.path_to_outskirts_taken = False
    $ persistent.path_to_tavern_taken = False 
    $ persistent.__dict__['_chosen'] = {}

style reset_paths_text is text:
    size 45
    hover_color "#FF00FF"             # Pink
    outlines [ (0, "#0000FF", 1, 1) ] # Blue
    color "#FF0000"                   # Red

screen evt_choose_char_txtbox:
    hbox:
        xalign 0.5
        yalign 0.1
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Choose your character."


screen evt_choose_char_images: 
    hbox: 
        xalign 0.5 
        yalign 0.5 
        yoffset 30 
        spacing 20 
        imagebutton: 
            idle "boychar2" 
            hover "boychar" 
            action Jump("path_chose_char1") 
        imagebutton: 
            idle "girlchar" 
            hover "girlchar2" 
            action Jump("path_chose_char2") 







screen evt_choose_path:
    hbox:
        xalign 0.5
        yalign 0.9
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Choose a path."

screen evt_choose_town_path:
    hbox:
        xalign 0.5
        yalign 0.1
        frame:
            background "#706969"
            xalign 0.5
            yalign 0.5
            padding (50,50)
            margin (0,0,10,0)
            text "Choose a path."

screen showName:
    style_prefix "showName"
    frame: #now we want to do vbox to make the input below the textbox
        xpos 550 #with this you define location of the vbox (if you would type xalign 0 and yalign 0 it would appear in top left corner)
        ypos 700
        xpadding 50
        ypadding 15
        xsize 690
        ysize 68
        add Solid ("000000")
        text "[player_name]"
        #there is a link to all of positional properties: https://www.renpy.org/doc/html/style_properties.html#position-style-properties
        #text "What is your name?": #we added text using this
        #    size 20 #in here you can edit the text with those: https://www.renpy.org/doc/html/style_properties.html#text-style-properties
        #    at transform: #with this you can animate the text
        #            alpha 0 #here you type parameters which are used at first
        #            pause 0.5 #you can add a pause
        #            linear 2 alpha 1.0 #now you add how it's changed (I used linear but here are all: https://www.renpy.org/doc/html/atl.html#warpers) then the time of the animation and then to what it is changed



screen enterName:
    style_prefix "enterName"
    frame: #now we want to do vbox to make the input below the textbox
        xpos 550 #with this you define location of the vbox (if you would type xalign 0 and yalign 0 it would appear in top left corner)
        ypos 700
        xpadding 50
        ypadding 15
        xsize 690
        ysize 68
        add Solid ("000000")
 
        input default "[player_name]":# now we add input which will be below the text because it's in the vbox. In default you can type something that will be already typed when the screen will be shown
            xanchor 0
            pixel_width(500) # this to not allow too long name
            value VariableInputValue("player_name") # with this you save the input to a variable.




# renpy.call_screen
screen screen_customization_nav:
    add "bg_customization"
    modal True  # prevents from interacting with assets under or below it
#    add screen showName
    
    
    #frame:
        #textbutton "Dismiss":
        #    xalign 0.5
        #    action Jump ("start")

    frame: #now we want to do vbox to make the input below the textbox
        xanchor 0.5
        yanchor 0.5
        xpos 895 #with this you define location of the vbox (if you would type xalign 0 and yalign 0 it would appear in top left corner)
        ypos 735
        xpadding 0  #50
        ypadding 0  #15
        xsize 600 #
        ysize 50 #68
        add Solid ("#9799FF") #("#00FFFF") 
        #background "backgrounds/character_customization/cc_name_box.png" #Assuming it is located in the images folder.
        #there is a link to all of positional properties: https://www.renpy.org/doc/html/style_properties.html#position-style-properties
        #text "What is your name?": #we added text using this
        #    size 20 #in here you can edit the text with those: https://www.renpy.org/doc/html/style_properties.html#text-style-properties
        #    at transform: #with this you can animate the text
        #            alpha 0 #here you type parameters which are used at first
        #            pause 0.5 #you can add a pause
        #            linear 2 alpha 1.0 #now you add how it's changed (I used linear but here are all: https://www.renpy.org/doc/html/atl.html#warpers) then the time of the animation and then to what it is changed

        #input default "[player_name]":#now we add input which will be below the text because it's in the vbox. In default you can type something that will be already typed when the screen will be shown
        #    xanchor 0.5
        #    pixel_width(500)#this to not allow too long name
        #    value VariableInputValue("player_name")#with this you save the input to a variable.
        style_prefix "enterName"
        hbox:
            button:
                xsize 600
                input:  
                    pixel_width(500)
                    value VariableInputValue("player_name") # with this you save the input to a variable.
                #action p_player_name_input.Toggle()
                action SetVariable("player_name", player_name)

    imagebutton auto "cc_she_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "She/Her")
        unhovered SetVariable("screen_tooltip", "")
        #action ToggleVariable("she_selected", True, False)
        #action [ToggleVariable("she_selected", True, False), SelectedIf(she_selected), If ("cc_she" in seen_labels, false=[Hide(None), None, Jump("set_customization_she_vars")])]
        action [SetVariable ("pronoun1_selected", "she"), SelectedIf(pronoun1_selected =="she"), If ("cc_she" in seen_labels, false=[Hide(None), None, Call("set_customization_she_vars")])]
 

    imagebutton auto "cc_he_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "He/Him")
        unhovered SetVariable("screen_tooltip", "")
        #action [ToggleVariable("he_selected", True, False), SelectedIf(he_selected),If ("cc_he" in seen_labels, false=[Hide(None), None, Jump("set_customization_he_vars")])]
        action [SetVariable ("pronoun1_selected", "she"), SelectedIf(pronoun1_selected =="he"), If ("cc_he" in seen_labels, false=[Hide(None), None, Call("set_customization_he_vars")])]
        #action ToggleVariable("he_selected", True, False)
        #action [If ("cc_she" in seen_labels, false=[Hide(None), None, Call("set_customization_he_vars")], SelectedIf(he_selected))]

    imagebutton auto "cc_they_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "They/Them")
        unhovered SetVariable("screen_tooltip", "")
        #action [ToggleVariable("they_selected", True, False), SelectedIf(they_selected),If ("cc_they" in seen_labels, false=[Hide(None), None, Jump("set_customization_they_vars")])]
        action [SetVariable ("pronoun1_selected", "she"), SelectedIf(pronoun1_selected =="they"), If ("cc_they" in seen_labels, false=[Hide(None), None, Call("set_customization_they_vars")])]
        #action ToggleVariable("they_selected", True, False)
        #action [If ("cc_they" in seen_labels, false=[Hide(None), None, Call("set_customization_she_vars")], SelectedIf(they_selected))]

    imagebutton auto "cc_confirm_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "Confirm")
        unhovered SetVariable("screen_tooltip", "")
        action If ("cc_confirm" in seen_labels, false=[Hide(None), None, Jump("path_crash_site")])

#    frame:
#        xpadding 50
#        ypadding 5
#        xalign 0.1
#        yalign 0.1
#        textbutton "Continue" action Jump("path_crash_site")
    
    #imagebutton auto "cc_name_%s":
    #    focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
    #    hovered SetVariable("screen_tooltip", "name")
    #    unhovered SetVariable("screen_tooltip", "")
    #    action If ("cc_name" in seen_labels, false=[Hide(None), None, Jump("set_customization_name_vars")])
 
    

style enterName_input:
    size 30
    color "000000"
    hover_color "#7836f4"
    bold True
    
    

style showName_text:
    size 30
    color "#F44336"


screen screen_crash_fork_nav:
    add "bg_fork"
    modal True  # prevents from interacting with assets under or below it
#    add screen showName

    hbox:
        xalign 0.5
        yalign 0.5
        xanchor 0.5
        xsize 500
        #ysize 500

        frame:
            background "#706969"
            
            #padding (50,50)
            #margin (0,0,10,0)
            text "[screen_tooltip]"

    imagebutton auto "left_moon_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "To your left, you spot an iridescent colored moon surrounded by four small planets. You aren’t sure why, but you feel a sense of warmth when you look at them.")
        unhovered SetVariable("screen_tooltip", "")
        action If ("cc_name" in seen_labels, false=[Hide(None), None, Jump("set_customization_name_vars")])



    imagebutton auto "left_path_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "Below you to your left, you observe a smooth, sandy-looking path leading out towards a lush outcropping of mountains.")
        unhovered SetVariable("screen_tooltip", "")
        action NullAction()

    imagebutton auto "right_moon_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "To your right, you spot a colossal moon. Its deeply cavernous, cerulean craters are in sharp contrast to the lighter-colored surface, creating a dangerously beautiful contrast. The longer you stare at it, the more uneasy you feel.")
        unhovered SetVariable("screen_tooltip", "")
        action NullAction()
 
    imagebutton auto "right_path_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "Below you to your right, you see a rocky, gravel path leading to a sparse spread of jagged, narrow mountains. When you lean to the side to get a better look at where the path leads, you think you see an opening. Could that be a tunnel?")
        unhovered SetVariable("screen_tooltip", "")
        action NullAction()

    frame:
        xpadding 50
        ypadding 5
        xalign 0.5
        yalign 0.1
        xanchor 0.5
        textbutton "Click to continue after checking the area" action Jump("crash_fork_menu")

screen tavern_nav:
    add "bg_tavern"
    modal True  # prevents from interacting with assets under or below it
    
    imagebutton auto "tavern_bin_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "Bin")
        unhovered SetVariable("screen_tooltip", "")
        action If ("tavern_bin" in seen_labels, false=[Hide(None), None, Jump ("path_tavern_bin")])
        
    imagebutton auto "tavern_heater_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "Heater")
        unhovered SetVariable("screen_tooltip", "")
        action If ("tavern_heater" in seen_labels, false=[Hide(None), None, Jump ("path_tavern_heater")])

    imagebutton auto "tavern_patron_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "Patron")
        unhovered SetVariable("screen_tooltip", "")
        action If ("tavern_patron" in seen_labels, false=[Hide(None), None, Jump ("path_tavern_patron")])

    imagebutton auto "tavern_sign_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "Sign")
        unhovered SetVariable("screen_tooltip", "")
        action If ("tavern_sign" in seen_labels, false=[Hide(None), None, Jump ("path_tavern_sign")])

    frame:
        xpadding 50
        ypadding 5
        xalign 0.1
        yalign 0.1
        textbutton "Continue" action Jump("path_tavern_drink")

