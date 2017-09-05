#  Find and Replace

words = "It's thanksgiving day. It's my birthday,too!"

words.find('day')     #  result = 18

newwords = words.replace('day', 'month',1)

print newwords        # result is "It's thanksgiving month. It's my birthday,too!"


# Min and Max

x = [2,54,-2,7,12,98]

print max(x)          # returns 98

print min(x)          # returns -2


# First and Last

x = ["hello",2,54,-2,7,12,98,"world"]

print x[:1]           # returns [‘hello’]

print x[len(x)-1:]    # ‘world’

y = x[:1]
y += x[len(x)-1:]     # result is  y = [‘hello’, ‘world’]


# New List

x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()              #  [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]


y = len(x)//2
half1 = x[:y] 
half2 = x[y:]

print "first half of the list", half1   # [-3, -2, 2, 6, 7]
print "second half of the list", half2  # [10, 12, 19, 32, 54, 98]

half2.insert(0,half1)                   # [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]

print(half2)
