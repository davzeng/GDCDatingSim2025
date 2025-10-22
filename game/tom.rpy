image bg_view:
    "bg_view.png"
    xysize(1920, 1080)
image bg_plants:
    "bg_plants.png"
    xysize(1920, 1080)
image bg_reactor:
    "bg_reactor.png"
    xysize(1920, 1080)

label tomIntro:
    "Tom" "Hellooo!"
    $ visited = []
    $ askedGoals = False
    $ askedShortTerm = False;
    menu tomIntro1:
        set visited
        "Who are you.":
            "Tom" "Pretty sure I’m Tom. Or something similar to that. I’m an {color=#f0f}officer{/color} of the game development club for what it’s worth."
            "Tom" "In my spare time I guess I play the piano and grow plants. I have something like 2 billion of those. Plants, not pianos."
            "Tom" "One day,  I’m 20 percent certain, I’ll find some way to fuse myself, my plants, and an analog/digital interface and enter my penultimate form."
            "Tom" "It can't be good, but I've gotta do it."
            "Tom" "I spend the other 80 percent of my certainty on being certain on other things."
        "What are you.":
            "Tom" "Most people think I’m human, whatever that is."
            "Tom" "They're generally right."
            jump tomIntro1
        "Why are you.":
            "Tom" "Well, if we’re being purely by cause-and-effect I am because 2 decades or so ago I was born in a hospital in Portland. Y’know. Standard and all, so I’m told. You just had to be there."
            "Tom" "Now, you could say that’s why I {i}was{/i}, but why I am {i}now{/i} is a different matter. Time has passed."
            "Tom" "And to that I’d answer I am because I have taken actions that have resulted in my remaining alive until this point."
            "Tom" "And the {i}why{/i} as to why I’ve taken those actions is because I intend to live."
            "Tom" "And the {i}why{/i} as to that is because I wish to, y’know, complete my goals in life or whatever."
            "Tom" "You could also just say I am because I think, or something."
            $ askedGoals = True
            jump tomIntro1
        "What are your goals." if askedGoals:
            "Tom" "Personal question so soon! Wow! What a specimen! Look at you!"
            "Tom" "Y’know, I guess the main thing is I just aspire to be a beneficial part of the world. Be the best person I can, be good to others."
            "Tom" "Beyond that? I’d say I want to find somebody to spend my life with. Have a house, garden, maybe a family. Do something with my career that improves the world."
            "Tom" "Short term goals though? Don’t really know, if I’m being honest..."
            "Tom" "What are yours?"
            menu:
                "I want to be an astronaut and shoot myself into space and leave Earth forever.":
                    "Tom" "That's pretty bold! But I can definitely respect that."
                    "Tom" "I believe in you. Shoot for the moon, miss, and land somewhere among stars you don’t know."
                    "Tom" "Tell the aliens I say hi ;)"
                "I want to get into a passionate and deep relationship with you.":
                    "Tom" "Oh! Wow! Uh."
                    "Tom" "Forward, aren't you?"
                    "Tom" "Well, you’ll just have to get to know me first. You can do that, can’t you?"
                "I want to eventually retreat into the Himalayas and discover the answer to end human suffering.":
                    "Tom" "Dude. Fire."
                    "Tom" "I respect that, let me know what I can do to help you with that."
                    "Tom" "Oh, and let me know if you find it out. The answer to it all, that is."
                "Do you really not have any short term goals?" if secretStep1:
                    $ askedShortTerm = True
                    "Tom" "Well... I, uh..."
                    "David" "Hey guys! How's the bingo sheets going?"
                    "David" "I've almost got mine filled all the way out!"
                    "David" "God, I can't wait to finish this meeting and get back to ZhuoZhi..."
                    "David" "Alas."
                    "David" "Good luck, you guys!"
                    "Tom" "Anyways, uh..."
            jump tomIntro1
        
    "Tom" "But yeah, I’ve been a {color=#f0f}game development officer{/color} for years now. I’m the head of our Reclamation, Advancement, and Technology division."
    "Tom" "The RAT division."
    "Tom" "I don’t even know how long I've been here... or how long there is left..."
    "Tom" "..."
    "Tom" "You have a bingo sheet, right? Let me take a look."
    "You give Tom the {color=#ff0}Bingo Sheet{/color}."
    "Tom" "Hmm ok."
    "Tom" "Yeah, I can fill out \"Knows the alchemical elements and how to use them\". Here you go!"
    "You got the {color=#ff0}Bingo Sheet{/color}."
    "Tom" "Can you fill something out on mine as well?"
    "You got the {color=#ff0}Tom's Bingo Sheet{/color}."
    menu:
        "{i}Fill out \"Owns a pre-1900s gaming console\".{/i}":
            "Tom" "Ah yes. The fabled Untendo 1.5 Cube. My great-great-grandfather loved to play {i}Kill and Eat: Peter’s Origins{/i} on that old iron box."
            "Tom" "You play anything on it?"
            menu:
                "{i}Train Wreck 5: The Wreckoning Comes to Crush, TX.{/i}":
                    "Tom" "Total locomotive classic. Good choice."
                "{i}Anachronism IV, Enter the Digital Age{/i}":
                    "Tom" "Mind-bending, that one's fucked up. Awesome"
                "{i}A Treatise on the Cultivation of Various Cereal Crops and their Usages in Feeding Livestock{/i}":
                    "Tom" "Ah, love a good cozy game."
            "You give Tom the {color=#ff0}Tom's Bingo Sheet{/color}."
            "Tom" "Thanks for that!"
        "{i}Fill out \"Has grown a plant to completion (any ending)\".{/i}":
            "You give Tom the {color=#ff0}Tom's Bingo Sheet{/color}."
            "Tom" "Ah sick!"
            "Tom" "Been trying to do that for years. Well, true ending completion, that is."
            "Tom" "I got first ending a while ago. Thank you!"
        "{i}Fill out \"Sleeps in real life AND in game\".{/i}":
            "You give Tom the {color=#ff0}Tom's Bingo Sheet{/color}."
            "Tom" "Oh wow! We really do have a lot in common don’t we?"
            "Tom" "Maybe we could, uh, put our Minecraft beds on adjacent blocks... if you wouldn’t mind..."
            "Tom" "..."
            "Tom" "Uh... thanks for the bingo!"
        "{i}Fill out \"Knows you're up to something\".{/i}" if askedShortTerm:
            "You give Tom the {color=#ff0}Tom's Bingo Sheet{/color}."
            "Tom" "Oh."
            "Tom" "Uh."
            "Tom" "Cool! Thanks, I was {i}trying{/i} to get that one filled out!"
            "Tom" "See you... around?"
            $ secretStep2 = True
            jump chooseOfficerIntro
    
    "Tom" "Hey, if you want to hang out later I think that’d be great."
    "Tom" "I’ve got a new tea set and just got some new loose leaf tea imported from {color=#0f0}Greenpath{/color}."
    "Tom" "You’re more than welcome to come by my place this weekend; we could play some video games, have some tea, and I could show off my plant collection!"
    "Tom" "Just let me know! ;)"

    jump chooseOfficerIntro

