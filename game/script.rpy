# The script of the game goes in this file.

# The game starts here.
label start:
    camera:
        perspective True
    #scene black 
    #with Pause(1)
    #show mytext "Dr. Psilicon Presents......" with dissolve
    #with Pause(2)
    #hide mytext with dissolve
    #with Pause(1)
    
    #return
    $ persistent.is_new_game = False
    jump path_char_customization
    #jump path_choose_char # in unusedcode.rpy
    #jump path_town_alley_again



label path_char_customization:
    scene black 

    call screen screen_customization_nav
#    jump path_choose_char  # in unusedcode.rpy


# called from eventscreens.rpy:screen screen_customization_nav
label set_customization_he_vars:
    $ pronouns = "He/Him"
    $ pronoun1 = "he"
    $ pronoun2 = "his"
    $ pronoun3 = "his"
    $ be = "is"
    $ pronoun1_selected = pronoun1
    
    #"pronoun: [pronoun1]: [pronouns]"
    jump path_char_customization
    
# called from eventscreens.rpy:screen screen_customization_nav
label set_customization_she_vars:
    $ pronouns = "She/Her"
    $ pronoun1 = "she"
    $ pronoun2 = "her"
    $ pronoun3 = "her"
    $ be = "is"
    $ pronoun1_selected = pronoun1
    
    #"pronoun: [pronoun1]: [pronouns]"
    jump path_char_customization
    
# called from eventscreens.rpy:screen screen_customization_nav
label set_customization_they_vars:
    $ pronouns = "They/Them"
    $ pronoun1 = "they"
    $ pronoun2 = "them"
    $ pronoun3 = "their"
    $ be = "are"
    $ pronoun1_selected = pronoun1
    #"pronoun: [pronoun1]: [pronouns]"
    jump path_char_customization
    
# Scene 1 Introduce Live2D protagonist side character (protl) and narrator character (narrator) with name from the screen_customization_nav in namebox  
label path_crash_site:
    scene black
    $ screen_tooltip = ""

    scene black
    #show bg_crashsite with dissolve
    play music "sounds/effects/SCENE_1_crash_beeps_alarms.mp3"

    #"Person Enters World, wake up on crash ship?"

    show protl protag_mad_breathing with dissolve:
        subpixel True pos (-0.2, 0.5)

    show bg_escapepod:
        subpixel True 
        blur 15.0
        parallel:
            xoffset 0 yoffset 0
            ease 0.15 xoffset 10 yoffset 8
            ease 0.15 xoffset -10 yoffset -8
            ease 0.15 xoffset 8 yoffset 6
            ease 0.15 xoffset -8 yoffset -6
            ease 0.15 xoffset 0 yoffset 0
        repeat
        parallel:
            blur 15.0


    $LongNVLText(narrator_none, (
    '''\
Smoke billows out of the crashed spacecraft. You, the sole survivor, wake up in a haze. Your blurry eyes, disoriented from the sharp impact, try to make sense of the destruction in front of you.
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Debris is scattered across the broken grass turf, like a distorted kaleidoscope. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Your breathing is staggered as you move to stand, clutching onto your wounded stomach. Blood pools out from inside your dark jumpsuit. 
    '''
    ))

    show protl protag_mad_talking:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator, (
    '''\
“W-where am I?” You ask in a whimper, stumbling out of the wreckage that once was your ship. 
    '''
    ))

    show protl protag_scared:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator, (
    '''\
Your memories were far and few between as your brain hadn’t made sense out of the situation yet. 
    '''
    ))

    show protl protag_lookup_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
The ship was supposed to have been indestructible. No one had been chasing you. The sensors were all clear. So what did the ship hit? 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
And what were the odds that the generator would have been the target of the impact? None of this made sense. 
    '''
    ))

    show protl protag_scared_stay:
        subpixel True 
        parallel:
            xpos -0.2 
            linear 0.27 xpos -0.2 
            linear 0.13 xpos -0.22 
            linear 0.19 xpos -0.2 
            linear 0.17 xpos -0.21 
            linear 0.17 xpos -0.2 
        parallel:
            ypos 0.5 
            linear 0.41 ypos 0.5 
            linear 0.18 ypos 0.55 
            linear 0.18 ypos 0.5 
            linear 0.16 ypos 0.55 
            linear 0.16 ypos 0.5 
    with Pause(1.19)
    show protl protag_scared_stay:
        pos (-0.2, 0.5) 
    
    $LongNVLText(narrator_none, (
    '''\
An involuntary coughing fit brought about from the dark smoke around you made you come back to your senses. 
    '''
    ))

    show protl protag_lookup_breathing_shocked:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
You look at your hand and are horrified to see tiny droplets of blood sprinkled all over your palm.  
    '''
    ))

    show protl protag_lookup_breathing_stay:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
You can make sense of this later. You need to focus on surviving. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Your movements were painfully slow, but you were able to maneuver around the wrecked ship to the ground below. 
    '''
    ))

    scene black
    show bg_crashsite with dissolve
    show smoke_effect1 
    show smoke_effect2
    show smoke_effect3

    $LongNVLText(narrator_none, (
    '''\
The grass was a welcome change in texture, soft and inviting unlike the harsh and distorted floor of the ship. 
    '''
    ))


    show protl protag_lookup_leftright:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
You had no idea where you crash landed. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
As the captain you had to make a quick decision when the ship had been hit, either take your chance on the neighboring moon or divert towards the nearest planet. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
It had seemed at the time that a planet would have more resources and potentially a civilization available, but after reviewing the landscape, you weren’t sure. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
While there was a blue sky and green grass, that’s where the comparisons ended between your home planet and the environment surrounding you. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
In the far distance welcomed a skyline of blooming mushrooms. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Using your best estimation, they had to have been as tall and thick as the redwoods you had been accustomed to seeing when you were a child. 
    '''
    ))

    show protl protag_scared:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Neon-colored flying dinosaur-looking creatures dotted the sky above. As they circled the crash site, they let out a screech. You recoiled, holding your hands protectively against your ears. 
    '''
    ))

    show protl protag_scared_talking:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator, (
    '''\
“Mushrooms as trees? Flying dinosaurs? Where am I?” 
    '''
    ))

    show protl protag_scared_stay:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Your heart starts to race when you realized that you were well and truly alone in this treacherous landscape. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
The small crew that had opted to not use the escape pods and stayed with you had all lost oxygen and died before the ship entered the planet’s atmosphere. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You truly didn’t know where to start. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
The communication system on the ship had shorted and broke before you could alert the nearest space station and you knew no one on this planet. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
With no food, no water, and only the clothes on your back, you look towards the two blistering suns in the horizon. 
    '''
    ))

    show protl protag_scared_talking:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator, (
    '''\
“Guess I’ll do this the old fashion way. Pick a direction and start walking.” 
    '''
    ))

    scene black
    show bg_crashsite at my_float

    show protl protag_scared_stay:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator, (
    '''\
You had trekked up the worn, uneven path in front of you. It was disconcerting as it appeared as though it hadn’t been used in half of a century. 
    '''
    ))


    $LongNVLText(narrator, (
    '''\
But seeming as though you had no other option, you continued onward, desperately hoping for a sign of civilization or at least another living being. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
You wonder what kinds of lifeforms live on this planet. This had been your first time in this galaxy–and of course it had ended terribly. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You had just wanted to be a space explorer like those you had grown to admire, but like most dreams, it was not what it appeared. 
    '''
    ))

    show protl protag_mad_breathing:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Crew that didn’t respect your authority, food that sprouted mold, and hygienic conditions that left little to be desired. 
    '''
    ))

    show protl protag_sigh:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
You sighed. It just seemed like your luck had gone from bad to worse. You don’t feel like you are that bad of a person. So why do you always get the shortest straw? 
    '''
    ))

    show protl protag_mad_breathing:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Guess that would be your next shower thought when you found running water. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You are exhausted from your half a day journey through the unending fields of green. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You clutch onto your wounded stomach, while the bleeding had blessedly stopped, you still felt a tremendous amount of pain. 
    '''
    ))


    $LongNVLText(narrator_none, (
    '''\
If you didn’t get help by tomorrow, you feared you may meet your demise on a deserted planet. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Your corpse feeding the humongous alien creatures that skulked around you in the distance. 
    '''
    ))

    show protl protag_mad_talking:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator, (
    '''\
“I refuse to be animal food, on my home planet or here!” You say with finality. You grit your teeth and continue onward. 
    '''
    ))

    show protl protag_mad_breathing:
        pos (-0.2, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
After another half an hour, you came across a change in scenery.
    '''
    ))

    stop music fadeout 3.0
    
    jump crash_fork




# Scene 2
# Fork in the road shown leading up to the screen_crash_fork_nav which gives the ability to test features before continuing 
label crash_fork:
    scene black
    show bg_fork with dissolve
    play music "sounds/effects/SCENE_2.mp3"
    
    show protl protag_lookup_leftright:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
What once was a temperate, lush, green landscape, turned into a dry, sandy, mountainous desert. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Even worse, the singular path you had been following diverged into two. You gulp.
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You had a feeling that there was a right or wrong answer to your choice from here. You had better choose the right one or fear the repercussions.
    '''
    ))
    $LongNVLText(narrator_none, (
    '''\
You decide to take a look around before you make your decision.
    '''
    ))

    # upon completion of the screen_crash_fork_nav will jump to crash_fork_menu
    call screen screen_crash_fork_nav




# Still part of Scene 2. Time to decide which path to take
label crash_fork_menu:
    $config.menu_include_disabled = False
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






# Scene 4/4a
# Return to the spaceship and restart or quit
label path_give_up:

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You stare at the fork in the road. With zero insight into the landscape and the perilous nature of the planet, you are facing a severe disadvantage.
    '''
    ))

    show protl protag_lookup_leftright:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Are your options really only to choose between a right or a left? You don’t think so. You still had a ship. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Sure it is partially on fire and almost entirely destroyed, but better the devil you know than the devil you don't, right? 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    scene black 
    show bg_fork at str_walking

    $LongNVLText(narrator_none, (
    '''\
Feeling safer already treading the beaten path–albeit a long one–you make the half’s day journey back to your ship. 
    '''
    ))


    $LongNVLText(narrator_none, (
    '''\
Your wound is probably infected from all of the sweat and dirt you’ve collected today, but the blood clotted so it is a far less messy affair. 
    '''
    ))

    show protl protag_sigh:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Breathing hard, clutching onto your ripped stomach, you feel weaker with every step you make. Though miraculously, you make it back to your ship. 
    '''
    ))

# Change BG to -> bg_crashsite
    scene black
    show bg_crashsite at str_walking with dissolve 

    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You are in far worse shape than when you first made the journey, but at least you are back.
    '''
    ))

    show bg_crashsite at slow_walking with dissolve 

    $LongNVLText(narrator_none, (
    '''\
With the last of your remaining strength, you climb up towards the cockpit. 
    '''
    ))

    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You nearly fall multiple times after losing your foothold–resulting in re-opening your stomach wound–but you somehow make it back to your cockpit. 
    '''
    ))

# Change BG to -> bg_cockpit
    scene black
    show bg_newcockpit with vpunch

    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Sweating profusely, you crawl into your tattered cockpit chair, the only notable item in the entire room.
    '''
    ))

    show protl protag_sigh:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You sigh as you lean back into the worn leather seat. 
    '''
    ))

    show protl protag_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You feel safe. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Quiet. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Alone.
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
The soft hum from the static of your broken flight instruments lulls you into a state of calm. 
    '''
    ))

    scene black
    hide bg_newcockpit with dissolve

    $LongNVLText(narrator_none, (
    '''\
With your clothes ripped, your hair disheveled, and night descending, you stare into the shattered windshield and slowly fade into a deep sleep. You never wake up. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You are at peace. 
    '''
    ))

    jump game_over
# GAME OVER–BAD ENDING 2





#(Effect - zoom in to the right path)
# Scene 2a
label path_right_path:
    hide screen evt_choose_path
    play music "sounds/effects/SCENE_2a.mp3"
  
    show bg_fork:
        subpixel True xzoom 1.0 yzoom 1.0 
        pos (0.5, 1.0) zpos 0.0 zoom 1.01 
        linear 1.31 pos (0.3, 1.5) zpos 0.0 zoom 1.5 
    with Pause(1.41)
    show bg_fork:
        pos (0.3, 1.5) zpos 0.0 zoom 1.5 
   
    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You stood transfixed at the shadowed silhouette of the strange moon behind the cover of the sharp mountain peaks. 
    '''
    ))
    
    $LongNVLText(narrator_none, (
    '''\
You feel it calling to you, moving your feet faster than your mind could keep up.
    '''
    ))

    $LongNVLText(narrator_none, (
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


    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Hairs prickle your back as you embrace the dark landscape. Something was following you. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You are not a soldier. You aren’t a survivalist. You are a wounded captain without a weapon or a ship. If something was following you, you are more than likely dead. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    scene black
    #show images/Speedlines.mp4 onlayer character
    show bg_rightpath at shake_and_fade


    $LongNVLText(narrator_none, (
    '''\
