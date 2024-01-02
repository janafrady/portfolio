def anagram(first,second):
  fList = []
  sList = []

  for letter in first.upper().replace(" ",""):
    fList.append(letter)
  for letter in second.upper().replace(" ",""):
    sList.append(letter)
  fList.sort()
  sList.sort()

  counter = 0
  if len(fList) == len(sList):
    if fList == sList:
      counter = 1
    else:
      return "\nNot anagrams"
  else:
    return "\nNot anagrams"

  if counter < 1:
    return "\nNot anagrams"
  elif fList == [] and sList == []:
    return "\nNot anagrams"
  else:
    return "\nAnagrams"
  

first = input("First text: ")
second = input("Second text: ")

print(anagram(first,second))
