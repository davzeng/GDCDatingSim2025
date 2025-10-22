image bg_plane:
    "bg_plane.png"
    xysize(1920, 1080)
image bg_sky:
    "bg_sky.png"
    xysize(1920, 1080)
image bg_ground:
    "bg_ground.png"
    xysize(1920, 1080)

transform scale(ratio):
    zoom ratio

transform weirdsydneyscale(ratio):
    zoom ratio
    anchor (0.0, 1.0)
    align (0.0, 1.0)

transform friend():
    anchor (0.5, 0.5)
    align (0.5, 0.5)
    zoom 0.2


init python:
    def sydneyshow(img_name):
        if "arms" in img_name:
            renpy.show(img_name, at_list=[scale(0.45)])
        else:
            renpy.show(img_name, at_list=[weirdsydneyscale(0.45)])

    def sydneyhide(img_name):
        """
        Hides the image by name.
        """
        renpy.hide(img_name)
        


label sydneyIntro:
    $ sydneyshow("syd standing happy2")
    s "Oh hi! I'm Sydney! Nice to meet you :) {i}meow{/i}"
    $ sydneyhide("syd standing happy2")
    menu:
        "Meow?":
            $ sydneyshow("syd arms neutral")
            s "Oh yeah. You know. Meow meow?"
            $ sydneyhide("syd arms neutral")
        "{i}Mrrrrrrrrr mmraa! Memeow?{/i}":
            $ sydneyshow("syd arms happy2")
            s "{i}Meowmeowmeowmeow meowmeow meowmeow meeeooooowwww~{/i}"
            $ sydneyhide("syd arms happy2")
        "Uhh.. yeah it's nice to meet you too.":
            $ sydneyshow("syd standing neutral2")
            s "Uh yeah."
            $ sydneyhide("syd standing neutral2")

    $ sydneyshow("syd standing happy4")
    s "So yeah you've got a bingo sheet right? Let's see..."
    $ sydneyhide("syd standing happy4")
    $ sydneyshow("syd standing concerned")
    s "\"Thinks fruits and vegetables came from {i}Stardew Valley{/i}\ uhh..."
    $ sydneyshow("syd standing concerned")
    $ sydneyhide("syd standing concerned")
    $ sydneyshow("syd standing2 happy")
    s "OMG yeah once I went to the state fair and was {color=#f00}SHOCKED{/color} to see pumpkins in real life."
    s "I can’t believe they’d so shamelessly rip off Stardew like that!"
    $ sydneyhide("syd standing2 happy")
    $ sydneyshow("syd standing2 happy")
    show syd standing2 doubtful at weirdsydneyscale(0.45)
    s "They made it so you can even grow giant pumpkins too? What the fart..."
    hide syd standing2 doubtful at weirdsydneyscale(0.45)
    menu:
        "Real life came first. Then {i}Stardew Valley{/i}.":
            show syd shocked at weirdsydneyscale(0.45)
            s "{b}YOU TAKE THAT BACK!!!{/b}"
            hide syd shocked at weirdsydneyscale(0.45)
            show syd arms sad at scale(0.45)
            s "..."
            hide syd arms sad at scale(0.45)
            show syd thumbsup happy4 at weirdsydneyscale(0.45)
            s "Sorry, what I meant to say was... erm... you’re wrong. Yup! ;D"
            hide syd thumbsup happy4 at weirdsydneyscale(0.45)
        "And they had the audacity to take cauliflower too!":
            show syd thumbsup happy3 at weirdsydneyscale(0.45)
            s "I know right! You get it."
            hide syd thumbsup happy3 at weirdsydneyscale(0.45)
        "...":
            show syd arms neutral at scale(0.45)
            s "Don’t give me that face, you know I’m right."
            hide syd arms neutral at scale(0.45)
    
    $ sydneyshow("syd standing happy4")
    s "Well, good chatting with you! If you ever want to hang out let's do that!"
    s "Sydney OUT!"
    $ sydneyhide("syd standing happy4")
    hide syd standing happy4 at weirdsydneyscale(0.45)
    jump chooseOfficerIntro

