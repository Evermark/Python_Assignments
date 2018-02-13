bI = 455
eI = 0
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]


def FilterType(value):
    # Test type vis type function
    # Create Conditional for Value = integer and how large
    if isinstance(value,int) and value >= 100:
        print "That's a big number!"
    elif isinstance(value,int):
        print "That's a small number"
    #Create Conditional for Value = String and Length
    elif isinstance(value,str) and len(value) >= 50:
        print "Long sentence"
    elif isinstance(value,str):
        print "Short sentence"
    #Conditional for Value = List and Length
    elif isinstance(value,list) and len(value) >= 10:
        print "Big List"
    else:
        print "Small List"

FilterType(bI)
FilterType(eI)
FilterType(sS)
FilterType(mS)
FilterType(aL)
FilterType(mL)
