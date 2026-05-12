# начальные условия
x = 10
y = 0
# первое условие в цикле
while x != 5:
   y = y+2*y-3
   x = x-1
# вторая ветвь
if x == y:
   x = x-y
   y = y+x
else:
   x = x+y
   y = y-x
print(y)