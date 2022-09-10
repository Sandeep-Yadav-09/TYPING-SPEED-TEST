from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

test = \
    ["""\n   There was once a hare who was friends with a tortoise. One day, he challenged the tortoise to a race. Seeing 
    how slow the tortoise was going, the hare thought he’ll win this easily. So he took a nap while the tortoise kept 
    on going. When the hare woke up, he saw that the tortoise was already at the finish line. Much to his chagrin, 
    the tortoise won the race while he was busy sleeping.""",
     """\n    Once there was a dog who wandered the streets night and day in search of food. One day, he found a big juicy 
    bone and he immediately grabbed it between his mouth and took it home. On his way home, he crossed a river and 
    saw another dog who also had a bone in its mouth. He wanted that bone for himself too. But as he opened his 
    mouth, the bone he was biting fell into the river and sank. That night, he went home hungry.""",
     """\n    After flying a long distance, a thirsty crow was wandering the forest in search of water. Finally, 
     he saw a pot half-filled with water. He tried to drink from it but his beak wasn’t long enough to reach the 
     water inside. He then saw pebbles on the ground and one by one, he put them in the pot until the water rose to 
     the brim. The crow then hastily drank from it and quenched his thirst."""]

test1 = r.choice(test)

print("\n****** TYPING SPEED TEST ******")
print(test1)
print()
print()
time_1 = time()
testinput = input(" Start Typing !: ")
time_2 = time()

print("Your Typing Speed is:", speed_time(time_1, time_2, testinput),"W/sec")
print("You committed", mistake(test1, testinput),"Errors")