You feel a cold sweat forming at your brow as you force your feet to move forward. Against all of your base instincts, you don’t look behind you. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
If you looked, you would accept the fear that threatened to spill out of your insides. 
    '''
    ))

    #scene black
    #show bg_rightpath with dissolve:
        #xpos 1.25 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0
        #subpixel True
        #size (1920, 1080) crop (0, 0, 860, 600) # first tuple is the size of game screen, 
                                                # second is size of picture in pixels
        #easein 4.0 crop (0, 430, 860, 600)    # first float is time in seconds, 
                                                # tuples are coordinates of the upper left corner of a rectangle 
                                                # x: final pan right distance (screen is 1920 wide)
                                                # y, final pan down distance (screen is 1080 high)
                                                # width, height: size of the cropped rect, 
                                                # and the second tuple is the size of that rectangle
        #easeout 5.0 crop (860, 300, 860, 600)       # here we change the y coordinate over 8 seconds to pan the image up


#(Effect - zoom in and pan left to the right (In Work))
    show protl protag_scared_talking:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator, (
    '''\
“I should’ve chosen the safer path,” you curse as you force yourself to come up with an escape plan.
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Over the thunderous beat of your heart, you hear soft footsteps coming towards you. Whatever was following you was doing so very slowly and very calmly. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
It must be a big, confident creature. You still have time. You could use it to your advantage that they want to play with their food. 
    '''
    ))

    show bg_rightpath with shake_and_fade:
        subpixel True
        zoom 1.0 align (0.5, 0.5)
        linear 1.5 zoom 1.5 align (1.0, 1.0)


    $LongNVLText(narrator_none, (
    '''\
About 10 meters ahead of you, you see that the jagged mountains converge, creating what could only be described as a small tunnel. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
If you were to make it through the narrow gap before the creature catches up to you, you could possibly delay your imminent death.
    '''
    ))

    #show bg_rightpath at center, Shake(None, 1.0, dist=5) with None

    scene black
    show bg_rightpath at my_running  

# (Effect - running, shake up and down (In Work)
    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You clutch onto your wounded stomach with a small prayer that your thrown together plan wouldn’t reopen the cut and begin your mad dash to the ominous tunnel.
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You wish you had trained harder when you had the chance. You barely made the cutoff for the academy with your running scores. Not for lack of talent, but for a lack of effort.
    '''
    ))


    $LongNVLText(narrator_none, (
    '''\
You curse your past self as you choke on your ragged breaths, involuntarily running in a zigzag pattern as you spare yourself a few glances behind you. 
    '''
    ))


    $LongNVLText(narrator_none, (
    '''\
With the lack of regular exercise, your feet threaten to trip on themselves at any moment as your hands desperately search for any sort of leverage point to pull yourself quicker to your destination. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
The air behind you begins to get warmer as you realize you are losing this race. 
    '''
    ))

    show protl protag_lookup_breathing_stay_talking:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator, (
    '''\
“Only a few more feet!” You shout to convince yourself you still had a chance. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You feel a presence looming over you with every step now. Matching you step by step. You aren’t going to make it, it’s faster. 
    '''
    ))

    show protl protag_lookup_leftright:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You scan the area in a desperate attempt to come up with another strategy, you could almost hold onto the entrance to the tunnel now. You had to do something. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You sharply turn left and then double back. Claws scraped against the mountain rock. You didn’t look back, you just threw your body into the tunnel’s entrance. 
    '''
    ))

    scene black
    show bg_insidecave with pushright

    $LongNVLText(narrator_none, (
    '''\
You hear screams coming outside of the narrow gap. You made it. You were safe! You could barely believe it. 
    '''
    ))

    show protl protag_lookup_breathing_stay_talking:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator, (
    '''\
“Go find food elsewhere, you confounded beast!” You roar, the sound echoing off of the rocky walls. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)
        
    $LongNVLText(narrator, (
    '''\
You only feel a little curious to know what kind of creature you had just barely outran, but not enough to peer through the opening to find out. 
    '''
    ))



    jump path_cave






# Scene 2c
label path_cave:
    scene black
    show  bg_insidecave with dissolve

    show protl protag_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
After taking a few minutes to properly settle your heartbeat, you blindly make your way down the pitch black tunnel. You use the only tool available to you to navigate–your sense of touch.
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You feel your way forward with your hands, taking much longer than you had the patience for. Out of the oven, into the fire they say. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
It had taken a half an hour of blind exploration until you found a light source to follow. You barely believe it when you realize that the light might actually lead you to somewhere safe. 
    '''
    ))

    jump path_cave_light



# Scene 2d
label path_cave_light:
    scene black
    show bg_lightinsidecave with dissolve

    show protl protag_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You examine the exit of the tunnel. You see grass and weeds dotting the ground in a pleasant array, a warm welcome from the horrific desert landscape you had just escaped from.
    '''
    ))

    $LongNVLText(narrator_none, (
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

    show protl protag_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You weakly limp towards the greenery in front of you. You find it to be a blessed respite from the dark, cold cavernous tunnel you had just escaped from.
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\

If your hands weren’t currently occupied by holding together your open stomach, you would’ve pinched yourself. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You take in the pleasant view as the soft rays of daylight descend across the grass and shallow water. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You glance at your reflection in the water beneath you, fighting every urge to drink from it. You may not be a survivalist by trade, but you certainly know the dangers of consuming still water–whether it be from an alien planet or not.  
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Drawing your eyes away from the shallow water, you peer towards the central mass in front of you. You aren’t sure if it is from the blood loss or pure exhaustion, but you almost mistook the small hut for a meaningless pile of branches and moss. You rub your eyes with your free hand, fearing it as a mirage. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You follow the narrow path towards the hut with trepidation–unsure if the worst case scenario is it being occupied or unoccupied. From the outside, you peer through the window covered by a holey, dirty red curtain, looking for any signs of movement. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Once you feel certain that no one is inside, you slowly and carefully pull the curtain aside to get a better look. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
“It is as dilapidated inside as it is outside,” you mutter as yourr eyes scan the inside, noticing the rotted wood as it had caved in from persistent pooling water and miscellaneous junk littered all around. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Curiously, the only place left–for the most part–untouched by the destruction was the dining room table, located noticeably in the center of the shelter. Whoever last used this hut had obviously used it for a singular activity. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Shelter was shelter though. At least you wouldn’t be sleeping outside tonight. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You walk towards the open entryway and start your search for supplies while you still have some energy left. Luckily, you are able to find some scraps of worn cloth in one of the junk piles, which you use to tend to your stomach wound. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You are finally starting to feel better about your situation. You had shelter, a–mostly–clean wound, and some half rotting food to eat. As you drift off to sleep you believe that maybe your situation isn’t so bad afterall? 
    '''
    ))
    #show bg_hut:
    #    blur 0.0 
    hide protl protag_breathing  with dissolve

    show bg_hut:
        subpixel True 
        blur 0.0 
        linear 2.0 blur 15.0 
    with Pause(1.00)
    show bg_hut:
        blur 15.0 

    # out_eye transition in definitions.rpy
    scene black with out_eye
    with Pause(1.5)
    
    jump path_hut_meet_terrorlightz


# Scene 2f 
# introduce terrorlightz character (terrorlightz)
label path_hut_meet_terrorlightz:
    scene black
    #show bg_insidehut with dissolve

    # in_eye transition in definitions.rpy 
    show bg_insidehut with in_eye:
        subpixel True 
        blur 15.0 
        easeout 8.00 blur 0.0 

    show protl protag_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(terrorlightz.c, (
    '''\
Your long overdue sleep is over soon when you hear a deep, guttural voice pierce your ears.“My, my, my. What is this?”"
    '''
    ))

    show protl protag_lookup_breathing:
        subpixel True pos (-0.2, 0.5)


    $LongNVLText(narrator_none, (
    '''\
Your eyes jerk open. In front of you stands a figure that appears to be a…person? 
    '''
    ))
    
    window auto hide
    show tll terrorlightz_breathing at center with dissolve:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  
    window auto show


    
    show protl protag_lookup_breathing_shocked:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator, (
    '''\
“W-who…what are you?” Your voice shakes as you retreat into the corner of your makeshift bed. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)


    show tll terrorlightz_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  
    

    $LongNVLText(terrorlightz.c, (
    '''\
“Now, now… Is that any way to talk to your gracious host?” 
    '''
    ))

    show tll terrorlightz_breathing at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(narrator_none, (
    '''\
You feel the vibrations from his voice coarse through your body. Unexplainably, the pale purple-skinned stranger stands before you, wearing a dark teal and amethyst colored pinstripe suit.
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
His glare produces a hypnotic effect that prevents you from moving your body. Meeting his gaze, you see an optical illusion. His eyes move in an inexplicable, neverending ciruclar motion. To further punctuate his ominous presence, smoke continuously emanates out from the corners of his almond eyes. 
    '''
    ))

    show protl protag_scared_talking:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator, (
    '''\
“I-I’m sorry, I didn’t know this space was occupied!” You meekly squeak. How poignant that the first intelligent creature you’ve come across is a straight nightmare.
    '''
    ))

    show protl protag_scared_stay:
        subpixel True pos (-0.2, 0.5)

    show tll terrorlightz_laughing_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(terrorlightz.c, (
    '''\
The ghastly alien cackles at your response. His sharp, pointed teeth glint in the light as he thrusts his head back. “See, now that’s better.” Returning his gaze to you, he gives you a half smirk. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    show tll terrorlightz_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(terrorlightz.c, (
    '''\
“Now that we are back to civility, I suppose introductions are in order.” 
    '''
    ))

    window auto hide
    show tll terrorlightz_breathing:
        subpixel True xpos 0.5 
        ypos 1.0 
        linear 0.81 ypos 1.15 
        linear 0.34 ypos 1.15 
        linear 0.45 ypos 1.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  
    with Pause(1.70)
    show tll terrorlightz_breathing:
        pos (0.5, 1.0) 
    window auto show

    $LongNVLText(narrator_none, (
    '''\
In a bizarre turn of events, he gives you an overdramatic bow, his arms outstretched with a flourish. 
    '''
    ))
 
    show tll terrorlightz_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  


    $LongNVLText(terrorlightz.c, (
    '''\
“It’s very nice to meet you, my name is Terrorlightz. I welcome you heartedly to my humble abode.” 
    '''
    ))

    show protl protag_scared_stay:
        subpixel True pos (-0.2, 0.5)

    show tll terrorlightz_breathing at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(narrator_none, (
    '''\
You are speechless. You can’t fathom how this many contradictions can exist in a singular space. In front of you, stands a nightmarish creature wearing a three-piece suit who supposedly lives in this broken down shack. You can’t tell if you want to laugh or cry. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Where in the world are you? 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
After resigning to your fate, you reluctantly return the favor. 
    '''
    ))

    show protl protag_lookup_breathing_stay_talking:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator, (
    '''\
“My name is [player_name]. As you can probably tell, I’m not from here.” 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)
    
    $LongNVLText(narrator_none, (
    '''\
You are careful with your words. You don’t trust this stranger. He was exceptionally unpredictable so you felt that the less you say, the better. 
    '''
    ))

    show tll terrorlightz_breathing at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(terrorlightz.c, (
    '''\
His eyes slit, his voice drawing out every word. 
    '''
    ))

    show tll terrorlightz_squint_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(terrorlightz.c, (
    '''\
“Oh my… So I’ve found myself a wounded alien? Now, this is interesting.”
    '''
    ))

    
    window auto hide
    show tll terrorlightz_breathing:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  
        ypos 1.0 xzoom 1.0 yzoom 1.0 
        linear 1.12 ypos 1.2 xzoom 1.3 yzoom 1.3 
    with Pause(1.22)
    show tll terrorlightz_breathing:
        ypos 1.2 xzoom 1.3 yzoom 1.3 
    window auto show


    $LongNVLText(narrator_none, (
    '''\
Before you could come up with a response, Terrorlightz offers you his hand. His eyes honed in on your torn and bloodied clothes. 
    '''
    ))

    window auto hide
    show tll terrorlightz_breathing:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        ypos 1.2 xzoom 1.3 yzoom 1.3 
        linear 1.16 ypos 1.0 xzoom 1.0 yzoom 1.0 
    with Pause(1.26)
    show tll terrorlightz_breathing:
        pos (0.5, 1.0) xzoom 1.0 yzoom 1.0 
    window auto show

    show tll terrorlightz_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(terrorlightz.c, (
    '''\
“Consider yourself lucky, alien. I have just the thing to fix you right up.” 
    '''
    ))

    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    show protl protag_sigh:
        subpixel True pos (-0.2, 0.5)
        
    show tll terrorlightz_breathing at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(narrator_none, (
    '''\
You stare at his outstretched hand momentarily before you grasp ahold of it. You weakly lift yourself off of the worn, broken couch. 
    '''
    ))
   
    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
The academy only taught you basic first aid and your half-assed attempt at putting your stomach back together isn’t going to cut it. You either slowly bleed out or take a chance that Terrorlightz doesn’t have ulterior motives. 
    '''
    ))

    show tll terrorlightz_squint_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  


    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(terrorlightz.c, (
    '''\
He almost reminds you of a shark when his sharpened, pointy teeth glint in the light. “Now, let's forage for some mushrooms.” 
    '''
    ))
    
    show tll terrorlightz_breathing at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    #window auto hide
    show tll terrorlightz_breathing:
        subpixel True xzoom 1.0 yzoom 1.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        parallel:
            pos (0.5, 1.0) zoom 1.0 
            linear 1.06 pos (0.97, 0.81) zoom 0.2 
        parallel:
            alpha 1.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            linear 1.02 alpha 1.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0478181468665897)*SaturationMatrix(1.0)*BrightnessMatrix(-0.75)*HueMatrix(0.0) 
    with Pause(1.16)
    show tll terrorlightz_breathing:
        pos (0.97, 0.81) zoom 0.2 alpha 1.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0478181468665897)*SaturationMatrix(1.0)*BrightnessMatrix(-0.75)*HueMatrix(0.0) 
    #window auto show



    $LongNVLText(narrator_none, (
    '''\
With a smooth flick of the wrist, Terrorlightz motions towards the door. Without waiting for any acknowledgement of your intention to follow him, he turns his back and exits the hut. 
    '''
    ))


    show protl protag_mad_breathing

    $LongNVLText(narrator_none, (
    '''\
He can’t be serious can he? He actually wants to forage for mushrooms? 
    '''
    ))


    $LongNVLText(narrator_none, (
    '''\
You hesitantly follow Terrorlightz outside of the hut. It goes against all of your instincts to trust this stranger, even more so to root around for unknown plants. But he hasn’t killed you yet and he’s had ample opportunities. That’s something, isn’t it? 
    '''
    ))

    hide protl protag_mad_breathing with dissolve
    pause 0.5


    jump path_hut_forage 






# Scene 2g
label path_hut_forage:
    scene black
    show bg_hut with dissolve

#    show tll terrorlightz_talking at right

    show protl protag_lookup_leftright:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Leaving the confines of your temporary shelter reminds you that you are still on an alien, unfamiliar planet. It felt much too easy to forget where you are–even with Terrorlightz’s jarring presence.
    '''
    ))

    show protl protag_scared_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Stepping out of the hut, the sunlight was blinding. You are forced to squint and throw your hands up to shield your eyes. It must be the start of a new day as the two suns in the sky are much brighter than before. Either you are right and the days here last a long time or the shock from the crash dulled your senses. 
    '''
    ))

    show protl protag_sigh:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You feel a sudden rush of homesickness. Will you ever be back home? You had craved space travel for so long and worked so hard to achieve it, but now it seems meaningless. 
    '''
    ))

    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
