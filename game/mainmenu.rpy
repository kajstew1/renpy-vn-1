#https://www.youtube.com/watch?v=klH54mu6If4&t=145s

define mainmenu_button_color = "#fff"
define mainmenu_button_hover = "#f00"
define mainmenu_button_inactive = "#444"
define mainmenu_button_black = "#000"
#define dim_matrix = ColorizeMatrix(Color(rgb=(0.9922, 0.9922, 1.0)))
#define dark_matrix = ColorizeMatrix(Color(rgb=(0.0, 0.0, 0.0)))
#define tooltip_text = ""

define matrix_normal = Matrix([
    1.0, 0.0, 0.0, 0.0,  #1 Red
    0.0, 1.0, 0.0, 0.0,  #2 Green
    0.0, 0.0, 1.0, 0.0,  #3 Blue
    0.0, 0.0, 0.0, 1.0   #4 Alpha
])
define matrix_red = Matrix([
    1.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 1.0
])



init 1000:
    transform buttonZoom:
        zoom .7
    screen tooltip_screen(tooltip_text):
        frame:
            xalign 1.0
            yalign 1.0
            text tooltip_text


    ## Navigation screen ###########################################################
    ##
    ## This screen is included in the main and game menus, and provides navigation
    ## to other menus, and to start the game.
    # https://itch.io/blog/630699/renpy-achievementsendings-screen-tooltips#:~:text=Tooltips%3A%201%201.%20Define%20a%20label%20where%20you,the%20set%2C%20you%20can%20write%20it%20like%20this.

    screen navigation():

        #vbox:
        if renpy.get_screen("main_menu"):
            #if main_menu:
            add gui.main_menu_background
            add "drp_logo"

            hbox:
                style_prefix "hnavigation"

                #xpos gui.navigation_xpos
                #yalign 0.5
                xalign 0.5
                yalign 1.0
                yoffset -50
                

                spacing gui.navigation_spacing

                #if main_menu: 
                if not show_main:
                    #spacing 100
                    $ newest_game = renpy.newest_slot(regexp="[^_]")

                    if not persistent.is_new_game:
                        if renpy.can_load("quitsave"):
                            #textbutton _("Resume") action FileLoad("quitsave", slot=True) text_size 50
                            imagebutton auto "gui/button/resume_%s.jpg":
                                focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                                # hovered SetVariable("screen_tooltip", "Resume")
                                # unhovered SetVariable("screen_tooltip", "")
                                at buttonZoom
                                action FileLoad("quitsave", slot=True)
                        elif renpy.can_load(newest_game):
                            #textbutton _("Resume") action FileLoad(newest_game, slot=True) text_size 50
                            imagebutton auto "gui/button/resume_%s.jpg":
                                focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                                # hovered SetVariable("screen_tooltip", "Resume")
                                # unhovered SetVariable("screen_tooltip", "")
                                at buttonZoom
                                action FileLoad(newest_game, slot=True)

                    #textbutton _("Start") action Start()
                    # Start
                    # imagebutton auto "gui/button/start_%s.jpg":
                    #     focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                    #     hovered SetVariable("screen_tooltip", "Start")
                    #     unhovered SetVariable("screen_tooltip", "")
                    #     at buttonZoom
                    #     action If ("start" in seen_labels, false=[Hide(None), None, Start()])
                    #textbutton _("New Game") action [SetVariable("persistent.is_new_game", False), Start()]  text_size 50
                    # textbutton _("New Game"):
                    #     text_size 50
                    #     action Start()
                    imagebutton auto "gui/button/start_%s.jpg":
                        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                        # hovered SetVariable("screen_tooltip", "Start")
                        # unhovered SetVariable("screen_tooltip", "")
                        at buttonZoom
                        action Start()


                    #textbutton _("Load") action ShowMenu("load")
                    # Load
                    imagebutton auto "gui/button/load_%s.jpg":
                        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                        # hovered SetVariable("screen_tooltip", "Load")
                        # unhovered SetVariable("screen_tooltip", "")
                        at buttonZoom
                        action If ("load" in seen_labels, false=[Hide(None), None, ShowMenu("load")])

                else:

                    #textbutton _("History") action ShowMenu("history")

                    #textbutton _("Save") action ShowMenu("save")


                    #textbutton _("Preferences") action ShowMenu("preferences")
                    imagebutton auto "gui/button/preferences_%s.jpg":
                            focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                            # hovered SetVariable("screen_tooltip", "Preferences")
                            # unhovered SetVariable("screen_tooltip", "")
                            at buttonZoom
                            action If ("preferences" in seen_labels, false=[Hide(None), None, ShowMenu("preferences")])

                if show_main:                 
                    #textbutton _("About") action ShowMenu("about")
                    # About
                    imagebutton auto "gui/button/about_%s.jpg":
                            focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                            # hovered SetVariable("screen_tooltip", "About")
                            # unhovered SetVariable("screen_tooltip", "")
                            at buttonZoom
                            action If ("about" in seen_labels, false=[Hide(None), None, ShowMenu("about")])

                    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                        ## Help isn't necessary or relevant to mobile devices.
                        #textbutton _("Help") action ShowMenu("help")
                        # Help
                        imagebutton auto "gui/button/help_%s.jpg":
                            focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                            # hovered SetVariable("screen_tooltip", "Help")
                            # unhovered SetVariable("screen_tooltip", "")
                            at buttonZoom
                            action If ("help" in seen_labels, false=[Hide(None), None, ShowMenu("help")])

                    if renpy.variant("pc"):

                        ## The quit button is banned on iOS and unnecessary on Android and
                        ## Web.
                        #textbutton _("Quit") action Quit(confirm=not main_menu)
                        #Quit
                        imagebutton auto "gui/button/quit_%s.jpg":
                            focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                            # hovered SetVariable("screen_tooltip", "Quit")
                            # unhovered SetVariable("screen_tooltip", "")
                            at buttonZoom
                            #action If ("quit" in seen_labels, false=[Hide(None), None, Quit(confirm=not main_menu)])
                            action If ("quit" in seen_labels, false=Quit(confirm=not main_menu))
                    # textbutton _("Return"):
                    #     style "return_button"
                    #     action [SetVariable('show_main', False), Return()]
                    imagebutton auto "gui/button/return_%s.jpg":
                        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                        # hovered SetVariable("screen_tooltip", "Return")
                        # unhovered SetVariable("screen_tooltip", "")
                        at buttonZoom
                        action [SetVariable('show_main', False), Return()]
                else:
                    # Main Menu
                    #textbutton "Main Menu":
                    # xalign .5 
                    # yalign .75 
                    # action [SetVariable('show_main', True), ShowMenu("main_menu")]
                    imagebutton auto "gui/button/main_%s.jpg":
                        xalign .5
                        yalign .75
                        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                        # hovered SetVariable("screen_tooltip", "Main")
                        # unhovered SetVariable("screen_tooltip", "")
                        at buttonZoom
                        action [SetVariable('show_main', True), ShowMenu("main_menu")]

            if screen_tooltip:
                text "[screen_tooltip]" italic True yalign 0.85 xalign .6
   
        else:
            vbox:
                style_prefix "navigation"

                xpos gui.navigation_xpos
                yalign 0.5
                

                spacing gui.navigation_spacing

                if main_menu:

                    textbutton _("Start") action Start()

                    #textbutton "Reset Paths" action ShowMenu("reset_paths")

                else:

                    textbutton _("History") action ShowMenu("history")

                    textbutton _("Save") action ShowMenu("save")

                textbutton _("Load") action ShowMenu("load")

                textbutton _("Preferences") action ShowMenu("preferences")

                if _in_replay:

                    textbutton _("End Replay") action EndReplay(confirm=True)

                elif not main_menu:

                    #textbutton _("Main Menu") action MainMenu()
                    textbutton _("Main Menu") action [SetVariable('show_main', True), ShowMenu("main_menu")]

                textbutton _("About") action ShowMenu("about")

                if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                    ## Help isn't necessary or relevant to mobile devices.
                    textbutton _("Help") action ShowMenu("help")

                if renpy.variant("pc"):

                    ## The quit button is banned on iOS and unnecessary on Android and
                    ## Web.
                    textbutton _("Quit") action Quit(confirm=not main_menu)
        


