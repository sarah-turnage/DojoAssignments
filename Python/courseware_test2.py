ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print drawer[0]  #prints documents
#access the drawer with index of 1 and print value
print drawer[1] #prints envelopes
#access the drawer with index of 2 and print value
print drawer[2] #prints pens

x = [1,2,3,4,5]
x.append(99)
print x
#the output would be [1,2,3,4,5,99]
x = [1,2,3,4,5]
x.insert(2,99)
print x
#the output would be [1,2,99,3,4,5]
x = [1,2,3,4,5]
x.remove(3)
print x
#the output would be [1,2,4,5]
x = [1,2,3,4,5]
x.pop()
print x
#the output would be [1,2,3,4]
y = [10,11,12,13,14]
y.pop(1)
print y
#the output would be [10,12,13,14]
x = [99,4,2,5,-3];
x.sort()
print x
#the output would be [-3,2,4,5,99];x = [99,4,2,5,-3];
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];
my_list = [1, 'Zen', 'hi']
print len(my_list)
# the output would be 3--gives number of items in the sequence
my_list = [1, 7, 3]
print max(my_list)
# the output would be 7
my_list = [1, 7, 3]
print min(my_list)
# the output would be 1my_list = [0, 'hi', '']
print any(my_list)
# the output would be True since a string would equate to true in this case
my_list = [0, '']
print any(my_list)
# the output would be False since 0 (zero) and an empty string will both be falsemy_list = [0, 'Zen', '']
print all(my_list)
# the output would be False
my_list = [4, 'hi']
print all(my_list)
# the output would be True since all are True