What was it all for? You would have never signed up if you knew you would end up alone, crash landed on a bizarre planet, foraging for–most likely poisonous–mushrooms with an absolute utter madman? 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
I’m sure your crew is laughing at you from the afterlife. How the mighty captain has fallen. 
    '''
    ))

    show protl protag_lookup_leftright:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Once your eyes finally adjust to the light, you scan the area, Terrorlightz is nowhere in sight. You were only a few steps behind him leaving the hut. Where could he have gone? 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You feel a sudden urge to run. To where, you aren’t sure, but once you find Terrorlightz, you are pretty positive you won’t have that option again. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
But at the same time, at least here you have shelter and some promise of food. You barely survived on your own, so it seems foolish to give into your instincts now. 
    '''
    ))

    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
With resignation, you decide to stick with Terrorlightz. Better than starving. 
    '''
    ))

    window auto hide
    show bg_hut:
        subpixel True yzoom 1.0 
        parallel:
            pos (0.5, 1.0) 
            linear 1.95 pos (0.65, 1.75) 
        parallel:
            zpos 0.0 
            linear 0.01 zpos 0.0 
        parallel:
            zoom 1.0 
            linear 0.01 zoom 1.0 
            linear 1.93 zoom 2.5 
    with Pause(2.05)
    show bg_hut:
        pos (0.65, 1.75) zpos 0.0 zoom 2.5 
    window auto show

    $LongNVLText(narrator_none, (
    '''\
You search south of the hut where a clump of tall trees swallow the nearby light, blanketing the floor in almost near darkness. If mushrooms grow similarly here as they did in your home planet, this is most likely where they would grow.
    '''
    ))


    show tll terrorlightz_menacing at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(narrator_none, (
    '''\
You find Terrorlightz hunched over the base of a thick tree trunk. His dissatisfaction is clear even with his back towards you. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    show tll terrorlightz_menacing_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(terrorlightz.c, (
    '''\
His deep, baritone voice almost shakes the ground when he says, “You must know, alien, that it is impolite to make someone wait.” 
    '''
    ))

    show tll terrorlightz_menacing at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(narrator_none, (
    '''\
You feel less terrified than you would’ve been thirty minutes ago, which surprises you. You suppose that giving into your fate helped to have lessened the blow.
    '''
    ))

    show protl protag_lookup_breathing_stay_talking:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator, (
    '''\
“Sorry. You're tall and I can barely walk. Makes for an unfortunate combination.” 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    show tll terrorlightz_squint_stay at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(narrator_none, (
    '''\
Ignoring your comment, Terrorlightz points to the ground in front of him. You had to move to stand next to him to see what he was pointing at. 
    '''
    ))

    show tll terrorlightz_squint_stay_up at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You furrow your brow. It was a small mushroom–no larger than a tennis ball–with a wide red brim, covered in a neon pink moss. 
    '''
    ))

    show protl protag_mad_talking:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator, (
    '''\
“What kind of mushroom is it?” 
    '''
    ))

    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    show tll terrorlightz_breathing at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  


    $LongNVLText(terrorlightz.c, (
    '''\
Back to his mischievous ways, Terrorlightz turns to face you wearing a devious grin. The spirals in his eyes roll faster than before. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Yup, you aren’t totally desensitized yet. He is still terrifying. 
    '''
    ))

    show tll terrorlightz_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(terrorlightz.c, (
    '''\
“This here, dear alien, is a Psilicon mushroom. Very rare indeed, you are quite lucky. Eat one of these and you’ll find what you are looking for.” 
    '''
    ))

    show tll terrorlightz_breathing at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    show protl protag_lookup_breathing_stay_talking:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator, (
    '''\
“What do you mean, find what I’m looking for? I just want something to patch myself back together.” 
    '''
    ))

    show tll terrorlightz_laughing_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    
    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(terrorlightz.c, (
    '''\
Terrorlightz cackles, plucking the fuzzy mushroom off the moist ground. He inspects it a bit closer and then offers it to you. “Oh, don’t you worry, this will heal you up, and so much more.”
    '''
    ))

    show tll terrorlightz_breathing at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)


    $LongNVLText(narrator_none, (
    '''\
You gulp. You definitely should have run when you had the chance. 
    '''
    ))


    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(terrorlightz.c, (
    '''\
Sweat beads your forehead as you contemplate your available options. 
    '''
    ))


    show protl protag_talking:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
“I appreciate the offer, but I think I’m okay,” you say, patting your stomach wound gently. “A few more nights rest and I’ll be good as new.” 
    '''
    ))

    show protl protag_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You give him your best used car salesman smile to add emphasis to your point. Is this all just a bluff? Yes. You reason that it would take at least a month to be back to full health. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
But Terrorlightz didn’t need to know that.
    '''
    ))
    
    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.2, 0.5)

    show tll terrorlightz_scary_stay at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  


    $LongNVLText(narrator_none, (
    '''\
You feel the hairs on your back raise when you meet his eyes. Behind the emptiness there was a hint of madness that wasn’t there before. The normally disconcerting smile crinkled into something more devious. 
    '''
    ))

    show tll terrorlightz_scary_stay_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  


    $LongNVLText(terrorlightz.c, (
    '''\
“That’s funny, because I don’t recall giving you an option.” 
    '''
    ))

    show tll terrorlightz_scary_smile at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  


    $LongNVLText(narrator_none, (
    '''\
You start slowly walking backwards as Terrorlightz, much too easily, wipes the dirt off of his pants and moves to stand up. Your hands involuntarily reflex from an unclenched to clenched position as your mind races between fight or flight mode. 
    '''
    ))

    show tll terrorlightz_scary_stay_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  

    $LongNVLText(terrorlightz.c, (
    '''\
With a cackle Terrorlightz holds the mushroom in an open palm towards you. “Now be a good alien and eat your vegetables.” 
    '''
    ))


    $LongNVLText(narrator_none, (
    '''\
Flight it is. You turn in the opposite direction, digging your heels into the muddy ground and take off into a sprint. 
    '''
    ))

    show bg_hut:
        subpixel True xpos 0.8 zoom 2.5 
        ypos 1.75 
        linear 0.19 ypos 2.0 
        linear 0.19 ypos 1.75 
        linear 0.21 ypos 2.0 
        linear 0.20 ypos 1.75 
        linear 0.21 ypos 2.0 
        linear 0.18 ypos 1.75 
        linear 0.20 ypos 2.0 
        linear 0.22 ypos 1.75 
        linear 0.19 ypos 2.0 
        linear 0.22 ypos 1.75 
        linear 0.21 ypos 2.0 
        linear 0.21 ypos 1.75 
        linear 0.23 ypos 2.0 
        linear 0.25 ypos 1.75 
        linear 0.24 ypos 2.0 
        linear 0.26 ypos 1.75 
    show tll terrorlightz_scary_stay:
        subpixel True xzoom 1.0 yzoom 1.0 
        zoom 1.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 3.09 zoom 0.5 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(-0.5)*HueMatrix(0.0) 
    with Pause(3.19)
    show tll terrorlightz_scary_stay:
        zoom 0.5 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(-0.5)*HueMatrix(0.0) 
    with Pause(3.19)
    
    with Pause(3.51)
    camera:
        zpos 0.0 
    show bg_hut:
        pos (0.8, 1.75) 

    show tll terrorlightz_scary_stay:
        subpixel True xzoom 1.0 yzoom 1.0 
        zoom 1.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 3.09 zoom 0.5 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(-0.5)*HueMatrix(0.0) 
    with Pause(3.19)
    show tll terrorlightz_scary_stay:
        zoom 0.5 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(-0.5)*HueMatrix(0.0) 
    camera:
        subpixel True 
        zpos 0.0 
        linear 0.65 zpos 0.0 
    window auto show




    $LongNVLText(narrator_none, (
    '''\
Why is this planet constantly trying to kill you? It would be nice to have one full day that wouldn’t require running for your life. 
    '''
    ))


    #window auto hide
    camera:
        subpixel True 
        zpos 0.0 
        linear 0.65 zpos 0.0 
    show bg_hut:
        subpixel True xpos 0.8 zoom 2.5 
        ypos 1.75 
        linear 0.19 ypos 2.0 
        linear 0.19 ypos 1.75 
        linear 0.21 ypos 2.0 
        linear 0.20 ypos 1.75 
        linear 0.21 ypos 2.0 
        linear 0.18 ypos 1.75 
        linear 0.20 ypos 2.0 
        linear 0.22 ypos 1.75 
        linear 0.19 ypos 2.0 
        linear 0.22 ypos 1.75 
        linear 0.21 ypos 2.0 
        linear 0.21 ypos 1.75 
        linear 0.23 ypos 2.0 
        linear 0.25 ypos 1.75 
        linear 0.24 ypos 2.0 
        linear 0.26 ypos 1.75 
    with Pause(3.51)
    camera:
        zpos 0.0 
    show bg_hut:
        pos (0.8, 1.75) 
    #window auto show



    $LongNVLText(narrator_none, (
    '''\
You feel lightheaded as you suck in air as quickly as you exhale. The humidity in the air feels thick in your lungs, making running a much harder endeavor. Mud spits onto your pants as you slide around the rotund trees, trying to distance yourself from the madman close onto your tail.
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You are already at a disadvantage since Terrorlightz knows the area much better than you do, but pray that the darkness from the tree canopy above you can increase your odds. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
There was little to no noise in the forest save for the soft squelching sounds as you and your assailant’s feet hit the wet ground. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
This feels worse than last night’s attack. Yesterday, you felt like you were the victim of a hungry animal. Today, it feels personal. 
    '''
    ))

    window auto hide
    show bg_hut with vpunch:
        pos (0.65, 1.75) zpos 0.0 zoom 2.5 
    window auto show
    
    $LongNVLText(narrator_none, (
    '''\
Your foot catches on a branch and you slide front first onto the ground. You taste mud as you grasp for a dry patch of ground for leverage, but you aren’t quick enough. 
    '''
    ))


    #window auto hide
    show tll terrorlightz_scary_stay:
        subpixel True pos (0.5, 1.0) xzoom 1.0 yzoom 1.0 
        parallel:
            blend 'normal' zoom 0.5 alpha 1.0 
            linear 2.00 blend 'normal' zoom 1.0 alpha 1.0 
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(-0.5)*HueMatrix(0.0) 
            linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(-0.5)*HueMatrix(0.0) 
            linear 1.99 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with Pause(2.10)
    show tll terrorlightz_scary_stay:
        blend 'normal' zoom 1.0 alpha 1.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    #window auto show

    show protl protag_lookup_breathing_shocked:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Before you can process what was happening, you are being lifted off the ground by your shirt. 
    '''
    ))

    show protl protag_scared_stay:
        subpixel True pos (-0.2, 0.5)

    show tll terrorlightz_scary_stay_talking at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  


    $LongNVLText(terrorlightz.c, (
    '''\
