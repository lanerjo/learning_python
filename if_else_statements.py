def clinic():
    print "you've just entered the clinic!"
    print "do you take the door on the left or the door on the right?"
    answer = raw_input("type left or right and hit 'enter'").lower()
    if answer == "left" or answer == "l":
        print "this is the verbal abuse room, you heap of crap"
    elif answer == "right" or answer == "r":
        print "of course this is the argument room, i told you that already"
    else:
        print "you didn't pick left or right! try again."
        clinic()
