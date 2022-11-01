import time
import os
c1=0
def s1():
    os.system('cls')
    print('Your ship wrecked and you washed ashore on a remote island. You wake up and find yourself alone,with nothing.\n You have survive.You sure you up to this task?')
    print('You find a bottle and some paper and a pen along the shore, some logs and rope. What do you do?')
    print('\n1. Write a message in the bottle and throw it in the ocean')
    print('2. Try building a boat and escaping the island')
    print('3. Keep waiting for someone to come and rescue you\n\n')
    i=int(input('>>>'))
    if i==1:
        os.system('cls')
        print('Good job. Now wait another 100 years before someone finds the bottle and find you')
        time.sleep(3)
        s1()
    elif i==2:
        os.system('cls')
        print('You build a raft with the logs and set out into the ocean')
        time.sleep(2)
        print('Suddenly a storm comes.')
        time.sleep(2)
        print('The ocean current destroys your raft and you drown')
        time.sleep(2)
        go(1)
    elif i==3:
        s2()
    else:
        s1()
def s2():
    global c1
    os.system('cls')
    print('You have been waiting for hours now. Why not try some other things while you wait for being rescued?\n')
    print('You can light a fire with sticks and stones, use your shirt to make flag, or shout and scream like an idiot.\nWhat would you do?')
    print('\n1. Let\'s get it blazing')
    print('2. I can go shirtless')
    print('3. I am an idiot\n\n')
    i=int(input('>>>'))
    if i==1:
        c1=c1+1
        os.system('cls')
        print('A storm came and put out the fire. Maybe something else?')
        time.sleep(3)
        if c1 % 3==0:
            s3()
        else:
            s2()
    elif i==2:
        c1=c1+1
        os.system('cls')
        print('A storm came and blew away the flag. Congrats, now you are both flagless and shirtless')
        time.sleep(3)
        if c1 % 3==0:
            s3()
        else:
            s2()
    elif i==3:
        c1=c1+1
        os.system('cls')
        print('Well, nobody can see you. Why not do something useful?')
        time.sleep(3)
        if c1 % 3==0:
            s3()
        else:
            s2()
    else:
        s2()
def s3():
    os.system('cls')
    print('Well all your attempts certainly didnt work and now you are tired and hungry.\nYou see some berries in the bushes and a lot of coconut trees around. There are also fish in the sea')
    print('So what do you want for lunch?\n')
    print('1. Lets have some berries')
    print('2. I\'ll go fishing')
    print('3. Coconuts are the best\n\n')
    i=int(input('>>>'))
    if i==1:
        os.system('cls')
        print('The berries were poisonous. Didnt you watch Discovery Channel?')
        time.sleep(3)
        go(1)
    elif i==2:
        os.system('cls')
        print('You have no experience in catching fish. Try something else')
        time.sleep(3)
        s3()
    elif i==3:
        s4()
    else:
        s3()
def s4():
    os.system('cls')
    print('You see a lot of coconut trees around. You climb up and get a coconut. Now you have to break into it\nWhat would you do?\n')
    print('1. Try hitting the coconut on a rock and break it')
    print('2. Try to tear the coconut with your teeth')
    print('3. Get one more coconut from the tree\n\n')
    i=int(input('>>>'))
    if i==1:
        s5()
    elif i==2:
        os.system('cls')
        print('You tried to bite the coconut hard and a tooth fell off. The would gave you an infection and you died')
        time.sleep(3)
        go(1)
    elif i==3:
        os.system('cls')
        print('After getting the coconut as tried to get down from the tree you foot slipped and you fell')
        go(1)
    else:
        s4()
def s5():
    os.system('cls')
    print('The coconut was a good choice. It has enough water and nutrients.\nNow its nearing dusk. The sun is about to set. What do you want to do?\n')
    print('\n1. Go explore the island')
    print('2. Have some rest and build a shelter\n\n')
    i=int(input('>>>'))
    if i==1:
       s6()
    elif i==2:
        s7()
    else:
        s5()
def s6():
    os.system('cls')
    print('You are exploring the island and its now night. You are walking in one direction while suddenly you hear a faint sound from another direction.\nWhat do you do?')
    print('\n1. Investigate the source of the sound')
    print('2. Keep walking')
    print('3. Go back\n\n')
    i=int(input('>>>'))
    if i==1:
        os.system('cls')
        print('You keep going and see some lights...')
        time.sleep(2)
        print('As you move closer, you see a magnificent resort, a luxury beach and lots of people')
        time.sleep(2)
        print('You have finally reached some civilisation. Congrats, you have been rescued')
        time.sleep(3)
        go()
    elif i==2:
        os.system('cls')
        print('You keep walking in the dark, and suddenly fall off a cliff')
        time.sleep(3)
        go(1)
    elif i==3:
        s5()
    else:
        s6()
def s7():
    os.system('cls')
    print('You realised you need some sleep after such an adventurous day. What do you do?\n')
    print('1. Make a small shelter using the coconut leaves')
    print('2. Dont make a shelter and sleep under the open sky')
    print('3. Sleep among the trees for shelter\n\n')
    i=int(input('>>>'))
    if i==1:
        s8()
    elif i==2:
        s8()
    elif i==3:
        os.system('cls')
        print('A coconut fell while you slept and cracked your skull. Never sleep under coconut trees')
        time.sleep(3)
        go(1)
def s8():
    os.system('cls')
    print('You wake up next morning and see helicoptors flying towards the island')
    time.sleep(2)
    print('They have come to rescue you. Glad you survived this long')
    time.sleep(2)
    print('By the way, did you know that there was a resort on the other side of the island?')
    time.sleep(2)
    print('Perhaps if you explored the island a bit more, you would have been rescued faster')
    time.sleep(2)
    go()
def go(d=0):
    if d==0:
        os.system('cls')
        print('YOU HAVE SUCCESSFULLY SURVIVED THE ISLAND.\n CONGRATULATIONS...!!!')
        time.sleep(5)
    else:
        os.system('cls')
        print('SORRY...YOU DIED...!!!')
        time.sleep(5)
    print('\n\n\n\nWOULD YOU LIKE TO REPLAY?')
    r=input('>>>')
    if r=='Y' or r=='y':
        s1()
s1()