import time

# prints out each character to simulate typing
def printing(phrase,wait=0.03):
  for let in phrase:
    print(let,end='',flush=True)
    time.sleep(wait)

# intro and loops until user exits the program
def intro(start = 0):
  if start == 0:
    printing("Hello! Welcome to the typing course!")
  printing("\nType Y to input a prompt or press ENTER for an automatically generated one.")
  response = input(" ")

  if response == "Y":
    self()
  else:
    first()
  printing("\n\n\nPress ENTER to continue or type anything to EXIT")
  response = input("")

  if response == "":
    intro(1)
  else:
    exit()

# exits the program
def exit():
  printing("\n\nGoodbye",0.02)

# function for the default prompt
def first():
  original = "The quick brown fox jumped over the lazy dog."
  printing("\n\nType this short sentence:\n\n")
  printing(original)
  printing("\n\nPress ENTER to begin")

  begin = input("")
  current = time.time()
  phrase = input("\n")
  after = time.time()

  totalTime = round(after-current,2)
  check(original,phrase,totalTime)

# prompt for the user to choose their own sentence to type
def self():
  original = printing("\nPaste your sentence or paragraph:")
  original = input(" ")

  printing("\nType this:\n\n")
  printing(original)
  printing("\n\nPress ENTER to begin")
  begin = input("")
  current = time.time()
  phrase = input("\n")
  after = time.time()
  totalTime = round(after-current,2)
  check(original,phrase,totalTime)

# checks the accuracy of what was typed
def check(original,phrase,totalTime):
  written = []
  og = []
  for x in phrase:
    written.append(x)
  for y in original:
    og.append(y)

# for each character correct, the user receives a point
  points = 0
  try:
    for z in range(len(og)):
      if og[z] == written[z]:
        points +=1
      elif written == " ":
        del written[z]
      else:
        del written[z]
        written.insert(z,og[z])
  except:
    None
  result(og,written,totalTime,points)

# prints the WPM and accuracy
def result(og,written,totalTime,points):

  try:
    WPM = round(len(og) / 5 / totalTime * 60,1)
    print("\n",WPM,sep='',end='')
    printing(" WPM")
    
    print("\n",round((points/len(og))*100,2),"%",sep='',end='')
    printing(" ACCURACY")
  except ZeroDivisionError:
    print("\nERROR calculating ACCURACY")
    None
  except:
    print("Error")
    None

# initiates the program
intro()
