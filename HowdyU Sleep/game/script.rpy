# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define littleguytransparent1 = Character("LG1")
define littleguytransparent2 = Character("LG2")

image coinInMiddle = "coininmiddle.png"
image coinmiddlemelt1 = "coinMelt1.png"
image coinmiddlemelt2 = "coinMelt2.png"
image coinmiddlemelt3 = "coinMelt3.png"
image LGuySwing = "guyswing.png"
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

    scene foggyBG



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Insert the game here"

    # This ends the game.

    return