You struggle against Terrolightz’s fierce grip as he positions you to face him. “You are a difficult one, aren’t you?” You desperately cling onto Terrorlightz’s fierce grip, trying to release yourself, but his strength is inhuman. 
    '''
    ))

    show tll terrorlightz_scary_stay at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  


    $LongNVLText(narrator_none, (
    '''\
Using his available hand, Terrolightz reaches into his pocket to retrieve the mushroom and shows it to you. Somehow, despite the scuffle, it is still perfectly preserved. The pink moss covering the mushroom faintly glows among the intense shade. 
    '''
    ))

    show protl protag_scared_stay:
        subpixel True pos (-0.2, 0.5)
    window auto hide

    $LongNVLText(narrator_none, (
    '''\
Your eyes grow wide when you realize that you don’t have a choice in this matter anymore. It’s dinner time. 
    '''
    ))

    show protl protag_scared:
        subpixel True pos (-0.2, 0.5)

    window auto show
    show tll terrorlightz_laughing at center:
        subpixel True alpha 1.0 additive 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)  
    window auto hide

    $LongNVLText(terrorlightz.c, (
    '''\
With a final cackle, Terrorlightz shoves the mushroom into your mouth, holding it closed until you finally swallow. 
    '''
    ))

    show protl protag_scared with vpunch:
        subpixel True pos (-0.2, 0.5)
    window auto hide

    $LongNVLText(narrator_none, (
    '''\
Then suddenly, Terrorlightz, just as easily as he picked you up, drops you to the ground and walks away, leaving you muddy and gasping for air. 
    '''
    ))

    hide tll with dissolve
    hide bg_hut with dissolve
    hide protl
    
    window auto hide
    camera:
        subpixel True zpos 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.5)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    scene black
    show bg_abstract1 at abstract_scene
    pause 5.0

    $LongNVLText(narrator_none, (
    '''\
Your consciousness fades as you enter a dream state. Your vision fills with abstract, colorful shapes that gently pulsate and come in and out of focus. You aren’t an individual anymore, you are part of a singularity. 
    '''
    ))

    window auto hide
    camera:
        subpixel True zpos 0.0 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.5)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    scene black
    show bg_abstract1 at abstract_scene

    #show bg_abstract1:
        #xpos 0 xzoom 1.0 yzoom 1.0 zoom 1.0 blur 2.0 

    scene black
    show bg_abstract1 at abstract_scene
    pause .5
    show bg_abstract2 with dissolve
    pause .5
    hide bg_abstract2 with dissolve
    pause .5
    scene black
    show bg_abstract1 at abstract_scene
    
    #hide bg_abstract1 with dissolve
    #pause 0.5
    #show bg_abstract2 with dissolve
    #hide bg_abstract2 with dissolve
    #show bg_abstract1 with dissolve


    $LongNVLText(narrator_none, (
    '''\
Thoughts and feelings that aren’t your own come through all at once in diverse pitch and tone. The senseless gibberish is impossible to describe, but you understand that it is trying to communicate with you. 
    '''
    ))

    hide bg_abstract1 with dissolve
    pause 0.5
    show bg_abstract2 with dissolve
    hide bg_abstract2 with dissolve
    show bg_abstract1 with dissolve
    hide bg_abstract1 with dissolve
    show bg_abstract2 with dissolve
    hide bg_abstract2 with dissolve
    show bg_abstract1 with dissolve
    hide bg_abstract1 with dissolve

    scene black
    
    window auto hide
    show bg_newcockpit:
        subpixel True alpha 1.0 
        parallel:
            blur 20.0 
            linear 0.28 blur 12.0 
            linear 0.27 blur 20.0 
            linear 0.50 blur 10.0 
            linear 1.01 blur 0.0 
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.5)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            linear 0.66 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            linear 1.11 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with Pause(2.16)
    show bg_newcockpit:
        blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

    $LongNVLText(narrator_none, (
    '''\
The geometric shapes start to shrink and organize themselves into what appears to be an image. After it takes shape, you recognize the image as a snapshot of a ship. 
    '''
    ))

    window auto hide
    show bg_newcockpit:
        subpixel True 
        parallel:
            alpha 1.0 
            linear 0.01 alpha 1.0 
        parallel:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            linear 0.01 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            linear 1.95 matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.65)*SaturationMatrix(0.5)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with Pause(2.06)
    show bg_newcockpit:
        alpha 1.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(0.65)*SaturationMatrix(0.5)*BrightnessMatrix(0.0)*HueMatrix(0.0) 


    $LongNVLText(narrator_none, (
    '''\
Wait. Is that your ship? 
    '''
    ))


    window auto hide
    show bg_newcockpit:
        subpixel True 
        xzoom 1.0 yzoom 1.0 zoom 1.0 
        linear 1.25 xzoom 0.9 yzoom 0.9 zoom 1.2 
    with Pause(1.35)
    show bg_newcockpit:
        xzoom 0.9 yzoom 0.9 zoom 1.2 


    $LongNVLText(narrator_none, (
    '''\
You focus closer in on the front console. On the captain's chair, you recognize the cheap, worn black leather with a sharp gash in the back and the rusty gear shifts positioned directly alongside it. After confirming the most familiar part of the ship, you inspect the rest of the vessel. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You can barely believe it. This is your ship!
    '''
    ))


    show bg_newcockpit with vpunch 
    
    window auto hide
    show protl protag_breathing onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7 
        subpixel True ypos 1 
        xpos -0.35 
        linear 0.82 xpos 0.4 
        subpixel True xpos .4 ypos 1 zoom 0.7 
    with Pause(0.92)
    show protl protag_breathing onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7 

    $LongNVLText(narrator_none, (
    '''\
You startle when a figure passes through you and sits in the captain’s chair. Even more so when you realize it is you. 
    '''
    ))

    show protl protag_breathing onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7 


    $LongNVLText(narrator_none, (
    '''\
Was this some sort of a test? Memory? Dream? Parallel universe? You have no idea. 
    '''
    ))

    show protl protag_breathing onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7


    $LongNVLText(narrator_none, (
    '''\
A disembodied voice snaps into existence. “Captain, we know it’s your birthday today, so the crew put together a little something for you.” 
    '''
    ))

    show protl protag_breathing onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
Was that Jack? You couldn’t tell, you are still the only visible figure in the room. 
    '''
    ))

    show protl protag_breathing onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator, (
    '''\
Your past self sat with hunched shoulders, looking in the opposite direction. In a monotone voice, you said, “Did you really?” 
    '''
    ))

    show protl protag_breathing onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
Jack’s voice changed to a higher, more confident pitch. “Of course, you are our captain after all.” 
    '''
    ))

    show protl protag_scared_stay onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
Only you know the expression on your face. Self-deprecation. Your crew hated you, you knew that better than anyone. You believe that this must be yet another prank to undermine your authority. 
    '''
    ))

    show protl protag_scared_stay onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
The pink wrapped package appears out of empty space in front of your past self. Even knowing what was coming, your past self still takes the half-hazardly packaged gift and opens it.
    '''
    ))

    show protl protag_scared_stay onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
You come close to inspect the gift. Why can’t you remember what was inside? 
    '''
    ))

    show protl protag_scared_stay onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
Inside the box and crinkled white tissue paper were two mushrooms. Both identical in size and shape with a white stem and neon red brim. 
    '''
    ))

    show protl protag_scared_stay onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
Your past self takes out one of the mushrooms and inspects the white dots decorating the top. 
    '''
    ))

    show protl protag_scared_stay onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
Jack’s voice echoes the metallic walls as he laughs. “Now go ahead and take a bite, captain.” 
    '''
    ))

    show protl protag_sigh onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
Your past self’s shoulders droop even farther in on themselves as your grip tightens onto the mushroom. You see rage in your eyes as well as sadness. 
    '''
    ))

    show protl protag_mad_talking onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator, (
    '''\
The sad captain whispers softly, “If you think you’ll make a laughing stock of me, you are wrong, Jack.” 
    '''
    ))

    show protl protag_talking onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
With a clenched fist, your past self quickly stands up from the captain’s chair and addresses the empty audience, “What a kind gift! How lucky I am to have such a wonderful crew.” 
    '''
    ))

    show protl protag_breathing onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
You gulp as you watch the familiar silhouette take the crushed mushroom and gobble it up with feigned joy. 
    '''
    ))

    show protl protag_talking onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    show protl protag_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator, (
    '''\
“Quite delicious, thank you.” 
    '''
    ))

    show protl protag_breathing onlayer transient:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .4 ypos 1 zoom 0.7

    hide protl protag_breathing with vpunch

    show protl protag_lookup_breathing onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
Your past self dramatically falls onto the floor, unconscious. The disembodied voices of your crew are cheering and high fiving each other. 
    '''
    ))

    show protl protag_lookup_breathing_stay_talking onlayer character:
        subpixel True alpha 1.0 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(2.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.8)*HueMatrix(0.0) blend 'normal' 
        subpixel True xpos .1 ypos 1 zoom 0.7

    $LongNVLText(narrator_none, (
    '''\
“Finally, we are free! Remember the story boys, the ship was due to crash on an unexplored planet and our courageous captain volunteered to stay behind so we could live.” 
    '''
    ))

    hide bg_cockpit with dissolve

    scene black with dissolve

    hide protl protag_lookup_breathing onlayer character


    $LongNVLText(narrator_none, (
    '''\
The scene changes and all the colors disappear, leaving nothing but pure darkness behind. 
    '''
    ))

    show protl protag_lookup_breathing_shocked onlayer transient:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Abruptly, you feel yourself being pulled back to your body and you wake up with a start, gasping for air. 
    '''
    ))

    show protl protag_mad_breathing onlayer transient:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You ignore the violent shaking of your legs as you pull yourself up. 
    '''
    ))

    show protl protag_mad_talking onlayer transient:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator, (
    '''\
You snarl, “Those sons of bitches! I won’t let them get away with this.” You violently clutch onto the passing trees as you start running through the thick mud. You have to get back to your ship. 
    '''
    ))

    show protl protag_mad_breathing onlayer transient:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
There has to be some way to fix this. 
    '''
    ))

    show protl protag_mad_breathing onlayer transient:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
In your blind rage, you don’t even notice that your stomach wound has healed. 
    '''
    ))

    jump ship_remember





# Scene 2h
label ship_remember:
#    scene black
#    show bg_hut with dissolve

    scene black
    show bg_insidecave at basic_fade, my_walking with dissolve:
        subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.5)*BrightnessMatrix(0.17)*HueMatrix(0.0) 


#, my_shake 

    pause 5

    show protl protag_mad_breathing onlayer transient:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Nothing but regret and resentment fill your mind as you clumsily stumble your way through the swamp and into the dark cave.
    '''
    ))

# (Effect: Shows running (fading and out) from bg_hut to bg_insidecave(In Work))
    
    show protl protag_mad_breathing onlayer transient:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Even though it was only yesterday that you first entered the cave, you feel none of the terror or fear you felt before.
    '''
    ))

    scene black
    show bg_crashsite at basic_fade, my_walking with dissolve


# (Shows running (fading and out) from bg_insidecave to bg_crashedsite)
    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
No matter what obstacle comes your way now, you are willing to face it. The only thing that matters is getting to your ship and righting the wrong against you."
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
After a matter of hours, you are exhausted and dehydrated. Your sore limbs fight against you, but you press on. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
In the distance you see the remnants of what was left of your ship. Your mangled body screams as you sprint to close the distance. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Black smoke still emanates from the ship’s exhaust as you approach the destruction. The contaminated air makes it more difficult to breathe than it should. 
    '''
    ))

    show bg_crashsite at slow_walking with vpunch

    $LongNVLText(narrator_none, (
    '''\
Your heart thunders against your chest as you scramble to climb the fallen, broken pieces of the crew cabin. 
    '''
    ))
    

    $LongNVLText(narrator_none, (
    '''\
It takes you a while, but you manage to make progress on your climb. 
    '''
    ))
    
    show bg_crashsite at slow_walking with vpunch

    $LongNVLText(narrator_none, (
    '''\
Your tired body almost gives out in the last stretch, but you use the handle from the blown out emergency exit door as leverage to pull yourself inside the ship. 
    '''
    ))

    scene black
    show bg_cockpit at basic_fade:
        subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.3)*BrightnessMatrix(0.1)*HueMatrix(0.0) 



    $LongNVLText(narrator_none, (
    '''\
Yesterday, you were so wounded and discombobulated that you weren’t able to process the damage. Now, you could finally understand the level of destruction the crash did to the ship. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
While most of the ship was in a desperate state of disrepair, your cockpit took the brunt of the damage. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
The ceiling had caved in, light pouring in from the gaps. You snickered solemnly to yourself, at least the light made it easier to navigate around the ship.
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
The windshield had shattered, spraying glass all throughout the cabin. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
To your right, you see what was left of your captain’s chair, only scattered pieces of black leather and wheels remain. In front of you, you see your warped and melted flight instruments. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You are pretty sure all of the consoles are busted, but you still try for hours to get the communication console back up and running. 
    '''
    ))

    show protl protag_sigh:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
