for i in range(1, 8):
    string = ''
    for j in range(1, 8):
     if j==i or j==(8-i):
       string += '#'
     else:
          string += ' '
    print(string)