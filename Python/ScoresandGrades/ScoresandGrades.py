'''
Scores and Grades Assignment'''

def scoresandgrades():
    import random
    grade = ("A","B","C","D")
    random_num = 0
    score = 0
    print("Scores and Grades")
    for i in range(0, 10):
        while score < 59:
            random_num = random.random() 
            score = int(random_num * 100)
            random_num = 0
        if score > 59 and score < 70:
            print('Score: '+str(score)+' ; Your grade is '+grade[3])
            score = 0
        elif score > 69 and score < 80:
            print('Score: '+str(score)+' ; Your grade is '+grade[2])
            score = 0
        elif score > 79 and score < 90:
            print('Score: '+str(score)+' ; Your grade is '+grade[1])
            score = 0
        else:
            print('Score: '+str(score)+' ; Your grade is '+grade[0])
            score = 0
    print("End of the program. Bye!")

scoresandgrades()