All you get is silence. 
    '''
    ))

    show protl protag_mad_breathing:
        subpixel True pos (-0.2, 0.5)

    scene black
    show bg_escapepod with dissolve:
        subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.1)*HueMatrix(0.0) 


    $LongNVLText(narrator_none, (
    '''\
In pure desperation, you maneuver yourself to the back of the ship. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
The crew wouldn’t be so inhumane that they would leave you without an escape pod. I mean, they hated you, but they wouldn’t be that cruel… would they? 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
The level of resignation you feel as you approach the empty escape pod unit is unparalleled to anything you have felt before. 
    '''
    ))

    show protl protag_mad_breathing with vpunch:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
You drop to your knees. Your tattered clothes gently sway in the wind through the gaps in the walls.
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
That’s it. You are stuck on a godforsaken planet with only a useless ship to your name. 
    '''
    ))
    scene black
    hide bg_escapepod with dissolve
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
    hide screen evt_choose_path
    scene black
    show bg_fork with dissolve:
        size (1920, 1080) 
        # Starting point with tuple of (x, y, width, height)
        crop (430, 430, 860, 600) 

        # Warpers: https://www.renpy.org/doc/html/transforms.html#warpers
        #     https://easings.net/

        # first float is time in seconds, 
        # first tuple are coordinates of the upper left corner of a rectangle, 
        # and the second tuple is the size of that rectangle
        # start in the center
        crop (430, 430, 860, 600) 
        pause 3.0

        # then look to the right path
        ease_quad 3.0 crop (600, 430, 860, 600)  

        # then look back to the left path
        ease_quad 6.0 crop (100, 430, 860, 600)

        pause 2.0
        # and then pan up
        ease_cubic 4.0 crop (0, 200, 860, 600) 



#(Effect - zoom in on left path)
    show protl protag_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Your eyes land on the seemingly safer option. The two suns and neighboring planets were hung in the sky like ornaments on a Christmas tree, brightly lighting the path in front of you.
    '''
    ))

    # scene black
    # show bg_fork with dissolve:
    #     #xpos 1.25 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0
    #     subpixel True
    #     size (1920, 1080) crop (0, 0, 860, 600) # first tuple is the size of game screen, 
    #                                             # second is size of picture in pixels
    #     easein 4.0 crop (860, 430, 860, 600)    # first float is time in seconds, 
    #                                             # tuples are coordinates of the upper left corner of a rectangle 
    #                                             # x: final pan right distance (screen is 1920 wide)
    #                                             # y, final pan down distance (screen is 1080 high)
    #                                             # width, height: size of the cropped rect, 
    #                                             # and the second tuple is the size of that rectangle
    #     #easeout 5.0 crop (0, 300, 860, 600)       # here we change the y coordinate over 8 seconds to pan the image up

# (Effect - zoom in on right path)
    show protl protag_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
The right path scared you. It called to you like a siren in turbulent waters, inviting you in with a sweet song."
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You try to stand your ground in fear of being pulled into the imposing moon’s imaginary gravitational pull. 
    '''
    ))

    # scene black
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


# (Effect - zoom out (In Work))
    show protl protag_breathing:
        subpixel True pos (-0.2, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Gritting your teeth, you tear your attention away from the dark path. Nothing good ever comes from embracing your inhibitions and dismissing your gut instincts." 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
With more effort than you thought was necessary, you force your feet to move towards the left path. 
    '''
    ))
    jump path_left_path



# Scene 3a
label path_left_path:
    scene black
    show bg_leftpath with dissolve
    
    show protl protag_mad_breathing: 
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
After walking a meter or two past the fork in the road, you breathe a sigh of relief. The dark spell the large moon had on you finally dissipated. You suddenly feel more yourself again.
    '''
    ))

    show protl protag_mad_breathing: 
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Using the array of planets and suns above you as an anchoring point, you continue your journey, even when it feels as though it will never end. 
    '''
    ))

    #nvl clear

    show protl protag_mad_talking: 
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator, (
    '''\
“I really wish I knew how long a day lasts on this god-forsaken planet,” you say to yourself. 
    '''
    ))

    show protl protag_mad_breathing: 
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Every time you feel like you are making decent progress, the unchanging environment around you reminds you that you aren’t in control of this journey. With no map, no navigation equipment, you only had yourself to reassure you that you are indeed on your way to finding some sort of resources or help. If nothing else, you at least had enough mental fortitude to do that. 
    '''
    ))

    show protl protag_lookup_leftright: 
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
To pass the time, your eyes scan the path for signs of footsteps–either friendly or unfriendly. Disconcertingly, you find neither. The wind hasn’t been that strong, so if someone had passed within the last 24 hours, you should be able to identify at least some remindents or indentations in the sand. But sadly, there was nothing. 
    '''
    ))

    show protl protag_sigh: 
        subpixel True pos (-0.17, 0.5)

    $LongNVLText(narrator_none, (
    '''\
Well your situation could be worse, you could be running away from some sort of monster, so there’s at least some sort of silver lining. 
    '''
    ))

    show protl protag_mad_breathing: 
        subpixel True pos (-0.17, 0.5)

    $LongNVLText(narrator_none, (
    '''\
After a few hours of exploring an endless desert path, you begin to feel weak. Your coughing fits–once rare–are now almost nonstop. In a way to deter the incoming madness from your frail constitution, you start to connect the blood spatters running across your palm for some sort of comfort. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You feel the chill in the air as darkness descends upon the landscape. This day had felt neverending. You feel placated in the fact that the days here didn’t last forever. 
    '''
    ))

    show protl protag_mad_breathing with hpunch: 
        subpixel True pos (-0.17, 0.5)
    
    window auto hide
    camera character:
        subpixel True 
        parallel:
            alpha 1.0 
            linear 2.67 alpha 1.0 
        parallel:
            blur 0.0 
            linear 1.23 blur 1.0 
            linear 1.44 blur 0.0 
    show bg_leftpath:
        subpixel True 
        blur 0.0 
        linear 0.66 blur 20.0 
        linear 0.72 blur 0.0 
        linear 0.75 blur 20.0 
    with Pause(2.77)
    camera character:
        alpha 1.0 blur 0.0 
    show bg_leftpath:
        blur 20.0 
    window auto show


    $LongNVLText(narrator_none, (
    '''\
Your vision begins to blur and your body feels immovable. Your face droops first, before your eyelids follow in suit. Soon you find yourself collapsed on the ground, surrounded by nothing but the night sky. Before you lose consciousness, you see in your periphery, the imposing moon that had taunted you earlier today. 
    '''
    ))

    hide protl protag_breathing with dissolve 
    pause 0.5 

    $LongNVLText(narrator_none, (
    '''\
“All's well that ends well I suppose.”
    '''
    ))
    
    hide bg_leftpath with dissolve
    
    jump path_hospital
   



# Scene 3b
label path_hospital:
    scene black with Fade(.5,0,.5)
    #show bg_hospital with Fade(3,3,3)
    #show bg_hospital with in_eye
    #show drp_casual_talking at right
    #show drpl drp_breathing at right
    #  sad angry


    show bg_hospital with in_eye:
        subpixel True 
        blur 15.0 
        easeout 8.00 blur 0.0 
    with Pause(8.10)
    show bg_hospital:
        blur 0.0 



    $LongNVLText(narrator_none, (
    '''\
Beep…Beep…Beep…
    '''
    ))

    show protl protag_breathing with dissolve:
        subpixel True pos (-0.17, 0.5)

    $LongNVLText(narrator_none, (
    '''\
A soft, rhythmic hum wakes you from your deep sleep. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Through bleary eyes, memories of you collapsing in the desert flood your mind. 
    '''
    ))

    show protl protag_lookup_breathing_shocked with vpunch: 
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
You’re…you’re alive? 
    '''
    ))

    show protl protag_lookup_breathing: 
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
As your focus sharpens, you take in your surroundings. 
    '''
    ))

    show protl protag_lookup_leftright: 
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (     
    '''\
To your right you see a heartbeat monitor. To your left you see a slew of medical machines laid out alongside you. Against the wall you see a big blue screen projecting writing that you don’t recognize. 
    '''
    ))

    show protl protag_scared_stay: 
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Crash landing on Psilicon 5, your perilous journey through the desert. Was that all a dream? Are you home? 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Before you let optimism take over you, you hear a gentle knock on the door. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Not waiting for a response, a figure enters through the doorway.
    '''
    ))

    show protl protag_lookup_breathing: 
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Under normal circumstances, you would be happy to see a doctor sporting a crisp white lab coat and blue scrubs holding onto a clipboard chock full of patient notes…But this isn’t a normal circumstance. 
    '''
    ))
    
    show protl protag_lookup_breathing_shocked: 
        subpixel True pos (-0.17, 0.5) 

    show drpl drp_breathing at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None
    
    
    show drpl drp_breathing:
        subpixel True xpos 0.5 
        parallel:
            ypos 1.0 
            linear 0.01 ypos 1.0 
            linear 1.08 ypos 1.5 
        parallel:
            xzoom 1.0 yzoom 1.0 
            linear 1.08 xzoom 1.5 yzoom 1.5 
    with Pause(1.19)
    show drpl drp_breathing:
        pos (0.5, 1.5) xzoom 1.5 yzoom 1.5 


    show protl protag_lookup_breathing_stay: 
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
The “doctor’s” skin was a sickly green, moss color. Taking up half of his face, in lieu of a typical head of hair and eyes, he had a vibrant red mushroom cap, dotted with yellow spots. 
    '''
    ))


    show drpl drp_breathing:
        subpixel True xpos 0.5 
        parallel:
            ypos 1.5 
            linear 0.98 ypos 1.0 
        parallel:
            xzoom 1.5 yzoom 1.5 
            linear 0.96 xzoom 1.0 yzoom 1.0 
    with Pause(1.08)
    show drpl drp_breathing:
        pos (0.5, 1.0) xzoom 1.0 yzoom 1.0 


    show protl protag_scared_stay:
        subpixel True pos (-0.17, 0.5)  

    $LongNVLText(narrator_none, (
    '''\
You silently curse under your breath as you grip the sheets in front of you. Your knuckles turning white, trying to contain your strange cocktail of emotions–fear, rage, sadness–from bursting out. 
    '''
    ))

    show protl protag_sigh:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Just when you thought you were out…
    '''
    ))

    show protl protag_mad_breathing:
        subpixel True pos (-0.17, 0.5)

    show drpl drp_neutral_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(drpsilicon.c, (
    '''\
“You’re lucky to be alive, that’s for sure, kid,” the doctor said in a gruff, unemotional voice. 
    '''
    ))

    show drpl drp_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    show protl protag_lookup_breathing:
        subpixel True pos (-0.17, 0.5)  

    $LongNVLText(narrator_none, (
    '''\
You turn to respond to the “doctor”. You already feel awkward. You were never taught on how to communicate with a half-man, half-mushroom.  
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
With the ability to make eye contact removed from the situation, you settle for focusing on the more human, bottom half of his face. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Still groggy and dehydrated, your words came out strained. 
    '''
    ))

    show protl protag_lookup_breathing_stay_talking:
        subpixel True pos (-0.17, 0.5)  

    $LongNVLText(narrator, (
    '''\
“Where am I?”
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    show drpl drp_mad:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
The doctor’s mouth tightened into a hard line. He is obviously displeased at your naivety. 
    '''
    ))

    show drpl drp_mad_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(drpsilicon.c, (
    '''\
“Great. A case of convenient amnesia.”
    '''
    ))

    show drpl drp_mad_tranistion_back:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
He taps impatiently with his fingers onto his clipboard as he weighs his options. After a short pause, he sighs in an overly dramatic fashion. 
    '''
    ))

    show drpl drp_scowling_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(drpsilicon.c, (
    '''\
“You are in a hospital on the planet Psilicon 5. Due to your subpar piloting, you destroyed a nature preserve. I surely hope you have that ship insured or else you may find yourself in quite the conundrum.” 
    '''
    ))

    show drpl drp_scowling:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    show protl protag_mad_breathing:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Nature preserve? Insurance? What the hell is he talking about? 
    '''
    ))

    show drpl drp_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
With the conceited notion he gave you a sufficient debriefing on your situation, the alien doctor starts scribbling notes on his notepad. 
    '''
    ))

    show drpl drp_neutral_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    show protl protag_lookup_breathing:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(drpsilicon.c, (
    '''\
“Since you only had a case of mild dehydration, you are free to leave at any time. Don’t worry about payment yet, with your ship crashed–we know you’re not going anywhere.” 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    show drpl drp_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
Placing his empty hand into his pocket, he briskly walks out of your room. 
    '''
    ))
    
    show drpl drp_neutral_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(drpsilicon.c, (
    '''\
“We have an escort assigned to you to get you acclimated to the town. He will be here shortly. Stay put for now.” 
    '''
    ))

    #show drp_casual_talking at exitright with dissolve
