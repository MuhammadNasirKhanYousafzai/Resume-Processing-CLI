import re,collections
alphabet = 'abcdefghijklmnopqrstuvwxyz' #set of alphabets


def inputwords(text):
    return re.findall('[A-Za-z]+', text)   #convert text to lower case and return


#function for building word list from input file
def words(text):
    return re.findall('[a-z]+', text.lower())   #convert text to lower case and return
#building dictionary that will contain all english words with priorities
def buildDictionary():
    Dictionary={}
    worden=open("trainingSet//wordsEn.txt",'r')   #file containing all english words
    trainingSet=open("trainingSet//big.txt",'r') #file containing training data set to build priority

    wordlist=words(worden.read())          #creating word list of all english words
    wordpriority=words(trainingSet.read()) #creating word list of all world occurs in training data set

    for word in wordlist:       #creating dictionary file for all possible words with initial priority of 1
        Dictionary[word]=1

    for word in wordpriority:   #buiding piority of words from a big set of data
        try:
           word=word.lower()
           Dictionary[word]=Dictionary[word]+1
        except:                     #if word is not in dictionary add it.because our training is reliable
            Dictionary[word]=1
    return Dictionary       #return the dictionary


def spellCorrection(word):
   wordx=buildDictionary()
   if len(word)<3:
    matched=[]
    matched.append(word[1]+word[0])
    for alphabets in range(len(word)):
        for val in alphabet:
            matched.append(word[alphabets]+val)
    sets=set(matched)

    return max(sets, key=wordx.get)
   else:
       splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
       #print "edit", splits
       deletes    = [a + b[1:] for a, b in splits if b]
       #print "delete",deletes
       transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
       #print transposes
       replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
       #print replaces
       inserts    = [a + c + b     for a, b in splits for c in alphabet]
      # print "here is insert", inserts
       sets= set(deletes + transposes + replaces + inserts)
       return max(sets, key=wordx.get)










def mainFunction( sentence):
    Dictionary=buildDictionary()
    spellerrors=0
    novelityerrors=0
    novelList=[]
    tediouserrors=0
    marginError=0
    grammarError=0

    worlist=inputwords(sentence)


    for word in worlist:
        try:
           # print word
            Dictionary[word.lower()]
        except:
           # correctWord=spellCorrection(word.lower())
            #try:
             #   if Dictionary[correctWord]:
              #      print "spell error ",word,"correction",correctWord
               #     spellerrors=spellerrors+1
           # except:
          #      if word[0]==correctWord[0].upper():
                 #   print "novel ",word
           #         novelityerrors=novelityerrors+1
            #        novelList.append(word)
               pass
               # else:
                  #  print "tedious error",word
             #       tediouserrors=tediouserrors+1

    print "spell errors :",spellerrors
    print "tedious errors",tediouserrors
