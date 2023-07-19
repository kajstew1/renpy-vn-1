# The script of the game goes in this file.





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
label start:
    
    # Display a message and show an alert box when a button is clicked
    # jump splashscreen2
    
    #show bg_crashsite with dissolve
    scene bg_crashsite with dissolve

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
    jump crash_fork


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
You had a feeling that there was a right or wrong answer to your choice from here. You had better choose the right one or fear the repercussions
    '''
    ))

    menu: 
        "Choose a path."
        "Left...":
            # if (persistent.path_to_outskirts_taken == False or persistent.path_to_tavern_taken == False):
            #show screen evt_choose_path
            #call screen evt_choose_route with dissolve
            $ persistent.path_to_town_taken = True
            jump path_town_fork
        "Right...":
            #if persistent.path_to_hut_taken == False:
            #show screen evt_choose_path 
            #call screen evt_choose_route with dissolve
            $ persistent.path_to_hut_taken = True
            jump path_hut
        "No thank you!": 
            return
    
    
    return

label path_hut:
    #show bg_tavern with dissolve
    hide screen evt_choose_path
    scene bg_hut with dissolve

    show terrorlightz_talking at left
    
    terrorlightz.c "Come inside to meet me."

    jump hut_meet_terrorlightz
    

label hut_meet_terrorlightz:
    scene bg_insidehut with dissolve

    show terrorlightz_talking at right
    
    terrorlightz.c "Some text meeting terrorlightz."

    jump hut_forage

label hut_forage:
    scene bg_hut with dissolve

    show terrorlightz_talking at right

    terrorlightz.c "Some text foraging."

    jump hut_remember

label hut_remember:
    scene bg_hut with dissolve

    show terrorlightz_talking at right

    terrorlightz.c "Some text remembering eating mushrooms on a way spaceship."

    jump game_over


label path_town_fork:
    scene bg_town with dissolve
    
    # terrorlightz.c "Which way do you want to go?"
    #show screen evt_choose_path
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
       
    


label path_town_outskirts:
    #show bg_tavern with dissolve
    #call screen bg_hut
    hide screen evt_choose_path
    scene bg_townoutskirts with dissolve
    
    show mysteryspacewoman_talking at left

    mysteryspacewoman.c "Hi. Could I get directions?"
    
    jump town_alley


label town_alley:
    scene bg_townalley with dissolve

    show terrorlightz_talking at right

    terrorlightz.c "Following a girl to a dark alley."

    jump game_over




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
