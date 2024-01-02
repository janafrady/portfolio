def pali(phrase):
  counter = 0
  phrase = phrase.upper().replace(" ","")
  y = len(phrase) - 1
  for x in range(len(phrase)):
    if phrase[x] == phrase[y]:
      counter +=1
    else:
      break
    y -= 1

  if counter < len(phrase)-1:
    print("It's not a palindrome.")
  else:
    print("It's a palindrome")

phrase = input("Enter a phrase: ")

pali(phrase)