#(EFFECT TODO:  Dr. Psilicon fades out, transition either fades him out to the BG or transition him out of frame)

    pause 0.2
    hide drpl drp_breathing with dissolve 
    pause 0.3


    $LongNVLText(narrator_none, (
    '''\
And just as he entered, he was gone. You let your head fall back onto your pillow as you try desperately to make sense of what just happened. 
    '''
    ))

    pause 0.2
    hide protl protag_lookup_breathing with dissolve
    pause 0.3

    $LongNVLText(narrator_none, (
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
    

# (Effect: Fades from black to BG)
# (Effect: Enters Commercial Cris (transition in))
   
    show protl protag_breathing:
        subpixel True pos (-0.2, 0.5) 

    show ccl cc_breathing at center with dissolve: 
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
About an hour passes until you finally meet your escort. At this point, you’ve gotten used to the unexpected, but even this was a bit much. 
    '''
    ))

    window auto hide
    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None
        pos (0.5, 1.0) xzoom 1.0 yzoom 1.0 
        linear 0.80 pos (0.5, 1.6) xzoom 1.75 yzoom 1.75 
    with Pause(0.90)
    show ccl cc_breathing:
        pos (0.5, 1.6) xzoom 1.75 yzoom 1.75 
    window auto show


    $LongNVLText(narrator_none, (
    '''\
Above your escort’s shoulder sits a small, outdated TV, projecting an unimpressed expression on his grayscale face. Dressed to the nines, he wears an expensive and sharply tailored suit.  
    '''
    ))

    window auto hide
    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None 
        parallel:
            xpos 0.5 
            linear 1.01 xpos 0.5 
        parallel:
            ypos 1.6 xzoom 1.75 yzoom 1.75 
            linear 1.02 ypos 1.0 xzoom 1.0 yzoom 1.0  
    with Pause(1.12)
    show ccl cc_breathing:
        pos (0.5, 1.0) xzoom 1.0 yzoom 1.0 
    window auto show

    $LongNVLText(narrator_none, (
    '''\
You brows knit together in confusion…Is this how people dress on Psilicon 5? He can’t possibly have a working retro-style TV for a head, can he? 
    '''
    ))

    show ccl cc_breathing at center: 
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None
    
    $LongNVLText(narrator_none, (
    '''\
Your escort flicks his wrist to look at his silver-plated watch impatiently. 
    '''
    ))

    show ccl cc_bored_talking: 
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
“Let’s get going, tourist. I don’t have all day.” 
    '''
    ))

    show ccl cc_bored: 
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator, (
    '''\
Without thinking, you blurt out what was on your mind. “Are you a cyborg?” 
    '''
    ))

    show ccl cc_squint_frown_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
He looks at you with squinted eyes and a frown. 
    '''
    ))
   
    show ccl cc_look_away_smile_angry_talking_stay:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
“Lucky me. I got the comedian.” 
    '''
    ))

    show ccl cc_look_away_smile_stay:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
To hide your embarrassment, you focus your attention on grabbing your things from the hospital bed. Pissing off your only hope of navigating the city. Great first impression. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
After gathering your meager belongings, mostly made up of the torn up clothes that you wore yesterday, you shuffle in awkward silence towards your escort. 
    '''
    ))

    show ccl cc_bored:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
Clearing his throat, your escort motions toward himself. 
    '''
    ))

    show ccl cc_bored_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
“Now that you’ve displayed your comedic talent, let us start with some introductions. My name is Commercial Cris. As the mayor of this town, I’d like to hearby welcome you to Aisthesis, Psilicon 5’s largest city.” 
    '''
    ))

    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator, (
    '''\
“Nice to meet you.” You hoist your folded-up belongings underneath your armpit and outstretch your free hand for a handshake. When you are met with just a confused stare, you proceed to return your hand to your side. “My name is [player_name] and as you’ve probably heard, my ship crash landed on this planet.” 
    '''
    ))

    show ccl cc_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
“So I’ve heard. Now let’s get started on your tour. I only have a few hours to spare before my next meeting,” 
    '''
    ))

    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
Commercial Cris says as he walks out the door, towards the hospital’s exit. 
    '''
    ))

    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    window auto hide
    show ccl cc_breathing:
        subpixel True ypos 1.0 zpos 0.0 
        xpos 0.5 
        linear 0.01 xpos 0.5 
        linear 1.11 xpos 1.2 
    with Pause(1.22)
    show ccl cc_breathing:
        pos (1.2, 1.0) 
    window auto show



    $LongNVLText(narrator_none, (
    '''\
You take the hint and follow him out of the hospital. 
    '''
    ))

    scene black
    show bg_town with pushright
    show ccl cc_breathing at center:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

# (Effect: Transition from hospital to town BG
# (Effect: Commercial Cris transitions in)
    $LongNVLText(narrator_none, (
    '''\
Upon opening the exit door, you are flooded with a flurry of noises. Jumbled voices speaking in an unfamiliar language, screeching of wheels from kiosks holding a variety of items, clattering of metal from the construction workers fixing the roads. It all felt so familiar yet so different. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Passing through the crowds with ease, Commercial Cris wastes no time to start his guided tour. 
    '''
    ))

    show ccl cc_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
“This town was built after the last war. Mainly functioning as a trading post approximately 100 “earth” years ago. Due to the proximity to an abundant amount of natural resources, Aisthesis thrived.” 
    '''
    ))
    
    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None
    
    $LongNVLText(narrator_none, (
    '''\
Even when a passing kiosk almost runs into him, Commercial Cris continues his tour without missing a step. 
    '''
    ))

    show ccl cc_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
“We have the best hospitals, schools, and transportation in all of Psilicon 5. Not to mention the alcohol!” Lifting his watch again to check the time, he says, “Since you’ve had quite the day, how about we grab ourselves a drink?” 
    '''
    ))

    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None


    window auto hide
    show bg_town:
        subpixel True 
        anchor (0.5, 1.0) xzoom 1.0 yzoom 1.0 
        linear 1.57 anchor (0.6, 0.55) xzoom 1.85 yzoom 1.85 
    show ccl cc_breathing:
        subpixel True ypos 2.0 
    with Pause(1.67)
    show bg_town:
        anchor (0.6, 0.55) xzoom 1.85 yzoom 1.85 
    window auto show


    $LongNVLText(narrator_none, (
    '''\
As much as you try to focus on Commercial Cris’s tour, you find it hard to concentrate when you are in such a densely packed crowd. Even more so when you look up to the tall, perfectly oddly-jagged shaped buildings. You had never seen such architecture before. You wonder how it was possible to build such a feat with such sharp, awkward angles. 
    '''
    ))



    $LongNVLText(narrator_none, (
    '''\
Distraction was dangerous in a city like this. You nearly fall to the ground after a passing alien crashes into your shoulder. 
    '''
    ))

    show bg_town with vpunch
    show bg_town with dissolve:
        subpixel True 
        anchor (0.5, 1.0) xzoom 1.0 yzoom 1.0 

# (Effect - shake screen...)
    $LongNVLText(narrator_none, (
    '''\
Your heart races as you realize that you can’t afford to fall in this crowd. This city wouldn’t wait for you. You would most certainly get run over. 
    '''
    ))
        
# (Effect: Show Commercial Cris in the distance)
    $LongNVLText(narrator_none, (
    '''\
The alien mumbles an apparent irritated apology before scurrying off, leaving you disoriented. 
    '''
    ))

    window auto hide
    show ccl cc_breathing:
        subpixel True zpos 0.0 rotate 0.0
        parallel:
            blend 'normal' matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
            linear 1.42 blend 'normal' matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.25)*BrightnessMatrix(-0.85)*HueMatrix(1.0)
        parallel:
            pos (0.5, 1.25)
            linear 1.44 pos (0.18, 1.2)
        parallel:
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
            linear 1.43 matrixtransform ScaleMatrix(0.19, 0.1956643356643356, 1.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        parallel:
            additive 0.0 blur 0.0
            linear 0.01 additive 0.0 blur 0.0
    with Pause(1.54)
    show ccl cc_breathing:
        blend 'normal' pos (0.18, 1.2) matrixtransform ScaleMatrix(0.19, 0.1956643356643356, 1.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.25)*BrightnessMatrix(-0.85)*HueMatrix(1.0)
    window auto show

    
    $LongNVLText(narrator_none, (
    '''\
In the short scuffle, you almost lose track of Commercial Cris, who has yet to notice—or care—that you aren’t behind him anymore.
    '''
    ))

    $LongNVLText(narrator_none, (
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
    scene bg_town
    show bg_townalley with pushright 
    
    #show terrorlightz_talking at right

    #terrorlightz.c "Following a girl to a dark alley."

    $LongNVLText(narrator_none, (
    '''\
You wait until Commercial Cris’s silhouette disappears into the crowd before you slip into the empty alleyway. Much like the alleys on your home planet, it is mostly filled with discarded trash and a distinct smell of urine. 
    '''
    ))

    show bg_townalley at my_walking with dissolve

# (Effect - screen bouncing up and down slowly, walking...)
    $LongNVLText(narrator_none, (
    '''\
As you pass by the first round of unused trash cans, you notice a few shady looking aliens leaning onto the walls. The phrase “try not to stand out” runs through your mind as you quickly put your hands in your pockets and briskly walk with a fake air of confidence. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
While you could dodge the shady alien’s stares, you couldn’t ignore the increasing sense of dread you feel as the hairs on your neck perk up. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
“It’s fine. I’m fine, just feeling a bit paranoid,” You say to yourself quietly. Just yesterday you were wandering an empty desert. Today, you are trying to dodge suspicious looking aliens. If this is any indicator how your week is going to go, you aren’t sure how long you are going to keep a hold of your sanity. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
After involuntarily holding your breath as your heart thunders against your chest, you finally exit the alleyway. 
    '''
    ))

    show bg_townoutskirts at my_walking with dissolve

# (Effect: Change scene: bg_town alley...)
    $LongNVLText(narrator_none, (
    '''\
Considering the bustling streets you left behind, you could only assume that you are now in the outskirts of the city. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
If you had thought the alleyway was empty, the outskirts are completely barren in comparison. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
The silence is eerie as you make your way through the town. The difference in atmosphere was so starkly different, you almost want to turn and run back to the main strip. The fear of the unknown is man’s greatest fear after all. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
But you resist the feeling and press on. The soft smack of your shoes hitting the synthetic cobblestone makes you hyper aware of your surroundings.
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Passing through empty fluorescent lit buildings, you wonder why there isn’t anyone else around. Is it a dangerous area? That doesn’t seem right. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Is it deserted? More likely, but why would they waste resources on keeping the buildings lit? 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You are so focused on making sense of your situation that you almost miss a trail of pink fabric peeking out from the corner of the next building. 
    '''
    ))

    scene black
    show bg_townalley 


# (Effect: Stop walking animation, look towards right side...)
    $LongNVLText(narrator_none, (
    '''\
You slow your pace and lean towards the corner. While the other side of the building is dark, you are able to trace the pink fabric to a silhouette of a person wearing a large dress.
    '''
    ))

    $LongNVLText(narrator_none, (
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


    $LongNVLText(narrator_none, (
    '''\
You hesitantly approach the alien on the other side of the dark corner. 
    '''
    ))

    show bg_townalley with dissolve

    $LongNVLText(narrator_none, (
    '''\
You knit your eyebrows together as you take in the strange…beautiful alien? 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Enveloped in a billowing, pastel pink-colored tulle dress, there stands a fragile-looking, turquoise-skinned alien. A soft trail of pink smoke, matching the color of dress, emanates off of her.  
    '''
    ))

    $LongNVLText(narrator_none, (
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
    $LongNVLText(narrator_none, (
    '''\
You let out a sigh of relief. Finally, a lucky break. You feel calmer already. 
    '''
    ))

    $LongNVLText(narrator, (
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
    $LongNVLText(narrator, (
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
    $LongNVLText(narrator, (
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
    $LongNVLText(narrator_none, (
    '''\
