# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Y/N")

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

    p "The words echo in your head as you run across the hall."

    "You've been looking forward to the first meeting of the Game Development Club for a week now."

    "How you overslept today is beyond you."

    "You make it to the end of the hall and throw the door open."

    menu:

        "H-hey, I'm sorry I'm late to club...":

            "David" "It's all good. Welcome in!"

        "H-hey, is this the Game Dev club?":

            "Sydney" "Yeah! Come in, we've just started"

        "Oh, so this is be the Game Dev Club.":

            "Tom" "Yes, that's us!"
    
    "Tom" "Welcome in, welcome in!"

    "Sebastian" "We make games here!"

    "Ande" "Oh hey, you new to the club?"

    p "Y-yeah, this is my first time here."

    "Anthony" "Ah great! New members are always fabulous."

    # This ends the game.

    return
