# The script of the game goes in this file.

init:

    transform my_shake:
        parallel:
            easein 0.2 xoffset 0 yoffset 30
            easeout 0.2 xoffset 0 yoffset -30
            #linear 0.1 xoffset 0 yoffset 10
            #linear 0.1 xoffset 0 yoffset -15
            #linear 0.1 xoffset 0 yoffset 0
            repeat 30
        parallel:
            linear 10 zoom 1.5

    transform my_bump:
        easein 0.2 xoffset 0 yoffset 100
        easeout 0.2 xoffset 0 yoffset -120
        #linear 0.1 xoffset 0 yoffset 10
        #linear 0.1 xoffset 0 yoffset -15
        #linear 0.1 xoffset 0 yoffset 0
        #repeat 10

    transform my_walking:
        parallel:
            easein 0.4 xoffset 0 yoffset 30
            easeout 0.4 xoffset 0 yoffset -30
            #linear 0.1 xoffset 0 yoffset 10
            #linear 0.1 xoffset 0 yoffset -15
            #linear 0.1 xoffset 0 yoffset 0
            repeat
        parallel:
            linear 10 zoom 1.5
        #parallel:
            #easein 4.0 crop (860, 430, 860, 600)

    transform basic_fade:
        on show:
            alpha 0.0
            linear 3.0 alpha 1.0
        on hide:
            alpha 1.0
            linear 10.0 alpha 0.0
  

    transform basic_fade_out:
        alpha 1.0
        linear 1.0 alpha 0.0

    transform basic_fade_in:
        alpha 0.0
        linear 1.0 alpha 1.0

    transform exitright:
        linear 3.0 xpos 1.5 xzoom -1.0

    

# The game starts here.
label start:
    
    #scene black 
    #show drp_motions dr_p_breathing

    #with Pause(1)
    #show mytext "Dr. Psilicon Presents......" with dissolve
    #with Pause(2)

    #hide mytext with dissolve
    #with Pause(1)
    
    #return
    jump path_char_customization
    #jump path_choose_char
    #jump path_town_outskirts




label path_char_customization:
    scene black 
    #show img_customization

    
#    if player_name == "":
#        $ player_name = player_name_default #here you type a name, that will be used, if the player types nothing

#    show screen showName
    call screen screen_customization_nav
#    hide screen showName

    jump path_choose_char


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





label set_customization_he_vars:
    $ pronouns = "He/Him"
    $ pronoun1 = "he"
    $ pronoun2 = "his"
    $ pronoun3 = "his"
    $ be = "is"
    $ pronoun1_selected = pronoun1
    
    #"pronoun: [pronoun1]: [pronouns]"
    jump path_char_customization
    

label set_customization_she_vars:
    $ pronouns = "She/Her"
    $ pronoun1 = "she"
    $ pronoun2 = "her"
    $ pronoun3 = "her"
    $ be = "is"
    $ pronoun1_selected = pronoun1
    
    #"pronoun: [pronoun1]: [pronouns]"
    jump path_char_customization
    

