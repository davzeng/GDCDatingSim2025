image bg_view:
    "bg_view.png"
    xysize(1920, 1080)
image bg_plants:
    "bg_plants.png"
    xysize(1920, 1080)
image bg_tvroom:
    "bg_reactor.png"
    xysize(1920, 1080)
image bg_classroom:
    "bg_classroom.png"
    xysize(1920, 1080)
image bg_reactor:
    "bg_reactor.png"
    xysize(1920, 1080)

label tomIntro:
    show tom greeting at scale(0.45)
    scene bg_classroom
    t "Hellooo!"
    $ visited = []
    $ askedGoals = False
    $ askedShortTerm = False;
    menu tomIntro1:
        set visited
        "Who are you.":
            show tom gesture doubtful2 at scale(0.45)
            t "Pretty sure I’m Tom. Or something similar to that. I’m an {color=#f0f}officer{/color} of the game development club for what it’s worth."
            show tom gesture happy at scale(0.45)
            t "In my spare time I guess I play the piano and grow plants. I have something like 2 billion of those. Plants, not pianos."
            show tom cross neutral at scale(0.45)
            t "One day,  I’m 20 percent certain, I’ll find some way to fuse myself, my plants, and an analog/digital interface and enter my penultimate form."
            show tom cross concerned2 at scale(0.45)
            t "It can't be good, but I've gotta do it."
            show tom standing happy3 at scale(0.45)
            t "I spend the other 80 percent of my certainty on being certain on other things."
        "What are you.":
            show tom standing doubtful at scale(0.45)
            t "Most people think I’m human, whatever that is."
            show tom standing happy3 at scale(0.45)
            t "They're generally right."
            jump tomIntro1
        "Why are you.":
            show tom cross neutral2 at scale(0.45)
            t "Well, if we’re being purely by cause-and-effect I am because 2 decades or so ago I was born in a hospital in Portland. Y’know. Standard and all, so I’m told. You just had to be there."
            t "Now, you could say that’s why I {i}was{/i}, but why I am {i}now{/i} is a different matter. Time has passed."
            show tom cross neutral at scale(0.45)
            t "And to that I’d answer I am because I have taken actions that have resulted in my remaining alive until this point."
            t "And the {i}why{/i} as to why I’ve taken those actions is because I intend to live."
            show tom side neutral2 at scale(0.45)
            t "And the {i}why{/i} as to that is because I wish to, y’know, complete my goals in life or whatever."
            show tom standing happy5 at scale(0.45)
            t "You could also just say I am because I think, or something."
            $ askedGoals = True
            jump tomIntro1
        "What are your goals." if askedGoals:
            show tom standing surprised at scale(0.45)
            t "Personal question so soon! Wow! What a specimen! Look at you!"
            show tom standing happy4 at scale(0.45)
            t "Y’know, I guess the main thing is I just aspire to be a beneficial part of the world. Be the best person I can, be good to others."
            show tom side neutral at scale(0.45)
            t "Beyond that? I’d say I want to find somebody to spend my life with. Have a house, garden, maybe a family. Do something with my career that improves the world."
            show tom side wince at scale(0.45)
            t "Short term goals though? Don’t really know, if I’m being honest..."
            show tom gesture happy2 at scale(0.45)
            t "What are yours?"
            menu:
                "I want to be an astronaut and shoot myself into space and leave Earth forever.":
                    show tom standing surprised at scale(0.45)
                    t "That's pretty bold! But I can definitely respect that."
                    t "I believe in you. Shoot for the moon, miss, and land somewhere among stars you don’t know."
                    show tom gesture happy3 at scale(0.45)
                    t "Tell the aliens I say hi ;)"
                "I want to get into a passionate and deep relationship with you.":
                    show tom standing surprised at scale(0.45)
                    t "Oh! Wow! Uh."
                    show tom bashful at scale(0.8)
                    t "Forward, aren't you?"
                    show tom standing happy4 at scale(0.45)
                    t "Well, you’ll just have to get to know me first. You can do that, can’t you?"
                "I want to eventually retreat into the Himalayas and discover the answer to end human suffering.":
                    show tom side happy at scale(0.45)
                    t "Dude. Fire."
                    t "I respect that, let me know what I can do to help you with that."
                    show tom side neutral at scale(0.45)
                    t "Oh, and let me know if you find it out. The answer to it all, that is."
                "Do you really not have any short term goals?" if secretStep1:
                    $ askedShortTerm = True
                    show tom standing concerned at scale(0.45)
                    t "Well... I, uh..."
                    hide tom standing concerned at scale(0.45)
                    show dav cool happy3 at scale(0.5)
                    "David" "Hey guys! How's the bingo sheets going?"
                    show dav hand happy at scale(0.5)
                    "David" "I've almost got mine filled all the way out!"
                    show dav hand pog at scale(0.5)
                    "David" "God, I can't wait to finish this meeting and get back to ZhuoZhi..."
                    show dav standing neutral at scale(0.5)
                    "David" "Alas."
                    show dav standing happy at scale(0.5)
                    "David" "Good luck, you guys!"
                    hide dav standing happy at scale(0.5)
                    show tom standing doubtful2 at scale(0.45)
                    t "Anyways, uh..."
            jump tomIntro1
        
    show tom standing doubtful2 at scale(0.45)
    t "But yeah, I’ve been a {color=#f0f}game development officer{/color} for years now. I’m the head of our Reclamation, Advancement, and Technology division."
    show tom standing shocked at scale(0.45)
    t "The RAT division."
    show tom standing doubtful at scale(0.45)
    t "I don’t even know how long I've been here... or how long there is left..."
    show tom cross neutral2 at scale(0.45)
    t "..."
    show tom gesture happy2 at scale(0.45)
    t "You have a bingo sheet, right? Let me take a look."
    "You give Tom the {color=#ff0}Bingo Sheet{/color}."
    show tom standing happy2 at scale(0.45)
    t "Hmm ok."
    t "Yeah, I can fill out \"Knows the alchemical elements and how to use them\". Here you go!"
    "You got the {color=#ff0}Bingo Sheet{/color}."
    show tom side neutral2 at scale(0.45)
    t "Can you fill something out on mine as well?"
    "You got the {color=#ff0}Tom's Bingo Sheet{/color}."
    menu:
        "{i}Fill out \"Owns a pre-1900s gaming console\".{/i}":
            show tom cross happy4 at scale(0.45)
            t "Ah yes. The fabled Untendo 1.5 Cube. My great-great-grandfather loved to play {i}Kill and Eat: Peter’s Origins{/i} on that old iron box."
            t "You play anything on it?"
            menu:
                "{i}Train Wreck 5: The Wreckoning Comes to Crush, TX.{/i}":
                    show tom cross happy2 at scale(0.45)
                    t "Total locomotive classic. Good choice."
                "{i}Anachronism IV, Enter the Digital Age{/i}":
                    show tom cross happy2 at scale(0.45)
                    t "Mind-bending, that one's fucked up. Awesome"
                "{i}A Treatise on the Cultivation of Various Cereal Crops and their Usages in Feeding Livestock{/i}":
                    show tom cross happy2 at scale(0.45)
                    t "Ah, love a good cozy game."
            "You give Tom the {color=#ff0}Tom's Bingo Sheet{/color}."
            show tom standing happy5 at scale(0.45)
            t "Thanks for that!"
        "{i}Fill out \"Has grown a plant to completion (any ending)\".{/i}":
            "You give Tom the {color=#ff0}Tom's Bingo Sheet{/color}."
            show tom cross happy2 at scale(0.45)
            t "Ah sick!"
            show tom gesture doubtful3 at scale(0.45)
            t "Been trying to do that for years. Well, true ending completion, that is."
            show tom gesture happy at scale(0.45)
            t "I got first ending a while ago. Thank you!"
        "{i}Fill out \"Sleeps in real life AND in game\".{/i}":
            "You give Tom the {color=#ff0}Tom's Bingo Sheet{/color}."
            show tom cross happy2 at scale(0.45)
            t "Oh wow! We really do have a lot in common don’t we?"
            show tom bashful at scale (1.6)
            t "Maybe we could, uh, put our Minecraft beds on adjacent blocks... if you wouldn’t mind..."
            t "..."
            show tom gesture happy3 at scale(0.45)
            t "Uh... thanks for the bingo!"
        "{i}Fill out \"Knows you're up to something\".{/i}" if askedShortTerm:
            "You give Tom the {color=#ff0}Tom's Bingo Sheet{/color}."
            show tom standing wince at scale(0.45)
            t "Oh."
            show tom standing concerned at scale(0.45)
            t "Uh."
            show tom standing happy at scale(0.45)
            t "Cool! Thanks, I was {i}trying{/i} to get that one filled out!"
            show tom side neutral at scale(0.45)
            t "See you... around?"
            $ secretStep2 = True
            jump chooseOfficerIntro
    
    show tom gesture happy3 at scale(0.45)
    t "Hey, if you want to hang out later I think that’d be great."
    show tom cross happy at scale(0.45)
    t "I’ve got a new tea set and just got some new loose leaf tea imported from {color=#0f0}Greenpath{/color}."
    t "You’re more than welcome to come by my place this weekend; we could play some video games, have some tea, and I could show off my plant collection!"
    show tom standing happy3 at scale(0.45)
    t "Just let me know! ;)"
    hide tom standing happy2

    jump chooseOfficerIntro

