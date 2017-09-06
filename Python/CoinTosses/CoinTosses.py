'''
Coin Tosses '''

def cointosses():
    import random
    coin = ("head","tail")
    random_num = 0
    count_head = 0
    count_tail = 0
    print("Starting the program...")
    for i in range(1, 5001):
        random_num = random.random() 
        round_num = int(round(random_num))
        if round_num == 0:
            count_head += 1
        else:
            count_tail += 1
        print("Attempt #"+str(i)+" Throwing a coin... It's a "+coin[round_num]+"! ... Got "+str(count_head)+" head(s) so far and "+str(count_tail)+ " tail(s) so far")

    print("Ending the program, thank you!")

cointosses()
