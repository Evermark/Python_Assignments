# def Scores_Grades():
import random
random_num = random.randint(60,100)
print "Scores and Grades"
for i in range(1,10):
    i = random_num
    # print random_num
    if i >= 60 and i <= 69:
        print "Score:" + str(i) + "; Your grade is a D."
    elif i >= 70 and i <= 79:
        print "Score:" + str(i) + "; Your grade is a C."
    elif i >= 80 and i <= 89:
        print "Score:" + str(i) + "; Your grade is a B."
    else:
        print "Score:" + str(i) + "; Your grade is a A."
