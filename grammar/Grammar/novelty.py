from __future__ import division
import re,collections
############################################################################################################################
#
#                                   Novelty checking functions
#
############################################################################################################################

##########################################
#  Function for making list prepositions #
##########################################
def prepositions():
    file=open('prepositions//prepositions.txt','r')
    preposition=file.read()
    prepositionList=[]
    for verb in preposition.split("\n"):
        prepositionList.append(verb)
    return prepositionList

########################################################
#  Function for making list of  input words            #
########################################################

def inputwords(text):
    return re.findall('[A-Za-z0-9]+', text.lower())
########################################################
#  Function for making list of  words with lower cass  #
########################################################
def words(text):
    return re.findall('[a-z]+', text.lower())   #convert text to lower case and return


###########################################
#  Function for making list of All verbs  #
###########################################
def verbs():
    file=open('verbs//Allverbs.txt','r')
    verbslist=file.read()
    verbslist=words(verbslist)
    DictionaryVerbs={}
    for verb in verbslist:
        DictionaryVerbs[verb]=1
    return DictionaryVerbs


###################################
#         auxiliary words         #
###################################
def auxiliaryWords():
    file=open('trainingSet//auxiliaryWords.txt','r')
    words=file.read()
    wordsList=[]
    for verb in words.split("\n"):
         wordsList.append(verb)
    return wordsList



###################################
#   conjunctions List words       #
###################################
def conjunctionsList():
    file=open('conjunctions//conjectonsList.txt','r')
    words=file.read()
    conjunctionList=[]
    for verb in words.split("\n"):
        conjunctionList.append(verb)
    return conjunctionList


###################################
#   All pronouns List words       #
###################################
def Allpronouns():
    file=open('pronouns//Allprouns.txt','r')
    words=file.read()
    pronoousList=[]
    for verb in words.split("\n"):
        pronoousList.append(verb)
    return pronoousList




###################################
#   tone and mode List words      #
###################################
def ModeList():
    file=open('trainingSet//toneMode.txt','r')
    words=file.read()
    conjunctionList=[]
    for verb in words.split("\n"):
        conjunctionList.append(verb)
    return conjunctionList

###################################
#    common nouns List words      #
###################################
def nounList():
    file=open('nouns//commonNoun.txt','r')
    words=file.read()
    nounList=[]
    for verb in words.split("\n"):
        nounList.append(verb)
    return nounList


###################################
#         adverbs List words      #
###################################
def adverbsList():
    file=open('adVerb_jective//adjverbs.txt','r')
    words=file.read()
    adverbList=[]
    for verb in words.split("\n"):
        adverbList.append(verb)
    return adverbList

###################################
#       adjective List words      #
###################################
def adjectiveList():
    file=open('adVerb_jective//adjective.txt','r')
    words=file.read()
    ajactivesList=[]
    for verb in words.split("\n"):
        ajactivesList.append(verb)
    return ajactivesList

###################################
#       common words List         #
###################################
def commonwords():
    file=open('trainingSet//wordlist.txt','r')
    words=file.read()
    ajactivesList=[]
    for verb in words.split("\n"):
        ajactivesList.append(verb)
    return ajactivesList



###################################
#       Novelty function          #
###################################
def novelty(list):
    noveltylist=[]
    vervsList=verbs()       #verbs
    modeWords=ModeList()    #list for word describing mode
    pronounsList=Allpronouns()  #list of all pronouns
    conjunctionList=conjunctionsList()  #list of all conjunction
    prepositionList=prepositions()      #list of prepositions
    auxiliaryword=auxiliaryWords()
    commonNounList=nounList()
    adverbs=adverbsList()
    adjective=adjectiveList()
    commonword=commonwords()
    length=len(list)
    for iterator in range(length):
        if commonword.__contains__(list[iterator]):
            pass
            #print list[iterator],

        elif vervsList.has_key(list[iterator]):
            pass
            #print list[iterator],
        elif adjective.__contains__(list[iterator]):
            pass
            #print list[iterator],
        elif adverbs.__contains__(list[iterator]):
            pass
            #print list[iterator],

        elif pronounsList.__contains__(list[iterator]):
            pass
            #print list[iterator],
        elif modeWords.__contains__(list[iterator]):
            pass
            #print list[iterator],


        elif prepositionList.__contains__(list[iterator]):
            pass
            #print list[iterator],

        elif auxiliaryword.__contains__(list[iterator]):
            pass
            #print list[iterator],
        elif conjunctionList.__contains__(list[iterator]) :
            pass
            #print list[iterator],
        elif commonNounList.__contains__(list[iterator]) :
            #print list[iterator],
            pass
        else:
            noveltylist.append(list[iterator])


    novelty=len(noveltylist)
    percentage=(novelty/length)*100

    print 'novelty per 100 words :',percentage,'%','total words in paragraph',len(list)
    return noveltylist

#######################################
#       main function for novelty     #
#######################################
def stringNovelty(string):
    print '-------------------------------------novelty---------------------------'
    worlist=inputwords(string)
    return novelty(worlist)