# https://itch.io/blog/630699/renpy-achievementsendings-screen-tooltips#:~:text=Tooltips%3A%201%201.%20Define%20a%20label%20where%20you,the%20set%2C%20you%20can%20write%20it%20like%20this.
    

#Since icons are all black only the first ColorizeMatrix value is needed
image mainmenu button start idle:
    "ui/buttons/start.png"
    #matrixcolor TintMatrix(Color(rgb=(1.0, 0.0, 0.0)))
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 1.0, 1.0)), Color(rgb=(1.0, 1.0, 1.0)))

#Since icons are all black only the first ColorizeMatrix value is needed
image mainmenu button start hover:
    "ui/buttons/start.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 0.0, 0.0)), Color(rgb=(1.0, 1.0, 1.0)))


#Since icons are all black only the first ColorizeMatrix value is needed
image mainmenu button load idle:
    "ui/buttons/load.png"
    #matrixcolor TintMatrix(Color(rgb=(1.0, 0.0, 0.0)))
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 1.0, 1.0)), Color(rgb=(1.0, 1.0, 1.0)))

#Since icons are all black only the first ColorizeMatrix value is needed
image mainmenu button load hover:
    "ui/buttons/load.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 0.0, 0.0)), Color(rgb=(1.0, 1.0, 1.0)))

