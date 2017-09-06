'''
Fun with Functions '''

# Odd/Even:

def odd_even():
    for i in range(1, 2001):
        if i % 2 == 0:
            print('Number is '+ str(i) +'.  This is an even number.')
        else:
            print('Number is '+ str(i) +'.  This is an odd number.')

odd_even()

# Multiply

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

# Hacker Challenge

def layered_multiples(arr):
    new_array = []
    for i in arr:
        k = 0
        str = ''
        while k < i:
            str += '1'
            k += 1
        new_array.append(str)
    new_array.append(str)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x