label set_customization_they_vars:
    $ pronouns = "They/Them"
    $ pronoun1 = "they"
    $ pronoun2 = "them"
    $ pronoun3 = "their"
    $ be = "are"
    $ pronoun1_selected = pronoun1
    #"pronoun: [pronoun1]: [pronouns]"
    jump path_char_customization
    



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
    
    $LongNVLText(sidenarrator, (
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
    scene black
    
    show drp_motions dr_p_breathing
    #show mytext "What name would you like to use?"
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="[player_name_default]"


    # show mytext "So Start your journey now!"
    # with Pause(2)

    # hide mytext with dissolve
    # with Pause(1)

    jump path_crash_site
    #return

# start of the game
# Scene 1
label path_crash_site:
    
    # Display a message and show an alert box when a button is clicked
    # jump splashscreen2
    scene black
    $ screen_tooltip = ""

#    with Pause(1)
#    show mytext "[player_name], you find yourself waking up on a crash ship."
#    with Pause(2)
  
#    hide mytext with dissolve
#    with Pause(1)

    #show bg_crashsite with dissolve
    scene black
    show bg_crashsite with dissolve
    play music "sounds/effects/SCENE_1_crash_beeps_alarms.mp3"

    #narration = new Character(.....)
    #Array and multiple lines only used for readability. They have no effect on the text printed.
   
    #"Person Enters World, wake up on crash ship?"

    $LongNVLText(narrator, (
    '''\
Smoke billows out of the crashed spacecraft. You, the sole survivor, wake up in a haze. Your blurry eyes, disoriented from the sharp impact, try to make sense of the destruction in front of you. Debris is scattered across the broken grass turf, like a distorted kaleidoscope. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Your breathing is staggered as you move to stand, clutching onto your wounded stomach. Blood pools out from inside your dark jumpsuit. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
“W-where am I?” You ask in a whimper, stumbling out of the wreckage that once was your ship. Your memories were far and few between as your brain hadn’t made sense out of the situation yet. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
The ship was supposed to have been indestructible. No one had been chasing you. The sensors were all clear. So what did the ship hit? And what were the odds that the generator would have been the target of the impact? None of this made sense. 
    '''
    ))

    
    $LongNVLText(narrator, (
    '''\
An involuntary coughing fit brought about from the dark smoke around you made you come back to your senses. You look at your hand and are horrified to see tiny droplets of blood sprinkled all over your palm.  
    '''
    ))

    $LongNVLText(narrator, (
    '''\
I can make sense of this later. I need to focus on surviving. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Your movements were painfully slow, but you were able to maneuver around the wrecked ship to the ground below. The grass was a welcome change in texture, soft and inviting unlike the harsh and distorted floor of the ship. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You had no idea where you crash landed. As the captain you had to make a quick decision when the ship had been hit, either take your chance on the neighboring moon or divert towards the nearest planet. It had seemed at the time that a planet would have more resources and potentially a civilization available, but after reviewing the landscape, you weren’t sure. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
While there was a blue sky and green grass, that’s where the comparisons ended between your home planet and the environment surrounding you. In the far distance welcomed a skyline of blooming mushrooms. Using your best estimation, they had to have been as tall and thick as the redwoods you had been accustomed to seeing when you were a child. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Neon-colored flying dinosaur-looking creatures dotted the sky above. As they circled the crash site, they let out a screech. You recoiled, holding your hands protectively against your ears. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
“Mushrooms as trees? Flying dinosaurs? Where am I?” 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Your heart starts to race when you realized that you were well and truly alone in this treacherous landscape. The small crew that had opted to not use the escape pods and stayed with you had all lost oxygen and died before the ship entered the planet’s atmosphere. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You truly didn’t know where to start. The communication system on the ship had shorted and broke before you could alert the nearest space station and you knew no one on this planet. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
With no food, no water, and only the clothes on your back, you look towards the two blistering suns in the horizon. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
“Guess I’ll do this the old fashion way. Pick a direction and start walking.” 
—                                                            
You had trekked up the worn, uneven path in front of you. It was disconcerting as it appeared as though it hadn’t been used in half of a century. But seeming as though you had no other option, you continued onward, desperately hoping for a sign of civilization or at least another living being. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You wonder what kinds of lifeforms live on this planet. This had been your first time in this galaxy–and of course it had ended terribly. You had just wanted to be a space explorer like those you had grown to admire, but like most dreams, it was not what it appeared. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Crew that didn’t respect your authority, food that sprouted mold, and hygienic conditions that left little to be desired. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You sighed. It just seemed like your luck had gone from bad to worse. You don’t feel like you are that bad of a person. So why do you always get the shortest straw? 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Guess that would be your next shower thought when you found running water. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You are exhausted from your half a day journey through the unending fields of green. You clutch onto your wounded stomach, while the bleeding had blessedly stopped, you still felt a tremendous amount of pain. If you didn’t get help by tomorrow, you feared you may meet your demise on a deserted planet. Your corpse feeding the humongous alien creatures that skulked around you in the distance. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
“I refuse to be animal food, on my home planet or here!” You say with finality. You grit your teeth and continue onward. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
After another half an hour, you came across a change in scenery.
    '''
    ))

    #stop sound
    stop music fadeout 3.0
    
    jump crash_fork




# Scene 2
label crash_fork:
    scene black
    show bg_fork with dissolve
    
    # terrorlightz.c "Which way do you want to go?"
    #show screen evt_choose_path
    $LongNVLText(narrator, (
    '''\
What once was a temperate, lush, green landscape, turned into a dry, sandy, mountainous desert. Even worse, the singular path you had been following diverged into two. You gulp. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You had a feeling that there was a right or wrong answer to your choice from here. You had better choose the right one or fear the repercussions.
    '''
    ))
    $LongNVLText(narrator, (
    '''\
You decide to take a look around before you make your decision.
    '''
    ))

    call screen screen_crash_fork_nav



label crash_fork_menu:
    menu: 
        "Do you take the right or left path?"
        "Left...":
            # if (persistent.path_to_outskirts_taken == False or persistent.path_to_tavern_taken == False):
            #show screen evt_choose_path
            #call screen evt_choose_route with dissolve
            $ persistent.path_to_town_taken = True
            jump path_left_path_decision
        "Right...":
            #if persistent.path_to_hut_taken == False:
            #show screen evt_choose_path 
            #call screen evt_choose_route with dissolve
            $ persistent.path_to_hut_taken = True
            jump path_right_path
        "No thank you!": 
            jump path_give_up
    
    
    return

# Scene 4a
label path_give_up:


    $LongNVLText(narrator, (
    '''\
You stare at the fork in the road. With zero insight into the landscape and the perilous nature of the planet, you are facing a severe disadvantage. Are your options really only to choose between a right or a left? You don’t think so. You still had a ship. Sure it is partially on fire and almost entirely destroyed, but better the devil you know than the devil you don't, right? 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Feeling safer already treading the beaten path–albeit a long one–you make the half’s day journey back to your ship. Your wound is probably infected from all of the sweat and dirt you’ve collected today, but the blood clotted so it is a far less messy affair. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Breathing hard, clutching onto your ripped stomach, you feel weaker with every step you make. Though miraculously, you make it back to your ship. 
    '''
    ))

# Change BG to -> bg_crashsite
    scene black
    show bg_crashsite with dissolve

    $LongNVLText(narrator, (
    '''\
You are in far worse shape than when you first made the journey, but at least you are back.
    '''
    ))

    $LongNVLText(narrator, (
    '''\
With the last of your remaining strength, you climb up towards the cockpit. You nearly fall multiple times after losing your foothold–resulting in re-opening your stomach wound–but you somehow make it back to your cockpit. 
    '''
    ))

# Change BG to -> bg_cockpit
    scene black
    show bg_cockpit with dissolve

    $LongNVLText(narrator, (
    '''\
Sweating profusely, you crawl into your tattered cockpit chair, the only notable item in the entire room. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You sigh as you lean back into the worn leather seat. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You feel safe. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Quiet. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Alone.
    '''
    ))

    $LongNVLText(narrator, (
    '''\
The soft hum from the static of your broken flight instruments lulls you into a state of calm. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
With your clothes ripped, your hair disheveled, and night descending, you stare into the shattered windshield and slowly fade into a deep sleep. You never wake up. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You are at peace. 
    '''
    ))
# GAME OVER–BAD ENDING 2
    return




# Scene 2a
label path_right_path:
    #show bg_tavern with dissolve
    hide screen evt_choose_path
    scene black
    show bg_fork with dissolve:
        #xpos 1.25 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0
        subpixel True
        size (1920, 1080) crop (0, 0, 860, 600) # first tuple is the size of game screen, 
                                                # second is size of picture in pixels
        easein 4.0 crop (860, 430, 860, 600)    # first float is time in seconds, 
                                                # tuples are coordinates of the upper left corner of a rectangle 
                                                # x: final pan right distance (screen is 1920 wide)
                                                # y, final pan down distance (screen is 1080 high)
                                                # width, height: size of the cropped rect, 
                                                # and the second tuple is the size of that rectangle
        easeout 5.0 crop (860, 300, 860, 600)       # here we change the y coordinate over 8 seconds to pan the image up
        

    $LongNVLText(narrator, (
    '''\
(Effect - zoom to the right... verify ok)
You stood transfixed at the shadowed silhouette of the strange moon behind the cover of the sharp mountain peaks. You feel it calling to you, moving your feet faster than your mind could keep up. 
    '''
    ))

    # show bg_fork with dissolve:
        

    $LongNVLText(narrator, (
    '''\
Without much of a voluntary choice, you make your way down the sandy, gravel path. 
    '''
    ))
    jump path_right_path_1


# Scene 2b
label path_right_path_1:
    #show bg_tavern with dissolve

    scene black
    show bg_rightpath with dissolve


    $LongNVLText(narrator, (
    '''\
Hairs prickle your back as you embrace the dark landscape. Something was following you. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You are not a soldier. You aren’t a survivalist. You are a wounded captain without a weapon or a ship. If something was following you, you are more than likely dead. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You feel a cold sweat forming at your brow as you force your feet to move forward. Against all of your base instincts, you don’t look behind you. If you looked, you would accept the fear that threatened to spill out of your insides. 
    '''
    ))

    scene black
    show bg_rightpath with dissolve:
        #xpos 1.25 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0
        subpixel True
        size (1920, 1080) crop (0, 0, 860, 600) # first tuple is the size of game screen, 
                                                # second is size of picture in pixels
        easein 4.0 crop (0, 430, 860, 600)    # first float is time in seconds, 
                                                # tuples are coordinates of the upper left corner of a rectangle 
                                                # x: final pan right distance (screen is 1920 wide)
                                                # y, final pan down distance (screen is 1080 high)
                                                # width, height: size of the cropped rect, 
                                                # and the second tuple is the size of that rectangle
        easeout 5.0 crop (860, 300, 860, 600)       # here we change the y coordinate over 8 seconds to pan the image up

    $LongNVLText(narrator, (
    '''\
(Effect - zoom in and pan left to the right (In Work))
“I should’ve chosen the safer path,” you curse as you force yourself to come up with an escape plan. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Over the thunderous beat of your heart, you hear soft footsteps coming towards you. Whatever was following you was doing so very slowly and very calmly. It must be a big, confident creature. You still have time. You could use it to your advantage that they want to play with their food. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
About 10 meters ahead of you, you see that the jagged mountains converge, creating what could only be described as a small tunnel. If you were to make it through the narrow gap before the creature catches up to you, you could possibly delay your imminent death.
    '''
    ))

    #show bg_rightpath at center, Shake(None, 1.0, dist=5) with None

    scene black
    show bg_rightpath at my_shake

    $LongNVLText(narrator, (
    '''\
(Effect - running, shake up and down (In Work)
You clutch onto your wounded stomach with a small prayer that your thrown together plan wouldn’t reopen the cut and begin your mad dash to the ominous tunnel. 
    '''
    ))

    scene black
    show bg_rightpath with dissolve

    $LongNVLText(narrator, (
    '''\
You wish you had trained harder when you had the chance. You barely made the cutoff for the academy with your running scores. Not for lack of talent, but for a lack of effort. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You curse your past self as you choke on your ragged breaths, involuntarily running in a zigzag pattern as you spare yourself a few glances behind you. With the lack of regular exercise, your feet threaten to trip on themselves at any moment as your hands desperately search for any sort of leverage point to pull yourself quicker to your destination. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
The air behind you begins to get warmer as you realize you are losing this race. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
“Only a few more feet!” You shout to convince yourself you still had a chance. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You feel a presence looming over you with every step now. Matching you step by step. You aren’t going to make it, it’s faster. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You scan the area in a desperate attempt to come up with another strategy, you could almost hold onto the entrance to the tunnel now. You had to do something. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You sharply turn left and then double back. Claws scraped against the mountain rock. You didn’t look back, you just threw your body into the tunnel’s entrance. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You hear screams coming outside of the narrow gap. You made it. You were safe! You could barely believe it. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
“Go find food elsewhere, you confounded beast!” You roar, the sound echoing off of the rocky walls. You only feel a little curious to know what kind of creature you had just barely outran, but not enough to peer through the opening to find out. 
    '''
    ))

    jump path_cave
    #jump hut_meet_terrorlightz





# Scene 2c
label path_cave:
    scene black
    show  bg_insidecave with dissolve

    #show terrorlightz_talking at right
    
    #terrorlightz.c "Some text meeting terrorlightz."

    $LongNVLText(narrator, (
    '''\
After taking a few minutes to properly settle your heartbeat, you blindly make your way down the pitch black tunnel. You use the only tool available to you to navigate–your sense of touch. You feel your way forward with your hands, taking much longer than you had the patience for. Out of the oven, into the fire they say. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
It had taken a half an hour of blind exploration until you found a light source to follow. You barely believe it when you realize that the light might actually lead you to somewhere safe. 
    '''
    ))

    jump path_cave_light


# Scene 2d
label path_cave_light:
    scene black
    show bg_lightinsidecave with dissolve

    $LongNVLText(narrator, (
    '''\
You examine the exit of the tunnel. You see grass and weeds dotting the ground in a pleasant array, a warm welcome from the horrific desert landscape you had just escaped from. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Not surprisingly, your wound had opened back up from your harrowing escape. You really hope that you find some sort of town or civilization soon, but even if you couldn’t find help, you feel secure that you had enough excitement for one day. 
It couldn’t get worse, could it? 
    '''
    ))
    jump path_hut



    

# Scene 2e
label path_hut:
    scene black
    show bg_hut with dissolve

    $LongNVLText(narrator, (
    '''\

You weakly limp towards the greenery in front of you. You find it to be a blessed respite from the dark, cold cavernous tunnel you had just escaped from. If your hands weren’t currently occupied by holding together your open stomach, you would’ve pinched yourself. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You take in the pleasant view as the soft rays of daylight descend across the grass and shallow water. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You glance at your reflection in the water beneath you, fighting every urge to drink from it. You may not be a survivalist by trade, but you certainly know the dangers of consuming still water–whether it be from an alien planet or not.  
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Drawing your eyes away from the shallow water, you peer towards the central mass in front of you. You aren’t sure if it is from the blood loss or pure exhaustion, but you almost mistook the small hut for a meaningless pile of branches and moss. You rub your eyes with your free hand, fearing it as a mirage. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You follow the narrow path towards the hut with trepidation–unsure if the worst case scenario is it being occupied or unoccupied. From the outside, you peer through the window covered by a holey, dirty red curtain, looking for any signs of movement. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Once you feel certain that no one is inside, you slowly and carefully pull the curtain aside to get a better look. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
“It is as dilapidated inside as it is outside,” you mutter as yourr eyes scan the inside, noticing the rotted wood as it had caved in from persistent pooling water and miscellaneous junk littered all around. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Curiously, the only place left–for the most part–untouched by the destruction was the dining room table, located noticeably in the center of the shelter. Whoever last used this hut had obviously used it for a singular activity. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Shelter was shelter though. At least you wouldn’t be sleeping outside tonight. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You walk towards the open entryway and start your search for supplies while you still have some energy left. Luckily, you are able to find some scraps of worn cloth in one of the junk piles, which you use to tend to your stomach wound. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You are finally starting to feel better about your situation. You had shelter, a–mostly–clean wound, and some half rotting food to eat. As you drift off to sleep you believe that maybe your situation isn’t so bad afterall? 
    '''
    ))

    jump path_hut_meet_terrorlightz


# Scene 2f
label path_hut_meet_terrorlightz:
    scene black
    show bg_insidehut with dissolve

    $LongNVLText(narrator, (
    '''\
(EFFECT: Goes from a blank screen to a blinking effect? )
Your long overdue sleep is over soon when you hear a deep, guttural voice pierce your ears.“My, my, my. What is this?” 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Your eyes jerk open. In front of you stands a figure that appears to be a…person? 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
“W-who…what are you?” Your voice shakes as you retreat into the corner of your makeshift bed. 
    '''
    ))

    show tll  at right
    
    $LongNVLText(terrorlightz.c, (
    '''\
“Now, now… Is that any way to talk to your gracious host?” You feel the vibrations from his voice coarse through your body. Unexplainably, the pale purple-skinned stranger stands before you, wearing a dark teal and amethyst colored pinstripe suit.
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
His glare produces a hypnotic effect that prevents you from moving your body. Meeting his gaze, you notice the complete lack of pupils. Instead you see an optical illusion. His eyes were made up of tight spirals, which move inexplicably in a circular fashion. To further punctuate his ominous presence, smoke continuously emanates out from the corners of his almond eyes. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
“I-I’m sorry, I didn’t know this space was occupied!” You meekly squeak. How poignant that the first intelligent creature you’ve come across is a straight nightmare.
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
The ghastly alien cackles at your response. His sharp, pointed teeth glint in the light as he thrusts his head back. “See, now that’s better.” Returning his gaze to you, he gives you a half smirk. “Now that we are back to civility, I suppose introductions are in order.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\In a bizarre turn of events, he gives you an overdramatic bow, his arms outstretched with a flourish. “It’s very nice to meet you, my name is Terrorlightz. I welcome you heartedly to my humble abode.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You are speechless. You can’t fathom how this many contradictions can exist in a singular space. In front of you, stands a nightmarish creature wearing a three-piece suit who supposedly lives in this broken down shack. You can’t tell if you want to laugh or cry. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Where in the world are you? 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
After resigning to your fate, you reluctantly return the favor. “My name is (MAIN CHARACTER NAME). As you can probably tell, I’m not from here.” You are careful with your words. You don’t trust this stranger. He was exceptionally unpredictable so you felt that the less you say, the better. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
His eyes slit, his voice drawing out every word. “Oh my… So I’ve found myself a wounded alien? Now, this is interesting.”
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Before you could come up with a response, Terrorlightz offers you his hand. His eyes honed in on your torn and bloodied clothes. “Consider yourself lucky, alien. I have just the thing to fix you right up.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You stare at his outstretched hand momentarily before you grasp ahold of it. You weakly lift yourself off of the worn, broken couch. The academy only taught you basic first aid and your half-assed attempt at putting your stomach back together isn’t going to cut it. You either slowly bleed out or take a chance that Terrorlightz doesn’t have ulterior motives. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
He almost reminds you of a shark when his sharpened, pointy teeth glint in the light. “Now, let's forage for some mushrooms.” 
    '''
    ))
    
    $LongNVLText(terrorlightz.c, (
    '''\
With a smooth flick of the wrist, Terrorlightz motions towards the door. Without waiting for any acknowledgement of your intention to follow him, he turns his back and exits the hut. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
He can’t be serious can he? He actually wants to forage for mushrooms? 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You hesitantly follow Terrorlightz outside of the hut. It goes against all of your instincts to trust this stranger, even more so to root around for unknown plants. But he hasn’t killed you yet and he’s had ample opportunities. That’s something, isn’t it? 
    '''
    ))


    jump path_hut_forage 


# Scene 2g
label path_hut_forage:
    scene black
    show bg_hut with dissolve

    show terrorlightz_talking at right


    $LongNVLText(terrorlightz.c, (
    '''\
Leaving the confines of your temporary shelter reminds you that you are still on an alien, unfamiliar planet. It felt much too easy to forget where you are–even with Terrorlightz’s jarring presence. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Stepping out of the hut, the sunlight was blinding. You are forced to squint and throw your hands up to shield your eyes. It must be the start of a new day as the two suns in the sky are much brighter than before. Either you are right and the days here last a long time or the shock from the crash dulled your senses. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You feel a sudden rush of homesickness. Will you ever be back home? You had craved space travel for so long and worked so hard to achieve it, but now it seems meaningless. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
What was it all for? You would have never signed up if you knew you would end up alone, crash landed on a bizarre planet, foraging for–most likely poisonous–mushrooms with an absolute utter madman? 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
I’m sure your crew is laughing at you from the afterlife. How the mighty captain has fallen. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Once your eyes finally adjust to the light, you scan the area, Terrorlightz is nowhere in sight. You were only a few steps behind him leaving the hut. Where could he have gone? 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You feel a sudden urge to run. To where, you aren’t sure, but once you find Terrorlightz, you are pretty positive you won’t have that option again. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
But at the same time, at least here you have shelter and some promise of food. You barely survived on your own, so it seems foolish to give into your instincts now. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
With resignation, you decide to stick with Terrorlightz. Better than starving. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You search south of the hut where a clump of tall trees swallow the nearby light, blanketing the floor in almost near darkness. If mushrooms grow similarly here as they did in your home planet, this is most likely where they would grow.
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You find Terrorlightz hunched over the base of a thick tree trunk. His dissatisfaction is clear even with his back towards you. His deep, baritone voice almost shakes the ground when he says, “You must know, alien, that it is impolite to make someone wait.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You feel less terrified than you would’ve been thirty minutes ago, which surprises you. You suppose that giving into your fate helped to have lessened the blow.
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
“Sorry. You're tall and I can barely walk. Makes for an unfortunate combination.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Ignoring your comment, Terrorlightz points to the ground in front of him. You had to move to stand next to him to see what he was pointing at. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You furrow your brow. It was a small mushroom–no larger than a tennis ball–with a wide red brim, covered in a neon pink moss. “What kind of mushroom is it?” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Back to his mischievous ways, Terrorlightz turns to face you wearing a devious grin. The spirals in his eyes roll faster than before. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Yup, you aren’t totally desensitized yet. He is still terrifying. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
“This here, dear alien, is a Psilicon mushroom. Very rare indeed, you are quite lucky. Eat one of these and you’ll find what you are looking for.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
“What do you mean, find what I’m looking for? I just want something to patch myself back together.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Terrorlightz cackles, plucking the fuzzy mushroom off the moist ground. He inspects it a bit closer and then offers it to you. “Oh, don’t you worry, this will heal you up, and so much more.”
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You gulp. You definitely should have run when you had the chance. 
    '''
    ))




    $LongNVLText(terrorlightz.c, (
    '''\
Sweat beads your forehead as you contemplate your available options. “I appreciate the offer, but I think I’m okay,” you say, patting your stomach wound gently. “A few more nights rest and I’ll be good as new.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You give him your best used car salesman smile to add emphasis to your point. Is this all just a bluff? Yes. You reason that it would take at least a month to be back to full health. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
But Terrorlightz didn’t need to know that.
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You feel the hairs on your back raise when you meet his eyes. Behind the emptiness there was a hint of madness that wasn’t there before. The normally disconcerting smile crinkled into something more devious. “That’s funny, because I don’t recall giving you an option.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You start slowly walking backwards as Terrorlightz, much too easily, wipes the dirt off of his pants and moves to stand up. Your hands involuntarily reflex from an unclenched to clenched position as your mind races between fight or flight mode. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
With a cackle Terrorlightz holds the mushroom in an open palm towards you. “Now be a good alien and eat your vegetables.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Flight it is. You turn in the opposite direction, digging your heels into the muddy ground and take off into a sprint. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Why is this planet constantly trying to kill you? It would be nice to have one full day that wouldn’t require running for your life. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You feel lightheaded as you suck in air as quickly as you exhale. The humidity in the air feels thick in your lungs, making running a much harder endeavor. Mud spits onto your pants as you slide around the rotund trees, trying to distance yourself from the madman close onto your tail.
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You are already at a disadvantage since Terrorlightz knows the area much better than you do, but pray that the darkness from the tree canopy above you can increase your odds. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
There was little to no noise in the forest save for the soft squelching sounds as you and your assailant’s feet hit the wet ground. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
This feels worse than last night’s attack. Yesterday, you felt like you were the victim of a hungry animal. Today, it feels personal. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Your foot catches on a branch and you slide front first onto the ground. You taste mud as you grasp for a dry patch of ground for leverage, but you aren’t quick enough. Before you can process what was happening, you are being lifted off the ground by your shirt. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You struggle against Terrolightz’s fierce grip as he positions you to face him. “You are a difficult one, aren’t you?” You desperately cling onto Terrorlightz’s fierce grip, trying to release yourself, but his strength is inhuman. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Using his available hand, Terrolightz reaches into his pocket to retrieve the mushroom and shows it to you. Somehow, despite the scuffle, it is still perfectly preserved. The pink moss covering the mushroom faintly glows among the intense shade. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Your eyes grow wide when you realize that you don’t have a choice in this matter anymore. It’s dinner time. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
With a final cackle, Terrorlightz shoves the mushroom into your mouth, holding it closed until you finally swallow. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Then suddenly, Terrolightz, just as easily as he picked you up, drops you to the ground and walks away, leaving you muddy and gasping for air. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Your consciousness fades as you enter a dream state. Your vision fills with abstract, colorful shapes that gently pulsate and come in and out of focus. You aren’t an individual anymore, you are part of a singularity. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Thoughts and feelings that aren’t your own come through all at once in diverse pitch and tone. The senseless gibberish is impossible to describe, but you understand that it is trying to communicate with you. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
The geometric shapes start to shrink and organize themselves into what appears to be an image. After it takes shape, you recognize the image as a snapshot of a ship. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Wait. Is that your ship? 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You focus closer in on the front console. On the captain's chair, you recognize the cheap, worn black leather with a sharp gash in the back and the rusty gear shifts positioned directly alongside it. After confirming the most familiar part of the ship, you inspect the rest of the vessel. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You can barely believe it. This is your ship!
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You startle when a figure passes through you and sits in the captain’s chair. Even more so when you realize it is you. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Was this some sort of a test? Memory? Dream? Parallel universe? You have no idea. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
A disembodied voice snaps into existence. “Captain, we know it’s your birthday today, so the crew put together a little something for you.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Was that Jack? You couldn’t tell, you are still the only visible figure in the room. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Your past self sat with hunched shoulders, looking in the opposite direction. In a monotone voice, you said, “Did you really?” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Jack’s voice changed to a higher, more confident pitch. “Of course, you are our captain afterall.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Only you know the expression on your face. Self-deprecation. Your crew hated you, you knew that better than anyone. You believe that this must be yet another prank to undermine your authority. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
The pink wrapped package appears out of empty space in front of your past self. Even knowing what was coming, your past self still takes the half-hazardly packaged gift and opens it.
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You come close to inspect the gift. Why can’t you remember what was inside? 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Inside the box and crinkled white tissue paper were two mushrooms. Both identical in size and shape with a white stem and neon red brim. Your past self takes out one of the mushrooms and inspects the white dots decorating the top. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Jack’s voice echoes the metallic walls as he laughs. “Now go ahead and take a bite, captain.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Your past self’s shoulders droop even farther in on themselves as your grip tightens onto the mushroom. You see rage in your eyes as well as sadness. The sad captain whispers softly, “If you think you’ll make a laughing stock of me, you are wrong, Jack.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
With a clenched fist, your past self quickly stands up from the captain’s chair and addresses the empty audience, “What a kind gift! How lucky I am to have such a wonderful crew.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You gulp as you watch the familiar silhouette take the crushed mushroom and gobble it up with feigned joy. “Quite delicious, thank you.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Your past self dramatically falls onto the floor, unconscious. The disembodied voices of your crew are cheering and high fiving each other. “Finally, we are free! Remember the story boys, the ship was due to crash on an unexplored planet and our courageous captain volunteered to stay behind so we could live.” 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
The scene changes and all the colors disappear, leaving nothing but pure darkness behind. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Abruptly, you feel yourself being pulled back to your body and you wake up with a start, gasping for air. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You ignore the violent shaking of your legs as you pull yourself up. You snarl, “Those sons of bitches! I won’t let them get away with this.” You violently clutch onto the passing trees as you start running through the thick mud. You have to get back to your ship. There has to be some way to fix this. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
In your blind rage, you don’t even notice that your stomach wound has healed. 
    '''
    ))

    jump ship_remember


# Scene 2h
label ship_remember:
    scene black
    show bg_hut with dissolve

    $LongNVLText(narrator, (
    '''\
"Nothing but regret and resentment fill your mind as you clumsily stumble your way through the swamp and into the dark cave."
    '''
    ))

    scene black
    show bg_insidecave at basic_fade, my_shake with dissolve

    $LongNVLText(narrator, (
    '''\
(Effect: Shows running (fading and out) from bg_hut to bg_insidecave(In Work))
"Even though it was only yesterday that you first entered the cave, you feel none of the terror or fear you felt before."
    '''
    ))

    scene black
    show bg_crashsite at basic_fade, my_shake with dissolve

    $LongNVLText(terrorlightz.c, (
    '''\
(Shows running (fading and out) from bg_insidecave to bg_crashedsite)
No matter what obstacle comes your way now, you are willing to face it. The only thing that matters is getting to your ship and righting the wrong against you. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
After a matter of hours, you are exhausted and dehydrated. Your sore limbs fight against you, but you press on. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
In the distance you see the remnants of what was left of your ship. Your mangled body screams as you sprint to close the distance. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Black smoke still emanates from the ship’s exhaust as you approach the destruction. The contaminated air makes it more difficult to breathe than it should. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Your heart thunders against your chest as you scramble to climb the fallen, broken pieces of the crew cabin. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
It takes you a while, but you manage to make progress on your climb. Your tired body almost gives out in the last stretch, but you use the handle from the blown out emergency exit door as leverage to pull yourself inside the ship. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
Yesterday, you were so wounded and discombobulated that you weren’t able to process the damage. Now, you could finally understand the level of destruction the crash did to the ship. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
While most of the ship was in a desperate state of disrepair, your cockpit took the brunt of the damage. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
The ceiling had caved in, light pouring in from the gaps. You snickered solemnly to yourself, at least the light made it easier to navigate around the ship.
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
The windshield had shattered, spraying glass all throughout the cabin. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
To your right, you see what was left of your captain’s chair, only scattered pieces of black leather and wheels remain. In front of you, you see your warped and melted flight instruments. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You are pretty sure all of the consoles are busted, but you still try for hours to get the communication console back up and running. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
All you get is silence. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
In pure desperation, you maneuver yourself to the back of the ship. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
The crew wouldn’t be so inhumane that they would leave you without an escape pod. I mean, they hated you, but they wouldn’t be that cruel… would they? 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
The level of resignation you feel as you approach the empty escape pod unit is unparalleled to anything you have felt before. 
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
You drop to your knees. Your tattered clothes gently sway in the wind through the gaps in the walls.
    '''
    ))

    $LongNVLText(terrorlightz.c, (
    '''\
That’s it. You are stuck on a godforsaken planet with only a useless ship to your name. 
    '''
    ))
    jump game_over


# Scene 2h1
label ship_remember_1:
    scene black
    show bg_hut with dissolve

    show terrorlightz_talking at right

    "Some text remembering eating mushrooms on a way spaceship."

    jump game_over



# Scene 3
label path_left_path_decision:
    #show bg_tavern with dissolve
    hide screen evt_choose_path
    scene black
    show bg_fork with dissolve:
        #xpos 1.25 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0
        subpixel True
        size (1920, 1080) crop (0, 0, 860, 600) # first tuple is the size of game screen, 
                                                # second is size of picture in pixels
        easein 4.0 crop (0, 430, 860, 600)    # first float is time in seconds, 
                                                # tuples are coordinates of the upper left corner of a rectangle 
                                                # x: final pan right distance (screen is 1920 wide)
                                                # y, final pan down distance (screen is 1080 high)
                                                # width, height: size of the cropped rect, 
                                                # and the second tuple is the size of that rectangle
        #easeout 5.0 crop (0, 300, 860, 600)       # here we change the y coordinate over 8 seconds to pan the image up
        



    $LongNVLText(narrator, (
    '''\
(Effect - zoom in on left path (In Work))
Your eyes land on the seemingly safer option. The two suns and neighboring planets were hung in the sky like ornaments on a Christmas tree, brightly lighting the path in front of you.  
    '''
    ))

    scene black
    show bg_fork with dissolve:
        #xpos 1.25 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0
        subpixel True
        size (1920, 1080) crop (0, 0, 860, 600) # first tuple is the size of game screen, 
                                                # second is size of picture in pixels
        easein 4.0 crop (860, 430, 860, 600)    # first float is time in seconds, 
                                                # tuples are coordinates of the upper left corner of a rectangle 
                                                # x: final pan right distance (screen is 1920 wide)
                                                # y, final pan down distance (screen is 1080 high)
                                                # width, height: size of the cropped rect, 
                                                # and the second tuple is the size of that rectangle
        #easeout 5.0 crop (0, 300, 860, 600)       # here we change the y coordinate over 8 seconds to pan the image up

    $LongNVLText(narrator, (
    '''\
(Effect - zoom in on right path (In Work))
The right path scared you. It called to you like a siren in turbulent waters, inviting you in with a sweet song. You try to stand your ground in fear of being pulled into the imposing moon’s imaginary gravitational pull. 
    '''
    ))

    scene black
    show bg_fork with dissolve:
        #xpos 1.25 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0
        subpixel True
        size (1920, 1080) crop (0, 0, 860, 600) # first tuple is the size of game screen, 
                                                # second is size of picture in pixels
        easein 4.0 crop (0, 0, 1920, 1080)    # first float is time in seconds, 
                                                # tuples are coordinates of the upper left corner of a rectangle 
                                                # x: final pan right distance (screen is 1920 wide)
                                                # y, final pan down distance (screen is 1080 high)
                                                # width, height: size of the cropped rect, 
                                                # and the second tuple is the size of that rectangle
        #easeout 5.0 crop (0, 300, 860, 600)       # here we change the y coordinate over 8 seconds to pan the image up


    $LongNVLText(narrator, (
    '''\
(Effect - zoom out (In Work))
Gritting your teeth, you tear your attention away from the dark path. Nothing good ever comes from embracing your inhibitions and dismissing your gut instincts. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
With more effort than you thought was necessary, you force your feet to move towards the left path. 
    '''
    ))
    jump path_left_path



# Scene 3a
label path_left_path:
    scene black
    show bg_leftpath with dissolve
    
    $LongNVLText(narrator, (
    '''\
!!!!Correct image?!!!!
After walking a meter or two past the fork in the road, you breathe a sigh of relief. The dark spell the large moon had on you finally dissipated. You suddenly feel more yourself again. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Using the array of planets and suns above you as an anchoring point, you continue your journey, even when it feels as though it will never end. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
“I really wish I knew how long a day lasts on this god-forsaken planet,” you say to yourself. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Every time you feel like you are making decent progress, the unchanging environment around you reminds you that you aren’t in control of this journey. With no map, no navigation equipment, you only had yourself to reassure you that you are indeed on your way to finding some sort of resources or help. If nothing else, you at least had enough mental fortitude to do that. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
To pass the time, your eyes scan the path for signs of footsteps–either friendly or unfriendly. Disconcertingly, you find neither. The wind hasn’t been that strong, so if someone had passed within the last 24 hours, you should be able to identify at least some remindents or indentations in the sand. But sadly, there was nothing. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Well your situation could be worse, you could be running away from some sort of monster, so there’s at least some sort of silver lining. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
After a few hours of exploring an endless desert path, you begin to feel weak. Your coughing fits–once rare–are now almost nonstop. In a way to deter the incoming madness from your frail constitution, you start to connect the blood spatters running across your palm for some sort of comfort. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You feel the chill in the air as darkness descends upon the landscape. This day had felt neverending. You feel placated in the fact that the days here didn’t last forever. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
Your vision begins to blur and your body feels immovable. Your face droops first, before your eyelids follow in suit. Soon you find yourself collapsed on the ground, surrounded by nothing but the night sky. Before you lose consciousness, you see in your periphery, the imposing moon that had taunted you earlier today. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
“All's well that ends well I suppose.”
    '''
    ))
    jump path_hospital


# Scene 3b
label path_hospital:
    scene black
    show bg_hospital with Fade(3,3,3)
    #show drp_casual_talking at right
    show drpl blush at right
    #  sad angry

    $LongNVLText(drpsilicon.c, (
    '''\
Beep…Beep…Beep…
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
A soft, rhythmic hum wakes you from your deep sleep. 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
Through bleary eyes, memories of you collapsing in the desert flood your mind. 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
You’re…you’re alive? 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
As your focus sharpens, you take in your surroundings. To your right you see a heartbeat monitor. To your left you see a slew of medical machines laid out alongside you. Against the wall you see a big blue screen projecting writing that you don’t recognize. 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
Crash landing on Psilicon 5, your perilous journey through the desert. Was that all a dream? Are you home? 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
Before you let optimism take over you, you hear a gentle knock on the door. 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
Not waiting for a response, a figure enters through the doorway.
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
Under normal circumstances, you would be happy to see a doctor sporting a crisp white lab coat and blue scrubs holding onto a clipboard chock full of patient notes…But this isn’t a normal circumstance. 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
The “doctor’s” skin was a sickly green, moss color. Taking up half of his face, in lieu of a typical head of hair and eyes, he had a vibrant red mushroom cap, dotted with yellow spots. 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
You silently curse under your breath as you grip the sheets in front of you. Your knuckles turning white, trying to contain your strange cocktail of emotions–fear, rage, sadness–from bursting out. 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
Just when you thought you were out…
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
“You’re lucky to be alive, that’s for sure, kid,” the doctor said in a gruff, unemotional voice. 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
You turn to respond to the “doctor”. You already feel awkward. You were never taught on how to communicate with a half-man, half-mushroom.  
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
With the ability to make eye contact removed from the situation, you settle for focusing on the more human, bottom half of his face. 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
Still groggy and dehydrated, your words came out strained. “Where am I?”
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
The doctor’s mouth tightened into a hard line. He is obviously displeased at your naivety. “Great. A case of convenient amnesia.”
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
He taps impatiently with his fingers onto his clipboard as he weighs his options. After a short pause, he sighs in an overly dramatic fashion. “You are in a hospital on the planet Psilicon 5. Due to your subpar piloting, you destroyed a nature preserve. I surely hope you have that ship insured or else you may find yourself in quite the conundrum.” 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
Nature preserve? Insurance? What the hell is he talking about? 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
With the conceited notion he gave you a sufficient debriefing on your situation, the alien doctor starts scribbling notes on his notepad. “Since you only had a case of mild dehydration, you are free to leave at any time. Don’t worry about payment yet, with your ship crashed–we know you’re not going anywhere.” 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
Placing his empty hand into his pocket, he briskly walks out of your room. “We have an escort assigned to you to get you acclimated to the town. He will be here shortly. Stay put for now.” 
    '''
    ))

    show drp_casual_talking at exitright with dissolve

    $LongNVLText(drpsilicon.c, (
    '''\
And just as he entered, he was gone. You let your head fall back onto your pillow as you try desperately to make sense of what just happened. 
    '''
    ))

    $LongNVLText(drpsilicon.c, (
    '''\
You fall back asleep. You hope this was just a long nightmare. 
    '''
    ))
    jump path_town_fork


# Scene 3c
label path_town_fork:
    scene black
    show bg_hospital with dissolve
    #show commercialcris_talking with moveinright
    show ccl cc_breathing

    $LongNVLText(commercialcris.c, (
    '''\
About an hour passes until you finally meet your escort. At this point, you’ve gotten used to the unexpected, but even this was a bit much. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Above your escort’s shoulder sits a small, outdated TV, projecting an unimpressed expression on his grayscale face. Dressed to the nines, he wears an expensive and sharply tailored suit.  
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You brows knit together in confusion…Is this how people dress on Psilicon 5? He can’t possibly have a working retro-style TV for a head, can he? 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Your escort flicks his wrist to look at his silver-plated watch impatiently. “Let’s get going, tourist. I don’t have all day.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Without thinking, you blurt out what was on your mind. “Are you a cyborg?” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
He looks at you with squinted eyes and a frown. “Lucky me. I got the comedian.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
To hide your embarrassment, you focus your attention on grabbing your things from the hospital bed. Pissing off your only hope of navigating the city. Great first impression. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
After gathering your meager belongings, mostly made up of the torn up clothes that you wore yesterday, you shuffle in awkward silence towards your escort. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Clearing his throat, your escort motions toward himself. “Now that you’ve displayed your comedic talent, let us start with some introductions. My name is Commercial Cris. As the mayor of this town, I’d like to hearby welcome you to Aisthesis, Psilicon 5’s largest city.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
“Nice to meet you.” You hoist your folded-up belongings underneath your armpit and outstretch your free hand for a handshake. When you are met with just a confused stare, you proceed to return your hand to your side. “My name is [player_name] and as you’ve probably heard, my ship crash landed on this planet.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
“So I’ve heard. Now let’s get started on your tour. I only have a few hours to spare before my next meeting,” Commercial Cris says as he walks out the door, towards the hospital’s exit. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You take the hint and follow him out of the hospital. 
    '''
    ))

    scene black
    show bg_town with pushright
    show commercialcris_talking at right

    $LongNVLText(commercialcris.c, (
    '''\
Upon opening the exit door, you are flooded with a flurry of noises. Jumbled voices speaking in an unfamiliar language, screeching of wheels from kiosks holding a variety of items, clattering of metal from the construction workers fixing the roads. It all felt so familiar yet so different. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Passing through the crowds with ease, Commercial Cris wastes no time to start his guided tour. “This town was built after the last war. Mainly functioning as a trading post approximately 100 “earth” years ago. Due to the proximity to an abundant amount of natural resources, Aisthesis thrived.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Even when a passing kiosk almost runs into him, Commercial Cris continues his tour without missing a step. “We have the best hospitals, schools, and transportation in all of Psilicon 5. Not to mention the alcohol!” Lifting his watch again to check the time, he says, “Since you’ve had quite the day, how about we grab ourselves a drink?” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
As much as you try to focus on Commercial Cris’s tour, you find it hard to concentrate when you are in such a densely packed crowd. Even more so when you look up to the tall, perfectly oddly-jagged shaped buildings. You had never seen such architecture before. You wonder how it was possible to build such a feat with such sharp, awkward angles. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Distraction was dangerous in a city like this. You nearly fall to the ground after a passing alien crashes into your shoulder. 
    '''
    ))

    show bg_town with vpunch


    $LongNVLText(commercialcris.c, (
    '''\
(Effect - shake screen...)
Your heart races as you realize that you can’t afford to fall in this crowd. This city wouldn’t wait for you. You would most certainly get run over. 
    '''
    ))

    show commercialcris_talking:
        parallel:
            #linear 1.0 xalign 1.0
            easein 3.0 xalign 0.3
        parallel:
            #linear 1.0 yalign 1.0
            linear 0.5 yalign 0.85
        parallel:
            linear 3.0 zoom .3
        parallel: 
            linear 3.0 alpha 0.3
        
    $LongNVLText(commercialcris.c, (
    '''\
(Effect: Show Commercial Cris in the distance)
The alien mumbles an apparent irritated apology before scurrying off, leaving you disoriented. In the short scuffle, you almost lose track of Commercial Cris, who has yet to notice—or care—that you aren’t behind him anymore. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Well if you want to lose your guide, now’s the time. To your right you see a blissfully empty alley you can escape to. 
    '''
    ))

    menu: 
        "Do you catch up to Commercial Cris or escape towards the alley?"
        "Go to the empty alley...":
            #3c1
            # if (persistent.path_to_outskirts_taken == False or persistent.path_to_tavern_taken == False):
            #show screen evt_choose_path
            #call screen evt_choose_route with dissolve
            $ persistent.path_to_town_taken = True
            jump path_town_alley
        "Catch up to Commercial Cris...":
            #if persistent.path_to_hut_taken == False:
            #show screen evt_choose_path 
            #call screen evt_choose_route with dissolve
            $ persistent.path_to_hut_taken = True
            jump path_tavern

    



# Scene 3c1
label path_town_alley:
    scene black
    show mswl myst_s_woman_breathing at left

    #show terrorlightz_talking at right

    #terrorlightz.c "Following a girl to a dark alley."

    $LongNVLText(commercialcris.c, (
    '''\
You wait until Commercial Cris’s silhouette disappears into the crowd before you slip into the empty alleyway. Much like the alleys on your home planet, it is mostly filled with discarded trash and a distinct smell of urine. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
(Effect - screen bouncing up and down slowly, walking...)
As you pass by the first round of unused trash cans, you notice a few shady looking aliens leaning onto the walls. The phrase “try not to stand out” runs through your mind as you quickly put your hands in your pockets and briskly walk with a fake air of confidence. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
While you could dodge the shady alien’s stares, you couldn’t ignore the increasing sense of dread you feel as the hairs on your neck perk up. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
“It’s fine. I’m fine, just feeling a bit paranoid,” You say to yourself quietly. Just yesterday you were wandering an empty desert. Today, you are trying to dodge suspicious looking aliens. If this is any indicator how your week is going to go, you aren’t sure how long you are going to keep a hold of your sanity. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
After involuntarily holding your breath as your heart thunders against your chest, you finally exit the alleyway. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
(Effect: Change scene: bg_town alley...)
Considering the bustling streets you left behind, you could only assume that you are now in the outskirts of the city. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
If you had thought the alleyway was empty, the outskirts are completely barren in comparison. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
The silence is eerie as you make your way through the town. The difference in atmosphere was so starkly different, you almost want to turn and run back to the main strip. The fear of the unknown is man’s greatest fear after all. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
But you resist the feeling and press on. The soft smack of your shoes hitting the synthetic cobblestone makes you hyper aware of your surroundings.
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Passing through empty fluorescent lit buildings, you wonder why there isn’t anyone else around. Is it a dangerous area? That doesn’t seem right. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Is it deserted? More likely, but why would they waste resources on keeping the buildings lit? 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You are so focused on making sense of your situation that you almost miss a trail of pink fabric peeking out from the corner of the next building. 
    '''
    ))

    scene black
    show bg_townalley 

    $LongNVLText(commercialcris.c, (
    '''\
(Effect: Stop walking animation, look towards right side...)
You slow your pace and lean towards the corner. While the other side of the building is dark, you are able to trace the pink fabric to a silhouette of a person wearing a large dress.
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You gulp. Another alien. Now will this be a friend or foe? 
    '''
    ))

    jump path_town_outskirts



# Scene 3c2
label path_town_outskirts:
    #show bg_tavern with dissolve
    #call screen bg_hut
    hide screen evt_choose_path
    
    scene black
    #show bg_townoutskirts with dissolve
    show bg_townalley with dissolve
    show mswl myst_s_woman_breathing at center


    $LongNVLText(mysteryspacewoman.c, (
    '''\
You hesitantly approach the alien on the other side of the dark corner. 
    '''
    ))

    show bg_townalley with dissolve

    $LongNVLText(mysteryspacewoman.c, (
    '''\
You knit your eyebrows together as you take in the strange…beautiful alien? 
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
Enveloped in a billowing, pastel pink-colored tulle dress, there stands a fragile-looking, turquoise-skinned alien. A soft trail of pink smoke, matching the color of dress, emanates off of her.  
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
She takes a few moments to examine you. After she is satisfied, she smirks at you as though she expected you to follow her. 
    '''
    ))

    show mswl myst_s_woman_talking at center 
    $LongNVLText(mysteryspacewoman.c, (
    '''\
Her face–composed of soft, feminine features–produces an empathetic smile. A gentle, melodic voice breaks through the silence. “Hello there, sweetie. Are you lost?” 
    '''
    ))

    show mswl myst_s_woman_breathing
    $LongNVLText(mysteryspacewoman.c, (
    '''\
You let out a sigh of relief. Finally, a lucky break. You feel calmer already. 
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
Smiling back awkwardly, you say, “You could say that. I’m new here and got separated from my escort.” It feels more like a half-truth, but she didn’t need to know that. 
    '''
    ))

    show mswl myst_s_woman_giggle
    $LongNVLText(mysteryspacewoman.c, (
    '''\
Her eyes widen slightly as she brings her slender hand towards her mouth. “Oh my, what poor luck you have. This is such a big city, afterall.”
    '''
    ))

    show mswl myst_s_woman_breathing
    $LongNVLText(mysteryspacewoman.c, (
    '''\
Feigning embarrassment, you look downward, clutching the back of your neck. “Yeah it was pretty busy downtown and I got a bit distracted by all of the sights.”
    '''
    ))

    show mswl myst_s_woman_talking
    $LongNVLText(mysteryspacewoman.c, (
    '''\
She cocked her head and frowned disapprovingly. “I can understand that, but do be careful. The first week I moved here I made a wrong turn and got mugged by some ruffians.” 
    '''
    ))

    show mswl myst_s_woman_breathing
    $LongNVLText(mysteryspacewoman.c, (
    '''\
You could believe that. An elegant alien like her walking by herself down the wrong street would make her a bigger target than even you–and you aren’t even from this planet. “I’m sorry to hear that. Considering the dangers, you could say I’ve been pretty fortunate.” 
    '''
    ))

    show mswl myst_s_woman_talking
    $LongNVLText(mysteryspacewoman.c, (
    '''\
“That you have, sweetie. Now where are you heading, maybe I could help?” 
    '''
    ))

    show mswl myst_s_woman_breathing
    $LongNVLText(mysteryspacewoman.c, (
    '''\
Where are you going? Do they have an immigration center here for unfortunate, lost off-world captains? 
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
After a few moments of pondering, you make up your mind. “The nearest ship station,” Maybe you could hitch a ride on the next spaceship heading towards your galaxy. You had valuable navigation skills so you could feasibly trade your services for a ride. 
    '''
    ))

    show mswl myst_s_woman_giggle
    $LongNVLText(mysteryspacewoman.c, (
    '''\
She giggles. “I knew you weren’t from here.” She cups her face with her palm as she purses her lips and looks off into the distance. 
    '''
    ))

    show mswl myst_s_woman_breathing 
    $LongNVLText(mysteryspacewoman.c, (
    '''\
(Effect - mysterious space woman bounces up and down for a few seconds.)
A minute goes by and you start doubting your odds. You start debating if you should ditch the pretty alien and try your luck exploring the city by yourself, but before you open your mouth to speak, she claps her hands excitedly and points toward the narrow alley in front of you. 
    '''
    ))

    show mswl myst_s_woman_talking
    $LongNVLText(mysteryspacewoman.c, (
    '''\
“Oh, of course! We are close to the northeastern facility.” She outstretches a hand towards you. “Come, I’ll take you.” 
    '''
    ))
    
    show mswl myst_s_woman_breathing
    $LongNVLText(mysteryspacewoman.c, (
    '''\
You take her hand and she leads you into the alley.
    '''
    ))

    jump path_town_alley_again

# Scene 3c3
label path_town_alley_again:
    #show bg_tavern with dissolve
    #call screen bg_hut
    hide screen evt_choose_path
    
    scene black
    #show bg_townoutskirts with dissolve
    show bg_townalley at my_walking with dissolve

    show mysteryspacewoman_talking at left

    $LongNVLText(mysteryspacewoman.c, (
    '''\
(Effect: WALKING ANIMATION)
After 30 minutes of seemingly aimless turns through endless rows of alleyways, you start to feel anxious. Every turn you take is the same as the last last. Dark and decrepit. While your guide is ever-confident, never once double-backed or hesitating, you still can’t comprehend that this endless maze of alleys would lead anywhere.    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
Is she lost? You hope not. She’s your only hope to get off of this god-forsaken planet. 
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
You clear your throat as you make another sharp turn. Finally, she lets go of your hand. Unsurprisingly, it looks just as uninviting as the last. “Um, are you sure we are going in the right direction?” 
    '''
    ))

    scene black
    show bg_townalley 
    show mysteryspacewoman_talking at left

    $LongNVLText(mysteryspacewoman.c, (
    '''\
You hear her giggle softly next to you. “Yes, of course, sweetie. You have to trust me.”
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
Trust her? How could you when you only met her an hour ago? Even worse, it is dark out. You lost the little amount of light you had left. Without daylight, you are completely and utterly helpless. 
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
It doesn’t seem like your guide is as knowledgeable as you once hoped so you start your own investigation. Though it’s hard to make out in the dark, you feel your way around using the cracked brick-lined walls as your guide. It only takes a minute or two of feeling around, but you start to grow more anxious when you collide with the wall on the other side of the alley. Your assumptions are correct–this alley is a dead end.  
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
You gulp and the hairs on the back of your neck perk up. This would be the perfect opportunity for someone to rob you. You shake your head and dismiss the thought. There is no way she is a criminal! 
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
As your mind was racing with how to handle this situation, you turn too quickly to the left and trip over an overturned trash can. EFFECT: BOUNCE The metallic lid screeches as it rolls through the alley.
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
A soft voice cuts through the darkness. “Don’t worry, sweetie. Let me help you up.” 
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
(Effect: PAN UP FROM BOTTOM OF ALIEN TO TOP) 
You look up and notice the pretty alien hovering over you. Your eyes widen. When did she get so close to you? You didn’t hear her following you.
     '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
You reach up to take her outstretched arm, but pull away before you make contact. Something is very, very wrong. 
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
(Effect: PAN IN CLOSER TO ALIEN’s FACE)
Upon closer inspection of her face, you notice that her eyes, once delicate and gentle, are now cold and expressionless. Her mouth, wider than before, displays pointed, jagged teeth.
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
The pink, elegant clothes she once wore melted away, revealing a horrifying wolf-like alien. Her voice, in a deeper pitch, mocks you, “What’s wrong, lost lamb?”
    '''
    ))

    $LongNVLText(mysteryspacewoman.c, (
    '''\
You scream for the last time as the terrifying alien licks its lips and dives into you. 
    '''
    ))


    jump game_over


# Scene 3c5
label path_tavern:
    scene bg_tavern with dissolve

    show commercialcris_neutral at right

    $LongNVLText(commercialcris.c, (
    '''\
You decide to stick with your guide. You are far away from home afterall. Where would you go? 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
The sidewalk is positively packed with people, making it difficult to catch up, but after some polite pushing, you are able to close the distance. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Attempting to hide your exhaustion from your escort, you slow your breaths to a normal pace. Your body is still recovering from your hospital trip. Heat stroke, dehydration, and a crash landing will do that to a person. But with the way your escort hadn’t even spared you a glance since you left the hospital, he didn’t seem to care. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Typical. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You felt a little lighter when the tavern came into view. Jovial mummers flood your ears as you approach the threshold. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Without a door to separate the outside from the inside, it is easy to spot the alien patrons sitting at the bar enjoying their drinks. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Holding onto the metal trim lining the doorway, Commercial Cris finally turns around to face you. The tv screen displays a clearly disingenuous, engineered grin on his face. With a flourish, he motions inside. “After you, tourist.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Eager to get away from the crowds, you walk into the tavern. You guess this is a good time as any to survey your surroundings. 
    '''
    ))


    jump path_tavern_nav


# Scene 3c5a
label path_tavern_nav:
    scene bg_tavern with dissolve

    $LongNVLText(narrator, (
    '''\
Explore the area by selecting an item. 
{w=3}{nw} 
    '''
    ))

    hide screen evt_choose_path
    call screen tavern_nav

    jump path_tavern_drink




label path_tavern_bin:
    $ seen_labels.add("tavern_bin")

    $LongNVLText(narrator, (
    '''\
Sitting idly outside sits a trash bin. You find some comfort in seeing that even on an alien planet, they have the same strategy to dispose of trash. 
    '''
    ))
    jump path_tavern_nav

label path_tavern_heater:
    $ seen_labels.add("tavern_heater")

    $LongNVLText(narrator, (
    '''\
Centrally placed in the tavern is a giant heater. Ornately decorated in carvings and hanging trinkets, it looms over the tavern’s patrons. You wonder how something that large emitting so much heat hadn’t burned the place down. Maybe it had? 
    '''
    ))
    jump path_tavern_nav
    
label path_tavern_patron:
    $ seen_labels.add("tavern_patron")

    $LongNVLText(narrator, (
    '''\
You notice the aliens sitting at the bar. Though you don’t understand their language, the crashing of their pint glasses and laughter made it apparent they are having a good time. 
    '''
    ))
    jump path_tavern_nav

label path_tavern_sign:
    $ seen_labels.add("tavern_sign")

    $LongNVLText(narrator, (
    '''\
Outside of the tavern hangs a single sign in an unfamiliar language. This must mark the name of the establishment. 
    '''
    ))

    jump path_tavern_nav



# Scene 3c6
label path_tavern_drink:
    scene black
    show bg_tavernbartender with dissolve

    show commercialcris_talking at right

    $LongNVLText(narrator, (
    '''\
You believe you have gotten a sufficient lay of the land. With a bit less hesitation you move deeper inside of the tavern, Commercial Cris following closely behind.
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Past the larger heater, you spy an empty table. You scoot the chair out and take a seat. You watch as Commercial Cris takes the seat directly across from you, his smile unwavering. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
“So, tourist. What’s your poison?” Commercial Cris asks, raising a hand to hail a passing waiter.
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You raise your eyebrow. You highly doubt that you could find a drink here that would resemble anything that you are familiar with so you just shrug. “I’ll have what you're having.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Eyeing your escort, you grit your teeth, quickly regretting your decision. Anything a tv-human hybrid could drink, probably isn’t good for you. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Assuming your thoughts, Commercial Cris chuckled. “Right.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
A green, scaly-faced alien approaches the table with a tablet device in hand. With a voice sounding like it was trapped underwater, she asks, eyeing Commercial Cris, “To what do we owe your presence, your majesty?” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Commercial Cris leans back onto his chair, hands laying lightly on his stomach. “Oh Belvania, you are a riot.” Tipping his large, rectangular head towards me, he says, “We have a special guest today. You know that spaceship that crashed on Plovita’s nature preserve? Well after the accident yesterday, I thought [player_name] could use a drink.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
The waiter’s beady, yellow eyes opened in surprise and looked towards you. After looking you up and down, she was obviously unimpressed. “Aye, pilot, did you get your license yesterday? You left quite the mess. It was all over the news.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Your nostrils flared and you clench your fist underneath the table. What an ignorant thing to say?! You hardly had much of a choice where you could land after the impact. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Sensing the rising tension, Commercial Cris clears his throat to take back the attention from the waitress. “My friend will take a glass of Jfetau. Nothing for me as usual.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
With a few practiced motions, the waitress places the order on the tablet and leaves the table. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You didn’t realize that you had been holding your breath until you unclench your fist and take a deep breath. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
So what if this planet doesn’t know the truth? If you play your cards right, you’ll be on the next ship and then none of this will matter. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You turn your focus back on Commercial Cris, who is looking around the tavern with a bored expression. You decide to be blunt and to the point. After that display of rudeness, you think it’s only fair to be candid. “Do you have an inter-galaxy space station here?” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
With a raised eyebrow and sour expression, Commercial Cris responds, “Yes of course. We aren’t primitives.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You feel your heart beat faster. Finally, some progress! 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Time to play the good samaritan here. This is your way out! 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You smile and open your mouth to respond, but before you can get any words out you hear glass breaking, loud cursing, and a scuffle.  Effect: Shake screen
    '''
    ))


    scene black
    show bg_insidetavern with dissolve
    show commercialcris_talking at right

    $LongNVLText(narrator, (
    '''\
You turn your head towards the loud noise. Across the tavern, you see three crouching silhouettes tumbling across the floor. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Nervously, you look towards your guide who seems utterly amused by this new development. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
With one hand on the table balancing the tv screen, he motions with his free hand towards the noise, “Lucky you, tourist. You get a show with your drink. We can call it an introduction to the culture of Aisthesis.”
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You take that as permission to break away from your awkward conversation and examine the scene. You scoot your chair back and approach the growing crowd encircling the fight.
    '''
    ))

# (Scene: CHANGE BG TO bg_tavernbartender)
    scene black
    show bg_tavernbartender with dissolve

    $LongNVLText(commercialcris.c, (
    '''\
Throughout your short tour of the city you’ve noticed that most of the creatures on Psilicon 5 are taller than you. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You try to stand on an empty chair to get a better view, but soon learn that it is ineffective. Instead, you squirm your way through the crowd until you finally get a better look. 
    '''
    ))

#    (Scene: CHANGE BG TO bg_tavernfight)
    scene black
    show bg_tavernfight with dissolve

    $LongNVLText(commercialcris.c, (
    '''\
In between the excited screeches of the crowd you hear what you could only assume are curses by the two fighting creatures.
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You have never seen anything like it before. A single “rat-like” alien sits, clutching onto the table, bracing for a fight. A larger, more imposing alien stands in front of the small alien snarling. Their onlooking table mates, a human and a green, bald-headed alien try without success to break up the fight.
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Before anyone could process the scene before them, glasses full of alcohol are thrown back and forth into the crowd. Broken bottles are scattered across the already dirty, uneven wood floor, making the situation more precarious than before. The crowd, disinterested or desensitized to the danger, continues to cheer on the fight.
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You question whether you should stay to watch the scuffle ensue, but before you can make a conscious decision, the human is thrown by the lion-headed alien into the crowd, right in front of your feet. In the heat of the moment, the human claws at your pant legs, trying to get up. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Right. Time to go. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Afraid that you are going to become an unwilling participant in this situation, you scurry back to your table. 
    '''
    ))

#    (Scene: CHANGE BG TO bg_insidetavern)
    scene black
    show bg_insidetavern with dissolve

    $LongNVLText(commercialcris.c, (
    '''\
After sitting back into your seat–which you find far more comfortable than before–you notice there is a pint of mysterious liquid in front of you. The waitress must have dropped off while you were away. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
You could really use a drink now. To hell with the consequences. With shaky hands, you take a sip. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Commercial Cris, all the more amused with your discomfort, smirks at you. “The roof is still intact so I would say you’ve just witnessed a pretty harmless fight.”
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Harmless fight he calls it. You nearly got hit in the face by an airborne glass bottle and run over by an over-excited crowd. On your home planet you may have witnessed a fight or two, but those mainly consisted of verbal-screaming matches. Physical fights were considered neanderthal tactics. So yeah, this is hardly “harmless” to you. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Ignoring the onslaught of Commercial Cris’s snide comments, you dose your discomfort in your drink. It tastes putrid, slimy, bitter, but blissfully alcoholic. After a few large gulps, you start to feel more relaxed. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Getting the hint that you aren’t going to react to his comments anymore, Commercial Cris frowns at you, glancing down at his watch impatiently. “Alright then, we are playing the quiet game. That’s alright. You have five minutes to finish your drink. I have more to show you and not enough time to do it.” 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Challenge accepted. With an air of feigned confidence, you chug the rest of your drink. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Aisthesis here you come.
    '''
    ))

    jump path_town_walk


# Scene 3c7
label path_town_walk:
    scene black
    show bg_town with dissolve

    show commercialcris_talking at right

    $LongNVLText(narrator, (
    '''\
Silently, Commercial Cris eyes you, tapping his watch with finality. With one last gulp of your drink, you get up. If your tavern experience told you anything, it is that this place is full of surprises. Now though, you are a tad tipsy—which makes this misadventure immeasurably less terrifying and much more exciting. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
With far less grace than before, you clumsily scoot your chair out and stand up, Commercial Cris already waiting at the door. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Your head spins faintly as you walk out of the tavern—almost in a straight line.
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Commercial Cris’s tour is about as good as his company at the tavern, short, brief, and a tad impatient. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
The biggest thing that stood out to you about the town is the architecture. The buildings were tall, but with jagged, pointy roofs. To match the structure, the windows are retrofitted in broken, kaleidoscope patterns. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Did windows serve a different purpose here? You couldn’t imagine that it is possible to see a clear image outside of them. Weird..but kind of cool at the same time. 
    '''
    ))

# (EDIT for Alyssa Made change to BG_TOWN and BG_TAVERNFIGHT (highlighted in yellow))

    $LongNVLText(commercialcris.c, (
    '''\
After only about 20 minutes, your “tour” of the town ended. He drops you off at exactly where you started, at the hospital. With a noncommittal grin and short wave he mentions he is late to a meeting and quickly scampers away. 
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
Being much drunker than you were this morning, you find his desertion less infuriating. Your only regret is that you didn’t get the chance to ask about the intergalactic space station. Maybe you could ask one of the nurses?  
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
With a sigh and zero options, you open the door and enter the hospital. Leaning back into your hospital bed you feel like you haven’t accomplished much today.  
    '''
    ))

# GAME OVER–Neutral Ending

    return



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

label reset:
    $ persistent._clear()
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
