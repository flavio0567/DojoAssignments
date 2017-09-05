'''
Checkerboard Assignment '''

result = ''
rows = 20
for i in xrange(rows):
  row = ''
  if i % 2 > 0.0:
    row += ' '+'* '*4
  else:
    row += '* '*4
  
  result += row + '\n'

print(result)
