# The script of the game goes in this file.

init:
    transform my_shake:
        easein 0.2 xoffset 0 yoffset 30
        easeout 0.2 xoffset 0 yoffset -30
        #linear 0.1 xoffset 0 yoffset 10
        #linear 0.1 xoffset 0 yoffset -15
        #linear 0.1 xoffset 0 yoffset 0
        repeat

# The game starts here.
label splashscreen:
    scene black 
    with Pause(1)
    show mytext "Dr. Psilicon Presents......" with dissolve
    with Pause(2)

    hide mytext with dissolve
    with Pause(1)

    # show mytext "The Back Story" with dissolve
    # with Pause(2)

    # hide mytext with dissolve
    # with Pause(1)

    return
    
label splashscreen2:
    scene black
    with Pause(1)
    show mytext "You find yourself waking up on a crash ship."
    with Pause(2)
  
    hide mytext with dissolve
    with Pause(1)

    # show mytext "So Start your journey now!"
    # with Pause(2)

    # hide mytext with dissolve
    # with Pause(1)

    jump xxxxx

# start of the game
# Scene 1
label start:
    
    # Display a message and show an alert box when a button is clicked
    # jump splashscreen2
    
    #show bg_crashsite with dissolve
    scene bg_crashsite with dissolve
    play music "sounds/effects/crash_beeps_alarms.mp3"

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
    scene bg_fork with dissolve
    
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

    menu: 
        "Choose a path."
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
            return
    
    
    return



# Scene 2a
label path_right_path:
    #show bg_tavern with dissolve
    hide screen evt_choose_path
    scene bg_fork with dissolve:
        #xpos 1.25 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0
        subpixel True
        size (1920, 1080) crop (0, 0, 860, 600) #first tuple is the size of game screen, second is size of picture in pixels
        easein 4.0 crop (860, 600, 860, 600) # first float is time in seconds, tuples are coordinates of the upper left corner of a rectangle, and the second tuple is the size of that rectangle
        easeout 8.0 crop (615, 0, 860, 600) #here we change the y coordinate over 8 seconds to pan the image up


    $LongNVLText(narrator, (
    '''\
(Effect - zoom to the right (In Work))
You stood transfixed at the shadowed silhouette of the strange moon behind the cover of the sharp mountain peaks. You feel it calling to you, moving your feet faster than your mind could keep up. 
    '''
    ))

    show bg_fork with dissolve:
        

    $LongNVLText(narrator, (
    '''\
Without much of a voluntary choice, you make your way down the sandy, gravel path. 
    '''
    ))
    jump path_right_path_1


# Scene 2b
label path_right_path_1:
    #show bg_tavern with dissolve

    scene bg_rightpath with dissolve


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

    scene bg_rightpath at my_shake

    $LongNVLText(narrator, (
    '''\
(Effect - running, shake up and down (In Work)
You clutch onto your wounded stomach with a small prayer that your thrown together plan wouldn’t reopen the cut and begin your mad dash to the ominous tunnel. 
    '''
    ))

    scene bg_rightpath with dissolve

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
    scene bg_insidecave with dissolve

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
    scene bg_lightinsidecave with dissolve

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
    scene bg_hut with dissolve

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
    scene bg_insidehut with dissolve

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

    show terrorlightz_talking at right
    
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


    jump path_hut_forage 


# Scene 2g
label path_hut_forage:
    scene bg_hut with dissolve

    show terrorlightz_talking at right

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

    jump hut_remember


# Scene 2h
label hut_remember:
    scene bg_hut with dissolve

    show terrorlightz_talking at right

    terrorlightz.c "Some text remembering eating mushrooms on a way spaceship."

    jump game_over



# Scene 3
label path_left_path_decision:
    #show bg_tavern with dissolve
    hide screen evt_choose_path
    scene bg_fork with dissolve

    $LongNVLText(narrator, (
    '''\
(Effect - zoom in on left path (In Work))
Your eyes land on the seemingly safer option. The two suns and neighboring planets were hung in the sky like ornaments on a Christmas tree, brightly lighting the path in front of you.  
    '''
    ))

    $LongNVLText(narrator, (
    '''\
(Effect - zoom in on right path (In Work))
The right path scared you. It called to you like a siren in turbulent waters, inviting you in with a sweet song. You try to stand your ground in fear of being pulled into the imposing moon’s imaginary gravitational pull. 
    '''
    ))

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



# Scene 3a1
label path_left_path:
    scene bg_leftpath with dissolve
    
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
 “All well that ends well I suppose.”
    '''
    ))
    jump path_town_fork


# Scene 3b1
label path_town_fork:
    scene bg_leftpath with dissolve
    
    menu: 
        "Choose a path."
        "Town...": 
            #if persistent.path_to_outskirts_taken == False:
            #show screen evt_cthoose_path
            #call screen evt_choose_route with dissolve
            $ persistent.path_to_outskirts_taken = True
            jump path_town_outskirts
        "Tavern...":
            #if persistent.path_to_tavern_taken == False:
            #show screen evt_choose_path 
            #call screen evt_choose_route with dissolve
            $ persistent.path_to_tavern_taken = True
            jump path_tavern
       
    

# Scene 3b1
label path_town_outskirts:
    #show bg_tavern with dissolve
    #call screen bg_hut
    hide screen evt_choose_path
    scene bg_townoutskirts with dissolve
    
    show mysteryspacewoman_talking at left

    mysteryspacewoman.c "Hi. Could I get directions?"
    
    jump town_alley


# Scene 3c1
label town_alley:
    scene bg_townalley with dissolve

    show terrorlightz_talking at right

    terrorlightz.c "Following a girl to a dark alley."

    jump game_over



# Scene 3a2
label path_tavern:
    #show bg_tavern with dissolve
    hide screen evt_choose_path

    call screen tavern_nav
    mysteryspacewoman.c "Hi. Could I get directions?"
    jump path_tavern_drink



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


label path_tavern_bin:
    $ seen_labels.add("tavern_bin")
    "Tavern bin reporting"
    jump path_town_fork

label path_tavern_heater:
    $ seen_labels.add("tavern_heater")
    "Tavern heater reporting"
    jump path_town_fork
    
label path_tavern_patron:
    $ seen_labels.add("tavern_patron")
    "Tavern patron reporting"
    jump path_town_fork

label path_tavern_sign:
    $ seen_labels.add("tavern_sign")
    "Tavern sign reporting"
    jump path_town_fork

label path_tavern_drink:
    jump path_town_fork

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