Where are you going? Do they have an immigration center here for unfortunate, lost off-world captains? 
    '''
    ))

    $LongNVLText(narrator, (
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

#(Effect - mysterious space woman bounces up and down for a few seconds.)
    show mswl myst_s_woman_breathing 
    $LongNVLText(narrator_none, (
    '''\
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
    $LongNVLText(narrator_none, (
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
    show mswl myst_s_woman_breathing

# (Effect: WALKING ANIMATION)
    $LongNVLText(narrator_none, (
    '''\
After 30 minutes of seemingly aimless turns through endless rows of alleyways, you start to feel anxious. Every turn you take is the same as the last last. Dark and decrepit. While your guide is ever-confident, never once double-backed or hesitating, you still can’t comprehend that this endless maze of alleys would lead anywhere.    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Is she lost? You hope not. She’s your only hope to get off of this god-forsaken planet. 
    '''
    ))

    $LongNVLText(narrator, (
    '''\
You clear your throat as you make another sharp turn. Finally, she lets go of your hand. Unsurprisingly, it looks just as uninviting as the last. “Um, are you sure we are going in the right direction?” 
    '''
    ))

    scene black
    show bg_townalley 
    show mswl myst_s_woman_giggle

    $LongNVLText(mysteryspacewoman.c, (
    '''\
You hear her giggle softly next to you. “Yes, of course, sweetie. You have to trust me.”
    '''
    ))

    show mswl myst_s_woman_breathing
    $LongNVLText(narrator_none, (
    '''\
Trust her? How could you when you only met her an hour ago? Even worse, it is dark out. You lost the little amount of light you had left. Without daylight, you are completely and utterly helpless. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
It doesn’t seem like your guide is as knowledgeable as you once hoped so you start your own investigation. Though it’s hard to make out in the dark, you feel your way around using the cracked brick-lined walls as your guide. It only takes a minute or two of feeling around, but you start to grow more anxious when you collide with the wall on the other side of the alley. Your assumptions are correct–this alley is a dead end.  
    '''
    ))

#point and click

    $LongNVLText(narrator_none, (
    '''\
You gulp and the hairs on the back of your neck perk up. This would be the perfect opportunity for someone to rob you. You shake your head and dismiss the thought. There is no way she is a criminal! 
    '''
    ))

    window auto hide
    show bg_townalley:
        subpixel True xzoom 1.0 zoom 1.25 
        parallel:
            xpos 0.5 zpos 0.0 
            linear 0.01 xpos 0.5 zpos 1.0 
        parallel:
            ypos 1.0 
            linear 0.01 ypos 1.0 
            linear 0.12 ypos 1.15 
            linear 0.11 ypos 1.0 
            linear 0.14 ypos 1.15 
    with Pause(0.48)
    show bg_townalley:
        pos (0.5, 1.15) zpos 1.0 
    window auto show

# EFFECT: BOUNCE 
    show mswl myst_s_woman_scary_transition
    $LongNVLText(narrator_none, (
    '''\
As your mind was racing with how to handle this situation, you turn too quickly to the left and trip over an overturned trash can. The metallic lid screeches as it rolls through the alley.
    '''
    ))

    show mswl myst_s_woman_scary
    $LongNVLText(narrator_none, (
    '''\
A soft voice cuts through the darkness. 
'''
    ))
    
    show mswl myst_s_woman_scary_happy_talking
    $LongNVLText(mysteryspacewoman.c, (
    '''\
“Don’t worry, sweetie. Let me help you up.” 
    '''
    ))

# (Effect: PAN UP FROM BOTTOM OF ALIEN TO TOP) 
    show mswl myst_s_woman_scary_happy
    #option to make her darker: subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.5)*HueMatrix(1.0) 
    
    $LongNVLText(narrator_none, (
    '''\
You look up and notice the pretty alien hovering over you. Your eyes widen. When did she get so close to you? You didn’t hear her following you.
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You reach up to take her outstretched arm, but pull away before you make contact. Something is very, very wrong. 
    '''
    ))

    show mswl myst_s_woman_scary:
        subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.5)*HueMatrix(1.0) 
        subpixel True 
        xzoom 2.0 yzoom 2.0 
        parallel:
            xpos 0.5 zoom 1.0 
            linear 3.05 xpos 0.5 zoom 1.75 
        parallel:
            ypos 1.0 
            linear 0.01 ypos 1.0 
            linear 3.05 ypos 2.75 
    with Pause(3.16)
    show mswl myst_s_woman_scary:
        pos (0.5, 2.75) zoom 1.75 
    
  
  #(Effect: PAN IN CLOSER TO ALIEN’s FACE)
    $LongNVLText(narrator_none, (
    '''\
Upon closer inspection of her face, you notice that her eyes, once delicate and gentle, are now cold and expressionless. Her mouth, wider than before, displays pointed, jagged teeth.
    '''
    ))

    show mswl myst_s_woman_scary
    $LongNVLText(narrator_none, (
    '''\
The pink, elegant clothes she once wore melted away, revealing a horrifying wolf-like alien. Her voice, in a deeper pitch, mocks you. 
    '''
    ))

    show mswl myst_s_woman_scary_happy_talking
    $LongNVLText(mysteryspacewoman.c, (
   '''\
“What’s wrong, lost lamb?”
    '''
    ))

    show mswl myst_s_woman_scary_happy
    $LongNVLText(narrator_none, (
    '''\
You scream for the last time as the terrifying alien licks its lips and dives into you. 
    '''
    ))


    jump game_over


# Scene 3c5
label path_tavern:
    
    show ccl cc_breathing:
        blend 'normal' pos (0.18, 1.2) matrixtransform ScaleMatrix(0.19, 0.1956643356643356, 1.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.25)*BrightnessMatrix(-0.85)*HueMatrix(1.0)

    $LongNVLText(narrator_none, (
    '''\
You decide to stick with your guide. You are far away from home afterall. Where would you go? 
    '''
    ))

    show bg_town at slow_walking

    show ccl cc_breathing:
        subpixel True 
        pos (0.18, 1.2) zoom 1.0 
        linear 2.32 pos (0.36, 1.55) zoom 1.9
    with Pause(2.42)
    show ccl cc_breathing:
        pos (0.36, 1.55) zoom 1.9 

    show ccl cc_breathing with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None


    $LongNVLText(narrator_none, (
    '''\
The sidewalk is positively packed with people, making it difficult to catch up, but after some polite pushing, you are able to close the distance. 
    '''
    ))

   
    $LongNVLText(narrator_none, (
    '''\
Attempting to hide your exhaustion from your escort, you slow your breaths to a normal pace. 
    '''
    )) 

      

    $LongNVLText(narrator_none, (
    '''\
Your body is still recovering from your hospital trip. Heat stroke, dehydration, and a crash landing will do that to a person.
    '''
    )) 

    $LongNVLText(narrator_none, (
    '''\
But with the way your escort hadn’t even spared you a glance since you left the hospital, he didn’t seem to care. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Typical. 
    '''
    ))
  
    scene black
    show bg_tavern with dissolve

    show protl protag_lookup_breathing:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
You felt a little lighter when the tavern came into view. Jovial mummers flood your ears as you approach the threshold. 
    '''
    ))

    show protl protag_lookup_leftright:
        subpixel True pos (-0.17, 0.5) 

    show bg_tavern:
        subpixel True 
        parallel:
            xpos 0.5 
            linear 1.33 xpos 0.6 
            linear 0.15 xpos 0.6 
            linear 1.34 xpos 0.4 
        parallel:
            ypos 1.0 
            linear 2.82 ypos 1.0 
        parallel:
            zoom 1.0 
            linear 0.01 zoom 1.0 
            linear 1.32 zoom 1.5 
    with Pause(2.92)
    show bg_tavern:
        pos (0.4, 1.0) zoom 1.5 


    $LongNVLText(narrator_none, (
    '''\
Without a door to separate the outside from the inside, it is easy to spot the alien patrons sitting at the bar enjoying their drinks. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    show bg_tavern:
        subpixel True 
        xpos 0.4 zoom 1.5 
        linear 1.43 xpos 0.5 zoom 1.0 
    with Pause(1.53)
    show bg_tavern:
        xpos 0.5 zoom 1.0 

    show ccl cc_bored at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
Holding onto the metal trim lining the doorway, Commercial Cris finally turns around to face you. 
    '''
    ))

    show ccl cc_bored_talking at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
The tv screen displays a clearly disingenuous, engineered grin on his face. With a flourish, he motions inside. “After you, tourist.” 
    '''
    ))
    
    hide ccl cc_bored with dissolve

    $LongNVLText(narrator_none, (
    '''\
Eager to get away from the crowds, you walk into the tavern. You guess this is a good time as any to survey your surroundings. 
    '''
    ))


    jump path_tavern_nav


# Scene 3c5a
label path_tavern_nav:
    hide protl
    scene bg_tavern with dissolve

    $LongNVLText(narrator_none, (
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

    $LongNVLText(narrator_none, (
    '''\
Sitting idly outside sits a trash bin. You find some comfort in seeing that even on an alien planet, they have the same strategy to dispose of trash. 
    '''
    ))
    jump path_tavern_nav

label path_tavern_heater:
    $ seen_labels.add("tavern_heater")

    $LongNVLText(narrator_none, (
    '''\
Centrally placed in the tavern is a giant heater. Ornately decorated in carvings and hanging trinkets, it looms over the tavern’s patrons. You wonder how something that large emitting so much heat hadn’t burned the place down. Maybe it had? 
    '''
    ))
    jump path_tavern_nav
    
label path_tavern_patron:
    $ seen_labels.add("tavern_patron")

    $LongNVLText(narrator_none, (
    '''\
You notice the aliens sitting at the bar. Though you don’t understand their language, the crashing of their pint glasses and laughter made it apparent they are having a good time. 
    '''
    ))
    jump path_tavern_nav

label path_tavern_sign:
    $ seen_labels.add("tavern_sign")

    $LongNVLText(narrator_none, (
    '''\
Outside of the tavern hangs a single sign in an unfamiliar language. This must mark the name of the establishment. 
    '''
    ))

    jump path_tavern_nav



# Scene 3c6
label path_tavern_drink:
    scene black
    show bg_tavernbartender with dissolve
    
    show protl protag_lookup_breathing:
        subpixel True pos (-0.17, 0.5) 

    show ccl cc_breathing at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
You believe you have gotten a sufficient lay of the land. With a bit less hesitation you move deeper inside of the tavern, Commercial Cris following closely behind.
    '''
    ))

    show ccl cc_breathing:
        parallel:
            subpixel True 
            ypos 1.0 
            linear 0.65 ypos 0.9 
            linear 0.38 ypos 1.0 
        parallel:
            additive 0.0 
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            blend None

    $LongNVLText(narrator_none, (
    '''\
Past the larger heater, you spy an empty table. You scoot the chair out and take a seat. You watch as Commercial Cris takes the seat directly across from you, his smile unwavering. 
    '''
    )) 
    
    show ccl cc_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
“So, tourist. What’s your poison?” Commercial Cris asks, raising a hand to hail a passing waiter.
    '''
    ))

    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
You raise your eyebrow. You highly doubt that you could find a drink here that would resemble anything that you are familiar with so you just shrug. 
    '''
    ))

    show protl protag_lookup_breathing_stay_talking:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator, (
    '''\
“I’ll have what you're having.” 
    '''
    ))

    show protl protag_mad_breathing:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Eyeing your escort, you grit your teeth, quickly regretting your decision. Anything a tv-human hybrid could drink, probably isn’t good for you. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    show ccl cc_amused_smug_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
Assuming your thoughts, Commercial Cris chuckled. “Right.” 
    '''
    ))

    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
A green, scaly-faced alien approaches the table with a tablet device in hand. 
    '''
    ))



    $LongNVLText(belvania, (
    '''\
With a voice sounding like it was trapped underwater, she asks, eyeing Commercial Cris, “To what do we owe your presence, your majesty?” 
    '''
    ))

    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
Commercial Cris leans back onto his chair, hands laying lightly on his stomach. 
    '''
    ))

    show ccl cc_amused_smug_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None


    $LongNVLText(commercialcris.c, (
    '''\
“Oh Belvania, you are a riot.” Tipping his large, rectangular head towards me, he says, “We have a special guest today."
    '''
    ))

    $LongNVLText(commercialcris.c, (
    '''\
"You know that spaceship that crashed on Plovita’s nature preserve? Well after the accident yesterday, I thought [player_name] could use a drink.” 
    '''
    ))

    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None


    $LongNVLText(narrator_none, (
    '''\
The waiter’s beady, yellow eyes opened in surprise and looked towards you. After looking you up and down, she was obviously unimpressed. 
    '''
    ))

    $LongNVLText(belvania, (
    '''\
“Aye, pilot, did you get your license yesterday? You left quite the mess. It was all over the news.” 
    '''
    ))

    show protl protag_scared:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Your nostrils flare and you clench your fist underneath the table. What an ignorant thing to say?! You hardly had much of a choice where you could land after the impact. 
    '''
    ))

    show protl protag_scared_stay :
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Sensing the rising tension, Commercial Cris clears his throat to take back the attention from the waitress. 
    '''
    ))

    show ccl cc_talking:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
“My friend will take a glass of Jfetau. Nothing for me as usual.” 
    '''
    ))

    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
With a few practiced motions, the waitress places the order on the tablet and leaves the table. 
    '''
    ))

    show protl protag_sigh:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
You didn’t realize that you had been holding your breath until you unclench your fist and take a deep breath. 
    '''
    ))

    show protl protag_mad_breathing:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
So what if this planet doesn’t know the truth? If you play your cards right, you’ll be on the next ship and then none of this will matter. 
    '''
    ))

    show protl protag_lookup_breathing:
        subpixel True pos (-0.17, 0.5) 

    show ccl cc_bored:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
