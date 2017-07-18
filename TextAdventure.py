import time

start = input("Type 'start' to begin adventure. Type anything else to exit. ")
if start == "start":
    print("""
    You find yourself standing in a foot of murky black water.
    Dim green light comes from a source somewhere behind you.
    You're wearing boots, a thick waterproof coat, and at your waist is a sheath with a heavy sword.
    You consider turning to see the source of the green tinted light, but you're also curious about your sword.
    You feel as if you are being watched, but that might just be your overactive imagination.""")
    time.sleep(.5)
    print("""
    Your options are:""")
    time.sleep(.5)
    print("""
    a) Press onward into the dark.
    b) Turn around to face the dim green light.
    c) Unsheath sword.""")
    time.sleep(.5)
    letter = input("""
    Type the letter of the action you wish to take. """)
    if letter == ("a") or letter == ("b") or letter == ("c"):
        if letter == ("a"):
            print("""
    Your foot hits a rock, a bump, something under the water.
    A chill goes up your spine and you lose balance, toppling with a splash and a cry of terror into the black water.
    A foul taste fills your mouth, and you go limp, losing consciousness, with your head under the water.
    Your corpse joins the many unfortunate others that have fallen here.""")
        if letter == ("b"):
            print("""
    The dim green light was coming from the glowing eyes of a large statue of a toad.
    The eyes seem to be small green fires glowing in stone eye sockets.
    The entire statue is damp and slimy, and seems to be ancient and magical.
    The toad's mouth seems to be a tunnel leading down, however, the large stone base of the statue has writing on either side.
    You hear footsteps coming swiftly from behind you.
    Quick. Time is of the essence. Would it be worth it to try and read the writing?
    The footsteps sound big, and the space you're in is large and open. The small tunnel may be the only place you'd be safe.
    However, you do have a sword. The footsteps get closer. You must choose quickly.
""")
            print("""
    Your options are:""")
            print("""
    a) Draw your sword and turn around to face the footsteps.
    b) Read the writing at the base of the statue.
    c) Run for the tunnel as fast as you can.
            """)
            letter2 = input("""
    Type the letter of the action you wish to take. """)
            if letter2 == ("a") or letter == ("b") or letter == ("c"):
                if letter2 == ("a"):
                    print("""
    The blade glows brightly, and after a second to adjust, you see a large slimy golem only a few feet in front of you.
    It has stopped coming towards you, however, and it's eyes are full of terror.
    Too late, you hear angry hissing and clicking echo around you and large spiders descend swiftly on delicate strings from the ceiling.
    You attempt to sheath the sword, but it's too late.
    The last thing your eyes will ever see are five giant spiders tearing the large golem to pieces, and the last thing you hear are your own shrill screams.""")
                if letter2 == ("b"):
                    print("""
    You run to the base of the statue.
    With the footsteps approaching, you read frantically.
    "Beware spiders!" is the first thing your eyes fall on. "Do not disturb the darkness."
    'It's not like I have a light,' you think.
    You duck as your brain alerts you to the swish of a weapon just in time.
    The footsteps came from a large, slimy golem wielding a heavy club.
    You  draw your sword.
    The blade glows brightly.
    The golems face fills with fear.
    "Oh." you think.
    Your only consolation is that death comes quickly.""")
                if letter2 == ("c"):
                    print("""
    You slide into the open entrance of the tunnel and run down the slippery stairs until you are sure you've lost whoever was making the footsteps.
    Immediately after you entered the tunnel, the feeling of being closely watched went away.
    A large sigh of relief escapes your lips.
    You feel as if you have escaped some great danger, but you don't know what.
    You guess you should be glad you don't have to find out.
    You draw your sword, and the light illuminates the way ahead.
    Luck seems to be on your side.
    You prepare to continue to see where this strange adventure will lead.

    THE END""")
        if letter == ("c"):
            print("""
    The sword comes free of its sheath with a satisfying 'chiink' sound of metal on metal.
    The blade is glowing brightly, and for a moment you are blinded by the sudden light.
    Your eyes adjust, and you realize your mistake.
    The water, now clear enough to see through, shows that all around you are drowned and bloody corpses.
    You look up quickly, trying to rid the image from your mind, and see large spiders coming angrily for the source of the light that so rudely awakened them.
    You turn to run. There are too many. You splash through the water, over the uneven ground. Foul water splashes up to your face and burns your skin.
    The first three spiders reach you at once.
    For an instant there is pain when three pairs of sharp mandibles pierce you at once, then there is nothing.
""")

    else:
        print("""
    That is not an option.""")
