found = False

multipos = 1
first = -99
second = 78 

def ggt(x, y):
   z = x % y
   if z == 0:
      return y
   return ggt(y, z)

while not found:
    if int((first*multipos-ggt(first,second))/second) == (first*multipos-ggt(first,second))/second:
        found = True
        print(multipos)
    multipos += 1