label tomDate:
    scene bg_view
    $ tomDateValue = 0
    t "Oh wow, it's pretty nice up here right now."
    t "..."
    t "You wanna stay here for a bit or head inside?"
    menu:
        "Let's stay here for a bit.":
            $ tomDateValue += 1
            t "Yeah, I agree. It's nice."
            "You both sit on the fire escape."
            "It's impossible to tell whether the sun is rising or setting."
            "The city stretches before you like a field of flowers and stumps. Small lights like fae move across and around it."
            "The {color=#a4a}mountain{/color} is quietly, almost silently, humming, a sound somehow outside of and beyond the sounds of the city. Tom hums along with it."
            menu:
                "{i}Hum{/i}":
                    "You both hum along with the mountain."
                    "You seem to recognize the tune."
                "{i}Don't{/i}":
                    "You sit here peacefully, listening to the tune hardly louder than the soft breeze."
            "It's nice here."
            "The tune slowly fades as the light from the sun grows more teal."
            "Tom sits up and holds out a hand."
            menu:
                "{i}Take it{/i}":
                    $ tomDateValue += 1
                    "Tom takes your hand and pulls you up. You feel warmth transfer between your palms."
                    t "Here we go :)"
                "{i}Don't{/i}":
                    "You stand up. Tom pretends as if he was reaching for something on the ground."
            t "Shall we head inside?"
            menu:
                "Ugh sure.":
                    $ tomDateValue -= 1
                    "Tom stares at you for a second."
                    t "Uh, ok, let's go."
                "Let's do it.":
                    "Sweet, c'mon in."
        "Let's go inside.":
            t "Sure, you're right, it's a bit cold out right now."
    
    "Tom leads you inside from the fire escape, through another person's bedroom, a hallway, and finally into his own room."
    scene bg_plants
    t "What do you think?"
    t "The room was a bit of a mess so I put of holographic projections of what it's meant to look like."
    menu:
        "Oh, this is cool asf.":
            $ tomDateValue += 1
            t "Hell yeah, thanks!"
            t "Sometimes I turn on all the projectors to display random lights and numbers and stuff."
            t "Reminds me of something in one of my favorite games."
        "This is nice!":
            t "Yeah, thanks! Sometimes I turn on all the projectors to display random lights and numbers and stuff."
        "Your room was a mess?":
            $ tomDateValue -= 1
            t "Hey dude, I'm working on it!"
    
    if tomDateValue < 3:
        t "Here, make yourself comfortable."
    else:
        t "Here, make yourself comfortable, my house is your house!"
    $ floorCount = 0
    menu sitting:
        "{i}Sit on the bed{/i}":
            "You sit on the bed. It creaks a bit as you sit."
            "It's green, like most things in his room."
            t "I like this bed a lot since it's got a bookshelf at the headboard!"
            t "Sadly, it's a bit old and squeaky though!"
            menu:
                "That's all cool! I like the books!":
                    t "Thanks! I try to keep all my favorites there."
                "{i}Nod contentedly{/i}":
                    "Tom nods back. :)"
                "Oh no... the squeakiness might be an issue...":
                    t "Uh, why's that..?"
                    menu:
                        "{i}Shrug{/i}":
                            t "Eh yeah, it's fine."
                        ";)":
                            "Tom blushes."
                            $ tomDateValue += 1
                            t "Oh.. I.. uh.. :)"
                            t "I'm sure it'd be fine."
        "{i}Sit on the chair{/i}":
            t "Mmm the gamer chair."
            t "It's actually one that my dad, uh, took from his work. Which means it's..."
            t "...really comfortable."
            t "My posture is still shit though."
            t "You play any games?"
            menu:
                "Nah, not really.":
                    t "What, uh, what made you come to Game Dev Club then?"
                    menu:
                        "{i}Stare{/i}":
                            $ tomDateValue -= 1
                            t "Uh."
                        "{i}Jump up and down rapidly!!!{/i}":
                            "Tom slowly nods."
                            t "Yeah! yeah! Great!"
                "From time to time, yeah!":
                    t "Nice!"
                    t "Here, one sec, let me get the tea."
                "SKONG IS REAL.":
                    $ tomDateValue += 1
                    t "{b}YESSSSSSSSSS!!{/b}"
                    t "Dude it's so good man I love it."
                    t "I can't believe it's actually, like, a thing."
                    t "The coming of the messiah."
                    t "Here, lemme go get the tea then we can continue!"
        "{i}Sit on the rug{/i}":
            $ floorCount += 1
            if floorCount > 5:
                t "Whatever, man."
            else:
                if floorCount == 1:
                    "The rug is patterned with stylized leaves and flowers. It's also green."
                    t "Love a classic pattern like that."
                    t "Classic pattern."
                t "You sure you'll be comfortable on the floor?"
                menu:
                    "{i}Stand up{/i}":
                        jump sitting
                    "Nah, I'll be fine here.":
                        t "Cool with me."
    
    "Tom goes to start making tea."
    t "I got some of this when I was in {color=#f00}Japan{/color} over the summer! And, maybe even cooler, I got these {i}containers{/i} for the loose leaf tea from {color=#0057AD}IKEA{/colors}."
    t "That's pretty much {color=#0057AD}Sweden{/colors}."
    $ hasTea = 0
    $ discussed = []
    jump conversation

    label conversation:
        
        if len(discussed) == 1 and hasTea == 0:
            t "Here's your tea! It may be a bit hot be careful!"
            "You got the {color=#ff0}Tea{/color}."
            $ hasTea = 1
        menu points:
            "So you play video games?" if 1 not in discussed:
                $ discussed.append(1)
                t "Well, duh, obviously Silksong. Skong. Sikong. Sog."
                t "I've been playing it a lot lately, but school can get in the way."
                t "What games do you like to play?"
                $ gamesDiscussed = []
                $ underTale = False
                menu games:
                    set gamesDiscussed
                    "Universal Paperclips":
                        $ tomDateValue += 0.5
                        t "I LOVE NOT USING CSS I LOVE NOT USING CSS I LOVE NOT USING CSS"
                        t "Absolute fire game."
                        t "\"In the end we all do what we must.\""
                        t "It's so crazy to meet somebody who I didn't recommend it to who's played it!"
                        t "That's awesome."
                        jump games
                    "Undertale":
                        $ tomDateValue += 0.5
                        $ underTale = True
                        t "That was like, the first game I ever played!"
                        t "Other than Minecraft, I suppose."
                        t "Have you played Deltarune yet?"
                        jump games
                    "Baba is You":
                        t "Another excellent pick."
                        t "The guy who made it... you know what other game he made?"
                        menu:
                            "Fez":
                                t "Nope!"
                            "Environmental Station Alpha":
                                $ tomDateValue += 0.25
                                t "Yeah! Love Arvi Teikari's work."
                            "Undertale":
                                $ tomDateValue -= 0.5
                                t "Well... not quite..."
                        jump games
                    "Silksong":
                        t "No yeah! I love it so much."
                        t "I'm surprised I'm not disappointed, it's hard to show up Hollow Knight."
                        t "Did you play Hollow Knight first?"
                        menu:
                            "Yes, of course.":
                                $ tomDateValue += 1
                                t "Very good, very good."
                            "Nope!":
                                $ tomDateValue -= 1
                                t "You gotta do that first! Very important!"
                    "Hollow Knight":
                        $ tomDateValue += 1
                        t "One of the first games I ever played! I have a very special relationship with this."
                        t "I originally played it on my shitty Mac desktop with the default Apple mouse and keyboard."
                        t "I loved it."
                        t "I also have almost 700 hours in it now lmao."
                        jump games
                    "Open Sorcery":
                        $ tomDateValue += 0.25
                        t "I just started playing that recently!  A friend of mine recommended it!"
                        t "It's pretty short but it's really good. We should have more text based games."
                        jump games
                    "Rust":
                        $ tomDateValue -= 1
                        t "I'm saying this for your own good, but you have to stop."
                        t "It's like cocaine. You engage with it, spend so much of your life and time..."
                        t "And when you sit up from your computer, the night growing cold, you realize you've accomplished nothing, {i}done{/i} nothing, for {i}hours{/i}."
                        t "Just... stop."
                        jump games
                    "Deltarune" if underTale:
                        $ tomDateValue += 0.25
                        t "I've just finished Chapter 3, Silksong's been keeping me from really getting into Chapter 4 but I'm real excited for it."
                        t "These {color=$ff0}birds{/color} are {color=$ff0}Pissing{/color me off..."
                        t "I'm the original         {color=$ff0}Starwalker{/color}"
                        jump games
                    "Rain World":
                        $ tomDateValue += 0.5
                        t "Woah! I swear we have so much in common here!"
                        t "I haven't gotten around to the Watcher DLC yet but I'm really excited too."
                        t "What's your favorite slugcat?"
                        menu:
                            "Monk":
                                t "Classic."
                            "Survivor":
                                t "The original experience. Love the lore."
                            "Hunter":
                                t "Yeah, nice."
                            "Gourmand":
                                t "BAHAHAHA he's so cute, man"
                            "Rivulet":
                                t "THAT CAMPAIGN! AGH! It's so damn good."
                            "Artificer":
                                t "Holy shit yeah, such a good story. Crushing ending though..."
                            "Spearmaster":
                                t "Yeah, they've got a really good design."
                            "Saint":
                                t "Such a wild campaign... yeah..."
                        jump games
                    "I love mobile games":
                        $ tomDateValue -= 1
                        t "Uh. Yeah. Sorry. Not what we're talking about."
                        jump games
                    "Noita":
                        $ tomDateValue += 0.25
                        t "I am so glad you've played that."
                        t "Good job."
                        jump games
                    "Hades":
                        t "Yeah, it's a pretty cool game."
                        jump games
                    "Disco Elysium":
                        t "I haven't got the chance to play it yet!"
                        t "Some of my former housemates have recommended it though."
                        jump games
                    "{i}Done talking about games{/i}":
                        jump conversation
            "So you play music?" if 2 not in discussed:
                $ discussed.append(2)
                t "I actually do!"
                t "I've played the piano for a while and I got this new instrument called a khaen recently so I'm going to try and learn that as well."
                menu:
                    "I play piano too!":
                        $ tomDateValue += 0.5
                        t "Oho! Maybe we could do a duet sometime!"
                        menu:
                            "I'd love that":
                                $ tomDateValue += 1
                                t "I would too, it's so rare one gets a good chance to do that."
                            "Maybe":
                                t "Just let me know!"
                            "NO! {i}growl!{/i}":
                                $ tomDateValue -= 1
                                t "AAAHHJJ!"
                                t "{i}deep breath{/i}"
                                t "I was is frighten."
                    "I play guitar!":
                        t "My dad plays guitar too! We sometimes have dueted \"Where is my Mind?\" by the Pixies."
                        t "Maybe we could do a duet sometime!"
                        menu:
                            "I'd love that":
                                $ tomDateValue += 1
                                t "I would too, it's so rare one gets a good chance to do that."
                            "Maybe":
                                t "Just let me know!"
                            "NO! {i}growl!{/i}":
                                $ tomDateValue -= 1
                                t "AAAHHJJ!"
                                t "{i}deep breath{/i}"
                                t "I was is frighten."
                    "I play a secret instrument.":
                        t "How marvelous. The world is full of so much mystery and potential beauty within it."
                jump conversation
            "I've been working on a project recently." if 3 not in discussed:
                $ discussed.append(3)
                t "Oh? Tell me about it?"
                menu:
                    "It's a writing piece.":
                        $ tomDateValue += 1
                        t "Oh nice! I write too! I'm actually an officer for the Poetry Club as well."
                        t "You should totally show up. ;)"
                        t "What do you mainly write?"
                        menu:
                            "Short stories.":
                                t "Same here! They're always good to be able to express a solid plotline or prompt."
                            "Poetry":
                                t "Same here! I got into it myself in high school. Check out E.E. Cummings."
                            "Novels":
                                t "Oh wow! I could never do that, my longest pieces are like... 40 pages. That's really cool, keep it up."
                        t "I'd love to see some of your writing sometime, if you'd be willing."
                        t "I know it's a personal thing though."
                        t "What do you write about?"
                        menu:
                            "Aliens":
                                t "GOD I been loving sci-fi recently! Please show it to me at some point!"
                                t "I read Three Body Problem a bit ago. Has to be one of my all time favorites."
                                t "Good luck on your work!"
                            "The wild":
                                t "Well, maybe this room can be a good inspiration, haha!"
                                t "Good luck on your work!"
                            "Complex emotions":
                                t "Oooooh I like that. Really delving into it."
                                t "It's tough to do right, but I believe in you!"
                                t "Good luck on your work!"
                            "Your mom":
                                $ tomDateValue -= 1.5
                                t "Hey! Rude!"
                                t "I thought you actually had a project!"
                                t "Pshhhh."
                    "It's a worldbuilding piece.":
                        t "Exciting, I've done a fair bit of that myself!"
                        $ tomDateValue += 1
                        menu:
                            "It's for a DnD game!":
                                t "I've been getting into DnD recently myself, I'm not terribly good at it yet thought."
                                t "My most recent character was a human fighter."
                                ""
                            "It's just a random little thing I've been working on in my spare time.":
                                t "I swear I'm always doing that too."
                                t "2 billion unfinished projects..."
                                t "So it goes!"
                        t "What's it about?"
                        menu:
                            "Aliens":
                                t "GOD I been loving sci-fi recently! Please show it to me at some point!"
                                t "I read Three Body Problem a bit ago. Has to be one of my all time favorites."
                                t "Good luck on your work!"
                            "The wild":
                                t "Well, maybe this room can be a good inspiration, haha!"
                                t "Good luck on your work!"
                            "Complex emotions":
                                t "Oooooh I like that. Really delving into it."
                                t "It's tough to do right, but I believe in you!"
                                t "Good luck on your work!"
                            "Your mom":
                                $ tomDateValue -= 1.5
                                t "Hey! Rude!"
                                t "I thought you actually had a project!"
                                t "Pshhhh."
                    "It's violent":
                        t "Uh... violent?"
                        menu:
                            "I'm building a gun.":
                                t "Uh.. why?"
                                menu:
                                    "I despise life.":
                                        $ tomDateValue -= 3
                                        t "..."
                                        t "That's..."
                                        t "Ok, well."
                                        t "Yeah, maybe. Uh. Don't."
                                    "It can't be good but you gotta do it. ({i}joke{/i})":
                                        "Tom pauses, then laughs a bit."
                                        t "You're weird."
                                        t "You're funny, but you're weird."
                            "{i}Stare ominously{/i}":
                                $ tomDateValue -= 1
                                t "Maybe we should, uh, perhaps talk about something else?"
                    "It's a secret.":
                        t "Secrets, secrets."
                        t "Fine, fine, fine."
                jump conversation
            "{i}Sip tea{/i}" if hasTea > 0 and len(discussed) < 3:
                if hasTea == 1:
                    "You sip the {color=#ff0}Tea{/color}."
                    $ hasTea += 1
                    t "How's it taste?"
                    menu:
                        "Fabulous!":
                            $ tomDateValue += 1
                            t "Sweet! Thank you!!"
                        "Disgusting!":
                            $ tomDateValue -= 1
                            t "Hey man! I tried my best!"
                elif hasTea < 7:
                    $ hasTea += 1
                    "You sip the {color=#ff0}Tea{/color} again."
                else:
                    "You sip the {color=#ff0}Tea{/color} a final time."
                    "You have used up the {color=#ff0}Tea{/color}."
                    "The remaining mug is but an empty shell, a spent vessel. It crumbles to dust in your hands."
                    $ hasTea = -1
                    t "Ah you finished it! Glad you liked it, or at least I assume?"
                    menu:
                        "Definitely":
                            t "Lovely!"
                            $ tomDateValue += 1
                        "Eh...":
                            t "You didn't have to drink it, you know."
                            $ tomDateValue -= 1
                jump conversation
        "Suddenly, you both hear a knocking on the door!"
        if hasTea > 0:
            "You set down your {color=#ff0}Tea{/color}" 

        "Tom pulls open the door. It's David!"
        t "Hi David! Fancy seeing you here."
        d "Oh hi, what's up?"
        t "You're the one who came here."
        d "Oh. Right. I thought we were doing our {color=$f0f}officer{/color} meeting today."
        t "I think I messaged it would be best to postpone. I've still got some work to do. Plus, I'm kinda busy right now."
        "David notices you."
        d "Oh hi!"
        t "I think you guys might've met at the last Game Dev Club meeting, yeah?"
        menu:
            "I have absolutely zero memory of this man.":
                t "Huh. I could've sworn you guys met. In fact, I will."
                t "Feck."
                t "Anyways, Y/N this is David, David this is Y/N"
                if tomDateValue > 6:
                    t "We've been having a lovely time here. :)"
                else:
                    t "We've been hanging out here for a bit."
            "Oh yeah! The hot and sexy and cool one!":
                t "Oh absolutely. Just look at him."
                d "I mean, you're seeing it."
            "Fuck you, David":
                t "Hey, what the heck."
                d "Hey, what'd I do!"
                d "{i}heh, i kinda like when they talk like that to me{/i}"
                t "..."
                t "Uh, anyways-"
                d "So. Ahem, what do you like to do?"
                menu:
                    "None of your damn business.":
                        d "{i}oh my god{/i}"
                        d "Hey, why don't we go... uh... grab boba?"
                        t "Hey wait-"
                        menu:
                            "Sure, ugh, fine.":
                                $ tomDateValue -= 1.5
                                t "You sure you don't want to stay here?"
                                menu:
                                    "I'm outta here":
                                        "You follow David out of the room, not looking back at all!"
                                        jump davidDate
                                    "Y'know, nevermind.":
                                        d "Aw, man."
                                        "Tom seems to relax a bit."
                            "I think I'd like to stay here.":
                                d "Well, maybe another time..."
                                d "{i}is my face red??{/i}"
                        t "It's, uh, been good to see you David."
                        t "See you at the {color=$f0f}officer{/color} meeting tomorrow?"
                        d "Yeah, sure. See you."
                        "David leaves the room."
                        jump endTomDate
                    "Video games":
                        d "Oh nice. I mean, you're in the club right?"
                        d "You should try gambling."
        t "Does tomorrow work fine for you for the meeting?"
        t "I think I'll be ready by then."
        d "Yeah, that should work. I should probably be getting back then, I've got so much work at this point."
        t "Hey, good to see you! Safe walk back!"
        d "Yeah! See you around!"
        "David leaves the room."
        jump endTomDate

    label endTomDate:
        "You stay over a bit longer."
        if hasTea == -1:
            "Tom makes you a second cup of tea."
        "You talk more about games and music and he shows you more of the room."
        if tomDateValue > 6:
            "You stay together until the sun finally manages to begin setting."
            "You both are deeply engaged in the conversation, until..."
            t "Oh my! I didn't realize how late it is! I have to make dinner!"
            t "You want to stay? I'm making curry."
            menu:
                "Totally!":
                    scene bg_tvroom
                    "You both head downstairs and cook together!"
                    "The curry turns out delicious and you both move to the couch and start watching a movie."
                    "Around intermission, Tom gets up and brings in some bowls of ice creams."
                    "As the movie continues..."
                    menu:
                        "{i}Put your arm around him{/i}":
                            "You put your arm around Tom's shoulder."
                            "He looks at you, blushes, and smiles."
                        "{i}Don't{/i}":
                            "Tom looks at you and smiles."
                    "You both scoot closer to each other, feeling cozy and warm and satisfied."
                    "Tom" "Hey, I really enjoyed today, I'd love to do this again if you'd like."
                    "He gives you a small hug."
                    "You got {color=#0ff}TOM GOOD ENDING{/color}."
                "I should probably go":
                    t "Well, this has been great!"
                    t "I'd love to have you over again and hang out more!"
                    t "Just uh, let me know?"
                    menu:
                        "Will do!":
                            t "Fantastic!"
                        "Maybe...":
                            t "Okay, that's chill."
                    t "See you later!"
                    "You leave."
                    "You got TOM NEUTRAL ENDING."
        elif tomDateValue < 0:
            "He seems to be getting pretty bored."
            t "Hey, well, I think you should probably start heading out. I've got a fair bit of work to do."
            t "Take care, ok?"
            menu:
                "When do you want to do this again?":
                    t "I, uh. Don't know when I'll next be free."
                    t "Probably not soon."
                "Ok.":
                    "Tom nods."
            
            t "Bye."
            "He closes the door and you hear him breathe a sigh of relief from behind it."
            "You leave."
            "You got {color=#f00}TOM BAD ENDING{/color}."
            return
        else:
            t "Hey, I've got to get to making dinner now but this has been pretty good!"
            t "I'd like to have you over again and hang out more!"
            t "Just uh, let me know?"
            menu:
                "Will do!":
                    t "Fantastic!"
                "Maybe...":
                    t "Okay, that's chill."
            t "See you later!"
            "You leave."
            "You got TOM NEUTRAL ENDING."
                    

label secretDate:
    scene bg_reactor
