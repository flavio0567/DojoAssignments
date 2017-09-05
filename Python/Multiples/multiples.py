'''
Multiples, Sum, Average Assignment '''

# Multiples

# printing odd numbers in a range of 1000

odds = (i for i in range(1,1000) if i%2!=0)
for i in odds:
    print i


# printing multiples of 5 in a range of 1,000,000

mult5 = (i for i in range(1,1000000) if i%5==0)
for i in mult5:
    print i

# Sum List

a = [1, 2, 5, 10, 255, 3]

print(sum(a))

# Average List

a = [1, 2, 5, 10, 255, 3]

print(sum(a)/len(a))

