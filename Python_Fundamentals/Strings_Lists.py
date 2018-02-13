words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')

new_words = words.replace('day','month')
print new_words

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1]
print x[0],x[len(x)-1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
# sorted list [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
y = x[:5]
x = x[5:]
x.insert(0,y)
print x
