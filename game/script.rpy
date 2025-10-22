# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Y/N")
define secretStep1 = False
define secretStep2 = False
define officerDate = 0

# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    p "I'm late! I'm late!"

    "The words echo in your head as you run across the hall."

    "You've been looking forward to the first meeting of the Game Development Club for a week now."

    "How you overslept today is beyond you."

    "You make it to the end of the hall and throw the door open."

    menu:
        "H-hey, I'm sorry I'm late to club...":

            "David" "It's all good. Welcome in!"

        "H-hey, is this the Game Dev club?":

            "Sydney" "Yeah! Come in, we've just started."

        "Oh, so this is be the Game Dev Club.":

            "Tom" "Yes, that's us!"
    
    "Tom" "Welcome in, welcome in!"

    "Sebastian" "We make games here!"

    "Ande" "Oh hey, you new to the club?"

    menu:
        "No, I'm a game development veteran.":

            "David"  "I, uh, I don't think I've seen you here before."
            "David" "Is your head ok?"
            "David" "Come in anyways, I suppose."

        "Y-yeah, this is my first time here.":
            
            "Anthony" "Ah great! New members are always fabulous."

        "Actually, I...{nw}":

            "Tom" "Well great! I just finished coding another {i}beautiful{/i} game in {color=#ff0}JavaScript{/color}."
            "Tom" "I promise I'm ok, mentally."
            "Tom" "Anyways."

    "Tom" "We meet on {color=#ff0}Wednesdays at 5:00{/color} each week!"
    "Tom" "A lot of people here have made games before but a lot of people here are new to it."
    "Tom" "Like you might be, yeah?"
    "Sydney" "We try to keep the club super beginner friendly! :D"
    "Sydney" "We’ll have meetings on, say, art or music or..."
    "Ande" "{b}OR PROGRAMMING!{/b}"
    "Sydney" "...and right now we're{fast} doing a bit of an icebreaker activity!"
    "Sebastian" "Here's a bingo sheet, try to fill it out as best as you can. ;)"

    "Sebastian handed you the {color=#ff0}Bingo Sheet{/color}."

    menu:
        "Inspect sheet":
            "The sheet is a bit wrinkled and each square has a game-development-themed requirement. The title says \"AWESOME BINGO\" in a futuristic font."
            "Many of the requirements seem abjectly impossible."
            "You decide to try and fill out the top row, which seems like one of the few achievable bingos."
            jump chooseOfficerIntro
        "Move into the crowd":
            jump chooseOfficerIntro
    label chooseOfficerIntro:
        default visitedOfficer = []
        default officersVisited = 0
        menu:
            set visitedOfficer
            "Approach Anthony":
                $ officersVisited += 1
                "Anthony" "Hello! Welcome to the club!"
                label anthonyIntroLoop:
                    menu:
                        "...hi!":
                            "Anthony" "...Hello!"
                            jump anthonyIntroLoop
                        "Can you mark something on my bingo sheet?":
                            jump anthonyIntro
            "Approach Tom":
                $ officersVisited += 1
                jump tomIntro
            "Approach Sydney":
                $ officersVisited += 1
                jump sydneyIntro
            "Approach Ande":
                $ officersVisited += 1
                jump andeIntro
            "Approach David":
                $ officersVisited += 1
                jump davidIntro
            "Approach Sebastian":
                $ officersVisited += 1
                jump sebastianIntro
            "Looks like I have a bingo" if officersVisited == 6:
                jump endIntro

    label anthonyIntro:
        "Anthony" "O-oh! You want {i}me{/i} to look at your sheet?"
        "Anthony" "Let's see... I could do this one... or that one... or maybe..."
        "Anthony" "Does Scratch count as a coding language?"
        "Anthony" "We can only check off one box, though, right? We gotta choose the best one."
        "Anthony" "Tom could probably do that coding one, and I think David also writes. But you probably want to save David for the {color=#f00}waifu{/color} box."
        "Anthony" "But what if..."
        menu anthonyIntro1: 
            "...":
                "Anthony" "Hmmmm..."
                jump anthonyIntro1
            "Just pick one!":
                "Anthony" "Do you want to be {i}sub-optimal{/i}?! Or do you want to {i}win{/i} this bingo?"
                "Anthony" "That's what I thought."
                "Anthony" "Now just give me a few more minutes to figure this out. Or maybe hours. I’ll make sure you have the {color=#f00}MAXIMUM{/color} chance of completing this bingo board!"
                "Anthony" "Wait ... \"maximum\" ... \"bingo\" ... \"figure\" ... I’ve got an idea!"
            "What if we narrowed it down?":
                "Anthony" "Hmm, restrict the solution space? I like the way you think!"
                "Anthony" "Wait ... \"solution\" ... \"think\" ... I’ve got an idea!"
            "Talk to another officer":
                "Anthony" "Woah woah woah where are you going?"
                "Anthony" "This problem needs to be solved! So we—yes, we—are going to sit here until we figure this out!"
                "Anthony" "Wait ... \"going\" ... \"problem\" ... “sit” ... I’ve got an idea!"
        
        "Anthony" "Do you have a pen or pencil or something? I also need some paper—wait, I can use the back of the bingo board!"
        "Anthony" "Now we just put all possible bingo configurations on a state diagram, estimate the transition probabilities, run some graph traversal..."
        "Anthony" "{cps=80}...compute the Laplacian, and...{p}...wait is that a zero or an \"O\"...?{p}...drop the seven, carry the two, and...{/cps}"
        "Anthony" "There we go! The optimal bingo box is simply the solution to this 25-degree polynomial!"
        "Anthony" "Yeah, I don’t know how to solve this."
        "Anthony" "And so much time has passed! I’ll just check the \"Been to Game Dev Club before\" box."
        "Anthony" "But that was a lot of fun! We should talk more if you have any other problems you want solved!"
        "Anthony" "Or not solved."
        "Anthony" "Regardless!"
        jump chooseOfficerIntro

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
                "Tom" "Now, you could say that’s why I {i}was{/i}, but why I am *now* is a different matter. Time has passed."
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
            
        "Tom" "But yeah, I’ve been a {color=#f0f}game development officer{/color} for years now. I’m the head of our Reclamation, advancement, and Technology division."
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

    label sydneyIntro:
        "Sydney" "Oh hi! I'm Sydney! Nice to meet you :) {i}meow{/i}"
        menu:
            "Meow?":
                "Sydney" "Oh yeah. You know. Meow meow?"
            "{i}Mrrrrrrrrr mmraa! Memeow?{/i}":
                "Sydney" "{i}Meowmeowmeowmeow meowmeow meowmeow meeeooooowwww~{/i}"
            "Uhh.. yeah it's nice to meet you too.":
                "Sydney" "Uh yeah."

        "Sydney" "So yeah you've got a bingo sheet right? Let's see..."
        "Sydney" "\"Thinks fruits and vegetables came from {i}Stardew Valley{/i}\" uhh..."
        "Sydney" "OMG yeah once I went to the state fair and was {color=#f00}SHOCKED{/color} to see pumpkins in real life."
        "Sydney" "I can’t believe they’d so shamelessly rip off Stardew like that!"
        "Sydney" "They made it so you can even grow giant pumpkins too? What the fart..."
        menu:
            "Real life came first. Then {i}Stardew Valley{/i}.":
                "Sydney" "{b}YOU TAKE THAT BACK!!!{/b}"
                "Sydney" "..."
                "Sydney" "Sorry, what I meant to say was... erm... you’re wrong. Yup! ;D"
            "And they had the audacity to take cauliflower too!":
                "Sydney" "I know right! You get it."
            "...":
                "Sydney" "Don’t give me that face, you know I’m right."
        
        "Well, good chatting with you! If you ever want to hang out let's do that! Sydney OUT!"
        jump chooseOfficerIntro

    label andeIntro:
        "Ande" "Hey..."
        $ visited = []
        menu andeIntro1:
            set visited
            "Hola!":
                "Ande" "Sorry, I don't speak {color=#f00}Japanese{/color}..."
                jump andeIntro1
            "Hey, I need my bingo filled out!":
                "Ande" "Yeah, I gotchu."
            "You sound nice...":
                "Ande" "Thanks, I get that a lot."
                "Ande" "Well, not a lot, but sometimes."
                "Ande" "Well, never, but thank you!"
                "Ande" "Anyways, lemme fill out your bingo!"
            "hey...":
                "Ande" "Hey..."
                jump andeIntro1

        "Ande" "Lemme take a look..."
        menu:
            "tuff.":
                "You give Ande the {color=#ff0}Bingo Sheet{/color}."

        "Ande" "Hmmmmmm..."
        "Ande" "...nothing about markiplier onlyfans is on here..."
        "Ande" "...nothing about ranked roblox gooning..."
        "Ande" "...nothing about {color=#ff0}pheromone-maxxing{/color} either..."
        "Ande" "{i}Who made this?!{/i}"
        "Ande" "Fine. I'll fill this one out!"
        "Ande draws a box on your Bingo Sheet outside of the grid, creating a row of 6, and fills it in."
        "You got the {color=#ff0}Bingo Sheet{/color}."
        "Ande" "By the way, do you play Roblox?"
        menu:
            "I love {i}cart ride into 17 pregnant hyenas{/i}!":
                "Ande" "Nice. I love {i}cart ride into 17 pregnant hyenas{/i} too. Roblox is really great!"
            "No...":
                "Ande" "Well, you should try it out sometime!"
            "You are weird.":
                "Ande" "...buddy, have you SEEN the other officers?"

        "Ande" "Well, thank you for showing up to the game development club! In fact, I wouldn't mind if you showed up to my class tomorrow. I lost my Roblox gaming buddy last time..."
        menu:
            "Thanks! I'll think about it!":
                "Ande" "See you there! I'll reserve a seat!"
            "I don't know if that's allowed.":
                "Ande" "Uhh..."
                menu:
                    "Thanks! I'll think about it!":
                        "Ande" "See you there! I'll reserve a seat!"
        jump chooseOfficerIntro

    label davidIntro:
        "David" "Yo. We haven’t filled out each other’s bingos have we?"
        menu:
            "No, we have not.":
                "David" "Well, what are you waiting for then?"
                "David" "Your paper. Hand it over."
                "You give David the {color=#ff0}Bingo Sheet{/color}."
            "Fill out my sheet already, bitch":
                "David" "You!!!"
                "David" "You would dare talk to an {color=#f0f}officer{/color} like that?"
                "David" "{i}hehe... I hope they shit talk me more.{/i}"
                "David" "Ahem."
        "David" "I’m David, head of the game dev club’s intelligence division."
        "David" "I like to play gacha games. Lots of gacha games."
        "David" "My favorite character is ZhuoZhi. I spent $2000 dollars maxing her out."
        "David" "{cps=80}But I’d pay double the amount of money for her to tie me down and{/cps}"
        "David" "..."
        "David" "Ahem."
        "David" "Sorry about that."
        "David" "Someday, I’m going to make my own gacha game and max out all the characters for myself."
        "David" "Here, let me fill out your bingo."
        "David fills out \"Has spent at least $1000 on a video game\"."
        "You got the {color=#ff0}Bingo Sheet{/color}."
        "David" "By the way, do you like boba?"
        "David" "If you do..?{w} I wouldn’t mind grabbing a drink with you tommorrow..."
        jump chooseOfficerIntro

    label sebastianIntro:
        "Sebastian" "Uh, hi."
        menu:
            "Hello, I need your help filling out my bingo sheet!":
                "Sebastian" "Uh, yeah sure."
                "You give Sebastian the {color=#ff0}Bingo Sheet{/color}."
        "Sebastian" "Oh, yeah I do sing the {i}Super Smash Bros.{/i} intro in the shower!"
        "Sebastian" "Wait, why is that on here."
        "Sebastian" "Anyways, here you go."
        "You got the {color=#ff0}Bingo Sheet{/color}."
        "Sebastian" "What's your name again?"
        menu:
            "{i}Say your real name{/i}":
                "Sebastian" "Ok, I'll probably forget that immediately after this meeting, but nice to meet you!"
            "{i}Say a fake name{/i}":
                "Sebastian" "Ok, I'll probably forget that immediately after this meeting, but nice to meet you, Bugs Draxton!"
            "What's yours?":
                "Sebastian" "Oh, well, uh my name is Sebastian but if you want to be like 53 percent niche you can call me Seabass."
        "Sebastian" "I'm pretty new as an {color=#f0f}officer{/color} but it's a pretty nice club."
        "Sebastian" "Some of the more long-time officers are a bit strange though."
        $ visited = []
        $ sebastianBut = False
        menu sebastianIntro1:
            set visited
            "Could I become an officer?":
                "Sebastian" "An {color=#f0f}officer{/color}, you mean?"
                "Sebastian" "Hah, you wouldn't want that."
            "Strange?":
                "Sebastian" "I mean, they do their work so it's all chill but..."
                $ sebastianBut = True
                jump sebastianIntro1
            "What's your favorite part of the job?":
                "Sebastian" "Has to be the pay."
                "Sebastian" "One purple lego piece an hour."
            "But..?" if sebastianBut:
                "Sebastian" "But I can't help but feel as if..."
                "Sebastian" "As if they're working on something."
                "Sebastian" "..."
                "Sebastian" "It's probably nothing."
                $ secretStep1 = True
                jump sebastianIntro1                        

        "Sebastian" "It's pretty great, though. You should show up next week."
        "Sebastian" "I'll see you around, yeah?"
        jump chooseOfficerIntro

    label endIntro:
        "David" "We have a winner!"
        "Ande" "Hey, uh, congrats!"
        "Tom" "Very impressive."
        "Sydney" "How is the bingo... 6 long?"
        "Sebastian" "Looks like now that we have a winner to our icebreaker, we can move on with our meeting!"
        "As the other {color=#f0f}officers{/color} move to the projector, Anthony hands you something as a trophy."
        "You got the {color=#ff0}Ice Broken Reward{/color}."
        "It's a, uh, bottle of Dasani."
        "You got the {color=#ff0}Dasani{/color}."
        "You sit down at a seat near the projector, watching the club presentation."
        if secretStep2 == False:
            "Every {color=#f0f}officer{/color} manages to slip you a smile during the slideshow."
        else:
            "Most of the {color=#f0f}officers{/color} manage to slip you a smile during the slideshow."
        "Eventually, the club begins to wind down and people filter out."
        menu:
            "Tell Anthony you want to talk more":
                jump acceptedAnthony
            "Tell Tom you'd like to grab tea together" if secretStep2 == False:
                jump acceptedTom
            "Meow at Sydney":
                jump acceptedSydney
            "Tell Ande you'd like to play Roblox together":
                jump acceptedAnde
            "Tell David you want to grab a drink together":
                jump acceptedDavid
            "Tell Sebastian you'd like to hang out":
                jump acceptedSebastian

        label acceptedAnthony:
            "Anthony" "TEXT"
            $ officerDate = 1
            jump intermission

        label acceptedTom:
            "Tom" "TEXT"
            $ officerDate = 2
            jump intermission

        label acceptedSydney:
            "Sydney" "TEXT"
            $ officerDate = 3
            jump intermission

        label acceptedAnde:
            "Ande" "TEXT"
            $ officerDate = 4
            jump intermission

        label acceptedDavid:
            "David" "Wonderful!"
            "David" "I'll see you friday after class!"
            $ officerDate = 5
            jump intermission

        label acceptedSebastian:
            "Sebastian" "TEXT"
            $ officerDate = 6
            jump intermission


        label intermission:
            "The next few days fly by until"
            if (officerDate == 1):
                jump anthonyDate
            elif (officerDate == 2):
                jump tomDate
            elif (officerDate == 3):
                jump sydneyDate
            elif (officerDate == 4):
                jump andeDate
            elif (officerDate == 5):
                jump davidDate
            elif (officerDate == 6):
                jump sebastianDate
        
        label anthonyDate:

        label tomDate:

        label sydneyDate:

        label andeDate:

        label davidDate:
            default affection = 0
            "You walk down the ave after your last class to the address David sent you."
            p "He said it should be near here..."
            "David only sent an address. No time... Or any sort of elaboration."
            "David" "Hi there. Where you waiting long?"
            menu:
                "No, not at all":
                    "David" "Great lets go in."
                "Yeah, you've kept me waiting for hours":
                    "David" "I-is that so?"
                    "David" "{i}oh my... they're glaring at me so harshly.{/i}"
                    "David" "{i}my face's turning red.{/i}"
                    $ affection += 1
            "The two of you walk into the boba place he's picked out."
            "This run down place would definitely not be your first choice."
            "David" "How do you like it?"
            menu:
                "It's alright.":
                    "David" "Well, at least you don't hate it."
                "What the h*** is this?":
                    "David" "You don't like it?"
                    "David" "I'm sorry, I should have picked a normaler place."
                    "David" "{i}jeez.{/i}"
                    "David" "{i}they're so blunt.{/i}"
                    $ affection += 1
            "David" "Anyways how has your day bee-"
            "A notificaiton pops up on his phone as he is talking."
            "David" "Oh crap! I nearly forgot to do my dailies."
            "He pulls out a phone and starts tapping away."
            menu:
                "Uhm... What are you doing?":
                    "He blushes."
                "Stare at him":
                    "..."
                    "......"
                    "........."
                    "..."
                    "......"
                    "........."
            "David" "Sorry about that."
            "David" "I shouldn't be gaming while someone is talking to me."
            menu:
                "Yeah, no sh*t":
                    "David" "R-right."
                    "David" "{i}oh...{/i}"
                    "David" "{i}my does my face heat up they raise their voice?{/i}"
                    $ affection += 1
                "It's fine":
                    "David" "R-really?"
                    $ affection -= 1
            "David" "Anyhow?"
            "David" "You play any gacha games?"
            menu:
                "Of course":
                    "David" "amazing!"
                    "The two of you spend the next hour talking about gacha games."
                    $ affection += 2
                "What... no":
                    "The rest of time passes in awkward, though not entirely unbearable, silence."
                    $ affection -= 1
            


            

        label sebastianDate:

    return
