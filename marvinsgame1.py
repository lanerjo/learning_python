print 'You have just entered the Scary House'
print 'You have 2 choices'
choice = raw_input("right or left")

if choice == 'right' or choice == 'r' or choice == 'left' or choice == 'l':
    if choice == 'left' or choice == 'l': 
        print 'You ran into a Killer Clown!' 
        Weapon = raw_input('Chose a weapon gun or knife!')
        if Weapon == 'gun': 
            print 'You picked up a gun with no bullets you are now dead! ):'
        elif Weapon == 'knife':
            print 'You have Picked up the knife And did not stab the clown you are now dead'
    if choice == 'right' or choice == 'r':
        print 'You have fallen into a whole and are dead ):'
else:
    print'you did not pick a valid door'
    exit()
