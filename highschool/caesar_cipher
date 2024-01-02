def cipher(phrase,shift):
  newWord = ''
  for letter in phrase:
    if letter.isalpha():
      if letter.islower():
        nu = ord(letter) + shift
        while nu > 122:
          nu -= 26
      elif letter.isupper():
        nu = ord(letter) + shift
        while nu > 90:
          nu -= 26
    else:
      nu = ord(letter)
    ch = chr(nu)
    newWord += ch
  return newWord

  
# asks user for phrase and shift amount
phrase = input("Enter a message: ")
while True:
  try:
    shift = int(input("Shift value: "))
    if shift >= 1 and shift <=25:
      break
    else:
      print("\nEnter a value between 1 and 25.")
  except:
    print("\nEnter a value between 1 and 25.")

print(cipher(phrase,shift))
