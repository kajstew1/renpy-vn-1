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

screen evt_choose_route: 
    hbox: 
        xalign 0.5 
        yalign 0.5 
        yoffset 30 
        spacing 20 
        imagebutton: 
            idle "boychar2" 
            hover "boychar" 
            action Jump("variable1") 
        imagebutton: 
            idle "girlchar" 
            hover "girlchar2" 
            action Jump("variable2") 


screen tavern_nav:
    add "bg_tavern"
    modal True  # prevents from interacting with assets under or below it
    
    imagebutton auto "tavern_bin_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "Bartender")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("placeholder")
        

    imagebutton auto "tavern_heater_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "Patron")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("placeholder")

    imagebutton auto "tavern_patron_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "Patron")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("placeholder")

    imagebutton auto "tavern_sign_%s":
        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
        hovered SetVariable("screen_tooltip", "Patron")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("placeholder")