label sydneyDate:
    $ sydneyDateValue = 0
    scene black
    "Everything’s dark since… y’know… Sydney has her hands over your eyes."
    "She said she had a surprise date idea and you can’t help but feel… on edge."
    s "Suuuurrppppppppiiiiissseeee!!!"
    "Her hands uncover your eyes to reveal... the inside of a plane?"
    scene bg_plane
    $ sydneyshow("syd arms happy3")
    s "Y’know that saying ‘love is in the air’? Since this is our first date, I figured we should be in the air!"
    s "To find love."
    $ sydneyhide("syd arms happy3")
    $ sydneyshow("syd arms concerned")
    s "Yeah."
    $ sydneyhide("syd arms concerned")
    show syd thumbsup happy3 at scale(0.45)
    s "We’re going skydiving!! Nothing’s more romantic than falling thousands of feet together!"
    hide syd thumbsup happy3 at scale(0.45)
    menu:
        "Ni hen mei (You are beautiful) ;)":
            show syd heart happy2 at scale(0.45)
            s "Hey thanks :D I don't get why you're telling me this now, but 謝謝 (thank you)!"
            show syd heart happy2 at scale(0.45)
        "Can I sit this one out?":
            $ sydneyDateValue -= 1
            show syd arms happy3 at scale(0.45)
            s "Hahahahaha!"
            hide syd arms happy3 at scale(0.45)
        "What the helly poop fart balls.":
            $ sydneyDateValue += 1
            show syd standing2 happy at scale(0.45)
            s "Woah! I thought I was the only one who said that. Twinsies!"
            hide syd standing2 happy at scale(0.45)

    $ sydneyshow("syd standing neutral")
    s "Alright, let’s go get our skydiving things ready so we can go into the sky and dive."
    $ sydneyhide("syd standing neutral")
    "You got the {color=#ff0}Skydiving Gear{/color}."
    "You equipped the {color=#ff0}Skydiving Gear{/color}.\n{color=#f00}ATK{/color} +0 | {color=#00f}DEF{/color} +3 | {color=#0f0}LUC{/color} +1"
    $ sydneyshow("syd thumbsup happy2")
    s "All geared up! You ready?"
    $ sydneyhide("syd thumbsup happy2")
    menu:
        "Hahahaha! {i}nervous laughter{/i}":
            $ sydneyDateValue -= 1
            $ sydneyshow("syd arms thinking")
            s "Why are you laughing...?"
            $ sydneyhide("syd arms thinking")
            $ sydneyshow("syd arms happy3")
            s "Well, no matter."
            $ sydneyhide("syd arms happy3")
            "Sydney pushes you off, then jumps off herself."
            scene black
            "Your eyes snap shut and a deep plummetting feeling sinks across your body."
            "Cold wind slices against you, tumbling, twirling."
            "You open your eyes."
            scene bg_sky
            $ sydneyshow("syd standing happy")
            s "WHHEEEEEEEEEEEEEE!!!"
            $ sydneyhide("syd standing happy")
        "Ready as I'll ever be!":
            $ sydneyshow("syd thumbsup happy3")
            s "“Yah yah yah yah yah yah yah!! That’s a good place to be lfgggggg!"
            $ sydneyhide("syd thumbsup happy3")
            $ sydneyshow("syd standing happy")
            s "Alright on the count of three..."
            s "3..."
            s "2..."
            $ sydneyhide("syd standing happy")
            "You jump."
            $ sydneyshow("syd shocked")
            s "HEY! WTF I didn't get to one!!"
            $ sydneyhide("syd shocked")
            "Sydney jumps after you!"
            scene bg_sky
        "Isshoni yarou~ (Let's do it together~)":
            $ sydneyDateValue += 1
            $ sydneyshow("syd heart happy")
            s "Awwww you’re sugoku kawaii!!! 恋愛マイスターっぽい~ (You're like a love master!)"
            $ sydneyhide("syd heart happy")
            $ sydneyshow("syd heart happy2")
            s "Ok let’s do it together!"
            $ sydneyhide("syd heart happy2")
            "You hold hands and JUMP!"
            scene bg_sky
        
    "As you're both falling, you notice you have company."
    $ sydneyshow("syd standing2 doubtful")
    "Tom" "Hey, uh. I didn't expect to see... you guys here."
    show tom standing concerned at scale(0.45), right
    "Tom comes in, zooming. He’s standing on some sort of flying contraption. Unlike some folks, he isn’t free-falling from the sky."
    hide tom standing concerned at scale(0.45), right
    $ sydneyhide("syd standing2 doubtful")
    if secretStep2:
        $ sydneyshow("syd standing2 happy")
        show tom standing concerned at scale(0.45), right
        s "I thought you were coming here tomorrow??"
        hide tom standing concerned at scale(0.45), right
        show tom standing doubtful2 at scale(0.45), right
        "Tom" "I think we can do it today, but... why're they here?"
        "Tom" "Is this..?"
        hide tom standing doubtful2 at scale(0.45), right
        $ sydneyhide("syd standing2 happy")
        menu:
            "We're on a date.":
                $ sydneyDateValue += 1
                "A look of understanding dawns on Tom's face and he seems to relax."
                show tom standing happy at scale(0.45), right
                "Tom" "Oh! I don't mean to intrude!"
                "Tom" "I do love a good day in the troposphere."
                hide tom standing happy at scale(0.45), right
            "I, erm, don't really know.":
                $ sydneyDateValue -= 1
                $ sydneyshow("syd standing2 happy")
                show tom standing doubtful3 at scale(0.45), right
                "Tom" "Sydney, what's, uh, happening?"
                $ sydneyhide("syd standing2 happy")
                $ sydneyshow("syd standing2 neutral")
                s "We're just... hanging out. I didn't think you'd be advancing the operation to today."
                hide tom standing doubtful3 at scale(0.45), right
                $ sydneyhide("syd standing2 neutral")
            "Wouldn't you like to know!?":
                $ sydneyshow("syd standing2 happy")
                show tom standing doubtful3 at scale(0.45), right
                "Tom" "Sydney, what's, uh, happening?"
                $ sydneyhide("syd standing2 happy")
                $ sydneyshow("syd standing2 thinking")
                hide tom standing doubtful3 at scale(0.45), right
                show tom standing shocked at scale(0.45), right
                s "I didn't think you'd be advancing the operation to today."
                $ sydneyhide("syd standing2 thinking")
                hide tom standing shocked at scale(0.45), right

        "You catch a glimpe of several glass canisters brimming with {color=#add8e6}air essence{/color}."
        menu:
            "What're those? {i}point at canisters{/i}":
                show tom standing happy at scale(0.45), right
                $ sydneyshow("syd thumbsup happy")
                s "Hey, let's focus on the skydiving yeah!"
                $ sydneyhide("syd thumbsup happy")
                $ sydneyshow("syd thumbsup happy2")
                s "You should just, y'know, forget all of this I think!"
                $ sydneyhide("syd thumbsup happy2")
                hide tom standing happy at scale(0.45), right
            "{i}to Tom{/i} What are you doing?":
                $ sydneyshow("syd thumbsup happy")
                show tom standing happy2 at scale(0.45), right
                "Tom" "I'm just..."
                "Tom" "I'm working on a project."
                "Tom" "That's all you need to know."
                "Sydney looks at you, her eyes telling you the same story."
                $ sydneyhide("syd thumbsup happy")
                hide tom standing happy2 at scale(0.45), right
            "{i}to Sydney{/i} You're beautiful":
                $ sydneyDateValue += 1
                show tom standing happy4 at scale(0.45), right
                $ sydneyshow("syd heart happy2")
                "OH!! Well! Thank you ^-^"
                $ sydneyhide("syd heart happy2")
                hide tom standing happy4 at scale(0.45), right

        "Tom begins to press some buttons and turn some dials on the control panel of the levitating device."
        "It seems as if he's about to leave, as the metal and wood under his feet begins to hum."
        menu:
            "{i}Leap onto Tom's craft.{/i}":
                $ sydneyshow("syd shocked")
                s "No!!"
                $ sydneyhide("syd shocked")
                show tom standing shocked at scale(0.45), right
                "Tom" "Agh!!!"
                hide tom standing shocked at scale(0.45), right
                "You swoop onto the deck of the vague machine, clutching a metal protrusion."
                "The entire construction is humming loudly. The glass canisters rattle and one breaks free from its bindings."
                show tom standing shocked at scale(0.45), right
                "Tom" "No, hey! Don't! Please!"
                hide tom standing shocked at scale(0.45), right
                "The canister shatters, spewing {color=#add8e6}air essence{/color}. The machine plummets from Sydney's course and you lose sight of her."
                "The aircraft tilts and you grasp tighter, struggling to keep your grip."
                "You notice Tom seems to have hit his head. He's unconscious."
                "The machine spins more and more, the ground creeps ever closer as a massive wall of little houses and trees."
                "It seems the craft it still attempting to navigate somewhere in this uncontrolled fall."
                menu:
                    "{i}Leap off and activate your parachute{/i}":
                        "You begin to leap from the failing machine, sparing one last glance at Tom before you do."
                        "You jump and begin to reach for your parachute cord."
                        "Yet, no more than three seconds after your foot leaves the deck, a seagull collides with the left side of your head."
                        scene black
                        "And then there is nothing but darkness."
                        "You plummet to the ground."
                        "You have died."
                        return
                    "{i}Grab Tom, leap off, and activate your parachute{/i}":
                        "You hoist Tom and buckle him hastily to your parachute gear and roll off the edge of the spiralling machine."
                        "Seconds later, you yank the parachute cord... and..."
                        "A parachute unfurls out behind you, the instant drag giving you both a tug."
                        "For some reason, small heart shaped balloons come out as well."
                        "The machine, now little more than a hodgepodge of splintered wood and twisted metal, crashes into the room of a blue house below you."
                "You steer to follow and descend into the hole."
                jump secretDate
            "{i}Ignore him.{/i}":
                "Another instant later, the humming reaches a peak and the machine zips off!"
                $ sydneyshow("syd standing neutral2")
                "Sydney seems to breathe a sigh of relief."
                $ sydneyhide("syd standing neutral2")

    else:
        show tom standing happy at scale(0.45), right
        $ sydneyshow("syd standing2 doubtful")
        "Tom" "Hey, how about I rescue you from this mess and show you an actually good time!"
        $ sydneyhide("syd standing2 doubtful")
        $ sydneyshow("syd arms thinking")
        s "HEY!!"
        hide tom standing happy at scale(0.45), right
        show tom standing surprised at scale(0.45), right
        "Tom" "Oh, I'm not talking to you Sydney. You’re on your own."
        hide tom standing surprised at scale(0.45), right
        $ sydneyhide("syd arms thinking")
        $ sydneyshow("syd arms concerned")
        show tom standing happy4 at scale(0.45), right
        s "*{i}{color=#f00}angry{/color} noises{/i}*"
        hide tom standing happy4 at scale(0.45), right
        show tom standing surprised at scale(0.45), right
        "Tom" "Just sayin', the ground there..."
        "He looks down over the edge of his ambiguous flying machine."
        hide tom standing surprised at scale(0.45), right
        $ sydneyhide("syd arms concerned")
        show tom standing surprised at scale(0.45), right
        $ sydneyshow("syd arms concerned")
        "Tom" "...is looking awfully close."
        hide tom standing surprised at scale(0.45), right
        show tom standing happy3 at scale(0.45), right
        "Tom" "Say the word and we can just chill out at my place! Have some tea, play some video games, y'know?"
        $ sydneyhide("syd arms concerned")
        hide tom standing happy3 at scale(0.45), right
        menu:
            "Without risk there is no reward. The path of wisdom lights itself only whence you, idk, go skydiving.":
                "Tom begins to weep at your wordsmithing and zooms away in a blink."
                $ sydneyDateValue += 1
                $ sydneyshow("syd shocked2")
                s "“What eloquence!! What grace! With which you just conducted yourself! With your words!!"
                $ sydneyhide("syd shocked2")
            "Agachate y conocelo agapate bueno bueno pan de de pan-":
                $ sydneyshow("syd arms doubtful")
                show tom standing wince at scale(0.45), right
                "Tom and Sydney" "?????"
                s "Ehh… ¿que? I don’t understand..."
                hide tom standing wince at scale(0.45), right
                show tom gesture concerned at scale(0.45), right
                "Tom" "Yo tampoco… I didn’t get that so I guess I’ll just leave?"
                $ sydneyhide("syd arms doubtful")
                $ sydneyshow("syd thumbsup neutral")
                s "Ok, bye!"
                hide tom gesture concerned at scale(0.45), right
                "Tom leaves on his flying object. Away he goes."
                $ sydneyhide("syd thumbsup neutral")
            "Please please PLEASE take me with you!!!":
                $ sydneyDateValue -= 1
                show tom standing happy4 at scale(0.45), right
                $ sydneyshow("syd standing2 concerned")
                s "Pthbthbthbthhbhb."
                "Tom" "Yessir, here we go!"
                $ sydneyhide("syd standing2 concerned")
                hide tom standing happy4 at scale(0.45), righ
                menu:
                    "Thank you thank you thank you!":
                        "You board Tom’s flying thingy and the two of you zoom off."
                        "You unequipped the {color=#ff0}Skydiving Gear{/color}.\n{color=#f00}ATK{/color} +0 | {color=#00f}DEF{/color} -3 | {color=#0f0}LUC{/color} -1"
                        "In the distance, you see Sydney stick her tongue out at the both of you before she grows wings and flies away herself."
                        "You fly back down to the ground and land at Tom's house."
                        show tom gesture happy3 at scale(0.45)
                        "Tom" "Safe flight! Nice. I only hit that landing half the time."
                        hide tom gesture happy3 at scale(0.45)
                        jump tomDate
                    "PSYCHEEEEE!":
                        show tom standing doubtful2 at scale(0.45), right
                        $ sydneyshow("syd standing2 neutral")
                        "Tom" "Oh. Uh...ok?"
                        s "huh..."
                        $ sydneyhide("syd standing2 neutral")
                        hide tom standing doubtful2 at scale(0.45), right
                        "Tom goes bye bye! Everyone say bye bye Tom!"
    $ sydneyshow("syd arms concerned")
    s "So where were we?"
    $ sydneyhide("syd arms concerned")
    $ sydneyshow("syd standing happy")
    s "Oh yeah! We’re still dropping from the sky."
    $ sydneyhide("syd standing happy")
    $ sydneyshow("syd standing happy2")
    s "How about let’s play 2 truths, 1 lie! Let me think… two truths, one lie…"
    $ sydneyhide("syd standing happy2")
    $ sydneyshow("syd standing happy3")
    s "Ok, my two truths, one lie.\n(INCOMING! SLUSHY NOOBZ REFERENCE! ok)"
    s "I have five toes... on one foot...{p}I fingered my ass once...{p}...and I've been to Iceland."
    s "Ok, which one's the {color=#f00}lie{/color}?"
    $ sydneyhide("syd standing happy3")
    menu:
        "The five toes one.":
            $ sydneyshow("syd arms happy3")
            s "I actually have 5 toes! 5 toes on each feets!"
            $ sydneyhide("syd arms happy3")
            $ sydneyshow("syd arms sad")
            s "You…you think I’ve fingered my ass before…?"
            $ sydneyshow("syd arms sad")
        "The ass one.":
            $ sydneyDateValue += 1
            $ sydneyshow("syd thumbsup happy2")
            s "I actually have fingered my ass once!"
            $ sydneyhide("syd thumbsup happy2")
            $ sydneyshow("syd standing2 happy2")
            s "But I’m glad you don’t think I have."
            $ sydneyhide("syd standing2 happy2")
        "Iceland?":
            $ sydneyDateValue -= 1
            $ sydneyshow("syd arms happy3")
            s "I actually have been to Iceland before!"
            $ sydneyhide("syd arms happy3")
            $ sydneyshow("syd overit")
            s "You…you think I’ve fingered my ass before."
            $ sydneyhide("syd overit")

    $ sydneyshow("syd standing happy")
    s "Ok, we’re close!! You ready to pull the parachute?"
    $ sydneyhide("syd standing happy")
    "You both pull open your parachutes."
    if sydneyDateValue > 1:
        "Your parachutes open and out come a swarm of heart-shaped balloons."
        "The clouds part to make way for the sun’s gentle light, bathing you two in its warmth."
        "You look into each other’s eyes, mesmerized by the {color=#d1a054}honey gold{/color} in hers and the also whatever pretty color is in yours."
        "A baby with wings flies close to you and you feel a prick on your…butt?\n{color=#0f9}HP{/color} -1"
        "You see Sydney also get hit by this baby’s heart-shaped arrow. Her head’s bleeding."
        scene bg_ground
        "As you touch down onto land, Sydney (still bleeding from the wound) holds up one of the heart-shaped balloons."
        $ sydneyshow("syd special 1")
        s "Here, a gift."
        $ sydneyhide("syd special 1")
        "Suddenly, she’s having a hard time keeping eye contact with you."
        $ sydneyshow("syd special 1")
        s "Um…"
        $ sydneyhide("syd special 1")
        $ sydneyshow("syd special 2")
        s "I had a really fun time today. And…"
        $ sydneyhide("syd special 2")
        "She plucks the arrow out of her head and wipes off the blood."
        $ sydneyshow("syd heart happy2")
        s "And I think I’ve fallen for you."
        s "(haha get it. fall? im not proud of this either.)"
        s "We should do this again some time >///<"
        $ sydneyhide("syd heart happy2")
        menu:
            "Haha, no!! I {i}never{/i} want to go skydiving again.":
                $ sydneyshow("syd arms neutral2")
                s "Oh. I mean, I guess it doesn’t have to be skydiving."
                $ sydneyhide("syd arms neutral2")
                $ sydneyshow("syd standing2 neutral")
                s "Umm ok bye? I’ll text you? I guess?"
                $ sydneyhide("syd standing2 neutral")
            "Same time tomorrow?":
                $ sydneyshow("syd arms doubtful")
                s "What the helly fart balls. I’m all skydived-out."
                $ sydneyhide("syd arms doubtful")
                $ sydneyshow("syd heart happy2")
                s "Next time let’s go to a public park and run and scream until they kick us out! It’ll be fun :D"
                $ sydneyhide("syd heart happy2")
                $ sydneyshow("syd heart happy")
                s "Byee I’ll send you a carrier pigeon!"
                $ sydneyhide("syd heart happy")
        "You achieved {color=#0ff}SYDNEY GOOD ENDING{/color}!"
        return
    elif sydneyDateValue < -1:
        "We pulled the parachute…right? Why isn’t anything happening…?"
        $ sydneyshow("syd shocked")
        s "LET ME TRY PULLING IT AGAINNN!!!"
        $ sydneyhide("syd shocked")
        $ sydneyshow("syd standing2 happy2")
        s "Yeah... nope!"
        $ sydneyhide("syd standing2 happy2")
        "You two plummet to the ground."
        "Sydney zooms past you and lands first. Oof."
        "The ground grows closer and closer, until…"
        "{i}crunch{/i}"
        scene black
        "..."
        scene white
        "..."
        "You wake suddenly. Where are you…? You can’t seem to remember anything."
        "It’s bright but unsettling. What’s going on?"
        "In the corner of your eye, you see a familiar face."
        "You turn to them, but can’t seem to figure out where you know them from."
        $ sydneyshow("syd standing happy2")
        s "Oh hi! I'm Sydney! Nice to meet you :) {i}meow{/i}"
        $ sydneyhide("syd standing happy2")
        "You realize where you are now. This is the evil zone."
        "The stupid chungus evil Sydney zone. Where you’ll be forever."
        "Bummer."
        "You achieved {color=#d00}SYDNEY BAD ENDING{/color}."
        return
    else:
        "The parachute opens in a normal and anticlimactic way."
        scene bg_ground
        "Your feet reach the ground, again in a normal and anticlimactic way."
        $ sydneyshow("syd arms happy")
        s "Uh...nice! Idk why I expected something bigger to happen."
        s "Well, I had a good time today!"
        $ sydneyhide("syd arms happy")
        $ sydneyshow("syd arms thinking")
        s "And well, I think we'd be better off as friends. I just didn't feel the sparks with you yknow?"
        $ sydneyhide("syd arms thinking")
        $ sydneyshow("syd standing2 happy2")
        s "And that's ok! Friends are boss. I like having friends."
        $ sydneyhide("syd standing2 happy2")
        $ sydneyshow("syd standing2 happy4")
        s "Ok this was fun it was nice to meet you let's do this again sometime ok bye!"
        $ sydneyhide("syd standing2 happy4")
        "Sydney struts away."
        show syd standing2 happy4 at friend()
        "Congratulations! You've made your very first friend :)"
        "You achieved SYDNEY NEUTRAL ENDING."
        return