# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Y/N", color="#ddd")
define d = Character("David", color="#e83")
define s = Character("Sydney", color="#6bc8d6")
define t = Character("Tom", color="#1aec87")
define a = Character("Ande", color="#fddc04")
define se = Character("Sebastian", color="#da97ea")
define an = Character("Anthony", color="#909def")

define secretStep1 = False
define secretStep2 = False
define officerDate = 0

image black = "#000"
image white = "#fff"
image bg_hall:
    "bg_hall.png"
    xysize(1920, 1080)
image bg_classroom:
    "bg_classroom.png"
    xysize(1920, 1080)
image bg_sky:
    "bg_sky.png"
    xysize(1920, 1080)

# The game starts here.
transform half_size:
    zoom 0.5

transform scale(ratio):
    zoom ratio

transform weirdsydneyscale(ratio):
    zoom ratio
    anchor (0.0, 1.0)
    align (0.0, 1.0)

label start:
    jump tomIntro
    scene black

    p "I'm late! I'm late!"

    scene bg_hall


    "The words echo in your head as you run across the hall."

    "You've been looking forward to the first meeting of the Game Development Club for a week now."

    "How you overslept today is beyond you."

    "You make it to the end of the hall and throw the door open."

    scene bg_classroom

    menu:
        "H-hey, I'm sorry I'm late to club...":
            show dav cool happy at half_size
            d "It's all good. Welcome in!"
            hide dav cool happy at half_size
        "H-hey, is this the Game Dev club?":
            show syd standing happy2 at weirdsydneyscale(0.45)
            s "Yeah! Come in, we've just started."
            hide syd standing happy2 at weirdsydneyscale(0.45)
        "Oh, so this is be the Game Dev Club.":
            show tom cross happy at scale(0.45)
            t "Yes, that's us!"
            hide tom cross happy at scale(0.45)
    
    show tom standing happy2 at scale(0.45)
    t "Welcome in, welcome in!"
    hide tom standing happy2 at scale(0.45)
    # show sebastian, right
    se "We make games here!"
    # show ande
    a "Oh hey, you new to the club?"
    # hide ande
    # hide sebastian, right
    menu:
        "No, I'm a game development veteran.":
            show dav hand concerned at half_size
            d  "I, uh, I don't think I've seen you here before."
            hide dav hand concerned at half_size
            show dav hand concerned2 at half_size
            d "Is your head ok?"
            hide dav hand concerned2 at half_size
            show dav cool happy at half_size
            d "Come in anyways, I suppose."
            hide dav cool happy at half_size

        "Y-yeah, this is my first time here.":
            # show anthony
            an "Ah great! New members are always fabulous."
            # hide anthony

        "Actually, I...":
            show tom flattered at scale(0.45)
            t "Well great! I just finished coding another {i}beautiful{/i} game in {color=#ff0}JavaScript{/color}."
            hide tom flattered at scale(0.45)
            show tom cross happy at scale(0.45)
            t "I promise I'm ok, mentally."
            hide tom cross happy at scale(0.45)
            show tom cross neutral at scale(0.45)
            t "Anyways."
            hide tom cross neutral at scale(0.45)

    show tom cross happy3 at scale(0.45)
    t "We meet on {color=#ff0}Wednesdays at 5:00{/color} each week!"
    t "A lot of people here have made games before but a lot of people here are new to it."
    hide tom cross happy3 at scale(0.45)
    show tom cross happy2 at scale(0.45)
    t "Like you might be, yeah?"
    hide tom cross happy2 at scale(0.45)

    show syd standing happy2 at weirdsydneyscale(0.45)
    s "We try to keep the club super beginner friendly! :D"
    s "We’ll have meetings on, say, art or music or..."
    hide syd standing happy2 at weirdsydneyscale(0.45)
    show syd standing neutral at weirdsydneyscale(0.45)
    # show ande
    a "{b}OR PROGRAMMING!{/b}"
    hide syd standing neutral at weirdsydneyscale(0.45)
    show syd standing happy2 at weirdsydneyscale(0.45)
    s "...and right now we're{fast} doing a bit of an icebreaker activity!"
    # hide ande
    hide syd standing happy2 at weirdsydneyscale(0.45)
    # show sebastian
    se "Here's a bingo sheet, try to fill it out as best as you can. ;)"

    "Sebastian handed you the {color=#ff0}Bingo Sheet{/color}."
    # hide sebastian

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
                an "Hello! Welcome to the club!"
                label anthonyIntroLoop:
                    menu:
                        "...hi!":
                            an "...Hello!"
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
        an "O-oh! You want {i}me{/i} to look at your sheet?"
        an "Let's see... I could do this one... or that one... or maybe..."
        an "Does Scratch count as a coding language?"
        an "We can only check off one box, though, right? We gotta choose the best one."
        an "Tom could probably do that coding one, and I think David also writes. But you probably want to save David for the {color=#f00}waifu{/color} box."
        an "But what if..."
        menu anthonyIntro1: 
            "...":
                an "Hmmmm..."
                jump anthonyIntro1
            "Just pick one!":
                an "Do you want to be {i}sub-optimal{/i}?! Or do you want to {i}win{/i} this bingo?"
                an "That's what I thought."
                an "Now just give me a few more minutes to figure this out. Or maybe hours. I’ll make sure you have the {color=#f00}MAXIMUM{/color} chance of completing this bingo board!"
                an "Wait ... \"maximum\" ... \"bingo\" ... \"figure\" ... I’ve got an idea!"
            "What if we narrowed it down?":
                an "Hmm, restrict the solution space? I like the way you think!"
                an "Wait ... \"solution\" ... \"think\" ... I’ve got an idea!"
            "Talk to another officer":
                an "Woah woah woah where are you going?"
                an "This problem needs to be solved! So we—yes, we—are going to sit here until we figure this out!"
                an "Wait ... \"going\" ... \"problem\" ... “sit” ... I’ve got an idea!"
        
        an "Do you have a pen or pencil or something? I also need some paper—wait, I can use the back of the bingo board!"
        an "Now we just put all possible bingo configurations on a state diagram, estimate the transition probabilities, run some graph traversal..."
        an "{cps=80}...compute the Laplacian, and...{p}...wait is that a zero or an \"O\"...?{p}...drop the seven, carry the two, and...{/cps}"
        an "There we go! The optimal bingo box is simply the solution to this 25-degree polynomial!"
        an "Yeah, I don’t know how to solve this."
        an "And so much time has passed! I’ll just check the \"Been to Game Dev Club before\" box."
        an "But that was a lot of fun! We should talk more if you have any other problems you want solved!"
        an "Or not solved."
        an "Regardless!"
        jump chooseOfficerIntro

    label andeIntro:
        a "Hey..."
        $ visited = []
        menu andeIntro1:
            set visited
            "Hola!":
                a "Sorry, I don't speak {color=#f00}Japanese{/color}..."
                jump andeIntro1
            "Hey, I need my bingo filled out!":
                a "Yeah, I gotchu."
            "You sound nice...":
                a "Thanks, I get that a lot."
                a "Well, not a lot, but sometimes."
                a "Well, never, but thank you!"
                a "Anyways, lemme fill out your bingo!"
            "hey...":
                a "Hey..."
                jump andeIntro1

        a "Lemme take a look..."
        menu:
            "tuff.":
                "You give Ande the {color=#ff0}Bingo Sheet{/color}."

        a "Hmmmmmm..."
        a "...nothing about Markiplier OnlyFans is on here..."
        a "...nothing about ranked Roblox gooning..."
        a "...nothing about {color=#ff0}pheromone-maxxing{/color} either..."
        a "{i}Who made this?!{/i}"
        a "Fine. I'll fill this one out!"
        "Ande draws a box on your Bingo Sheet outside of the grid, creating a row of 6, and fills it in."
        "You got the {color=#ff0}Bingo Sheet{/color}."
        a "By the way, do you play Roblox?"
        menu:
            "I love {i}cart ride into 17 pregnant hyenas{/i}!":
                a "Nice. I love {i}cart ride into 17 pregnant hyenas{/i} too. Roblox is really great!"
            "No...":
                a "Well, you should try it out sometime!"
            "You are weird.":
                a "...buddy, have you SEEN the other {color=#f0f}officers{/color}?"

        a "Well, thank you for showing up to the game development club! In fact, I wouldn't mind if you showed up to my class tomorrow. I lost my Roblox gaming buddy last time..."
        menu:
            "Thanks! I'll think about it!":
                a "See you there! I'll reserve a seat!"
            "I don't know if that's allowed.":
                a "Uhh..."
                menu:
                    "Thanks! I'll think about it!":
                        a "See you there! I'll reserve a seat!"
        jump chooseOfficerIntro

    label davidIntro:
        d "Yo. We haven’t filled out each other’s bingos have we?"
        menu:
            "No, we have not.":
                d "Well, what are you waiting for then?"
                d "Your paper. Hand it over."
                "You give David the {color=#ff0}Bingo Sheet{/color}."
            "Fill out my sheet already, bitch":
                d "You!!!"
                d "You would dare talk to an {color=#f0f}officer{/color} like that?"
                d "{i}hehe... I hope they shit talk me more.{/i}"
                d "Ahem."
        d "I’m David, head of the game dev club’s intelligence division."
        d "I like to play gacha games. Lots of gacha games."
        d "My favorite character is ZhuoZhi. I spent $2000 dollars maxing her out."
        d "{cps=100}But I’d pay double the amount of money for her to tie me down and...{/cps}"
        d "..."
        d "Ahem."
        d "Sorry about that."
        d "Someday, I’m going to make my own gacha game and max out all the characters for myself."
        d "Here, let me fill out your bingo."
        "David fills out \"Has spent at least $1000 on a video game\"."
        "You got the {color=#ff0}Bingo Sheet{/color}."
        d "By the way, do you like boba?"
        d "If you do..?{w} I wouldn’t mind grabbing a drink with you tommorrow..."
        jump chooseOfficerIntro

    label sebastianIntro:
        se "Uh, hi."
        menu:
            "Hello, I need your help filling out my bingo sheet!":
                se "Uh, yeah sure."
                "You give Sebastian the {color=#ff0}Bingo Sheet{/color}."
        se "Oh, yeah I do sing the {i}Super Smash Bros.{/i} intro in the shower!"
        se "Wait, why is that on here."
        se "Anyways, here you go."
        "You got the {color=#ff0}Bingo Sheet{/color}."
        se "What's your name again?"
        menu:
            "{i}Say your real name{/i}":
                se "Ok, I'll probably forget that immediately after this meeting, but nice to meet you!"
            "{i}Say a fake name{/i}":
                se "Ok, I'll probably forget that immediately after this meeting, but nice to meet you, Bugs Draxton!"
            "What's yours?":
                se "Oh, well, uh my name is Sebastian but if you want to be like 53 percent niche you can call me Seabass."
        se "I'm pretty new as an {color=#f0f}officer{/color} but it's a pretty nice club."
        se "Some of the more long-time {color=#f0f}officers{/color} are a bit strange though."
        $ visited = []
        $ sebastianBut = False
        menu sebastianIntro1:
            set visited
            "Could I become an officer?":
                se "An {color=#f0f}officer{/color}, you mean?"
                se "Hah, you wouldn't want that."
            "Strange?":
                se "I mean, they do their work so it's all chill but..."
                $ sebastianBut = True
                jump sebastianIntro1
            "What's your favorite part of the job?":
                se "Has to be the pay."
                se "One purple lego piece an hour."
            "But..?" if sebastianBut:
                se "But I can't help but feel as if..."
                se "As if they're working on something."
                se "..."
                se "It's probably nothing."
                $ secretStep1 = True
                jump sebastianIntro1                        

        se "It's pretty great, though. You should show up next week."
        se "I'll see you around, yeah?"
        jump chooseOfficerIntro

    label endIntro:
        d "We have a winner!"
        a "Hey, uh, congrats!"
        t "Very impressive."
        show syd standing concerned at weirdsydneyscale(0.45)
        s "How is the bingo... 6 long?"
        hide syd standing concerned at weirdsydneyscale(0.45)
        se "Looks like now that we have a winner to our icebreaker, we can move on with our meeting!"
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
            # "Tell Anthony you want to talk more":
            #     jump acceptedAnthony
            "Tell Tom you'd like to grab tea together" if secretStep2 == False:
                jump acceptedTom
            "Meow at Sydney":
                jump acceptedSydney
            # "Tell Ande you'd like to play Roblox together":
            #     jump acceptedAnde
            "Tell David you want to grab a drink together":
                jump acceptedDavid
            # "Tell Sebastian you'd like to hang out":
            #     jump acceptedSebastian

        label acceptedAnthony:
            an "TEXT"
            $ officerDate = 1
            jump intermission

        label acceptedTom:
            t "Hey, that's awesome!"
            t "I can pick you up if you'd like, I always love driving."
            t "Here, what days are you free..."
            "You both exchange {color=#ff0}Contact Information{/color}."
            $ officerDate = 2
            jump intermission

        label acceptedSydney:
            show syd standing happy2 at scale(0.45)
            s "{i}Mreeow meow mrraaahhh!{/i}"
            hide syd standing happy2 at scale(0.45)
            show syd standing happy at scale(0.45)
            s "A date? Yeah sure! I'd love that!"
            s "Oh yeah. I've got a great surprise idea."
            hide syd standing happy at scale(0.45)
            "Sydney puts her hands over your eyes."
            $ officerDate = 3
            jump intermission

        label acceptedAnde:
            a "TEXT"
            $ officerDate = 4
            jump intermission

        label acceptedDavid:
            d "Wonderful!"
            d "I'll see you Friday after class!"
            $ officerDate = 5
            jump intermission

        label acceptedSebastian:
            se "TEXT"
            $ officerDate = 6
            jump intermission


        label intermission:
            if (officerDate == 1):
                jump anthonyDate
            elif (officerDate == 2):
                scene black
                "Later..."
                "You're at the place Tom said he could pick you up."
                "You hear a whirring steadily growing in volume that occupies all pitches of the auditory spectrum."
                "You look up and descending upon you is a mess of steel and timber, coursing through the air by some unknown principle."
                "Tom is proudly driving it."
                scene bg_sky
                "He extends a hand to help you board the mysterious contraption and the both of you woosh off!"
                "The ride on ambiguopter is smooth and bumpy..."
                t "Glad you were able to make this work out! It's good to see you! :)"
                "He's shouting over the noise of the... engines? Rotors? Distillation columns?"
                "It's hard to tell what they are."
                t "I built this thing myself! It even gets good mileage!!"
                "You eventually begin to descend to a blue house. Tom manages to land on the fire escape. It's unclear whether or not this is an accident."
                jump tomDate
            elif (officerDate == 3):
                jump sydneyDate
            elif (officerDate == 4):
                jump andeDate
            elif (officerDate == 5):
                "Some time passes until when you planned to meet David."
                "You walk down the Ave after your last class to the address he sent you."
                p "He said it should be near here..."
                "David only sent an address. No time... Or any sort of elaboration."
                d "Hi there. Where you waiting long?"
                menu:
                    "No, not at all":
                        d "Great lets go in."
                    "Yeah, you've kept me waiting for hours":
                        d "I-is that so?"
                        d "{i}oh my... they're glaring at me so harshly.{/i}"
                        d "{i}my face's turning red.{/i}"
                jump davidDate
            elif (officerDate == 6):
                jump sebastianDate
        
        # label anthonyDate:

        # label andeDate:

        # label sebastianDate:

    return
