str = "If monkeys like bananas, then I must be a monkey!"
print str
print str.find("monkey")
print str.replace("monkey", "alligator")

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1] #never would have gotten that second one on my own--had to look

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[0:len(x)/2]
second_list = x[len(x)/2:len(x) - 1]
print "first_list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list #don't get this one either--code review?
