# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define littleguytransparent1 = Character("LG1")
define littleguytransparent2 = Character("LG2")

image coinInMiddle = "coininmiddle.png"
image coinmiddlemelt1 = "coinMelt1.png"
image coinmiddlemelt2 = "coinMelt2.png"
image coinmiddlemelt3 = "coinMelt3.png"
image LGSwing = "guyswing.png"
image LGHoldCoin = "littleguycoin1.png"
image LGFlip = "littleguyflip.png"
image LGHeads = "littleguyheads.png"
image LGHeadsFall = "littleguyheadsfalling.png"
image LGTails = "littleguytails.png"
image coinReflect1 = "reflection1.png"
image coinReflect2 = "reflection2.png"
image coinReflect3 = "reflection3.png"
image swing1 = "swing1.png"
image swing2 = "swing2.png"
image swing3 = "swing3.png"
image foggyBG = "upclosefoggy.png"



# The game starts here.



label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # "Swings in Mauerpark, Berlin" by maaark https://freesound.org/people/maaark/sounds/164157/
    # "Forest, trees rustling in the wind" by arpeggio1980 https://freesound.org/people/arpeggio1980/sounds/523389/
    play sound "windRustling.mp3" volume 0.5 loop
    scene foggyBG
    play sound "swings.mp3" volume 0.5 
    pause
    scene swing1
    pause
    scene swing2
    pause
    scene swing1
    pause
    scene swing3
    pause
    scene swing1
    pause
    scene swing1
    pause
    scene swing2
    pause
    scene swing1
    pause
    scene swing3
    pause
    scene swing1
    pause
    scene LGSwing
    menu : 
        "Go to the figure" :
            jump figure
        "Go to the figure" :
            jump figure
        "Go to the figure" :
            jump figure
    stop sound 
           
label figure:
    scene foggyBG
    show littleguytransparent1
    pause 
    show littleguytransparent2
    pause 
    show littleguytransparent1
    # littleguytransparent1
    "I see you're by yourself this time..."
    "I don’t know about you, but this joint's pretty run down."
    play sound "swings.mp3" volume 0.5 
    "Do like this noise? I sure do"
    pause
    stop sound 
    scene foggyBG
    scene LGHoldCoin
    "Don't worry about me, you'll be on your own dime."
    pause 
    scene LGFlip
    pause 
    scene LGHeads 
    pause 
    scene LGFlip
    pause 
    scene LGTails
    pause 
    scene LGFlip
    pause 
    scene LGHeads 
    pause 
    scene LGHeadsFall
    pause 
    scene coinReflect1
    pause 
    scene coinReflect2
    pause 
    scene coinReflect3



    #  stop sound fadeout 0.5


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.


    # This ends the game.

    return
