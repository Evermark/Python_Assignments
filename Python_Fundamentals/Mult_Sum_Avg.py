# 1 to 1000
#created for loop with range to 1000
for x in range (1, 1000):
#if statement qualify x as odd using modulus operator
    if x % 2 == 1:
        print x

# 5 to 1,000,000
#create for loop with range to 1 million
for x in range (5, 1000000,5):
        print x

#Sum of List & Average
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in range (0, len(a)):
    sum = sum+a[i]
    print sum
#using sun var and divide by number of values to get average
avg = sum/len(a)
print avg
