'''
Type List Assignment '''

#input

my_list = ['magical unicorns',19,'hello',98.98,'world']


#output
result = ''
sum = 0

for i in my_list:
    if isinstance(i, str):
        result +=i
        result +=' '
    elif isinstance(i, int):
        sum += i
    elif isinstance(i, float):
        sum += i

if result != '' and sum > 0:
  print("The list you entered is of mixed type")
  print('String: ', result)
  print('Sum: ', sum)
elif result == '' and sum > 0:
  print("The list you entered is of integer type")
  print('Sum: ', sum)
else:
  print("The list you entered is of string type")
  print('String: ', result) 
  