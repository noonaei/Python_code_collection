pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print (original)
  word= original.lower()
  #making the word lower case, doesnt modify the actual string!
  first = word[0]
  #the first letter of the word.
  new_word=word[1:len(word)]+ first+ pyg
  #word[1:len(word)] > from the second letter till the end of the word
  # + > string concatenation
  print (new_word)
else:
  print ('empty')
