'''
Jana Frady
Drawing the Peano Curve using Turtle
'''

import turtle as peano

num = 512 # num=128 and order=4 for a complete square

peano.setup(width=num, height=num)
peano.screensize(canvwidth=num, canvheight=num, bg='black')
peano.setworldcoordinates(0, 0, peano.window_width(), peano.window_height())
peano.pencolor('white')
peano.speed(0)
peano.penup()

sS = peano.screensize()
x = peano.window_width()
y = peano.window_height()

order = 2 # number of iterations
N = 3**order # number of squares in the order
total = N * N # total number of points

path = []

def peanofunc(i):
    index = i
#               0      1      2      3      4      5      6     7       8
    points = [(0,0), (0,1), (0,2), (1,2), (1,1), (1,0), (2,0), (2,1), (2,2)]
    while i > 8:
        i -= 9

    x, y = points[i]

    for j in range(1,order+1):
   
        if index > 8:
            while index%9 != 0:
                index-=1
                
            index //= 9
            length = 3**j
            if index%9 == 0:
                pass
            
            elif index%9 == 1:
                x = length-1-x
                    
                y += length
                
            elif index%9 == 2:
                y += length*2
                
            elif index%9 == 3:
                y = length-1-y
                
                x += length
                y += length*2

            elif index%9 == 4:
                x = length-1-x
                y = length-1-y

                x += length
                y += length

            elif index%9 == 5:
                y = length-1-y
                x += length

            elif index%9 == 6:
                x += length*2

            elif index%9 == 7:
                x = length-1-x

                x += length*2
                y += length

            elif index%9 == 8:
                x += length*2
                y += length*2

    return x,y

length = x//N
for i in range(0,total):
    x = (peanofunc(i)[0]*length) + length//2
    y = (peanofunc(i)[1]*length) + length//2
    path.append((x,y))

for index in range(len(path)):
    peano.goto(path[index][0], path[index][1])
    #peano.write(index)
    peano.pendown()

peano.hideturtle()
peano.done()