You turn your focus back on Commercial Cris, who is looking around the tavern with a bored expression. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
You decide to be blunt and to the point. After that display of rudeness, you think it’s only fair to be candid. 
    '''
    ))
    
    show protl protag_lookup_breathing_stay_talking:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator, (
    '''\
“Do you have an inter-galaxy space station here?” 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    show ccl cc_look_away_smile_angry_talking_stay:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
With a raised eyebrow and sour expression, Commercial Cris responds, “Yes of course. We aren’t primitives.” 
    '''
    ))

    show ccl cc_breathing:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
You feel your heart beat faster. Finally, some progress! 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Time to play the good samaritan here. This is your way out! 
    '''
    ))

    show protl protag_breathing with vpunch:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
You smile and open your mouth to respond, but before you can get any words out you hear glass breaking, loud cursing, and a scuffle. 
    '''
    ))


    scene black
    show bg_insidetavern with dissolve

    show protl protag_lookup_breathing:
        subpixel True pos (-0.17, 0.5) 
    
    show ccl cc_breathing at center:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None
   
    $LongNVLText(narrator_none, (
    '''\
You turn your head towards the loud noise. Across the tavern, you see three crouching silhouettes tumbling across the floor. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
You turn your head towards the loud noise. Across the tavern, you see three crouching silhouettes tumbling across the floor. 
    '''
    ))

    show ccl cc_amused_smug_breathing:
            subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
Nervously, you look towards your guide who seems utterly amused by this new development. 
    '''
    ))

    show ccl cc_amused_smug_breathing:
            subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
With one hand on the table balancing the tv screen, he motions with his free hand towards the noise. 
    '''
    )) 

    show ccl cc_amused_smug_talking:
            subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
“Lucky you, tourist. You get a show with your drink. We can call it an introduction to the culture of Aisthesis.”
    '''
    ))

    show ccl cc_amused_smug_breathing:
            subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
You take that as permission to break away from your awkward conversation and examine the scene. You scoot your chair back and approach the growing crowd encircling the fight.
    '''
    ))

# (Scene: CHANGE BG TO bg_tavernbartender)
    scene black
    show bg_tavernbartender with dissolve

    $LongNVLText(narrator_none, (
    '''\
Throughout your short tour of the city you’ve noticed that most of the creatures on Psilicon 5 are taller than you. 
    '''
    ))

    show protl protag_lookup_breathing_stay onlayer character:
        subpixel True 
        ypos 0.5 
        linear 0.82 ypos 0.4 
        linear 0.18 ypos 0.4 
        linear 0.54 ypos 0.5 
    with Pause(1.64)
    show protl protag_lookup_breathing_stay onlayer character:
        ypos 0.5 

    $LongNVLText(narrator_none, (
    '''\
You try to stand on an empty chair to get a better view, but soon learn that it is ineffective. Instead, you squirm your way through the crowd until you finally get a better look. 
    '''
    ))

#    (Scene: CHANGE BG TO bg_tavernfight)
    scene black
    show bg_tavernfight with dissolve

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
In between the excited screeches of the crowd you hear what you could only assume are curses by the two fighting creatures.
    '''
    ))

    # Still testing this part
    show growl:
        zoom 1.5
        xalign 0.3
        yalign 0.7
    pause 1.0
    hide growl

    pause 1.0
    show roar:
        zoom 1.5
        xalign 0.5
        yalign 0.2
    pause 1.0
    hide roar

    pause 1.0
    show smash:
        zoom 1.5
        xalign 0.7
        yalign 0.5
    pause 1.0
    hide smash
    pause 1.0
    


    window auto hide
    show bg_tavernfight:
        subpixel True 
        parallel:
            xpos 0.5 
            linear 1.28 xpos 0.7 
            linear 0.13 xpos 0.7 
            linear 1.09 xpos 0.3 
            linear 0.14 xpos 0.3 
            linear 0.89 xpos 0.5 
        parallel:
            zoom 1.0 
            linear 1.28 zoom 1.5 
            linear 1.22 zoom 1.5 
            linear 1.02 zoom 1.0 
    with Pause(3.63)
    show bg_tavernfight:
        xpos 0.5 zoom 1.0 
    window auto show

    $LongNVLText(narrator_none, (
    '''\
You have never seen anything like it before. A single “rat-like” alien sits, clutching onto the table, bracing for a fight. A larger, more imposing alien stands in front of the small alien snarling. Their onlooking table mates, a human and a green, bald-headed alien try without success to break up the fight.
    '''
    ))

    scene black
    show bg_tavernfight with vpunch

    $LongNVLText(narrator_none, (
    '''\
Before anyone could process the scene before them, glasses full of alcohol are thrown back and forth into the crowd. 
    '''
    ))

    scene black
    show bg_tavernfight with vpunch

    $LongNVLText(narrator_none, (
    '''\
Broken bottles are scattered across the already dirty, uneven wood floor, making the situation more precarious than before. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
The crowd, disinterested or desensitized to the danger, continues to cheer on the fight.
    '''
    ))

    show protl protag_scared_stay:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
You question whether you should stay to watch the scuffle ensue. 
    '''
    )) 
    
    scene black
    show bg_tavernfight with vpunch

    show protl protag_lookup_breathing_shocked:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Before you can make a conscious decision, the human is thrown by the lion-headed alien into the crowd, right in front of your feet. 
    '''
    ))

    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
In the heat of the moment, the human claws at your pant legs, trying to get up. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Right. Time to go. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Afraid that you are going to become an unwilling participant in this situation, you scurry back to your table. 
    '''
    ))

#    (Scene: CHANGE BG TO bg_insidetavern)
    scene black
    show bg_insidetavern with dissolve

    show protl protag_sigh:
        subpixel True pos (-0.17, 0.5) 

    show ccl cc_breathing at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
After sitting back into your seat–which you find far more comfortable than before–you notice there is a pint of mysterious liquid in front of you. 
    '''
    ))
    
    show protl protag_mad_breathing:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
The waitress must have dropped off while you were away. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
You could really use a drink now. To hell with the consequences. With shaky hands, you take a sip. 
    '''
    ))
    
    show protl protag_lookup_breathing:
        subpixel True pos (-0.17, 0.5) 

    show ccl cc_amused_smug_breathing at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None


    $LongNVLText(narrator_none, (
    '''\
Commercial Cris, all the more amused with your discomfort, smirks at you. 
    '''
    ))
    
    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    show ccl cc_amused_smug_talking at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None
    $LongNVLText(commercialcris.c, (
    '''\
“The roof is still intact so I would say you’ve just witnessed a pretty harmless fight.”
    '''
    ))

    show protl protag_mad_breathing:
        subpixel True pos (-0.17, 0.5) 

    show ccl cc_breathing at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None
   
    $LongNVLText(narrator_none, (
    '''\
Harmless fight he calls it. You nearly got hit in the face by an airborne glass bottle and run over by an over-excited crowd. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
On your home planet you may have witnessed a fight or two, but those mainly consisted of verbal-screaming matches. Physical fights were considered neanderthal tactics. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
So yeah, this is hardly “harmless” to you. 
    '''
    ))

    show protl protag_lookup_breathing:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Ignoring the onslaught of Commercial Cris’s snide comments, you dose your discomfort in your drink. It tastes putrid, slimy, bitter, but blissfully alcoholic. 
    '''
    ))
  
    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
After a few large gulps, you start to feel more relaxed. 
    '''
    ))
  
    show ccl cc_bored at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(narrator_none, (
    '''\
Getting the hint that you aren’t going to react to his comments anymore, Commercial Cris frowns at you, glancing down at his watch impatiently. 
    '''
    ))

    show ccl cc_bored_talking at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    $LongNVLText(commercialcris.c, (
    '''\
“Alright then, we are playing the quiet game. That’s alright. You have five minutes to finish your drink. I have more to show you and not enough time to do it.” 
    '''
    ))

    show ccl cc_bored at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None

    show protl protag_mad_breathing:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Challenge accepted. With an air of feigned confidence, you chug the rest of your drink. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Aisthesis here you come.
    '''
    ))

    jump path_town_walk


# Scene 3c7
label path_town_walk:
    
    show ccl cc_breathing at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None


    show protl protag_lookup_breathing_stay:
        subpixel True pos (-0.17, 0.5) 

    $LongNVLText(narrator_none, (
    '''\
Silently, Commercial Cris eyes you, tapping his watch with finality. With only a few sips left, you take the last gulp of your drink. 
    '''
    ))


    $LongNVLText(narrator_none, (
    '''\
If your tavern experience told you anything, it is that this place is full of surprises. 
    '''
    ))


    $LongNVLText(narrator_none, (
    '''\
Now though, you are a tad tipsy—which makes this misadventure immeasurably less terrifying and much more exciting. 
    '''
    ))
    
    show protl protag_lookup_breathing_stay onlayer character:
        subpixel True 
        ypos 0.5 
        linear 1.11 ypos 0.4 
        linear 0.32 ypos 0.4 
        linear 0.49 ypos 0.5

    $LongNVLText(narrator_none, (
    '''\
With far less grace than before, you clumsily scoot your chair out and stand up, Commercial Cris already waiting at the door. 
    '''
    ))

    show protl protag_lookup_breathing_stay onlayer character:
        subpixel True 
        xpos -0.17
        linear 0.20 xpos -0.17
        linear 0.57 xpos -0.19 
        linear 0.54 xpos -0.19
        linear 0.57 xpos -0.15
        linear 0.42 xpos -0.15 
        linear 0.42 xpos -0.17

    $LongNVLText(narrator_none, (
    '''\
Your head spins faintly as you walk out of the tavern—almost in a straight line.
    '''
    ))

    scene black
    show bg_town with dissolve

    $LongNVLText(narrator_none, (
    '''\
Commercial Cris’s tour is about as good as his company at the tavern, short, brief, and a tad impatient. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
The biggest thing that stood out to you about the town is the architecture. 
    '''
    ))

    show bg_town:
        subpixel True 
        parallel:
            xpos 0.5 
            linear 1.31 xpos 0.5 
            linear 0.17 xpos 0.5 
            linear 0.80 xpos 0.6 
        parallel:
            ypos 1.0 
            linear 1.31 ypos 1.3 
            linear 0.17 ypos 1.3 
        parallel:
            zoom 1.0 
            linear 1.31 zoom 1.3 
    with Pause(2.38)
    show bg_town:
        pos (0.6, 1.3) zoom 1.3 


    $LongNVLText(narrator_none, (
    '''\
The buildings were tall, but with jagged, pointy roofs. To match the structure, the windows are retrofitted in broken, kaleidoscope patterns. 
    '''
    ))

    $LongNVLText(narrator_none, (
    '''\
Did windows serve a different purpose here? You couldn’t imagine that it is possible to see a clear image outside of them. Weird..but kind of cool at the same time. 
    '''
    ))

# (EDIT for Alyssa Made change to BG_TOWN and BG_TAVERNFIGHT (highlighted in yellow))

    show bg_town:
        subpixel True 
        parallel:
            pos (0.6, 1.3) 
            linear 1.23 pos (0.5, 1.0) 
        parallel:
            zoom 1.3 
            linear 1.24 zoom 1.0 
    with Pause(1.34)
    show bg_town:
        pos (0.5, 1.0) zoom 1.0 

    $LongNVLText(narrator_none, (
    '''\
After only about 20 minutes, your “tour” of the town ended. He drops you off at exactly where you started, at the hospital. 
    '''
    ))

    show ccl cc_amused_smug_breathing at center with dissolve:
        subpixel True additive 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.5)*SaturationMatrix(1.75)*BrightnessMatrix(0.0)*HueMatrix(0.0) blend None


    $LongNVLText(narrator_none, (
    '''\
With a noncommittal grin and short wave he mentions he is late to a meeting and quickly scampers away. 
    '''
    ))

    hide ccl cc_amused_smug_breathing with dissolve


    show protl protag_lookup_breathing_stay onlayer character:
        subpixel True 
        xpos -0.17
        linear 0.20 xpos -0.17
        linear 0.57 xpos -0.19 
        linear 0.54 xpos -0.19
        linear 0.57 xpos -0.15
        linear 0.42 xpos -0.15 
        linear 0.42 xpos -0.17

    $LongNVLText(narrator_none, (
    '''\
Being much drunker than you were this morning, you find his desertion less infuriating. 
    '''
    ))


    $LongNVLText(narrator_none, (
    '''\
Your only regret is that you didn’t get the chance to ask about the intergalactic space station. Maybe you could ask one of the nurses?  
    '''
    ))

    scene black 
    show bg_hospital with dissolve

    $LongNVLText(narrator_none, (
    '''\
With a sigh and zero options, you open the door and enter the hospital. Leaning back into your hospital bed you feel like you haven’t accomplished much today.  
    '''
    ))

# GAME OVER–Neutral Ending

    jump game_over



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
