def TypeList(one_list):
    new_str = "" #Create an empty string to add to at the end of the function
    a_string = False #This boolan helps in conditional determining if item is a string
    sum = 0 #sum is 0 becuase we don't know the numer yet to be used for the sum
    for element in one_list:
        if isinstance(element, str):
            new_str += element + " "
            a_string = True
        elif isinstance(element, int):
            sum += element
        elif isinstance(element, float):
            sum += element
        else:
            Continue
    if sum > 0 and a_string == False:
        print "There are no words. You have an integer list"
    elif sum == 0 and a_string == True:
        print "There a no numbers. You have a string list"
    else:
        print "You have a mixed values list"
        print "The sum of your list is", sum
        print "String:", new_str

TypeList(["Turkey", "Cheese", 45, 22, "Dog", "Fense"])
TypeList(["baseball", "soccer", "hockey", "snowboarding"])
TypeList([43, 12, 5])
# CountString = l.Count(value)
# CountInteger = l.Count(value)
