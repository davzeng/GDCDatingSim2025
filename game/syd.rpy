transform scale(ratio):
    zoom ratio

# I am only keeping this here because I don't want to re-do everything -Sydney
transform weirdsydneyscale(ratio):
    zoom ratio
    anchor (0.0, 1.0)
    align (0.0, 1.0)


init python:
    def sydneyshow(img_name):
        """
        Shows an image using the correct transform.
        - If 'arms' in image name → uses scale(0.45)
        - Else → uses weirdsydneyscale(0.45)
        """
        if "arms" in img_name:
            renpy.show(img_name, at_list=[scale(0.45)])
        else:
            renpy.show(img_name, at_list=[weirdsydneyscale(0.45)])

    def sydneyhide(img_name):
        """
        Hides the image by name.
        """
        renpy.hide(img_name)


label sydneyDate:
    $ sydneyDateValue = 0
    "Everything’s dark since… y’know… Sydney has her hands over your eyes. She said she had a surprise date idea and you can’t help but feel… on edge."
    show syd standing2 happy2 at weirdsydneyscale(0.45)
    "Sydney" "Suuuurrppppppppiiiiissseeee!!!"
    hide syd standing2 happy2 at weirdsydneyscale(0.45)
    "Her hands uncover your eyes to reveal... a plane's interior?"
    show syd arms happy3 at scale(0.45), left
    "Sydney" "Y’know that saying ‘love is in the air’? Since this is our first date, I figured we should be in the air!"
    "Sydney" "To find love."
    hide syd arms happy3 at scale(0.45), left
    show syd arms concerned at scale(0.45), left
    "Sydney" "Yeah."
    hide syd arms concerned at scale(0.45), left
    show syd thumbsup happy3 at scale(0.45)
    "Sydney" "We’re going skydiving!! Nothing’s more romantic than falling thousands of feet together!"
    hide syd thumbsup happy3 at scale(0.45)
    menu:
        "Ni hen mei ;)":
            show syd heart happy2 at scale(0.45)
            "Sydney" "Hey thanks :D I don't get why you're telling me this now, but 謝謝!"
            show syd heart happy2 at scale(0.45)
        "Can I sit this one out?":
            $ sydneyDateValue -= 1
            show syd arms happy3 at scale(0.45)
            "Sydney" "Hahahahaha!"
            hide syd arms happy3 at scale(0.45)
        "What the helly poop fart balls.":
            $ sydneyDateValue += 1
            show syd standing2 happy at scale(0.45)
            "Sydney" "Woah! I thought I was the only one who said that. Twinsies!"
            hide syd standing2 happy at scale(0.45)

    show syd standing neutral at scale(0.45)
    "Sydney" "Alright, let’s go get our skydiving things ready so we can go into the sky and dive."
    "You got the {color=#ff0}Skydiving Gear{/color}."
    "You equipped the {color=#ff0}Skydiving Gear{/color}.\n{color=#f00}ATK{/color} +0 | {color=#00f}DEF{/color} +3 | {color=#0f0}LUC{/color} +1"
    "Sydney" "All geared up! You ready?"
    menu:
        "Hahahaha!":
            $ sydneyDateValue -= 1
            "Sydney" "Why are you laughing...?"
            "Sydney" "Well, no matter."
            "Sydney pushes you off, then jumps off herself."
            "Your eyes snap shut and a deep plummetting feeling sinks across your body."
            "Cold wind slices against you, tumbling, twirling."
            "You open your eyes."
            "Sydney" "WHHEEEEEEEEEEEEEE!!!"
        "Ready as I'll ever be!":
            "Sydney" "“Yah yah yah yah yah yah yah!! That’s a good place to be lfgggggg!"
            "Sydney" "Alright on the count of three..."
            "Sydney" "3..."
            "Sydney" "2..."
            "You jump."
            "Sydney" "HEY! WTF I didn't get to one!!"
            "Sydney jumps after you!"
        "Isshoni yarou~":
            $ sydneyDateValue += 1
            "Sydney" "Awwww you’re sugoku kawaii!!! 恋愛マイスターっぽい~"
            "Sydney" "Ok let’s do it together!"
            "You hold hands and JUMP!"
        
    "As you're both falling, you notice you have company."
    "Tom" "Hey, uh. I didn't expect to see... you guys here."
    "Tom comes in, zooming. He’s standing on some sort of flying contraption. Unlike some folks, he isn’t free-falling from the sky."
    if secretStep2:
        "Sydney" "I thought you were coming here tomorrow??"
        "Tom" "I think we can do it today, but... why're they here?"
        "Tom" "Is this..?"
        menu:
            "We're on a date.":
                $ sydneyDateValue += 1
                "A look of understanding dawns on Tom's face and he seems to relax."
                "Tom" "Oh! I don't mean to intrude!"
                "Tom" "I do love a good day in the troposphere."
            "I, erm, don't really know.":
                $ sydneyDateValue -= 1
                "Tom" "Sydney, what's, uh, happening?"
                "Sydney" "We're just... hanging out. I didn't think you'd be advancing the operation to today."
            "Wouldn't you like to know!?":
                "Tom" "Sydney, what's, uh, happening?"
                "Sydney" "I didn't think you'd be advancing the operation to today."
        
        "You catch a glimpe of several glass canisters brimming with {color=#add8e6}air essence{/color}."
        menu:
            "What're those? {i}point at canisters{/i}":
                "Sydney" "Hey, let's focus on the skydiving yeah!"
                "Sydney" "You should just, y'know, forget all of this I think!"
            "{i}to Tom{/i} What are you doing?":
                "Tom" "I'm just..."
                "Tom" "I'm working on a project."
                "Tom" "That's all you need to know."
                "Sydney looks at you, her eyes telling you the same story."
            "{i}to Sydney{/i} You're beautiful":
                $ sydneyDateValue += 1
                "OH!! Well! Thank you ^-^"

        "Tom begins to press some buttons and turn some dials on the control panel of the levitating device."
        "It seems as if he's about to leave, as the metal and wood under his feet begins to hum."
        menu:
            "{i}Leap onto Tom's craft.{/i}":
                "Sydney" "No!!"
                "Tom" "Agh!!!"
                "You swoop onto the deck of the vague machine, clutching a metal protrusion."
                "The entire construction is humming loudly. The glass canisters rattle and one breaks free from its bindings."
                "Tom" "No, hey! Don't! Please!"
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
                "Sydney seems to breathe a sigh of relief."

    else:
        "Tom" "Hey, how about I rescue you from this mess and show you an actually good time!"
        "Sydney" "HEY!!"
        "Tom" "Oh, I'm not talking to you Sydney. You’re on your own."
        "Sydney" "{i}{color=#f00}angry{/color} noises{/i}"
        "Tom" "Just sayin', the ground there..."
        "He looks down over the edge of his ambiguous flying machine."
        "Tom" "...is looking awfully close."
        "Tom" "Say the word and we can just chill out at my place! Have some tea, play some video games, y'know?"
        menu:
            "Without risk there is no reward. The path of wisdom lights itself only whence you, idk, go skydiving.":
                "Tom begins to weep at your wordsmithing and zooms away in a blink."
                $ sydneyDateValue += 1
                "Sydney" "“What eloquence!! What grace! With which you just conducted yourself! With your words!!"
            "Agachate y conocelo agapate bueno bueno pan de de pan-":
                "Tom and Sydney" "?????"
                "Sydney" "Ehh… ¿que? I don’t understand..."
                "Tom" "Yo tampoco… I didn’t get that so I guess I’ll just leave?"
                "Sydney" "Ok, bye!"
                "Tom leaves on his flying object. Away he goes."
            "Please please PLEASE take me with you!!!":
                $ sydneyDateValue -= 1
                "Sydney" "Pthbthbthbthhbhb."
                "Tom" "Yessir, here we go!"
                menu:
                    "Thank you thank you thank you!":
                        "You board Tom’s flying thingy and the two of you zoom off."
                        "In the distance, you see Sydney stick her tongue out at the both of you before she grows wings and flies away herself."
                        "You fly back down to the ground and land at Tom's house."
                        "Tom" "Safe flight! Nice. I only hit that landing half the time."
                        "Tom" "Come inside, come inside!"
                        jump tomDate
                    "PSYCHEEEEE!":
                        "Tom" "Oh. Uh...ok?"
                        "Sydney" "huh..."
    "Sydney" "So where were we?"
    "Sydney" "Oh yeah! We’re still dropping from the sky."
    "Sydney" "How about let’s play 2 truths, 1 lie! Let me think… two truths, one lie…"
    "Sydney" "Ok, my two truths, one lie.\n(INCOMING! SLUSHY NOOBZ REFERENCE! ok)"
    "Sydney" "I have five toes... on one foot...{p}I fingered my ass once...{p}...and I've been to Iceland."
    "Sydney" "Ok, which one's the {color=#f00}lie{/color}?"
    menu:
        "The five toes one.":
            "Sydney" "I actually have 5 toes! 5 toes on each feets!"
            "Sydney" "You…you think I’ve fingered my ass before…?"
        "The ass one.":
            $ sydneyDateValue += 1
            "Sydney" "I actually have fingered my ass once!"
            "Sydney" "But I’m glad you don’t think I have."
        "Iceland?":
            $ sydneyDateValue -= 1
            "Sydney" "I actually have been to Iceland before!"
            "Sydney" "You…you think I’ve fingered my ass before…?"

    "Sydney" "Ok, we’re close!! You ready to pull the parachute?"
    "You both pull open your parachutes."
    if sydneyDateValue > 1:
        "Your parachutes open and out come a swarm of heart-shaped balloons."
        "The clouds part to make way for the sun’s gentle light, bathing you two in its warmth."
        "You look into each other’s eyes, mesmerized by the {color=#d1a054}honey gold{/color} in hers and the also whatever pretty color is in yours."
        "A baby with wings flies close to you and you feel a prick on your…butt?\n{color=#0f9}HP{/color} -1"
        "You see Sydney also get hit by this baby’s heart-shaped arrow. Her head’s bleeding."
        "As you touch down onto land, Sydney (still bleeding from the wound) holds up one of the heart-shaped balloons."
        "Sydney" "Here, a gift."
        "Suddenly, she’s having a hard time keeping eye contact with you."
        "Sydney" "Um…"
        "Sydney" "I had a really fun time today. And…"
        "Sydney" "And I think I’ve fallen for you."
        "Sydney" "(haha get it. fall? im not proud of this either.)"
        "Sydney" "We should do this again some time >///<"
        menu:
            "Haha, no!! I {i}never{/i} want to go skydiving again.":
                "Sydney" "Oh. I mean, I guess it doesn’t have to be skydiving."
                "Sydney" "Umm ok bye? I’ll text you? I guess?"
            "Same time tomorrow?":
                "Sydney" "What the helly fart balls. I’m all skydived-out."
                "Sydney" "Next time let’s go to a public park and run and scream until they kick us out! It’ll be fun :D"
                "Sydney" "Byee I’ll send you a carrier pigeon!"
        "You achieved {color=#0ff}SYDNEY GOOD ENDING{/color}!"
        return
    elif sydneyDateValue < -1:
        "We pulled the parachute…right? Why isn’t anything happening…?"
        "Sydney" "LET ME TRY PULLING IT AGAINNN!!!"
        "Sydney" "Yeah... nope!"
        "You two plummet to the ground."
        "Sydney zooms past you and lands first. Oof."
        "The ground grows closer and closer, until…"
        "{i}crunch{/i}"
        "..."
        "..."
        "You wake suddenly. Where are you…? You can’t seem to remember anything."
        "It’s bright but unsettling. What’s going on?"
        "In the corner of your eye, you see a familiar face."
        "You turn to them, but can’t seem to figure out where you know them from."
        "Sydney" "Oh hi I'm Sydney! Nice to meet you :) {i}meow{/i}"
        "You realize where you are now. This is the evil zone."
        "The stupid chungus evil Sydney zone. Where you’ll be forever."
        "Bummer."
        "You achieved {color=#d00}SYDNEY BAD ENDING{/color}."
        return
    else:
        "The parachute opens in a normal and anticlimactic way."
        "Your feet reach the ground, again in a normal and anticlimactic way."
        "Sydney" "Uh...nice! Idk why I expected something bigger to happen."
        "Sydney" "Well, I had a good time today!"
        "Sydney" "And well, I think we'd be better off as friends. I just didn't feel the sparks with you yknow?"
        "Sydney" "And that's ok! Friends are boss. I like having friends."
        "Sydney" "Ok this was fun it was nice to meet you let's do this again sometime ok bye!"
        "Sydney struts away."
        "Congratulations! You've made your very first friend :)"
        "You achieved SYDNEY NEUTRAL ENDING."
        return