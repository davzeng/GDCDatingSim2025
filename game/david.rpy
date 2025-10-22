image bg_boba:
    "bg_boba.png"
    xysize(1920, 1080)

label davidDate:
    default affection = 0
    "The two of you walk into the boba place he's picked out."
    scene bg_boba
    "This run down place would definitely not be your first choice."
    d "How do you like it?"
    menu:
        "It's alright.":
            d "Well, at least you don't hate it."
        "What the h*** is this?":
            d "You don't like it?"
            d "I'm sorry, I should have picked a normaler place."
            d "{i}jeez.{/i}"
            d "{i}they're so blunt.{/i}"
            $ affection += 1
    d "Anyways how has your day bee-"
    "A notification pops up on his phone as he is talking."
    d "Oh crap! I nearly forgot to do my dailies."
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
            $ affection += 1
    d "Sorry about that."
    d "I shouldn't be gaming while someone is talking to me."
    menu:
        "Yeah, no sh*t.":
            d "R-right."
            d "{i}oh...{/i}"
            d "{i}my does my face heat up they raise their voice?{/i}"
            $ affection += 1
        "It's fine.":
            d "R-really?"
            $ affection -= 1
    d "Anyhow?"
    d "You play any gacha games?"
    menu:
        "Of course.":
            d "amazing!"
            "The two of you spend the next hour talking about gacha games."
            $ affection += 2
        "What... no.":
            "The rest of time passes in awkward, though not entirely unbearable, silence."
            $ affection -= 1
    "Eventually, it's time for you to head out... it's almost morning!"
    if affection <= 1:
        "David leads you out of the building."
        d "Hey, it was... a time hanging out."
        d "I'll see you around?"
        "You achieved DAVID NEUTRAL ENDING."
    else:
        "TEXTTTTT"
        "david bein down bad prolly"
        "You achieved {color=#0ff}DAVID GOOD ENDING{/color}!"