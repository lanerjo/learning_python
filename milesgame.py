import random
import time
import math
print("Welcome to ATV Road Trip!!!")
time.sleep(1)
stuck=0
print("Good luck because your gonna need it...")
time.sleep(1)
first_round=0
second_round=0
third_round=0
while True:
    print("You need 250 miles to complete the first round")
    time.sleep(1)
    first_number_1=random.choice([100,200,300])
    second_number_1=random.choice([0,10,20,30,40,50,60,70,80,90])
    third_number_1=random.choice([0,1,2,3,4,5,6,7,8,9])
    mystery_1=first_number_1+second_number_1+third_number_1
    first_roll_1=random.choice([25,25,25,35,35,35,50,50,50,75,75,75,100,100,150,150,200,mystery_1,mystery_1,mystery_1])
    if first_roll_1==mystery_1:
        print("Mystery miles!!!")
        time.sleep(1)
    print("You got a mile of:",first_roll_1)
    first_round=first_round+first_roll_1
    time.sleep(1)
    print("Your total miles so far in this round is:", first_round)
    time.sleep(1)
    first_number_2=random.choice([100,200,300])
    second_number_2=random.choice([0,10,20,30,40,50,60,70,80,90])
    third_number_2=random.choice([0,1,2,3,4,5,6,7,8,9])
    mystery_2=first_number_2+second_number_2+third_number_2
    first_roll_2=random.choice([25,25,25,35,35,35,50,50,50,75,75,75,100,100,150,150,200,mystery_2,mystery_2,mystery_2])
    print("Rolling again...")
    time.sleep(1)
    if first_roll_2==mystery_2:
        print("Mystery!!!")
        time.sleep(1)
    print("You got a mile of:", first_roll_2)
    first_round=first_round+first_roll_2
    time.sleep(1)
    print("Your total miles so far in this round is:", first_round)
    time.sleep(1)
    first_number_3=random.choice([100,200,300])
    second_number_3=random.choice([0,10,20,30,40,50,60,70,80,90])
    third_number_3=random.choice([0,1,2,3,4,5,6,7,8,9])
    mystery_3=first_number_3+second_number_3+third_number_3
    first_roll_3=random.choice([25,25,25,35,35,35,50,50,50,75,75,75,100,100,150,150,200,mystery_3,mystery_3,mystery_3])
    print("Rolling again...")
    time.sleep(1)
    if first_roll_3==mystery_3:
        print("Mystery!!!")
        time.sleep(1)
    print("You got a mile of:", first_roll_3)
    first_round=first_round+first_roll_3
    time.sleep(1)
    print("You got a total milage of:", first_round)
    time.sleep(1)
    print("Congratulations on your total milage, but you might get stuck!")
    time.sleep(4)
    print("Lets find out! You have a 50/50 shot of getting stuck!")
    time.sleep(1)
    print("""If you get stuck, you can choose to take the lose of 50 miles or
you can take a chance on another 50/50. If you win that, you get 50 miles added
to your total milage for this round and no points off. However, if you lose, then
you get 100 miles off! If you do not get stuck, nothing happens to your score.""")
    time.sleep(10)
    chance_1=random.randint(1,2)
    if chance_1 == 1:
        print("Congratulations on not getting stuck!!!")
        time.sleep(1)
    if chance_1 == 2:
        print("Sorry, you got stuck!!!")
        stuck=stuck+1
        print("It happens, sorry buddy.")
        time.sleep(4)
        lose_choice_1=raw_input("Press y to take a chance of getting out and added score or n for taking the hit:")
        if lose_choice_1 == 'y' or 'Y':
            chance_taken_1=random.randint(1,2)
            if chance_taken_1 == 1:
                print("Congratulations on getting unstuck early!")
                print("You got 50 miles added!!!")
                first_round=first_round+50
                print("Your milage total is now:", first_round)
                time.sleep(5)
            else:
                print("You got stuck again!")
                print("Ouch!!! 100 points off!!!")
                first_round=first_round-100
                print("Your milage total is now:", first_round)
                time.sleep(5)
        if lose_choice_1 != 'y' or 'Y':
            print("You have decided to take the hit!")
            time.sleep(1)
            first_round=first_round-50
            print("Your mileage total is now:", first_round)
            time.sleep(1)
    if first_round < 250:
        print("Sorry, you lost!")
        time.sleep(1)
        break
    if first_round >= 250:
        print("Congratulations!!! You have passed the first round!!!")
        print("You can try for round 2 or you can select your prize of a rubber duck.")
        time.sleep(1)
        prize_pick_round_1=raw_input("Press y to get prize and end game or any other key to continue:")
        if prize_pick_round_1 == 'y' or 'Y':
            print("You have chosen the rubber ducky!")
            print("I hope your happy with it!")
            print("Ending game...")
            time.sleep(5)
            break
        if prize_pick_round_1 != 'y' or 'Y':
            continue
        break