label tomDate:
    scene bg_view
    $ tomDateValue = 0
    "Tom" "Oh wow, it's pretty nice up here right now."
    "Tom" "..."
    "Tom" "You wanna stay here for a bit or head inside?"
    menu:
        "Let's stay here for a bit.":
            $ tomDateValue += 1
            "Tom" "Yeah, I agree. It's nice."
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
                    "Tom" "Here we go :)"
                "{i}Don't{/i}":
                    "You stand up. Tom pretends as if he was reaching for something on the ground."
            "Tom" "Shall we head inside?"
            menu:
                "Ugh sure.":
                    $ tomDateValue -= 1
                    "Tom stares at you for a second."
                    "Tom" "Uh, ok, let's go."
                "Let's do it.":
                    "Sweet, c'mon in."
        "Let's go inside.":
            "Tom" "Sure, you're right, it's a bit cold out right now."
    
    "Tom leads you inside from the fire escape, through another person's bedroom, a hallway, and finally into his own room."
    scene bg_plants
    "Tom" "What do you think?"
    "Tom" "The room was a bit of a mess so I put of holographic projections of what it's meant to look like."
    menu:
        "Oh, this is cool asf.":
            $ tomDateValue += 1
            "Tom" "Hell yeah, thanks!"
            "Tom" "Sometimes I turn on all the projectors to display random lights and numbers and stuff."
            "Tom" "Reminds me of something in one of my favorite games."
        "This is nice!":
            "Tom" "Yeah, thanks! Sometimes I turn on all the projectors to display random lights and numbers and stuff."
        "Your room was a mess?":
            $ tomDateValue -= 1
            "Tom" "Hey dude, I'm working on it!"
    
    if tomDateValue < 3:
        "Tom" "Here, make yourself comfortable."
    else:
        "Tom" "Here, make yourself comfortable, my house is your house!"
    $ floorCount = 0
    menu sitting:
        "{i}Sit on the bed{/i}":
            "You sit on the bed. It creaks a bit as you sit."
            "It's green, like most things in his room."
            "Tom" "I like this bed a lot since it's got a bookshelf at the headboard!"
            "Tom" "Sadly, it's a bit old and squeaky though!"
            menu:
                "That's all cool! I like the books!":
                    "Tom" "Thanks! I try to keep all my favorites there."
                "{i}Nod contentedly{/i}":
                    "Tom nods back. :)"
                "Oh no... the squeakiness might be an issue...":
                    "Tom" "Uh, why's that..?"
                    menu:
                        "{i}Shrug{/i}":
                            "Tom" "Eh yeah, it's fine."
                        ";)":
                            "Tom blushes."
                            $ tomDateValue += 1
                            "Tom" "Oh.. I.. uh.. :)"
                            "Tom" "I'm sure it'd be fine."
        "{i}Sit on the chair{/i}":
            "Tom" "Mmm the gamer chair."
            "Tom" "It's actually one that my dad, uh, took from his work. Which means it's..."
            "Tom" "...really comfortable."
            "Tom" "My posture is still shit though."
            "Tom" "You play any games?"
            menu:
                "Nah, not really.":
                    "Tom" "What, uh, what made you come to Game Dev Club then?"
                    menu:
                        "{i}Stare{/i}":
                            $ tomDateValue -= 1
                            "Tom" "Uh."
                        "{i}Jump up and down rapidly!!!{/i}":
                            "Tom slowly nods."
                            "Tom" "Yeah! yeah! Great!"
                "From time to time, yeah!":
                    "Tom" "Nice!"
                    "Tom" "Here, one sec, let me get the tea."
                "SKONG IS REAL.":
                    $ tomDateValue += 1
                    "Tom" "{b}YESSSSSSSSSS!!{/b}"
                    "Tom" "Dude it's so good man I love it."
                    "Tom" "I can't believe it's actually, like, a thing."
                    "Tom" "The coming of the messiah."
                    "Tom" "Here, lemme go get the tea then we can continue!"
        "{i}Sit on the rug{/i}":
            $ floorCount += 1
            if floorCount > 5:
                "Tom" "Whatever, man."
            else:
                if floorCount == 1:
                    "The rug is patterned with stylized leaves and flowers. It's also green."
                    "Tom" "Love a classic pattern like that."
                    "Tom" "Classic pattern."
                "Tom" "You sure you'll be comfortable on the floor?"
                menu:
                    "{i}Stand up{/i}":
                        jump sitting
                    "Nah, I'll be fine here.":
                        "Tom" "Cool with me."
    
    "Tom goes to start making tea."
    "Tom" "I got some of this when I was in {color=#f00}Japan{/color} over the summer! And, maybe even cooler, I got these {i}containers{/i} for the loose leaf tea from {color=#0057AD}IKEA{/colors}."
    "Tom" "That's pretty much {color=#0057AD}Sweden{/colors}."
    $ hasTea = 0
    $ discussed = []
    jump conversation

    label conversation:
        
        if len(discussed) == 1 and hasTea == 0:
            "Tom" "Here's your tea! It may be a bit hot be careful!"
            "You got the {color=#ff0}Tea{/color}."
            $ hasTea = 1
        menu points:
            "So you play video games?" if 1 not in discussed:
                $ discussed.append(1)
                "Tom" "Well, duh, obviously Silksong. Skong. Sikong. Sog."
                "Tom" "I've been playing it a lot lately, but school can get in the way."
                "Tom" "What games do you like to play?"
                $ gamesDiscussed = []
                $ underTale = False
                menu games:
                    set gamesDiscussed
                    "Silksong":
                        "Tom" "No yeah! I love it so much."
                        "Tom" "I'm surprised I'm not disappointed, it's hard to show up Hollow Knight."
                        "Tom" "Did you play Hollow Knight first?"
                        menu:
                            "Yes, of course.":
                                $ tomDateValue += 1
                                "Tom" "Very good, very good."
                            "Nope!":
                                $ tomDateValue -= 1
                                "Tom" "You gotta do that first! Very important!"
                    "Hollow Knight":
                        $ tomDateValue += 1
                        "Tom" "One of the first games I ever played! I have a very special relationship with this."
                        "Tom" "I originally played it on my shitty Mac desktop with the default Apple mouse and keyboard."
                        "Tom" "I loved it."
                        "Tom" "I also have almost 700 hours in it now lmao."
                        jump games
                    "Open Sorcery":
                        $ tomDateValue += 0.25
                        "Tom" "I just started playing that recently!  A friend of mine recommended it!"
                        "Tom" "It's pretty short but it's really good. We should have more text based games."
                        jump games
                    "Rust":
                        $ tomDateValue -= 1
                        "Tom" "I'm saying this for your own good, but you have to stop."
                        "Tom" "It's like cocaine. You engage with it, spend so much of your life and time..."
                        "Tom" "And when you sit up from your computer, the night growing cold, you realize you've accomplished nothing, {i}done{/i} nothing, for {i}hours{/i}."
                        "Tom" "Just... stop."
                        jump games
                    "Undertale":
                        $ tomDateValue += 0.5
                        $ underTale = True
                        "Tom" "That was like, the first game I ever played!"
                        "Tom" "Other than Minecraft, I suppose."
                        "Tom" "Have you played Deltarune yet?"
                        jump games
                    "Deltarune" if underTale:
                        $ tomDateValue += 0.25
                        "Tom" "I've just finished Chapter 3, Silksong's been keeping me from really getting into Chapter 4 but I'm real excited for it."
                        "Tom" "These {color=$ff0}birds{/color} are {color=$ff0}Pissing{/color me off..."
                        "Tom" "I'm the original         {color=$ff0}Starwalker{/color}"
                        jump games
                    "Universal Paperclips":
                        $ tomDateValue += 0.5
                        "Tom" "I LOVE NOT USING CSS I LOVE NOT USING CSS I LOVE NOT USING CSS"
                        "Tom" "Absolute fire game."
                        "Tom" "\"In the end we all do what we must.\""
                        "Tom" "It's so crazy to meet somebody who I didn't recommend it to who's played it!"
                        "Tom" "That's awesome."
                        jump games
                    "Rain World":
                        $ tomDateValue += 0.5
                        "Tom" "Woah! I swear we have so much in common here!"
                        "Tom" "I haven't gotten around to the Watcher DLC yet but I'm really excited too."
                        "Tom" "What's your favorite slugcat?"
                        menu:
                            "Monk":
                                "Tom" "Classic."
                            "Survivor":
                                "Tom" "The original experience. Love the lore."
                            "Hunter":
                                "Tom" "Yeah, nice."
                            "Gourmand":
                                "Tom" "BAHAHAHA he's so cute, man"
                            "Rivulet":
                                "Tom" "THAT CAMPAIGN! AGH! It's so damn good."
                            "Artificer":
                                "Tom" "Holy shit yeah, such a good story. Crushing ending though..."
                            "Spearmaster":
                                "Tom" "Yeah, they've got a really good design"
                            "Saint":
                                "Tom" "Such a wild campaign... yeah..."
                        jump games
                    "I love mobile games":
                        $ tomDateValue -= 1
                        "Tom" "Uh. Yeah. Sorry. Not what we're talking about."
                        jump games
                    "Noita":
                        $ tomDateValue += 0.25
                        "Tom" "I am so glad you've played that."
                        "Tom" "Good job."
                        jump games
                    "Baba is You":
                        "Tom" "Another excellent pick."
                        "Tom" "The guy who made it... you know what other game he made?"
                        menu:
                            "Fez":
                                "Tom" "Nope!"
                            "Environmental Station Alpha":
                                $ tomDateValue += 0.25
                                "Tom" "Yeah! Love Arvi Teikari's work."
                            "Undertale":
                                $ tomDateValue -= 0.5
                                "Tom" "Well... not quite..."
                        jump games
                    "Hades":
                        "Tom" "Yeah, it's a pretty cool game."
                        jump games
                    "Disco Elysium":
                        "Tom" "I haven't got the chance to play it yet!"
                        "Tom" "Some of my former housemates have recommended it though."
                        jump games
                    "{i}Done talking about games{/i}":
                        jump conversation
            "So you play music?" if 2 not in discussed:
                $ discussed.append(2)
                "Tom" "I actually do!"
                "Tom" "I've played the piano for a while and I got this new instrument called a khaen recently so I'm going to try and learn that as well."
                menu:
                    "I play piano too!":
                        $ tomDateValue += 0.5
                        "Tom" "Oho! Maybe we could do a duet sometime!"
                        menu:
                            "I'd love that":
                                $ tomDateValue += 1
                                "Tom" "I would too, it's so rare one gets a good chance to do that."
                            "Maybe":
                                "Tom" "Just let me know!"
                            "NO! {i}growl!{/i}":
                                $ tomDateValue -= 1
                                "Tom" "AAAHHJJ!"
                                "Tom" "{i}deep breath{/i}"
                                "Tom" "I was is frighten."
                    "I play guitar!":
                        "Tom" "My dad plays guitar too! We sometimes have dueted \"Where is my Mind?\" by the Pixies."
                        "Tom" "Maybe we could do a duet sometime!"
                        menu:
                            "I'd love that":
                                $ tomDateValue += 1
                                "Tom" "I would too, it's so rare one gets a good chance to do that."
                            "Maybe":
                                "Tom" "Just let me know!"
                            "NO! {i}growl!{/i}":
                                $ tomDateValue -= 1
                                "Tom" "AAAHHJJ!"
                                "Tom" "{i}deep breath{/i}"
                                "Tom" "I was is frighten."
                    "I play a secret instrument.":
                        "Tom" "How marvelous. The world is full of so much mystery and potential beauty within it."
                jump conversation
            "I've been working on a project recently." if 3 not in discussed:
                $ discussed.append(3)
                "Tom" "Oh? Tell me about it?"
                menu:
                    "It's a writing piece.":
                        $ tomDateValue += 1
                        "Tom" "Oh nice! I write too! I'm actually an officer for the Poetry Club as well."
                        "Tom" "You should totally show up. ;)"
                        "Tom" "What do you mainly write?"
                        menu:
                            "Short stories.":
                                "Tom" "Same here! They're always good to be able to express a solid plotline or prompt."
                            "Poetry":
                                "Tom" "Same here! I got into it myself in high school. Check out E.E. Cummings."
                            "Novels":
                                "Tom" "Oh wow! I could never do that, my longest pieces are like... 40 pages. That's really cool, keep it up."
                        "Tom" "I'd love to see some of your writing sometime, if you'd be willing."
                        "Tom" "I know it's a personal thing though."
                        "Tom" "What do you write about?"
                        menu:
                            "Aliens":
                                "Tom" "GOD I been loving sci-fi recently! Please show it to me at some point!"
                                "Tom" "I read Three Body Problem a bit ago. Has to be one of my all time favorites."
                                "Tom" "Good luck on your work!"
                            "The wild":
                                "Tom" "Well, maybe this room can be a good inspiration, haha!"
                                "Tom" "Good luck on your work!"
                            "Complex emotions":
                                "Tom" "Oooooh I like that. Really delving into it."
                                "Tom" "It's tough to do right, but I believe in you!"
                                "Tom" "Good luck on your work!"
                            "Your mom":
                                $ tomDateValue -= 1.5
                                "Tom" "Hey! Rude!"
                                "Tom" "I thought you actually had a project!"
                                "Tom" "Pshhhh."
                    "It's a worldbuilding piece.":
                        "Tom" "Exciting, I've done a fair bit of that myself!"
                        $ tomDateValue += 1
                        menu:
                            "It's for a DnD game!":
                                "Tom" "I've been getting into DnD recently myself, I'm not terribly good at it yet thought."
                                "Tom" "My most recent character was a human fighter."
                                ""
                            "It's just a random little thing I've been working on in my spare time.":
                                "Tom" "I swear I'm always doing that too."
                                "Tom" "2 billion unfinished projects..."
                                "Tom" "So it goes!"
                        "Tom" "What's it about?"
                        menu:
                            "Aliens":
                                "Tom" "GOD I been loving sci-fi recently! Please show it to me at some point!"
                                "Tom" "I read Three Body Problem a bit ago. Has to be one of my all time favorites."
                                "Tom" "Good luck on your work!"
                            "The wild":
                                "Tom" "Well, maybe this room can be a good inspiration, haha!"
                                "Tom" "Good luck on your work!"
                            "Complex emotions":
                                "Tom" "Oooooh I like that. Really delving into it."
                                "Tom" "It's tough to do right, but I believe in you!"
                                "Tom" "Good luck on your work!"
                            "Your mom":
                                $ tomDateValue -= 1.5
                                "Tom" "Hey! Rude!"
                                "Tom" "I thought you actually had a project!"
                                "Tom" "Pshhhh."
                    "It's violent":
                        "Tom" "Uh... violent?"
                        menu:
                            "I'm building a gun.":
                                "Tom" "Uh.. why?"
                                menu:
                                    "I despise life.":
                                        $ tomDateValue -= 3
                                        "Tom" "..."
                                        "Tom" "That's..."
                                        "Tom" "Ok, well."
                                        "Tom" "Yeah, maybe. Uh. Don't."
                                    "It can't be good but you gotta do it. (joke)":
                                        "Tom pauses, then laughs a bit."
                                        "Tom" "You're weird."
                                        "Tom" "You're funny, but you're weird."
                            "{i}Stare ominously{/i}":
                                $ tomDateValue -= 1
                                "Tom" "Maybe we should, uh, perhaps talk about something else?"
                    "It's a secret.":
                        "Tom" "Secrets, secrets."
                        "Tom" "Fine, fine, fine."
                jump conversation
            "{i}Sip tea{/i}" if hasTea > 0 and len(discussed) < 3:
                if hasTea == 1:
                    "You sip the {color=#ff0}Tea{/color}."
                    $ hasTea += 1
                    "Tom" "How's it taste?"
                    menu:
                        "Fabulous!":
                            $ tomDateValue += 1
                            "Tom" "Sweet! Thank you!!"
                        "Disgusting!":
                            $ tomDateValue -= 1
                            "Tom" "Hey man! I tried my best!"
                elif hasTea < 7:
                    $ hasTea += 1
                    "You sip the {color=#ff0}Tea{/color} again."
                else:
                    "You sip the {color=#ff0}Tea{/color} a final time."
                    "You have used up the {color=#ff0}Tea{/color}."
                    "The remaining mug is but an empty shell, a spent vessel. It crumbles to dust in your hands."
                    $ hasTea = -1
                    "Tom" "Ah you finished it! Glad you liked it, or at least I assume?"
                    menu:
                        "Definitely":
                            "Tom" "Lovely!"
                            $ tomDateValue += 1
                        "Eh...":
                            "Tom" "You didn't have to drink it, you know."
                            $ tomDateValue -= 1
                jump conversation
        "Suddenly, you both hear a knocking on the door!"
        if hasTea > 0:
            "You set down your {color=#ff0}Tea{/color}" 

        "Tom pulls open the door. It's David!"
        




label secretDate:
