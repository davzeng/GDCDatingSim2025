image bg_boba:
    "bg_boba.png"
    xysize(1920, 1080)
image black = "#000"

label davidDate:
    default affection = 0
    "The two of you walk into the boba place he's picked out."
    scene bg_boba
    "This run down place would definitely not be your first choice."
    show dav cool neutral3 at half_size
    d "How do you like it?"
    menu:
        "It's alright.":
            show dav cool neutral2 at half_size
            d "Well, at least you don't hate it."
        "What the h*** is this?":
            show dav cool concerned at half_size
            d "You don't like it?"
            show dav hand concerned at half_size
            d "I'm sorry, I should have picked a normaler place."
            show dav standing upset at half_size
            d "{i}jeez.{/i}"
            d "{i}they're so blunt.{/i}"
            $ affection += 1
    show dav standing happy at half_size
    d "Anyways how has your day bee-"
    "A notification pops up on his phone as he is talking."
    show dav vividpog at half_size
    d "Oh crap! I nearly forgot to do my dailies."
    show dav hand concerned2 at half_size
    "He pulls out a phone and starts tapping away."
    menu:
        "Uhm... What are you doing?":
            
            "He blushes."
        "Stare at him":
            "..."
            show dav hand neutral2 at half_size
            "......"
            "........."
            show dav hand concerned2 at half_size
            "..."
            show dav standing stare at half_size
            "......"
            show dav hand concerned2 at half_size
            "........."
            $ affection += 1
    show david standing concerned at half_size
    d "Sorry about that."
    show david hand neutral at half_size
    d "I shouldn't be gaming while someone is talking to me."
    menu:
        "Yeah, no sh*t.":
            show dav standing upset at half_size
            d "R-right."
            show dav hand neutral2 at half_size
            d "{i}oh...{/i}"
            d "{i}my does my face heat up they raise their voice?{/i}"
            $ affection += 1
        "It's fine.":
            show dav hand pog at half_size
            d "R-really?"
            $ affection -= 1
    show dav standing happy3 at half_size
    d "Anyhow?"
    show dav standing happy2 at half_size
    d "You play any gacha games?"
    menu:
        "Of course.":
            show dav cool happy3 at half_size
            d "amazing!"
            "The two of you spend the next hour talking about gacha games."
            $ affection += 2
        "What... no.":
            show dav standing concerned at half_size
            "The rest of time passes in awkward, though not entirely unbearable, silence."
            $ affection -= 1
    show dav hand neutral2 at half_size
    "Eventually, it's time for you to head out... it's almost morning!"
    if affection <= 1:
        "David leads you out of the building."
        show dav standing concerned at half_size
        d "Hey, it was... a time hanging out."
        show dav cool concerned2 at half_size
        d "I'll see you around?"
        hide dav cool concerned
        scene black
        "You achieved DAVID NEUTRAL ENDING."
    else:
        show dav vividpog at scale(0.6)
        "david bein down bad prolly"
        hide dav vividpog
        scene black
        "You achieved {color=#0ff}DAVID GOOD ENDING{/color}!"