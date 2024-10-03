#https://www.youtube.com/watch?v=klH54mu6If4&t=145s

define quickmenu_button_color = "#fff"
define quickmenu_button_hover = "#f00"
define quickmenu_button_inactive = "#444"
define quickmenu_button_black = "#000"
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

init -1000:

    transform buttonZoom:
        zoom .05

    screen tooltip_screen(tooltip_text):
        frame:
            xalign 1.0
            yalign 1.0
            text tooltip_text


    screen quick_menu():
        # Make sure it appears on top of the other screens
        zorder 200

        style_prefix "quick"

# https://itch.io/blog/630699/renpy-achievementsendings-screen-tooltips#:~:text=Tooltips%3A%201%201.%20Define%20a%20label%20where%20you,the%20set%2C%20you%20can%20write%20it%20like%20this.
# back <arrow>, history, skip <arrow>, aut o, save, quicksave, quickload, prefs
# textbutton _("Back") action Rollback()
# textbutton _("History") action ShowMenu('history')
# textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
# textbutton _("Auto") action Preference("auto-forward", "toggle")
# textbutton _("Save") action ShowMenu('save')
# textbutton _("Q.Save") action QuickSave()
# textbutton _("Q.Load") action QuickLoad()
# textbutton _("Prefs") action ShowMenu('preferences')

        if quick_menu:
            vbox:
                xalign 1.0
                yalign 1.0

                $ toolt = GetTooltip()
                if toolt:
                    text toolt

                hbox:
                    # back/rollback
                    imagebutton:
                        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                        idle "quick button back idle"
                        hover "quick button back hover"
                        tooltip "Go Back"
                        # idle Transform("ui/buttons/back.png", matrixcolor=matrix_normal)
                        # hover Transform("ui/buttons/back.png", matrixcolor=matrix_red)
                        # hovered SetVariable("screen_tooltip", "Go Back")
                        # unhovered SetVariable("screen_tooltip", "")
                        #hover im.MatrixColor("ui/buttons/back.png", im.matrix.colorize("#ffffff", "#00ff00"))
                        #insensitive "quick button back insensitive"
                        #unhovered toolt.Action("")
                        #hovered [SetVariable("tooltip_text", "This is a tooltip"), Show("tooltip_screen")]
                        #unhovered Hide("tooltip_screen")
                        at buttonZoom
                        action Rollback()

                    # history
                    imagebutton:
                        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                        idle "quick button history idle"
                        hover "quick button history hover"
                        tooltip "History"
                        at buttonZoom
                        action ShowMenu('history')

                    # skip
                    imagebutton:
                        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                        idle "quick button skip idle"
                        hover "quick button skip hover"
                        tooltip "Skip"
                        at buttonZoom
                        action Skip() alternate Skip(fast=True, confirm=True)

                    # auto
                    imagebutton:
                        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                        idle "quick button auto idle"
                        hover "quick button auto hover"
                        tooltip "Auto"
                        at buttonZoom
                        action Preference("auto-forward", "toggle")

                    # save
                    imagebutton:
                        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                        idle "quick button save idle"
                        hover "quick button save hover"
                        tooltip "Save"
                        at buttonZoom
                        action ShowMenu('save')

                    # quick save
                    imagebutton:
                        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                        idle "quick button qsave idle"
                        hover "quick button qsave hover"
                        tooltip "Quick Save"
                        at buttonZoom
                        action QuickSave()

                    # quick load
                    imagebutton:
                        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                        idle "quick button qload idle"
                        hover "quick button qload hover"
                        tooltip "Quick Load"
                        at buttonZoom
                        action QuickLoad()

                    # Settings
                    imagebutton:
                        focus_mask True  # in case any transparent pixels in image mask in the image box they are clickable
                        idle "quick button preferences idle"
                        hover "quick button preferences hover"
                        tooltip "Preferences"
                        at buttonZoom
                        action ShowMenu('preferences')


#Since icons are all black only the first ColorizeMatrix value is needed
image quick button back idle:
    "ui/buttons/back.png"
    #matrixcolor TintMatrix(Color(rgb=(1.0, 0.0, 0.0)))
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 1.0, 1.0)), Color(rgb=(1.0, 1.0, 1.0)))

#Since icons are all black only the first ColorizeMatrix value is needed
image quick button back hover:
    "ui/buttons/back.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 0.0, 0.0)), Color(rgb=(1.0, 1.0, 1.0)))



image quick button history idle:
    "ui/buttons/history.png"
    #matrixcolor TintMatrix(Color(rgb=(1.0, 0.0, 0.0)))
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 1.0, 1.0)), Color(rgb=(1.0, 1.0, 1.0)))

image quick button history hover:
    "ui/buttons/history.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 0.0, 0.0)), Color(rgb=(1.0, 1.0, 1.0)))



image quick button skip idle:
    "ui/buttons/skip.png"
    #matrixcolor TintMatrix(Color(rgb=(1.0, 0.0, 0.0)))
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 1.0, 1.0)), Color(rgb=(1.0, 1.0, 1.0)))

image quick button skip hover:
    "ui/buttons/skip.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 0.0, 0.0)), Color(rgb=(1.0, 1.0, 1.0)))



image quick button auto idle:
    "ui/buttons/auto.png"
    #matrixcolor TintMatrix(Color(rgb=(1.0, 0.0, 0.0)))
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 1.0, 1.0)), Color(rgb=(1.0, 1.0, 1.0)))

image quick button auto hover:
    "ui/buttons/auto.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 0.0, 0.0)), Color(rgb=(1.0, 1.0, 1.0)))



image quick button save idle:
    "ui/buttons/save.png"
    #matrixcolor TintMatrix(Color(rgb=(1.0, 0.0, 0.0)))
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 1.0, 1.0)), Color(rgb=(1.0, 1.0, 1.0)))

image quick button save hover:
    "ui/buttons/save.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 0.0, 0.0)), Color(rgb=(1.0, 1.0, 1.0)))


image quick button qsave idle:
    "ui/buttons/qsave.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 1.0, 1.0)), Color(rgb=(1.0, 1.0, 1.0)))

image quick button qsave hover:
    "ui/buttons/qsave.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 0.0, 0.0)), Color(rgb=(1.0, 1.0, 1.0)))



image quick button qload idle:
    "ui/buttons/qload.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 1.0, 1.0)), Color(rgb=(1.0, 1.0, 1.0)))

image quick button qload hover:
    "ui/buttons/qload.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 0.0, 0.0)), Color(rgb=(1.0, 1.0, 1.0)))



image quick button preferences idle:
    "ui/buttons/preferences.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 1.0, 1.0)), Color(rgb=(1.0, 1.0, 1.0)))

image quick button preferences hover:
    "ui/buttons/preferences.png"
    matrixcolor ColorizeMatrix(Color(rgb=(1.0, 0.0, 0.0)), Color(rgb=(1.0, 1.0, 1.0)))
