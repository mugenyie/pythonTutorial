def remove_duplicates(string):
  stringlist = list(string)
  newlist = list(set(stringlist))
  newstring = ''.join(map(str,newlist))
  lengthdiff = len(stringlist)-len(newlist)
  print "(%s,%d)" % (newstring, lengthdiff)







  

def is_isogram(word):
    if not isinstance(word, str):
        raise TypeError('Argument should be a string')
    if word.strip() == "":
        isogram = False
    if not word:
        isogram = False
    else:
        isogram = len(word) == len(set(word.lower()))
    return isogram