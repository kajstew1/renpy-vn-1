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
