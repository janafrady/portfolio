# Imported to use square root function in area calculation
import math

# Imported turtle to use drawing feature
import turtle

sc = turtle.Screen()
sc.setup(500, 200)
sc.bgcolor("gray")
turtle.shape("turtle")
turtle.setheading(90)
sc.title("Drawing of the Triangle")


# Number of triangles input
amount = ''


while amount.strip() == '':
  try:
    amount = int(input("How many triangles? "))
    break
  except:
    print('')
    print("Enter an integer")


# Defines triangle function
def triangle(amount):
  
    marker = 0
  
    while marker < amount:
  
  # Side length inputs
  
      a = ''
      b = ''
      c = ''
      breakOut = 0
  
      while breakOut == 0:
        try:
          print(" ")
          print("")
          print("Enter side lengths.")
          a = int(input("Side 1: "))
          b = int(input("Side 2: "))
          c = int(input("Side 3: "))
          break
        except:
          print('')
          print("Enter integers.")
  
      check = 0
  
  # Resorting values from smallest to largest
      values = []
      values.extend([a, b, c])
      values.sort()
      a = int(values[0])
      b = int(values[1])
      c = int(values[2])
  
  # s calculation for the area formula
      s = ((a + b + c) / 2)
  
  # Checks if the sides create a triangle
      if a + b > c:
        check = 1
      else:
        print('')
        print("not a triangle")
      marker += 1
  
  # If it is a triangle
      if check == 1:
  
  # Calculates the perimeter
        perimeter = a + b + c
  
  # Calculates the area
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
  
  # Checks if the triangle is equilateral, scalene, or isosceles
        type = ["equilateral", "scalene", "isosceles"]
        if a == b == c:
          type_name = type[0]
        if a != b and a != c and b != c:
          type_name = type[1]
        if a == b and b != c or b == c and b != a or a == c and a != b:
          type_name = type[2]
  
  # Checks if the triangle is acute, right, or obtuse
        pytha = ["acute", "right", "obtuse"]
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
          pytha_name = pytha[1]
        if pow(a, 2) + pow(b, 2) > pow(c, 2):
          pytha_name = pytha[0]
        if pow(a, 2) + pow(b, 2) < pow(c, 2):
          pytha_name = pytha[2]
  
  # Prints all values
        print(' ')
        print("P = " + str(perimeter) + '    ' + "A = " + str(round(area, 3)) + '    ' + type_name + '    ' + pytha_name)
  
  # Law of Cosines to find angles
  
        angleA = math.acos((pow(a, 2) - pow(b, 2) - pow(c, 2)) / (-2 * b * c))
        angleA = round(angleA * (180 / (math.pi)), 3)
        print("side a: " + str(a) + "     " + "angle A: " + str(angleA))
  
        angleB = math.acos((pow(b, 2) - pow(a, 2) - pow(c, 2)) / (-2 * a * c))
        angleB = round(angleB * (180 / (math.pi)), 3)
        print("side b: " + str(b) + "     " + "angle B: " + str(angleB))
  
        angleC = math.acos((pow(c, 2) - pow(a, 2) - pow(b, 2)) / (-2 * a * b))
        angleC = round(angleC * (180 / (math.pi)), 3)
        print("side c: " + str(c) + "     " + "angle c: " + str(angleC))
  
  # Turtle draws triangle
  
        turtle.clear()
        turtle.showturtle()
        turtle.setpos(0,0)
        turtle.pendown()
        turtle.pencolor('blue')
        turtle.setheading(90)
        turtle.right(90 - angleC)
        turtle.fd(b*10)
        turtle.right(180 - angleA)
        turtle.fd(c*10)
        turtle.right(180 - angleB)
        turtle.fd(a*10)  
  
  # Label the sides
        turtle.hideturtle()
        turtle.penup()
        turtle.pencolor('black')
        turtle.setposition((8*a),(8*b))
        turtle.write(c)
  
        turtle.setposition((-6*a),(5*b))
        turtle.write(b)
  
        turtle.setposition((a*6),(-5*b))
        turtle.write(a)

triangle(amount)
