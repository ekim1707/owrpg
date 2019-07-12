# saving this personal project for later

import random

class Attack:
    def __init__(self, health, power, accuracy, dodge, ultimate, ultcount):
        self.health = health
        self.power = power
        self.accuracy = accuracy
        self.dodge = dodge
        self.ultimate = ultimate
        self.ultcount = ultcount
    
    def alive(self):
        if self.health <= 0:
            return False
        else:
            return True

class Healer:
    def __init__(self, heal, assist, ultimate, mercyvar, ultcount):
        self.heal = heal
        self.assist = assist
        self.ultimate = ultimate
        self.mercyvar = mercyvar
        self.ultcount = ultcount

class Hero(Attack):
    def attack(self, enemy):
        if choice2 == 'mercy':
            countera = 0
            while countera < 1: 
                horp = input('Do you want Mercy to Heal or Power Assist you? (H or P)? ').lower()
                if horp == 'h':
                    hhealer.mercyvar = 1
                    random1 = random.randint(1, (heroa.accuracy + enemya.dodge))
                    if random1 == 1:
                        enemya.health -= self.power
                        self.ultimate = int(self.power * 0.20)
                        if enemya.health <= 0:
                            print(choice3.capitalize() + " is dead.")
                            countera += 1
                            break
                        else:
                            print("You do %d damage." % self.power)
                            print("You will be healed by %d next turn." % (hhealer.heal))
                            print("You gained an extra %d ult charge and 4 passive charge." % self.ultimate)
                            print(choice2.capitalize() + " gained 4 passive ult charge.")
                            if choice3 == 'reaper':
                                if enemya.health >= 250:
                                    thealer.mercyvar = 1
                                else:
                                    thealer.mercyvar = 0
                                    randomthh = random.randint(1, (enemya.dodge + 1))
                                    if randomthh == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.20)
                                        enemya.health = min(250, enemya.health)
                                        print(choice4.capitalize() + "'s healing attempt connected.")
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                    else:
                                        thealer.ultimate = 0
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained 4 passive ult charge.")
                            else:
                                if enemya.health >= 200:
                                    thealer.mercyvar = 1
                                else:
                                    thealer.mercyvar = 0
                                    randomthh1 = random.randint(1, (enemya.dodge + 1))
                                    if randomthh1 == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.20)
                                        enemya.health = min(200, enemya.health)
                                        print(choice4.capitalize() + "'s healing attempt connected.")
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                    else:
                                        thealer.ultimate = 0
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained 4 passive ult charge.")
                            countera += 1
                    else:
                        print("You missed.")
                        if choice3 == 'reaper':
                            if enemya.health >= 250:
                                thealer.mercyvar = 1
                                print(choice3.capitalize() + " still has full health and no healing occured.")
                                print("You will be healed by %d next turn." % (hhealer.heal))
                                print("Everyone gained 4 passive ult charge.")
                            else:
                                thealer.mercyvar = 0
                                randomm5 = random.randint(1, (enemya.dodge + 1))
                                if randomm5 == 1:
                                    enemya.health += thealer.heal
                                    thealer.ultimate = int(thealer.heal * 0.20)
                                    enemya.health = min(250, enemya.health)
                                    print("You will be healed by %d next turn." % (hhealer.heal))
                                    print("You gained 4 passive ult charge.")
                                    print(choice2.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + "'s healing attempt connected.")
                                    print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 2 passive ult charge.")
                                    print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                else:
                                    thealer.ultimate = 0
                                    print("You will be healed by %d next turn." % (hhealer.heal))
                                    print("You gained 4 passive ult charge.")
                                    print(choice2.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + "'s healing attempt missed.")
                                    print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained 4 passive ult charge.")
                        else:
                            if enemya.health >= 200:
                                thealer.mercyvar = 1
                                print(choice3.capitalize() + " still has full health and no healing occured.")
                                print("You will be healed by %d next turn." % (hhealer.heal))
                                print("Everyone gained 4 passive ult charge.")
                            else:
                                thealer.mercyvar = 0
                                randomthh1 = random.randint(1, (enemya.dodge + 1))
                                if randomthh1 == 1:
                                    enemya.health += thealer.heal
                                    thealer.ultimate = int(thealer.heal * 0.20)
                                    enemya.health = min(200, enemya.health)
                                    print("You will be healed by %d next turn." % (hhealer.heal))
                                    print("You gained 4 passive ult charge.")
                                    print(choice2.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + "'s healing attempt connected.")
                                    print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                else:
                                    thealer.ultimate = 0
                                    print("You will be healed by %d next turn." % (hhealer.heal))
                                    print("You gained 4 passive ult charge.")
                                    print(choice2.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + "'s healing attempt missed.")
                                    print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained 4 passive ult charge.")
                        countera += 1
                        self.ultimate = 0
                elif horp == 'p':
                    hhealer.mercyvar = 0
                    random2 = random.randint(1, (heroa.accuracy + enemya.dodge))
                    if random2 == 1:
                        newpower = (self.power + (self.power * hhealer.assist))
                        self.ultimate = int(newpower * 0.26)
                        enemya.health -= newpower
                        if enemya.health <= 0:
                            print(choice3.capitalize() + " is dead.")
                            countera += 1
                            break
                        else:
                            print("You do %d damage." % newpower)
                            print("You will not be healed next turn.")
                            print("You gained an extra %d ult charge and 4 passive charge." % self.ultimate)
                            print(choice2.capitalize() + " gained 4 passive ult charge.")
                            if choice3 == 'reaper':
                                if enemya.health >= 250:
                                    thealer.mercyvar = 1
                                else:
                                    thealer.mercyvar = 0
                                    randomthh2 = random.randint(1, (enemya.dodge + 1))
                                    if randomthh2 == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.20)
                                        enemya.health = min(250, enemya.health)
                                        print(choice4.capitalize() + "'s healing attempt connected.")
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                    else:
                                        thealer.ultimate = 0
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained 4 passive ult charge.")
                            else:
                                if enemya.health >= 200:
                                    thealer.mercyvar = 1
                                else:
                                    thealer.mercyvar = 0
                                    randomthh3 = random.randint(1, (enemya.dodge + 1))
                                    if randomthh3 == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.20)
                                        enemya.health = min(200, enemya.health)
                                        print(choice4.capitalize() + "'s healing attempt connected.")
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                    else:
                                        thealer.ultimate = 0
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained 4 passive ult charge.")
                            countera += 1
                    else:
                        print("You missed.")
                        if choice3 == 'reaper':
                            if enemya.health >= 250:
                                thealer.mercyvar = 1
                                print(choice3.capitalize() + " still has full health and no healing occured.")
                                print("You will not be healed next turn.")
                                print("Everyone gained 4 passive ult charge.")
                            else:
                                thealer.mercyvar = 0
                                randomm6 = random.randint(1, (enemya.dodge + 1))
                                if randomm6 == 1:
                                    enemya.health += thealer.heal
                                    thealer.ultimate = int(thealer.heal * 0.20)
                                    enemya.health = min(250, enemya.health)
                                    print("You will not be healed next turn.")
                                    print("You gained 4 passive ult charge.")
                                    print(choice2.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + "'s healing attempt connected.")
                                    print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                else:
                                    thealer.ultimate = 0
                                    print("You will not be healed next turn.")
                                    print("You gained 4 passive ult charge.")
                                    print(choice2.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + "'s healing attempt missed.")
                                    print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained 4 passive ult charge.")
                        else:
                            if enemya.health >= 200:
                                thealer.mercyvar = 1
                                print(choice3.capitalize() + " still has full health and no healing occured.")
                                print("You will not be healed next turn.")
                                print("Everyone gained 4 passive ult charge.")
                            else:
                                thealer.mercyvar = 0
                                randomthh1 = random.randint(1, (enemya.dodge + 1))
                                if randomthh1 == 1:
                                    enemya.health += thealer.heal
                                    thealer.ultimate = int(thealer.heal * 0.20)
                                    enemya.health = min(200, enemya.health)
                                    print("You will not be healed next turn.")
                                    print("You gained 4 passive ult charge.")
                                    print(choice2.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + "'s healing attempt connected.")
                                    print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                else:
                                    thealer.ultimate = 0
                                    print("You will not be healed next turn.")
                                    print("You gained 4 passive ult charge.")
                                    print(choice2.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + "'s healing attempt missed.")
                                    print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained 4 passive ult charge.")
                        countera += 1
                        self.ultimate = 0
                else:
                    print("Invalid answer.")
        else:
            random3 = random.randint(1, (heroa.accuracy + enemya.dodge))
            if random3 == 1:
                newpower1 = (self.power + (self.power * hhealer.assist))
                self.ultimate = int((newpower1 * 0.25))
                enemya.health -= newpower1
                # hhealer.ultimate = int((self.power * hhealer.heal)/2)
                if enemya.health <= 0:
                    print(choice3.capitalize() + " is dead.")
                else:
                    print("You do %d damage." % newpower1)
                    print("You will be healed by %d next turn." % (hhealer.heal))
                    print("You gained an extra %d ult charge and 4 passive charge." % self.ultimate)
                    print(choice2.capitalize() + " gained 4 passive ult charge.")
                    if choice3 == 'reaper':
                        if enemya.health >= 250:
                            thealer.mercyvar = 1
                        else:
                            thealer.mercyvar = 0
                            randomthh5 = random.randint(1, (enemya.dodge + 1))
                            if randomthh5 == 1:
                                enemya.health += thealer.heal
                                thealer.ultimate = int(thealer.heal * 0.20)
                                enemya.health = min(250, enemya.health)
                                print(choice4.capitalize() + "'s healing attempt connected.")
                                print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                            else:
                                thealer.ultimate = 0
                                print(choice4.capitalize() + "'s healing attempt missed.")
                                print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                print(choice4.capitalize() + " gained 4 passive ult charge.")
                    else:
                        if enemya.health >= 200:
                            thealer.mercyvar = 1
                        else:
                            thealer.mercyvar = 0
                            randomthh6 = random.randint(1, (enemya.dodge + 1))
                            if randomthh6 == 1:
                                enemya.health += thealer.heal
                                thealer.ultimate = int(thealer.heal * 0.20)
                                enemya.health = min(200, enemya.health)
                                print(choice4.capitalize() + "'s healing attempt connected.")
                                print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                            else:
                                thealer.ultimate = 0
                                print(choice4.capitalize() + "'s healing attempt missed.")
                                print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                print(choice4.capitalize() + " gained 4 passive ult charge.")
            else:
                print("You missed.")
                if choice3 == 'reaper':
                    if enemya.health >= 250:
                        thealer.mercyvar = 1
                        print(choice3.capitalize() + " still has full health and no healing occured.")
                        print("You will be healed by %d next turn." % (hhealer.heal))
                        print("Everyone gained 4 passive ult charge.")
                    else:
                        thealer.mercyvar = 0
                        randomm1 = random.randint(1, (enemya.dodge + 1))
                        if randomm1 == 1:
                            enemya.health += thealer.heal
                            thealer.ultimate = int(thealer.heal * 0.20)
                            enemya.health = min(250, enemya.health)
                            print("You will be healed by %d next turn." % (hhealer.heal))
                            print("You gained 4 passive ult charge.")
                            print(choice2.capitalize() + " gained 4 passive ult charge.")
                            print(choice4.capitalize() + "'s healing attempt connected.")
                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                        else:
                            thealer.ultimate = 0
                            print("You will be healed by %d next turn." % (hhealer.heal))
                            print("You gained 4 passive ult charge.")
                            print(choice2.capitalize() + " gained 4 passive ult charge.")
                            print(choice4.capitalize() + "'s healing attempt missed.")
                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                else:
                    if enemya.health >= 200:
                        thealer.mercyvar = 1
                        print(choice3.capitalize() + " still has full health and no healing occured.")
                        print("You will be healed by %d next turn." % (hhealer.heal))
                        print("Everyone gained 4 passive ult charge.")
                    else:
                        thealer.mercyvar = 0
                        randomm2 = random.randint(1, (enemya.dodge + 1))
                        if randomm2 == 1:
                            enemya.health += thealer.heal
                            thealer.ultimate = int(thealer.heal * 0.20)
                            enemya.health = min(200, enemya.health)
                            print("You will be healed by %d next turn." % (hhealer.heal))
                            print("You gained 4 passive ult charge.")
                            print(choice2.capitalize() + " gained 4 passive ult charge.")
                            print(choice4.capitalize() + "'s healing attempt connected.")
                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                        else:
                            thealer.ultimate = 0
                            print("You will be healed by %d next turn." % (hhealer.heal))
                            print("You gained 4 passive ult charge.")
                            print(choice2.capitalize() + " gained 4 passive ult charge.")
                            print(choice4.capitalize() + "'s healing attempt missed.")
                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                self.ultimate = 0

    def secondary(self, enemy):
        if choice1 == 'tracer':
            hhealer.mercyvar = 1
            print(recall)
            heroa.health = max(recall)
            print("Your health has been restored to " + str(heroa.health))
        elif choice1 == 'soldier':
            counterb = 0
            if choice2 == 'mercy':
                while counterb < 1: 
                    horps = input('Do you want Mercy to Heal or Power Assist you? (H or P)? ').lower()
                    if horps == 'h':
                        hhealer.mercyvar = 1
                        randoms1 = random.randint(1, (1 + enemya.dodge))
                        if randoms1 == 1:
                            self.ultimate = int(120 * 0.20)
                            enemya.health -= 120
                            if enemya.health <= 0:
                                print("Your helix rocket connected, and " + choice3.capitalize() + " is dead.")
                            else:
                                print("Your helix rocket connects and does 120 damage.")
                                print("You will be healed by %d next turn." % (hhealer.heal))
                                print("You gained an extra %d ult charge and 4 passive charge." % self.ultimate)
                                print(choice2.capitalize() + " gained 4 passive ult charge.")
                                if choice3 == 'reaper':
                                    if enemya.health >= 250:
                                        thealer.mercyvar = 1
                                    else:
                                        thealer.mercyvar = 0
                                        randomthh7 = random.randint(1, (enemya.dodge + 1))
                                        if randomthh7 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.20)
                                            enemya.health = min(250, enemya.health)
                                            print(choice4.capitalize() + "'s healing attempt connected.")
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                                else:
                                    if enemya.health >= 200:
                                        thealer.mercyvar = 1
                                    else:
                                        thealer.mercyvar = 0
                                        randomthh8 = random.randint(1, (enemya.dodge + 1))
                                        if randomthh8 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.20)
                                            enemya.health = min(200, enemya.health)
                                            print(choice4.capitalize() + "'s healing attempt connected.")
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                            counterb += 1
                        else:
                            print("You missed.")
                            if choice3 == 'reaper':
                                if enemya.health >= 250:
                                    thealer.mercyvar = 1
                                    print(choice3.capitalize() + " still has full health and no healing occured.")
                                    print("You will be healed by %d next turn." % (hhealer.heal))
                                    print("Everyone gained 4 passive ult charge.")
                                else:
                                    thealer.mercyvar = 0
                                    randomm7 = random.randint(1, (enemya.dodge + 1))
                                    if randomm7 == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.20)
                                        enemya.health = min(250, enemya.health)
                                        print("You will be healed by %d next turn." % (hhealer.heal))
                                        print("You gained 4 passive ult charge.")
                                        print(choice2.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + "'s healing attempt connected.")
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                    else:
                                        thealer.ultimate = 0
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained 4 passive ult charge.")
                            else:
                                if enemya.health >= 200:
                                    thealer.mercyvar = 1
                                    print(choice3.capitalize() + " still has full health and no healing occured.")
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained 4 passive ult charge.")
                                else:
                                    thealer.mercyvar = 0
                                    randomthh1 = random.randint(1, (enemya.dodge + 1))
                                    if randomthh1 == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.20)
                                        enemya.health = min(200, enemya.health)
                                        print("You will be healed by %d next turn." % (hhealer.heal))
                                        print("You gained 4 passive ult charge.")
                                        print(choice2.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + "'s healing attempt connected.")
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                    else:
                                        thealer.ultimate = 0
                                        print("You will be healed by %d next turn." % (hhealer.heal))
                                        print("You gained 4 passive ult charge.")
                                        print(choice2.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained 4 passive ult charge.")
                    self.ultimate = 0
                    counterb += 1
                    if horps == 'p':
                        hhealer.mercyvar = 1
                        randoms2 = random.randint(1, (1 + enemya.dodge))
                        if randoms2 == 1:
                            self.ultimate = int(160 * 0.20)
                            enemya.health -= 160
                            if enemya.health <= 0:
                                print("Your helix rocket connected, and " + choice3.capitalize() + " is dead.")
                            else:
                                print("Your helix rocket connects and does 160 damage.")
                                print("You will not be healed next turn.")
                                print("You gained an extra %d ult charge and 4 passive charge." % self.ultimate)
                                print(choice2.capitalize() + " gained 4 passive ult charge.")
                                if choice3 == 'reaper':
                                    if enemya.health >= 250:
                                        thealer.mercyvar = 1
                                    else:
                                        thealer.mercyvar = 0
                                        randomthh9 = random.randint(1, (enemya.dodge + 1))
                                        if randomthh9 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.20)
                                            enemya.health = min(250, enemya.health)
                                            print(choice4.capitalize() + "'s healing attempt connected.")
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                                else:
                                    if enemya.health >= 200:
                                        thealer.mercyvar = 1
                                    else:
                                        thealer.mercyvar = 0
                                        randomthh10 = random.randint(1, (enemya.dodge + 1))
                                        if randomthh10 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.20)
                                            enemya.health = min(200, enemya.health)
                                            print(choice4.capitalize() + "'s healing attempt connected.")
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                        else:
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                        else:
                            print("You missed.")
                            if choice3 == 'reaper':
                                if enemya.health >= 250:
                                    thealer.mercyvar = 1
                                    print(choice3.capitalize() + " still has full health and no healing occured.")
                                    print("You will not be healed next round.")
                                    print("Everyone gained 4 passive ult charge.")
                                else:
                                    thealer.mercyvar = 0
                                    randomm8 = random.randint(1, (enemya.dodge + 1))
                                    if randomm8 == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.20)
                                        enemya.health = min(250, enemya.health)
                                        print("You will not be healed next round.")
                                        print("You gained 4 passive ult charge.")
                                        print(choice2.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + "'s healing attempt connected.")
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                    else:
                                        thealer.ultimate = 0
                                        print("You will not be healed next round.")
                                        print("You gained 4 passive ult charge.")
                                        print(choice2.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained 4 passive ult charge.")
                            else:
                                if enemya.health >= 200:
                                    thealer.mercyvar = 1
                                    print(choice3.capitalize() + " still has full health and no healing occured.")
                                    print("You will not be healed next round.")
                                    print("Everyone gained 4 passive ult charge.")
                                else:
                                    thealer.mercyvar = 0
                                    randomthh1 = random.randint(1, (enemya.dodge + 1))
                                    if randomthh1 == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.20)
                                        enemya.health = min(200, enemya.health)
                                        print("You will not be healed next round.")
                                        print("You gained 4 passive ult charge.")
                                        print(choice2.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + "'s healing attempt connected.")
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                    else:
                                        thealer.ultimate = 0
                                        print("You will be not be healed next round.")
                                        print("You gained 4 passive ult charge.")
                                        print(choice2.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained 4 passive ult charge.")
                    self.ultimate = 0
                    counterb += 1
            else:
                randoms3 = random.randint(1, (1 + enemya.dodge))
                if randoms3 == 1:
                    self.ultimate = int(150 * 0.25)
                    enemya.health -= 150
                    if enemya.health <= 0:
                        print("Your helix rocket connected, and " + choice3.capitalize() + " is dead.")
                    else:
                        print("Your helix rocket connects and does 150 damage.")
                        print("You will be healed by %d next turn." % (hhealer.heal))
                        print("You gained an extra %d ult charge and 4 passive charge." % self.ultimate)
                        print(choice2.capitalize() + " gained 4 passive ult charge.")
                        if choice3 == 'reaper':
                            if enemya.health >= 250:
                                thealer.mercyvar = 1
                            else:
                                thealer.mercyvar = 0
                                randomthh11 = random.randint(1, (enemya.dodge + 1))
                                if randomthh11 == 1:
                                    enemya.health += thealer.heal
                                    thealer.ultimate = int(thealer.heal * 0.20)
                                    enemya.health = min(250, enemya.health)
                                    print(choice4.capitalize() + "'s healing attempt connected.")
                                    print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                else:
                                    thealer.ultimate = 0
                                    print(choice4.capitalize() + "'s healing attempt missed.")
                                    print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained 4 passive ult charge.")
                        else:
                            if enemya.health >= 200:
                                thealer.mercyvar = 1
                            else:
                                thealer.mercyvar = 0
                                randomthh10 = random.randint(1, (enemya.dodge + 1))
                                if randomthh10 == 1:
                                    enemya.health += thealer.heal
                                    thealer.ultimate = int(thealer.heal * 0.20)
                                    enemya.health = min(200, enemya.health)
                                    print(choice4.capitalize() + "'s healing attempt connected.")
                                    print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                else:
                                    print(choice4.capitalize() + "'s healing attempt missed.")
                                    print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained 4 passive ult charge.")
                        counterb += 1
                else:
                    print("You missed.")
                    if choice3 == 'reaper':
                        if enemya.health >= 250:
                            thealer.mercyvar = 1
                            print(choice3.capitalize() + " still has full health and no healing occured.")
                            print("You will be healed by %d next turn." % (hhealer.heal))
                            print("Everyone gained 4 passive ult charge.")
                        else:
                            thealer.mercyvar = 0
                            randomm3 = random.randint(1, (enemya.dodge + 1))
                            if randomm3 == 1:
                                enemya.health += thealer.heal
                                thealer.ultimate = int(thealer.heal * 0.20)
                                enemya.health = min(250, enemya.health)
                                print("You will be healed by %d next turn." % (hhealer.heal))
                                print("You gained 4 passive ult charge.")
                                print(choice2.capitalize() + " gained 4 passive ult charge.")
                                print(choice4.capitalize() + "'s healing attempt connected.")
                                print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                            else:
                                thealer.ultimate = 0
                                print("You will be healed by %d next turn." % (hhealer.heal))
                                print("You gained 4 passive ult charge.")
                                print(choice2.capitalize() + " gained 4 passive ult charge.")
                                print(choice4.capitalize() + "'s healing attempt missed.")
                                print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                print(choice4.capitalize() + " gained 4 passive ult charge.")
                    else:
                        if enemya.health >= 200:
                            thealer.mercyvar = 1
                        else:
                            thealer.mercyvar = 0
                            randomm4 = random.randint(1, (enemya.dodge + 1))
                            if randomm4 == 1:
                                enemya.health += thealer.heal
                                thealer.ultimate = int(thealer.heal * 0.20)
                                enemya.health = min(200, enemya.health)
                                print("You will be healed by %d next turn." % (hhealer.heal))
                                print("You gained 4 passive ult charge.")
                                print(choice2.capitalize() + " gained 4 passive ult charge.")
                                print(choice4.capitalize() + "'s healing attempt connected.")
                                print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                            else:
                                thealer.ultimate = 0
                                print("You will be healed by %d next turn." % (hhealer.heal))
                                print("You gained 4 passive ult charge.")
                                print(choice2.capitalize() + " gained 4 passive ult charge.")
                                print(choice4.capitalize() + "'s healing attempt missed.")
                                print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                print(choice4.capitalize() + " gained 4 passive ult charge.")
            self.ultimate = 0
        elif choice1 == 'pharah':
            hhealer.mercyvar = 1
            randomp = random.randint(1, 8 + enemya.dodge)
            if randomp == 1:
                enemya.health = 0
                print("Your boop connected. " + choice3.capitalize() + " fell off the map and died.")
            else:
                print("Your boop was not successful.")

    def ultabl(self, enemy):
        if choice1 == 'tracer':
            newrandom = random.randint(1, (2 + enemya.dodge))
            if newrandom == 1:
                enemya.health -= 300
                if enemya.health <= 0:
                    print("You stuck the pulse bomb, and " + choice3.capitalize() + " is dead.")
                else:
                    enemya.health += thealer.heal
                    thealer.ultimate = int(thealer.heal * 0.20)
                    print("You stuck the pulse bomb and did 300 damage.")
                    print("You were healed by %d" % hhealer.heal)
                    print("Your ult charge is reset to 0 percent.")
                    print(choice3.capitalize() + " was healed by %d." % thealer.heal)
                    print(choice3.capitalize() + " gained 4 passive ult charge.")
            else:
                print("You missed.")
        if choice1 == 'soldier':
            if soldier.ultcount > 0:
                input("Soldier76's visor is on, and he will not miss primary fire for the next %d turn(s). Press ENTER." % self.ultcount)
                if choice2 == 'mercy':
                    countera = 0
                    while countera < 1: 
                        horp = input('Do you want Mercy to Heal or Power Assist you? (H or P)? ').lower()
                        if horp == 'h':
                            hhealer.mercyvar = 1
                            enemya.health -= self.power
                            if enemya.health <= 0:
                                print(choice3.capitalize() + " is dead.")
                                countera += 1
                                break
                            else:
                                print("You do %d damage." % self.power)
                                print("You will be healed by %d next turn." % (hhealer.heal))
                                print("Your ultimate charge is reset to 0.")
                                print(choice2.capitalize() + " gained 4 passive ult charge.")
                                if choice3 == 'reaper':
                                    if enemya.health >= 250:
                                        thealer.mercyvar = 1
                                    else:
                                        thealer.mercyvar = 0
                                        randomthh = random.randint(1, (enemya.dodge + 1))
                                        if randomthh == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.20)
                                            enemya.health = min(250, enemya.health)
                                            print(choice4.capitalize() + "'s healing attempt connected.")
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                                else:
                                    if enemya.health >= 200:
                                        thealer.mercyvar = 1
                                    else:
                                        thealer.mercyvar = 0
                                        randomthh1 = random.randint(1, (enemya.dodge + 1))
                                        if randomthh1 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.20)
                                            enemya.health = min(200, enemya.health)
                                            print(choice4.capitalize() + "'s healing attempt connected.")
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                                countera += 1
                        elif horp == 'p':
                            hhealer.mercyvar = 0
                            newpower = (self.power + (self.power * hhealer.assist))
                            enemya.health -= newpower
                            if enemya.health <= 0:
                                print(choice3.capitalize() + " is dead.")
                                countera += 1
                                break
                            else:
                                print("You do %d damage." % newpower)
                                print("You will not be healed next turn.")
                                print("Your ultimate charge is reset to 0.")
                                print(choice2.capitalize() + " gained 4 passive ult charge.")
                                if choice3 == 'reaper':
                                    if enemya.health >= 250:
                                        thealer.mercyvar = 1
                                    else:
                                        thealer.mercyvar = 0
                                        randomthh2 = random.randint(1, (enemya.dodge + 1))
                                        if randomthh2 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.20)
                                            enemya.health = min(250, enemya.health)
                                            print(choice4.capitalize() + "'s healing attempt connected.")
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                                else:
                                    if enemya.health >= 200:
                                        thealer.mercyvar = 1
                                    else:
                                        thealer.mercyvar = 0
                                        randomthh3 = random.randint(1, (enemya.dodge + 1))
                                        if randomthh3 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.20)
                                            enemya.health = min(200, enemya.health)
                                            print(choice4.capitalize() + "'s healing attempt connected.")
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                                countera += 1
                        else:
                            print("Invalid answer.")
                else:
                    newpower1 = (self.power + (self.power * hhealer.assist))
                    enemya.health -= newpower1
                    # hhealer.ultimate = int((self.power * hhealer.heal)/2)
                    if enemya.health <= 0:
                        print(choice3.capitalize() + " is dead.")
                    else:
                        print("You do %d damage." % newpower1)
                        print("You will be healed by %d next turn." % (hhealer.heal))
                        print("Your ultimate charge is reset to 0.")
                        print(choice2.capitalize() + " gained 4 passive ult charge.")
                        if choice3 == 'reaper':
                            if enemya.health >= 250:
                                thealer.mercyvar = 1
                            else:
                                thealer.mercyvar = 0
                                randomthh5 = random.randint(1, (enemya.dodge + 1))
                                if randomthh5 == 1:
                                    enemya.health += thealer.heal
                                    thealer.ultimate = int(thealer.heal * 0.20)
                                    enemya.health = min(250, enemya.health)
                                    print(choice4.capitalize() + "'s healing attempt connected.")
                                    print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                else:
                                    thealer.ultimate = 0
                                    print(choice4.capitalize() + "'s healing attempt missed.")
                                    print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained 4 passive ult charge.")
                        else:
                            if enemya.health >= 200:
                                thealer.mercyvar = 1
                            else:
                                thealer.mercyvar = 0
                                randomthh6 = random.randint(1, (enemya.dodge + 1))
                                if randomthh6 == 1:
                                    enemya.health += thealer.heal
                                    thealer.ultimate = int(thealer.heal * 0.20)
                                    enemya.health = min(200, enemya.health)
                                    print(choice4.capitalize() + "'s healing attempt connected.")
                                    print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                else:
                                    thealer.ultimate = 0
                                    print(choice4.capitalize() + "'s healing attempt missed.")
                                    print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained 4 passive ult charge.")
                heroa.ultcount -= 1
                if heroa.ultcount == 0:
                    print("Soldier's visor is now off.")
        if choice1 == 'pharah':
            if pharah.ultcount > 0:
                input("Pharah will rocket barrage for the next %d turn(s). Press ENTER to continue" % pharah.ultcount)
                if choice2 == 'mercy':
                    counterp = 0
                    while counterp < 1: 
                        rbhp = input('Do you want Mercy to Heal or Power Assist you? (H or P)? ').lower()
                        if rbhp == 'h':
                            hhealer.mercyvar = 1
                            randomrb1 = random.randint(1, (1 + enemy.dodge))
                            if randomrb1 == 1:
                                enemya.health -= 150
                                if enemya.health <= 0:
                                    print(choice3.capitalize() + " is dead.")
                                    counterp += 1
                                    break
                                else:
                                    print("You do 150 damage.")
                                    print("You will be healed by %d next turn." % (hhealer.heal))
                                    print("Your ultimate charge is reset to 0.")
                                    print(choice2.capitalize() + " gained 4 passive ult charge.")
                                    if choice3 == 'reaper':
                                        if enemya.health >= 250:
                                            thealer.mercyvar = 1
                                        else:
                                            thealer.mercyvar = 0
                                            randomrb2 = random.randint(1, (enemya.dodge + 1))
                                            if randomrb2 == 1:
                                                enemya.health += thealer.heal
                                                thealer.ultimate = int(thealer.heal * 0.20)
                                                enemya.health = min(250, enemya.health)
                                                print(choice4.capitalize() + "'s healing attempt connected.")
                                                print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                                print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                            else:
                                                thealer.ultimate = 0
                                                print(choice4.capitalize() + "'s healing attempt missed.")
                                                print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                                print(choice4.capitalize() + " gained 4 passive ult charge.")
                                    else:
                                        if enemya.health >= 200:
                                            thealer.mercyvar = 1
                                        else:
                                            thealer.mercyvar = 0
                                            randomrb3 = random.randint(1, (enemya.dodge + 1))
                                            if randomrb3 == 1:
                                                enemya.health += thealer.heal
                                                thealer.ultimate = int(thealer.heal * 0.20)
                                                enemya.health = min(200, enemya.health)
                                                print(choice4.capitalize() + "'s healing attempt connected.")
                                                print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                                print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                            else:
                                                thealer.ultimate = 0
                                                print(choice4.capitalize() + "'s healing attempt missed.")
                                                print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                                print(choice4.capitalize() + " gained 4 passive ult charge.")
                                counterp += 1
                            else:
                                print("Your rocket barrage missed.")
                                print("You will be healed by %d next turn." % (hhealer.heal))
                                print("Your ultimate charge is reset to 0.")
                                print(choice2.capitalize() + " gained 4 passive ult charge.")
                                if choice3 == 'reaper':
                                    if enemya.health >= 250:
                                        thealer.mercyvar = 1
                                    else:
                                        thealer.mercyvar = 0
                                        randomrbm1 = random.randint(1, (enemya.dodge + 1))
                                        if randomrbm1 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.20)
                                            enemya.health = min(250, enemya.health)
                                            print(choice4.capitalize() + "'s healing attempt connected.")
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                                else:
                                    if enemya.health >= 200:
                                        thealer.mercyvar = 1
                                    else:
                                        thealer.mercyvar = 0
                                        randomrbm2 = random.randint(1, (enemya.dodge + 1))
                                        if randomrbm2 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.20)
                                            enemya.health = min(200, enemya.health)
                                            print(choice4.capitalize() + "'s healing attempt connected.")
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                        elif rbhp == 'p':
                            hhealer.mercyvar = 0
                            randomrbb1 = random.randint(1, enemy.dodge)
                            if randomrbb1 == 1:
                                newrbpower = (150 + (150 * hhealer.assist))
                                enemya.health -= newrbpower
                                if enemya.health <= 0:
                                    print(choice3.capitalize() + " is dead.")
                                    counterp += 1
                                    break
                                else:
                                    print("You do %d damage." % newrbpower)
                                    print("You will not be healed next turn.")
                                    print("Your ultimate charge is reset to 0.")
                                    print(choice2.capitalize() + " gained 4 passive ult charge.")
                                    if choice3 == 'reaper':
                                        if enemya.health >= 250:
                                            thealer.mercyvar = 1
                                        else:
                                            thealer.mercyvar = 0
                                            randomrb4 = random.randint(1, (enemya.dodge + 1))
                                            if randomrb4 == 1:
                                                enemya.health += thealer.heal
                                                thealer.ultimate = int(thealer.heal * 0.20)
                                                enemya.health = min(250, enemya.health)
                                                print(choice4.capitalize() + "'s healing attempt connected.")
                                                print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                                print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                            else:
                                                thealer.ultimate = 0
                                                print(choice4.capitalize() + "'s healing attempt missed.")
                                                print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                                print(choice4.capitalize() + " gained 4 passive ult charge.")
                                    else:
                                        if enemya.health >= 200:
                                            thealer.mercyvar = 1
                                        else:
                                            thealer.mercyvar = 0
                                            randomrb5 = random.randint(1, (enemya.dodge + 1))
                                            if randomrb5 == 1:
                                                enemya.health += thealer.heal
                                                thealer.ultimate = int(thealer.heal * 0.20)
                                                enemya.health = min(200, enemya.health)
                                                print(choice4.capitalize() + "'s healing attempt connected.")
                                                print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                                print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                            else:
                                                thealer.ultimate = 0
                                                print(choice4.capitalize() + "'s healing attempt missed.")
                                                print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                                print(choice3.capitalize() + " gained 4 passive ult charge.")
                                                print(choice4.capitalize() + " gained 4 passive ult charge.")
                                counterp += 1
                            else:
                                print("Your rocket barrage missed.")
                                print("You will be healed by %d next turn." % (hhealer.heal))
                                print("Your ultimate charge is reset to 0.")
                                print(choice2.capitalize() + " gained 4 passive ult charge.")
                                if choice3 == 'reaper':
                                    if enemya.health >= 250:
                                        thealer.mercyvar = 1
                                    else:
                                        thealer.mercyvar = 0
                                        randomrbm3 = random.randint(1, (enemya.dodge + 1))
                                        if randomrbm3 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.20)
                                            enemya.health = min(250, enemya.health)
                                            print(choice4.capitalize() + "'s healing attempt connected.")
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                                else:
                                    if enemya.health >= 200:
                                        thealer.mercyvar = 1
                                    else:
                                        thealer.mercyvar = 0
                                        randomrbm4 = random.randint(1, (enemya.dodge + 1))
                                        if randomrbm4 == 1:
                                            enemya.health += thealer.heal
                                            thealer.ultimate = int(thealer.heal * 0.20)
                                            enemya.health = min(200, enemya.health)
                                            print(choice4.capitalize() + "'s healing attempt connected.")
                                            print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                        else:
                                            thealer.ultimate = 0
                                            print(choice4.capitalize() + "'s healing attempt missed.")
                                            print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                            print(choice3.capitalize() + " gained 4 passive ult charge.")
                                            print(choice4.capitalize() + " gained 4 passive ult charge.")
                                counterp += 1
                        else:
                            print("Invalid answer.")
                else:
                    randomrbb2 = random.randint(1, enemya.dodge)
                    if randomrbb2 == 1:
                        newrbpower1 = (150 + (150 * hhealer.assist))
                        enemya.health -= newrbpower1
                        # hhealer.ultimate = int((self.power * hhealer.heal)/2)
                        if enemya.health <= 0:
                            print(choice3.capitalize() + " is dead.")
                        else:
                            print("You do %d damage." % newrbpower1)
                            print("You will be healed by %d next turn." % (hhealer.heal))
                            print("Your ultimate charge is reset to 0.")
                            print(choice2.capitalize() + " gained 4 passive ult charge.")
                            if choice3 == 'reaper':
                                if enemya.health >= 250:
                                    thealer.mercyvar = 1
                                else:
                                    thealer.mercyvar = 0
                                    randomrb6 = random.randint(1, (enemya.dodge + 1))
                                    if randomrb6 == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.20)
                                        enemya.health = min(250, enemya.health)
                                        print(choice4.capitalize() + "'s healing attempt connected.")
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                    else:
                                        thealer.ultimate = 0
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained 4 passive ult charge.")
                            else:
                                if enemya.health >= 200:
                                    thealer.mercyvar = 1
                                else:
                                    thealer.mercyvar = 0
                                    randomrb7 = random.randint(1, (enemya.dodge + 1))
                                    if randomrb7 == 1:
                                        enemya.health += thealer.heal
                                        thealer.ultimate = int(thealer.heal * 0.20)
                                        enemya.health = min(200, enemya.health)
                                        print(choice4.capitalize() + "'s healing attempt connected.")
                                        print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                    else:
                                        thealer.ultimate = 0
                                        print(choice4.capitalize() + "'s healing attempt missed.")
                                        print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                        print(choice3.capitalize() + " gained 4 passive ult charge.")
                                        print(choice4.capitalize() + " gained 4 passive ult charge.")
                    else:
                        print("Your rocket barrage missed.")
                        print("You will be healed by %d next turn." % (hhealer.heal))
                        print("Your ultimate charge is reset to 0.")
                        print(choice2.capitalize() + " gained 4 passive ult charge.")
                        if choice3 == 'reaper':
                            if enemya.health >= 250:
                                thealer.mercyvar = 1
                            else:
                                thealer.mercyvar = 0
                                randomrbm6 = random.randint(1, (enemya.dodge + 1))
                                if randomrbm6 == 1:
                                    enemya.health += thealer.heal
                                    thealer.ultimate = int(thealer.heal * 0.20)
                                    enemya.health = min(250, enemya.health)
                                    print(choice4.capitalize() + "'s healing attempt connected.")
                                    print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                else:
                                    thealer.ultimate = 0
                                    print(choice4.capitalize() + "'s healing attempt missed.")
                                    print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained 4 passive ult charge.")
                        else:
                            if enemya.health >= 200:
                                thealer.mercyvar = 1
                            else:
                                thealer.mercyvar = 0
                                randomrbm4 = random.randint(1, (enemya.dodge + 1))
                                if randomrbm4 == 1:
                                    enemya.health += thealer.heal
                                    thealer.ultimate = int(thealer.heal * 0.20)
                                    enemya.health = min(200, enemya.health)
                                    print(choice4.capitalize() + "'s healing attempt connected.")
                                    print("After healing, " + choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained %d ult charge and 4 passive charge." % thealer.ultimate)
                                else:
                                    thealer.ultimate = 0
                                    print(choice4.capitalize() + "'s healing attempt missed.")
                                    print(choice3.capitalize() + "'s health is %d." % enemya.health)
                                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                                    print(choice4.capitalize() + " gained 4 passive ult charge.")
                heroa.ultcount -= 1
                if heroa.ultcount == 0:
                    print("Pharah's rocket barrage has now ended.")
    
    def healult(self, enemy):
        if choice2 == 'mercy':
            print("Mercy will increase your health by 60 for 15 straight turns.")
        if choice2 == 'zen':
            print("Zenyatta will restore you health by 300 for 6 straight turns.")

    def print_status(self):
        print("You have %d health, %d power, %d acc, and %d dodge." % (self.health, self.power, self.accuracy, self.dodge))
        print(choice3.capitalize() + " has %d health, %d power, %d acc, and %d dodge." % (enemya.health, enemya.power, enemya.accuracy, enemya.dodge))
        if choice1 == 'tracer':
            print("Your sec ability cooldown count is at %d turns." % min(cooldownh, 12))
        if choice1 == 'soldier':
            print("Your sec ability cooldown count is at %d turns." % min(cooldownh, 8))
        if choice1 == 'pharah':
            print("Your sec ability cooldown count is at %d turns." % min(cooldownh, 9))
        print("Your ult charge is at %d percent." % min(100, ulth))
        print(choice2.capitalize() + "'s ult charge is at %d percent." % (min(100, healult)))
        print(choice3.capitalize() + "'s ult charge is at %d percent." % (min(100, ulte)))
        print(choice4.capitalize() + "'s ult charge is at %d percent." % (min(100, thealult)))
        # print(choice3.capitalize() + "'s ult charge is at %d percent." % min(100, ulte))

class Talon(Attack):
    def attack(self, enemy):
        thealer.ultimate = 0
        randomt = random.randint(1, (enemya.accuracy + heroa.dodge))
        if randomt == 1:
            if self.health > 0:
                self.ultimate = int(self.power * 0.20)
                heroa.health -= self.power
                print(choice3.capitalize() + " did %d damage." % self.power)
                if thealer.mercyvar == 1:
                    randomta1 = random.randint(1, (heroa.dodge + 1))
                    if randomta1 == 1:
                        thealer.ultimate = int(thealer.assist * 0.20)
                        heroa.health -= thealer.assist
                        print(choice4.capitalize() + " also connected and did %d damage." % thealer.assist)
                    else:
                        print(choice4.capitalize() + " attempted to shoot you but missed.")
                elif thealer.mercyvar == 0:
                    print(choice4.capitalize() + " was healing and did not attempt to shoot you.")
                if heroa.health <= 0:
                    print("You are dead.")
                else:
                    print(choice3.capitalize() + " gained an extra %d ult charge and 4 passive charge." % self.ultimate)
                    print(choice4.capitalize() + " gained an extra %d ult charge and 4 passive charge." % thealer.ultimate)
                    if choice1 == 'tracer':
                        if choice2 == 'mercy':
                            print(hhealer.mercyvar)
                            if hhealer.mercyvar == 1:
                                heroa.health += hhealer.heal
                                hhealer.ultimate = int(hhealer.heal * 0.20)
                                heroa.health = min(150, heroa.health)
                        else:
                            heroa.health += hhealer.heal
                            hhealer.ultimate = int(hhealer.heal * 0.20)
                            heroa.health = min(150, heroa.health)
                    else:
                        if choice2 == 'mercy':
                            if hhealer.mercyvar == 1:
                                heroa.health += hhealer.heal
                                hhealer.ultimate = int(hhealer.heal * 0.20)
                                heroa.health = min(200, heroa.health)
                        else:
                            heroa.health += hhealer.heal
                            hhealer.ultimate = int(hhealer.heal * 0.20)
                            heroa.health = min(200, heroa.health)
                    print("After healing, your health is %d." % heroa.health)
                    print("You gained 4 passive ult charge.")
                    print(choice2.capitalize() + " gained %d ult charge along with 4 passive charge." % hhealer.ultimate)
        else:
            print(choice3.capitalize() + " missed.")
            self.ultimate = 0
            if thealer.mercyvar == 1:
                randomta2 = random.randint(1, (heroa.dodge + 1))
                if randomta2 == 1:
                    thealer.ultimate = int(thealer.assist * 0.20)
                    heroa.health -= thealer.assist
                    print(choice4.capitalize() + " connected and did %d damage." % thealer.assist)
                    if heroa.health <= 0:
                        print("You are dead.")
                    else:
                        if choice1 == 'tracer':
                            if choice2 == 'mercy':
                                if hhealer.mercyvar == 1:
                                    heroa.health += hhealer.heal
                                    hhealer.ultimate = int(hhealer.heal * 0.20)
                                    heroa.health = min(150, heroa.health)
                            else:
                                heroa.health += hhealer.heal
                                hhealer.ultimate = int(hhealer.heal * 0.20)
                                heroa.health = min(150, heroa.health)
                        else:
                            if choice2 == 'mercy':
                                if hhealer.mercyvar == 1:
                                    heroa.health += hhealer.heal
                                    hhealer.ultimate = int(hhealer.heal * 0.20)
                                    heroa.health = min(200, heroa.health)
                            else:
                                heroa.health += hhealer.heal
                                hhealer.ultimate = int(hhealer.heal * 0.20)
                                heroa.health = min(200, heroa.health)
                        print(choice3.capitalize() + " gained 4 passive charge.")
                        print(choice4.capitalize() + " gained %d ult charge along with 4 passive charge." % thealer.ultimate)
                        print("After healing, your health is %d." % heroa.health)
                        print("You gained 4 passive ult charge.")
                        print(choice2.capitalize() + " gained %d ult charge along with 4 passive charge." % hhealer.ultimate)
                else:
                    print(choice4.capitalize() + " attempted to shoot you but missed.")
                    if choice1 == 'tracer':
                        if choice2 == 'mercy':
                            if heroa.health >= 150:
                                heroa.health = min(150, heroa.health)
                            else:
                                if hhealer.mercyvar == 1:
                                    heroa.health += hhealer.heal
                                    hhealer.ultimate = int(hhealer.heal * 0.20)
                                    heroa.health = min(150, heroa.health)
                        else:
                            if heroa.health >= 150:
                                heroa.health = min(150, heroa.health)
                            else:
                                heroa.health += hhealer.heal
                                hhealer.ultimate = int(hhealer.heal * 0.20)
                                heroa.health = min(150, heroa.health)
                    else:
                        if choice2 == 'mercy':
                            if heroa.health >= 200:
                                heroa.health = min(200, heroa.health)
                            else:
                                if hhealer.mercyvar == 1:
                                    heroa.health += hhealer.heal
                                    hhealer.ultimate = int(hhealer.heal * 0.20)
                                    heroa.health = min(200, heroa.health)
                        else:
                            if heroa.health >= 200:
                                heroa.health = min(200, heroa.health)
                            else:
                                heroa.health += hhealer.heal
                                hhealer.ultimate = int(hhealer.heal * 0.20)
                                heroa.health = min(200, heroa.health)
                    print("After healing, your health is %d." % heroa.health)
                    print("You gained 4 passive ult charge.")
                    print(choice2.capitalize() + " gained %d ult charge along with 4 passive charge." % hhealer.ultimate)
                    print(choice3.capitalize() + " gained 4 passive ult charge.")
                    print(choice4.capitalize() + " gained 4 passive ult charge.")
            else:
                print(choice4.capitalize() + " was healing and did not attempt to shoot you.")
                if choice1 == 'tracer':
                    if choice2 == 'mercy':
                        if heroa.health >= 150:
                            heroa.health = min(150, heroa.health)
                        else:
                            if hhealer.mercyvar == 1:
                                heroa.health += hhealer.heal
                                hhealer.ultimate = int(hhealer.heal * 0.20)
                                heroa.health = min(150, heroa.health)
                    else:
                        if heroa.health >= 150:
                            heroa.health = min(150, heroa.health)
                        else:
                            heroa.health += hhealer.heal
                            hhealer.ultimate = int(hhealer.heal * 0.20)
                            heroa.health = min(150, heroa.health)
                else:
                    if choice2 == 'mercy':
                        if heroa.health >= 200:
                            heroa.health = min(200, heroa.health)
                        else:
                            if hhealer.mercyvar == 1:
                                heroa.health += hhealer.heal
                                hhealer.ultimate = int(hhealer.heal * 0.20)
                                heroa.health = min(200, heroa.health)
                    else:
                        if heroa.health >= 200:
                            heroa.health = min(200, heroa.health)
                        else:
                            heroa.health += hhealer.heal
                            hhealer.ultimate = int(hhealer.heal * 0.20)
                            heroa.health = min(200, heroa.health)
                print("After healing, your health is %d." % heroa.health)
                print("You gained 4 passive ult charge.")
                print(choice2.capitalize() + " gained %d ult charge along with 4 passive charge." % hhealer.ultimate)
                print(choice3.capitalize() + " gained 4 passive ult charge.")
                print(choice4.capitalize() + " gained 4 passive ult charge.")
    
    # def secondary(self, enemy):

    # def ultabl(self, enemy):

    # def healult(self, enemy):

# self, health, power, accuracy, dodge, ultimate charger, ultimate counter
tracer = Hero(150, 30, 1, 3, 0, 0)
soldier = Hero(200, 40, 1, 2, 0, 0)
pharah = Hero(200, 55, 2, 1, 0, 0)
mercy = Healer(50, 0.30, 0, 0, 0)
zen = Healer(30, 0.25, 0, 0, 0)
reaper = Talon(250, 90, 1, 1, 0, 0)
junkrat = Talon(200, 50, 2, 1, 0, 0)
widow = Talon(200, 120, 3, 2, 0, 0)
baptiste = Healer(30, 20, 0, 0, 0)
ana = Healer(75, 70, 0, 0, 0)

while 1 == 1:
    print("WELCOME TO OVERWATCH RPG"), print("")
    print("This is a 2v2 RPG featuring the heroes of Overwatch against Talon and their other enemies."), print("")
    print("HEROES"), print("")
    print("ATTACK: HP, DMG, ACC (1 high, 3 low), Dodge (1 low, 3 high), Secondary, Ultimate"), print("")
    print("TRACER: 150, 30, 1, 3, Recall: return to highest health in previous 3 turns (12 cd), Pulse Bomb: 300 dmg with stick (enemy dodge + 1 acc)")
    print("SOLDIER76: 200, 40, 1, 2, Helix Rocket: 120 dmg (enemy dodge + 1) (8 cd), Visor: 100 percent acc of primary fire for 6 straight turns")
    print("PHARAH: 200, 55, 2, 1, Boop: instakill (enemy dodge + 8) (9 cd), Barrage: 150 dmg (enemy dodge + 1) for 3 straight turns."), print("")
    print("SUPPORT: Heal/turn, DMG Assist, Sec, ULT"), print("")
    print("MERCY: +50, 30%, Resurrect: restores full health to fallen hero (30 cd), Valkyrie: increase to +60 h/t for 15 turns")
    print("ZENYETTA: +30, 25%, Orb: +48 dmg 1/5 acc (? cd), Transcendence: restores 300 hp for 6 straight turns"), print("")
    print("ENEMIES (*Note: Enemies will use Secondary and Ultimate as soon as they are able to."), print("")
    print("ATTACK:"), print("")
    print("REAPER: 250, 90, 1, 1, Wraith Form: cannot give or take dmg for 3 straight turns but receives healing (8 cd), Death Blossom: deals 170 dmg for 3 straight turns")
    print("JUNKRAT: 200, 50, 2, 1, Steel Trap: (varied probability) acc drops to 1 for 4 straight turns (10 cd), Riptire: 600 dmg 1/2 acc")
    print("WIDOWMAKER: 200, 120 bs 200 hs, 3, 2, Grapple: rest one turn and restore health (10 cd), Infra-Sight: increase acc 1/2 bs 1/4 hs for 15 turns"), print("")
    print("SUPPORT (*Note: Enemy healers will always attack until healing is required):"), print("")
    print("BAPTISTE: +60 (enemy dodge + 1), +75 dmg (hero dodge + 1), Immortality Field: prevents enemy health from dropping below 20 percent for 8 turns (20 cd), Amp Matrix: dmg assist increased to 40 percent for 4 turns")
    print("ANA: +75 (enemy dodge + 1), +70 dmg (hero dodge + 1), Sleep Dart: guarantees enemy 1/1 acc for one turn (12 cd), Nano Boost: restores enemy health full, 50 percent dmg assist, and hero dmg reduced 50 percent for 8 turns")
    while 1 == 1:
        cont = input("Press ENTER to continue")
        break
    break

while 1 == 1:
    choice1 = input("Choose your hero (Tracer, Soldier76, or Pharah): ").lower()
    if choice1 == 'tracer':
        heroa = tracer
        recall = []
        break
    elif choice1 == 'soldier':
        heroa = soldier
        break
    elif choice1 == 'pharah':
        heroa = pharah
        break
    else:
        print("Invalid choice.")
while 1 == 1:
    choice2 = input("Choose your healer (Mercy or Zenyatta): ").lower()
    if choice2 == 'mercy':
        hhealer = mercy
        break
    elif choice2 == 'zenyatta':
        hhealer = zen
        break
    else:
        print("Invalid choice.")
while 1 == 1:
    choice3 = input("Choose your enemy (Reaper, Junkrat, or Widowmaker): ").lower()
    if choice3 == 'reaper':
        enemya = reaper
        break
    elif choice3 == 'junkrat':
        enemya = junkrat
        break
    elif choice3 == 'widowmaker':
        enemya = widow
        break
    else:
        print("Invalid choice.")
while 1 == 1:
    choice4 = input("Choose your enemy's healer (Baptiste or Ana): ").lower()
    if choice4 == 'baptiste':
        thealer = baptiste
        break
    elif choice4 == 'ana':
        thealer = ana
        break
    else:
        print("Invalid choice.")

cooldownh = 12
cooldowne = 10
ulth = 0
healult = 0
ulte = 0
thealult = 0
while heroa.alive() and enemya.alive():
    while 1 == 1:
        if heroa.ultcount > 0:
            heroa.ultabl(enemya)
            break
        ulth = min(ulth, 100)
        healult = min(healult, 100)
        my_random = random.randint(1, 5)
        print("What do you want to do?")
        print("1. primary fire")
        print("2. secondary ability")
        print("3. ultimate ability")
        print("4. check status")
        print("5. run")
        user_input = input()
        if user_input == "1":
            if choice1 == 'tracer':
                recall.append(heroa.health)
                if len(recall) > 3:
                    recall.pop(0)
            heroa.attack(enemya)
            cooldownh += 1
            ulth += (4 + heroa.ultimate)
            healult += 4
            ulte += 4
            thealult += (4 + thealer.ultimate)
            break
        elif user_input == "2":
            if choice1 == 'tracer':
                recall.append(heroa.health)
                if len(recall) > 3:
                    recall.pop(0)
            if choice1 == 'tracer':
                if cooldownh < 12:
                    print("Sec ability still on cooldown.")
                else:
                    heroa.secondary(enemya)
                    cooldownh = 0
                    ulth += (4 + heroa.ultimate)
                    healult += 4
                    ulte += 4
                    thealult += (4 + thealer.ultimate)
                    break
            elif choice1 == 'soldier':
                if cooldownh < 8:
                    print("Sec ability still on cooldown.")
                else:
                    heroa.secondary(enemya)
                    cooldownh = 0
                    ulth += (4 + heroa.ultimate)
                    healult += 4
                    ulte += 4
                    thealult += (4 + thealer.ultimate)
                    break
            elif choice1 == 'pharah':
                if cooldownh < 9:
                    print("Sec ability still on cooldown.")
                else:
                    heroa.secondary(enemya)
                    cooldownh = 0
                    ulth += (4 + heroa.ultimate)
                    healult += 4
                    ulte += 4
                    thealult += (4 + thealer.ultimate)
                    break
        elif user_input == "3":
            if choice1 == 'tracer':
                recall.append(heroa.health)
                if len(recall) > 3:
                    recall.pop(0)
            if ulth == 100:
                if choice1 == 'soldier':
                    heroa.ultcount = 6
                if choice1 == 'pharah':
                    heroa.ultcount = 3
                heroa.ultabl(enemya)
                ulth = 0
                healult += 4
                ulte += 4
                thealult += (4 + thealer.ultimate)
                cooldownh += 1
                break
            else:
                print("Ultimate ability not sufficiently charged.")
        elif user_input == "4":
            heroa.print_status()
        elif user_input == "5":
            print("Goodbye.")
            heroa.health = 0
            break
        else:
            print("Invalid input")

    while heroa.alive() and enemya.alive(): 
        if healult >= 100:
            while 1 == 1:
                user_input3 = input("Use heal ult? ('Y' or 'N'): ").lower()
                if user_input3 == 'y':
                    heroa.healult(enemya)
                    healult = 0
                    break
                elif user_input3 == 'n':
                    break
                else:
                    print("Invalid choice.")
        break

    while heroa.alive() and enemya.alive():
        print(choice3.capitalize() + " will now attack. Ults will be used when possible, and sec abilities will be used as appropriate.")
        user_input2 = input("Press ENTER to continue.")
        if choice3 == 'reaper':
            # if ulte == 100:
            #     enemya.ult(heroa)
            #     cooldowne += 1
            # elif enemya.health < heroa.power:
            #     if cooldowne = 8:
            #         enemya.secondary(heroa)
            #         cooldowne = 0
            if 1 == 2:
                pass
            else:
                enemya.attack(heroa)
                ulth += 4
                healult += (4 + hhealer.ultimate)
                ulte += (4 + enemya.ultimate)
                thealult += (4 + thealer.ultimate)
                cooldowne += 1
                break
        if choice3 == 'junkrat':
            # if ulte == 100:
            #     enemya.ult(heroa)
            #     cooldowne += 1
            # elif cooldowne = 10:
            #     print("Junkrat laid a trap with his turn.")
            #     cooldowne = 0
            if 1 == 2:
                pass
            else:
                enemya.attack(heroa)
                ulth += 4
                healult += (4 + hhealer.ultimate)
                ulte += (4 + enemya.ultimate)
                thealult += (4 + thealer.ultimate)
                cooldowne += 1
                break
        if choice3 == 'widowmaker':
            # if enemya.health < heroa.power:
            #     if cooldowne = 10:
            #         enemya.secondary(heroa)
            #         cooldowne = 0
            # elif ulte == 100:
            #     enemya.ult(heroa)
            #     cooldowne += 1
            if 1 == 2:
                pass
            else:
                enemya.attack(heroa)
                ulth += 4
                healult += (4 + hhealer.ultimate)
                ulte += (4 + enemya.ultimate)
                thealult += (4 + thealer.ultimate)
                cooldowne += 1
                break