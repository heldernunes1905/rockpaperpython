import random
#rps goes in values of 1,2,3 lower number loses unless its 1 and 3 bc 3 will beat 1

def checkwinner(hand,robothand): #check who won
    if(hand == robothand):#both are same value
        return "Tie"
    
    elif(hand == 3 or robothand == 3): #if one is scissors then they compare individually
        
        if(hand == 3 and robothand == 1 or hand == 2 and robothand == 3): 
            return "Sadly you loose"
        elif(hand == 3 and robothand == 2 or hand == 1 and robothand == 3):
            return "Congrats on winning"    

    elif(hand < robothand):#user has lower so they lose
        return "Sadly you loose"

    
    elif(hand > robothand):#bot is lower so user wins
        return "Congrats on winning"

    return 0
    
def checkinputted(hand):
    if(hand == "1" or hand == "2" or hand == "3"):
        return hand
    elif(hand == "rock" or hand == "paper" or hand == "scissors" ):
        if(hand == "rock"):
            hand = 1
        elif(hand == "paper"):
            hand = 2
        elif(hand == "scissors"):
            hand = 3
    else:
        return 0
    return hand

#just print what was chosen
def turntostring(h,rh):
    if(h == 1):
        print("You chose Rock")
    elif(h == 2):
        print("You chose Paper")
    elif(h == 3):
        print("You chose Scissors")

    if(rh == 1):
        print("The bot chose Rock")
    elif(rh == 2):
        print("The bot chose Paper")
    elif(rh == 3):
        print("The bot chose Scissors")



print("Choose your hand:")
print("1-rock")
print("2-paper")
print("3-scissors")

hand = input().lower()#make input lowercase just in case user inputs string
robothand = random.randint(1,3)#get random number

hand = int(checkinputted(hand))#check what was inputed and turn into int
turntostring(hand,robothand)# show what was chosen by user and the bot


if(hand != 0):#if 0 means user inputted something they shouldnt
    winner = checkwinner(hand,robothand)#check who won
    print(winner)
else:
    print("Wrong value inserted")

