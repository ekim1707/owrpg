# OWRPG

Hello. This was my first solo-project in coding that I worked on separately from class during our first couple weeks learning Python.

## Contents
  * What It Is
  * What We Used
  * Challenges
  * Screenshots
  * Github Link
  * Code Examples

## What It Is
This is a derivative of the RPG game exercise that we did in class as a class exercise. I thought the template that the bootcamp gave for the RPG game exercise would be a good fit with the video game Overwatch, so I thought it would be interesting and challenging to try to combine the two.

## What I Used
  * Python3

## Challenges
The greatest challenge was managing massive lines of codes. At this point in our learning, I wasn't advanced enough to be conscious of keeping code clean and efficient (i.e. by using functions rather than repetitive code blocks over and over). Thus the code is as inefficient and long as it possibly could be, and that also made for quite a challenge when trying to debug later on. I decided to leave it as it is rather than "fixing" it for the sake of preserving the integrity of my learning history and also because "fixing" it would potentially take more time than just completing it the way it already is.

## Screenshots
![alt text](https://github.com/ekim1707/owrpg/blob/master/owrpgss1.png 'owrpgss1.png')
![alt text](https://github.com/ekim1707/owrpg/blob/master/owrpgss2.png 'owrpgss2.png')

## Github Link
[Github](https://github.com/ekim1707/owrpg)

## Code Examples
  Use of classes and class constructors:
```
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
```
  An example of how managing ultimates works:
```
while heroa.alive() and enemya.alive():
print(choice3.capitalize() + " will now attack. Ults will be used when possible, and sec abilities will be used as appropriate.")
user_input2 = input("Press ENTER to continue.")
if choice3 == 'reaper':
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
```
## Contributors 
* Eugene Kim: https://github.com/ekim1707 
