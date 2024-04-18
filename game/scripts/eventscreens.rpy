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
        #there is a link to all of positional properties: https://www.renpy.org/doc/html/style_properties.html#position-style-properties
        #text "What is your name?": #we added text using this
        #    size 20 #in here you can edit the text with those: https://www.renpy.org/doc/html/style_properties.html#text-style-properties
        #    at transform: #with this you can animate the text
        #            alpha 0 #here you type parameters which are used at first
        #            pause 0.5 #you can add a pause
        #            linear 2 alpha 1.0 #now you add how it's changed (I used linear but here are all: https://www.renpy.org/doc/html/atl.html#warpers) then the time of the animation and then to what it is changed

        input default "[player_name_default]":#now we add input which will be below the text because it's in the vbox. In default you can type something that will be already typed when the screen will be shown
            xanchor 0
            pixel_width(500)#this to not allow too long name
            value VariableInputValue("player_name")#with this you save the input to a variable.

#        textbutton "OK":
#                action Jump("enter_name_continue")#in action you type what will happen, when you click ok
#                keysym('K_RETURN', 'K_KP_ENTER') #you can also add keysym to activate it with a keyboard
#                activate_sound("audio/tick.ogg") #you can also add a sound when clicked

style enterName_input:
    size 30
    color "FFFFFF"

style showName_text:
    size 30
    color "FFFFFF"

# renpy.call_screen
screen screen_customization_nav:
    add "bg_customization"
    modal True  # prevents from interacting with assets under or below it
#    add screen showName

    imagebutton auto "cc_name_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "name")
        unhovered SetVariable("screen_tooltip", "")
        action If ("cc_name" in seen_labels, false=[Hide(None), None, Jump("set_customization_name_vars")])
 
    imagebutton auto "cc_she_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "She/Her")
        unhovered SetVariable("screen_tooltip", "")
        #action ToggleVariable("she_selected", True, False)
        action [ToggleVariable("she_selected", True, False), If ("cc_she" in seen_labels, false=[Hide(None), None, Jump("set_customization_she_vars")])]
        #selected (True)

    imagebutton auto "cc_he_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "He/Him")
        unhovered SetVariable("screen_tooltip", "")
        action If ("cc_he" in seen_labels, false=[Hide(None), None, Jump("set_customization_he_vars")])
        #action ToggleVariable("he_selected", True, False)
        #selected (True)



    imagebutton auto "cc_they_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "They/Them")
        unhovered SetVariable("screen_tooltip", "")
        action If ("cc_they" in seen_labels, false=[Hide(None), None, Jump("set_customization_they_vars")])
        #action ToggleVariable("they_selected", True, False)
        #selected (True)

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
    
    frame: #now we want to do vbox to make the input below the textbox
        xpos 550 #with this you define location of the vbox (if you would type xalign 0 and yalign 0 it would appear in top left corner)
        ypos 700
        xpadding 50
        ypadding 15
        xsize 690
        ysize 68
        add Solid ("000000")
        #there is a link to all of positional properties: https://www.renpy.org/doc/html/style_properties.html#position-style-properties
        #text "What is your name?": #we added text using this
        #    size 20 #in here you can edit the text with those: https://www.renpy.org/doc/html/style_properties.html#text-style-properties
        #    at transform: #with this you can animate the text
        #            alpha 0 #here you type parameters which are used at first
        #            pause 0.5 #you can add a pause
        #            linear 2 alpha 1.0 #now you add how it's changed (I used linear but here are all: https://www.renpy.org/doc/html/atl.html#warpers) then the time of the animation and then to what it is changed

        input default "[player_name]":#now we add input which will be below the text because it's in the vbox. In default you can type something that will be already typed when the screen will be shown
            xanchor 0
            pixel_width(500)#this to not allow too long name
            value VariableInputValue("player_name")#with this you save the input to a variable.



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
