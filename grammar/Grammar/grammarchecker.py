from __future__ import division
import inflect

import re,collections


#########################
#  defining alphabets   #
#########################

alphabet = 'abcdefghijklmnopqrstuvwxyz' #set of alphabets

#######################################
#  Function for making list of  words #
#######################################

def inputwords(text):
    return re.findall('[A-Za-z0-9\'\".-?]+', text.lower())   #convert text to lower case and return


########################################################
#  Function for making list of  words with lower cass  #
########################################################
def words(text):
    return re.findall('[a-z]+', text.lower())   #convert text to lower case and return



#################################################
#  Function for making Dictionary with priority #
#################################################
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



###########################################
#  Function for making list of subjects   #
###########################################
def subject():
    file=open('pronouns//subject.txt','r')
    subjectForm=file.read()
    subjectList=[]
    for verb in subjectForm.split("\n"):
        subjectList.append(verb)
    return subjectList


#################################################
#  Function for making list of objective forms  #
#################################################
def objectiveSub():
    file=open('pronouns//object.txt','r')
    objectForm=file.read()
    objectiveList=[]
    for verb in objectForm.split("\n"):
        verb=verb.strip()
        objectiveList.append(verb)
    return objectiveList

#################################################
#   for making list  preposition nouns that are not allowed #
#################################################
def prepostionNouns():
    file=open('pronouns//prepositionNouns.txt','r')
    objectForm=file.read()
    objectiveList=[]
    for verb in objectForm.split("\n"):
        verb=verb.strip()
        objectiveList.append(verb)
    return objectiveList


#################################################
# Function for making list of Possessive subject#
#################################################
def possiveSub():
    file=open('pronouns//possesive.txt','r')
    possessiveForm=file.read()
    possessiveList=[]
    for verb in possessiveForm.split("\n"):
        possessiveList.append(verb)
    return possessiveList

#################################################
#  Function for making list of First Forms verbs#
#################################################
def firstFormsOFVerbs():
    file=open('verbs//firstFormsOfVerbs.txt','r')
    firstForm=file.read()
    verbList=[]
    for verb in firstForm.split("\n"):
        verbList.append(verb)
    return verbList


#################################################
#  Function for making list of  verbs with e/es #
#################################################
def sEsFormsOFVerbs():
    file=open('verbs//sEsFormsOfVerbs.txt','r')
    sEsForm=file.read()
    verbList=[]
    for verb in sEsForm.split("\n"):
        verbList.append(verb)
    return verbList

#################################################
#  Function for making list of ing forms  verbs #
#################################################
def ingFormsOFVerbs():
    file=open('verbs//ingFormsOfVerbs.txt','r')
    ingForm=file.read()
    verbList=[]
    for verb in ingForm.split("\n"):
        verbList.append(verb)
    return verbList

#################################################
#  Function for making list of secnd forms verbs#
#################################################
def  secondFormsOFVerbs() :
    file=open('verbs//secondFormsOfVerbs.txt','r')
    secondForm=file.read()
    verbList=[]
    for verb in secondForm.split("\n"):
        verbList.append(verb)
    return verbList


#################################################
#  Function for making list of third forms verbs#
#################################################
def thirdFormsOFVerbs():
    file=open('verbs//thirdFormsOfVerbs.txt','r')
    thirdForm=file.read()
    verbList=[]
    for verb in thirdForm.split("\n"):
        verbList.append(verb)
    return verbList



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
#   tone and mode List words      #
###################################
def ModeList():
    file=open('trainingSet//toneMode.txt','r')
    words=file.read()
    conjunctionList=[]
    for verb in words.split("\n"):
        conjunctionList.append(verb)
    return conjunctionList


#################################################
#  Function for making list of auxiliary verbs  #
#################################################

def AuxiliaryVerbs():#,'may','might'
    list=['do','does','did','has','have','had','is','am','are','was','were','be','being','been','should','could','would','shall','will','may','might']
    return list
    #might ,must,can could





###########################################
#  Function for making list of relations  #
###########################################

def relationShip():
    file=open('trainingSet//relationalWork.txt','r')
    relations=file.read()
    relationList=[]
    for verb in relations.split("\n"):
        relationList.append(verb)
    return relationList



###################################
#   Function for calculating time #
###################################
def timePeriod():
    timelist=['ever','minutes','hour','hours','whole','century','centuries','years','year','months','month','days']
    return timelist

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
#   short forms  verb words       #
###################################
def shortAuxiliaryVerbs():
    dictionary={'aren\'t':'are','isn\'t':'is','doesn\'t':'does','didn\'t':'did','won\'t':'will','hasn\'t':'has','haven\'t':'have','couldn\'t':'could','don\'t':'do'}
    return dictionary

###################################
#    Order of auxiliary verbs     #
###################################
def auxiliaryVerbsOrder(auxlist):

    if len(auxlist)<2:
        return True

    elif auxlist[0]=='is':
        if len(auxlist)>2:
            return False
        elif len(auxlist)>1 and auxlist[1]!='being':
            return False
        else:
            return True

    elif auxlist[0]=='are':
        if len(auxlist)>2:
            return False
        elif len(auxlist)>1 and auxlist[1]!='being':
            return False
        else:
            return True

    elif auxlist[0]=='am':
        if len(auxlist)>2:
            return False
        elif len(auxlist)>1 and auxlist[1]!='being':
            return False
        else:
            return True

    elif auxlist[0]=='was':
        if len(auxlist)>2:
            return False
        elif len(auxlist)>1 and auxlist[1]!='being':
            return False
        else:
            return True

    elif auxlist[0]=='were':
        if len(auxlist)>2:
            return False
        elif len(auxlist)>1 and auxlist[1]!='being':
            return False
        else:
            return True

    elif auxlist[0]=='had':
        if len(auxlist)>2:
            return False
        elif len(auxlist)>1 and auxlist[1]!='been':
            return False
        else:
            return True

    elif auxlist[0]=='has':
        if len(auxlist)>2:
            return False
        if len(auxlist)>1 and auxlist[1]!='been':
            return False
        else:
            return True

    elif auxlist[0]=='have':
        if len(auxlist)>2:
            return False
        if len(auxlist)>1 and auxlist[1]!='been':
            return False
        else:
            return True

    elif auxlist[0]=='will' or auxlist[0]=='would':
        if len(auxlist)>3:
            return False
        if len(auxlist)==2 and auxlist[1]=='be':
            return True
        elif len(auxlist)==2 and auxlist[1]=='have':
            return True
        elif len(auxlist)==3 and auxlist[1]=='have' and auxlist[2]=='been' :
            return True
        else:
            return False


    elif auxlist[0]=='shall' or auxlist[0]=='should':
        if len(auxlist)>3:
            return False
        if len(auxlist)==2 and auxlist[1]=='be':
            return True
        elif len(auxlist)==2 and auxlist[1]=='have':
            return True
        elif len(auxlist)==3 and auxlist[1]=='have' and auxlist[2]=='been' :
            return True
        else:
            return False

    elif auxlist[0]=='might' or auxlist[0]=='may':
        if len(auxlist)>3:
            return False
        if len(auxlist)==2 and auxlist[1]=='be':
            return True
        elif len(auxlist)==2 and auxlist[1]=='have':
            return True
        elif len(auxlist)==3 and auxlist[1]=='have' and auxlist[2]=='been' :
            return True
        else:
            return False

###################################
#    punctuation of sentences     #
###################################
def removePunctaution(str):
    punctuation=['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
    result = ""
    #print "first index of ",str,str[0]
  #  if str.__contains__('?') and str.index('?')+1<len(str):
       # if alphabet.__contains__(str[str.index('?')+1]):
        #    print 'punchuation error',str


   # if str.__contains__('.') and str.index('.')+1<len(str):
    #      if alphabet.__contains__(str[str.index('.')+1]):
     #       print 'punchuation error',str


    #if str.__contains__(',') and str.index(',')+1<len(str):
     #   if alphabet.__contains__(str[str.index(',')+1]):
      #      print 'punchuation error',str


    for character in str:
       if(character not in punctuation):
           result += character

    return result
##############################################################
#                                                            #
#                      function for                          #
#                   check tenses mistake                     #
#                                                            #
##############################################################

def tenses(worlist):

    ###################################
    #  Forms of verbs initialization  #
    ###################################

    sub=subject()       #list for subjects
    preposition=prepositions()
    objective=objectiveSub()
    possivelist=possiveSub()
    article=False
    ###################################
    #  Forms of verbs initialization  #
    ###################################
    firstForm=firstFormsOFVerbs()   #list for first forms of verbs
    secondForm=secondFormsOFVerbs() #list for second forms of verbs
    thirdForm=thirdFormsOFVerbs()   #list for third form of verbs
    sEsForm=sEsFormsOFVerbs()       #list for sEs forms of verbs
    ingForm=ingFormsOFVerbs()       #list for ing forms of verbs
    pronounsPreposition=['of','to','for','at','in','outside','on','by','over','with','without','from','under','onto','unlike','below','within','regarding','toward']
    modelist=ModeList()
    conjuncton=conjunctionsList()
    sentenceSubjects=None #buffer list for subject
    sentenceVerbs=None        #buffer for verbs
    verblist=verbs()
    auxiliary=AuxiliaryVerbs()
    relation=relationShip()
    timeCaluation=timePeriod()
    prepositionNouns=prepostionNouns()
    endOfSentence=False
    shortform=shortAuxiliaryVerbs()
    ###################################
    #checking each sentence for errors#
    ###################################

    tempAux=[]
    length=len(worlist)
    for iterator in  range(length):

        #finding end of sentence with the help of dot(.) / questoin mark(?) /quote notation(")
        if worlist[iterator].__contains__('?') or worlist[iterator].__contains__('.') or worlist[iterator].__contains__('"'):
           worlist[iterator]=removePunctaution(worlist[iterator])
           endOfSentence=True
        #removing comma's from word and checking for punctuation
        if worlist[iterator].__contains__(','):
           worlist[iterator]=removePunctaution(worlist[iterator])
        #short forms of verbs
        if shortform.has_key(worlist[iterator]):
            worlist[iterator]=shortform[worlist[iterator]]
        #if consecutive words are same
        if iterator+1<length and worlist[iterator]==worlist[iterator+1]:
            print 'consecutive words are same',worlist[iterator],worlist[iterator+1]
        #finding subject of sentence
        elif sub.__contains__(worlist[iterator]):

            if worlist[iterator]=='that' and possivelist.__contains__(worlist[iterator+1]):
                del tempAux[:]
                sentenceSubjects=None
                article=True
            elif  sentenceSubjects==None and article==False:

                sentenceSubjects=worlist[iterator]
            elif article==True and sentenceVerbs==None and sentenceSubjects==None and len(tempAux)<1:
                sentenceSubjects=worlist[iterator]
            elif sentenceVerbs==None and len(tempAux)<1 and sentenceSubjects!=None:

               sentenceSubjects=worlist[iterator]


            elif sentenceVerbs!=None and (sentenceSubjects!=None or article==True):

                sentenceSubjects=worlist[iterator]
                del tempAux[:]
                sentenceVerbs=None

            elif (sentenceSubjects!=None or article==True) and len(tempAux)>0:
                sentenceSubjects=worlist[iterator]
                del tempAux[:]
            article=False
        elif conjuncton.__contains__(worlist[iterator]):
            sentenceSubjects=None
            del tempAux[:]
            sentenceVerbs=None

        #add auxiliary verbs to sentence
        elif auxiliary.__contains__(worlist[iterator]) and not (iterator-1>-1 and (worlist[iterator-1]=='an' or worlist[iterator-1]=='a' or worlist[iterator-1]=='the')):
                tempAux.append(worlist[iterator])
                if not auxiliaryVerbsOrder(tempAux):
                    del tempAux[:]
                    sentenceVerbs=None
                    tempAux.append(worlist[iterator])


        elif verblist.has_key(worlist[iterator])and not (iterator+1<length and auxiliary.__contains__(worlist[iterator+1])) and   sentenceVerbs!=None and not(iterator-1>-1 and objective.__contains__(worlist[iterator-1])) and not(iterator-1>-1  and modelist.__contains__(worlist[iterator-1])) and not(len(worlist)>iterator+2 and worlist[iterator+1]=='up')  and not verblist.__contains__(worlist[iterator-1]) and not possivelist.__contains__(worlist[iterator-1]) and worlist[iterator-1]!='no' and (worlist[iterator-1]!='a' and worlist[iterator-1]!='the' and worlist[iterator-1]!='an' and not conjunctionsList().__contains__(worlist[iterator-1]) and not relationShip().__contains__(worlist[iterator-1])):
            sentenceVerbs=worlist[iterator]

            ###################################
            #    without Auxiliary  verbs     #
            ###################################
            if len(tempAux)<1:
                if sentenceSubjects==None and article==False:
                    pass

                elif (sentenceSubjects=='they' or sentenceSubjects=='i' or sentenceSubjects=='that' or sentenceSubjects == 'you' or sentenceSubjects =='we') and not secondForm.__contains__(worlist[iterator]):
                    if not firstForm.__contains__(worlist[iterator]):
                        print 'first form error',worlist[iterator],worlist[iterator+1],worlist[iterator+2]

                elif worlist[iterator-1]=='can' and firstForm.__contains__(worlist[iterator]):
                    pass
                elif len(worlist)>iterator+1 and worlist[iterator+1]=='as' and thirdForm.__contains__(worlist[iterator]):
                    pass
                elif article==True and firstForm.__contains__(worlist[iterator]):
                    pass
                elif (sentenceSubjects!='they' and sentenceSubjects!='i' and sentenceSubjects != 'you' and sentenceSubjects!='we') and not secondForm.__contains__(worlist[iterator]) and not ingForm.__contains__(worlist[iterator]):
                   #if word form is not first form then it is grammatical error
                    if not sEsForm.__contains__(worlist[iterator]):
                        print 's/es Form expected error',worlist[iterator-1],worlist[iterator],worlist[iterator+1]
                elif ingForm.__contains__(worlist[iterator]) and article==True:
                    pass
                else:
                    #if sentence is has not auxiliary verb and is not second form it is error
                    if not secondForm.__contains__(worlist[iterator]):
                         print "second form expected",worlist[iterator],sentenceSubjects



            ###################################
            #       DO Auxiliary  verb        #
            ###################################

            elif tempAux[0]=='do':
                if  firstForm.__contains__(worlist[iterator]) and (sentenceSubjects=='i' or sentenceSubjects=='we' or sentenceSubjects=='they' or sentenceSubjects=='you' or article==True or sentenceSubjects==None):
                    pass
                else:
                    print 'error in use of do',worlist[iterator],worlist[iterator+1],sentenceSubjects



            ###################################
            #    Does Auxiliary  verb         #
            ###################################

            elif tempAux[0]=='does':
                if firstForm.__contains__(worlist[iterator]) and (sentenceSubjects!='i' and sentenceSubjects!='we' and sentenceSubjects!='they' and sentenceSubjects!='you'):
                   pass
                else:
                    print 'error in use of does'


            ###################################
            #     did Auxiliary  verb         #
            ###################################

            elif tempAux[0]=='did':
                if not firstForm.__contains__(worlist[iterator]):
                    print 'first form error',worlist[iterator]


            ###################################
            #    may/might Auxiliary  verb    #
            ###################################
            elif tempAux[0]=='may' or tempAux[0]=='might':
                if firstForm.__contains__(worlist[iterator]) and len(tempAux)<2 :
                    pass
                elif len(tempAux)==2 and thirdForm.__contains__(worlist[iterator]) and tempAux[1]=='be' :
                    pass

                elif len(tempAux)==3 and(thirdForm.__contains__(worlist[iterator]) or ingForm.__contains__(worlist[iterator]))and tempAux[1]=='have' and tempAux[2]=='been':
                    pass
                else:
                  print 'improper use of might',tempAux[:],worlist[iterator]



            ###################################
            #    will Auxiliary  verb         #
            ###################################
            elif tempAux[0]=='will' or tempAux[0]=='would':
                if firstForm.__contains__(worlist[iterator]) and len(tempAux)<2 and sentenceSubjects!='i' and sentenceSubjects!='we' :
                    pass

                elif len(tempAux)==2 and ingForm.__contains__(worlist[iterator]) and tempAux[1]=='be' and sentenceSubjects!='i' and sentenceSubjects!='we' :
                    pass#future indefinite tense


                elif len(tempAux)==2 and thirdForm.__contains__(worlist[iterator]) and tempAux[1]=='have' and sentenceSubjects!='i' and sentenceSubjects!='we' :
                    pass#future indefinite tense

                elif len(tempAux)==3 and (ingForm.__contains__(worlist[iterator])or thirdForm.__contains__(worlist[iterator]))and tempAux[1]=='have' and tempAux[2]=='been' and sentenceSubjects!='i' and sentenceSubjects!='we' :
                    pass#future indefinite tense
                elif article==True:
                    pass
                else:
                  print 'improper use of will',worlist[iterator],worlist[iterator+1],tempAux


            ###################################
            #    shall Auxiliary  verb        #
            ###################################
            elif tempAux[0]=='shall' or tempAux[0]=='should':
                if firstForm.__contains__(worlist[iterator]) and len(tempAux)<2 and (sentenceSubjects=='i' or sentenceSubjects=='we') :
                    pass
                elif len(tempAux)<3 and ingForm.__contains__(worlist[iterator]) and tempAux[1]=='be' and (sentenceSubjects=='i' or sentenceSubjects=='we' ):
                  #  del tempAux[:]
                        pass
                elif len(tempAux)==2 and thirdForm.__contains__(worlist[iterator]) and tempAux[1]=='have' and (sentenceSubjects=='i' or sentenceSubjects=='we' ):
                    pass#future indefinite tense
                elif len(tempAux)==2 and ingForm.__contains__(worlist[iterator]) and tempAux[1]=='have'and tempAux[1]=='been' and (sentenceSubjects=='i' or sentenceSubjects=='we' ):
                    pass#future indefinite tense
                elif article==True:
                    pass
                else:
                  #del tempAux[:]
                  print 'improper use shall',sentenceSubjects,worlist[iterator],worlist[iterator+1]
                  continue


            ###################################
            #    is Auxiliary  verb           #
            ###################################
            elif tempAux[0]=='is':

                if len(tempAux)<2 and (thirdForm.__contains__(worlist[iterator]))and  (sentenceSubjects!='i' and sentenceSubjects!='you' and sentenceSubjects!='we' and sentenceSubjects!='they' and sentenceSubjects!='these' and sentenceSubjects!='those'):
                    pass
                elif len(tempAux)<2 and (pronounsPreposition.__contains__(worlist[iterator-1])and firstForm.__contains__(worlist[iterator]))and sentenceSubjects!='i' and sentenceSubjects!='you' and sentenceSubjects!='we' and sentenceSubjects!='they' and sentenceSubjects!='these' and sentenceSubjects!='those':
                    pass
                elif len(tempAux)<2 and (ingForm.__contains__(worlist[iterator]))and  (sentenceSubjects!='i' and sentenceSubjects!='you' and sentenceSubjects!='we' and sentenceSubjects!='they' and sentenceSubjects!='these' and sentenceSubjects!='those'):
                    pass
                elif len(tempAux)==2 and tempAux[1]=='being' and  thirdForm.__contains__(worlist[iterator]) and sentenceSubjects!='i' and sentenceSubjects!='you' and sentenceSubjects!='we' and sentenceSubjects!='they' and sentenceSubjects!='these' and sentenceSubjects!='those':
                    pass
                else:
                    print 'error in use of is',sentenceSubjects,worlist[iterator],tempAux[:]

            ###################################
            #      an Auxiliary  verb         #
            ###################################
            elif tempAux[0]=='am':
                if len(tempAux)<2 and sentenceSubjects=='i' and ingForm.__contains__(worlist[iterator]):
                      pass

                elif len(tempAux)==2 and tempAux[1]=='being' and sentenceSubjects=='i' and thirdForm.__contains__(worlist[iterator]):
                    pass
                else:
                        print 'error in use of am'


            ###################################
            #     Are Auxiliary  verb         #
            ###################################
            elif tempAux[0]=='are':

                if len(tempAux)<2 and (ingForm.__contains__(worlist[iterator]) or thirdForm.__contains__(worlist[iterator])) and( sentenceSubjects=='you' or sentenceSubjects=='we' or sentenceSubjects=='they' or sentenceSubjects=='these' or sentenceSubjects=='those' or sentenceSubjects=='which' or  sentenceSubjects==None):
                    pass
                elif len(tempAux)==2 and tempAux[1]=='being' and ingForm.__contains__(worlist[iterator]) and( sentenceSubjects=='you' or sentenceSubjects=='we' or sentenceSubjects=='they' or sentenceSubjects=='these' or sentenceSubjects=='which' or sentenceSubjects=='those'or sentenceSubjects==None):
                    pass
                else:
                    print 'error in use of are',worlist[iterator],sentenceSubjects
            ###################################
            #     Was Auxiliary  verb         #
            ###################################

            elif tempAux[0]=='was':
                if len (tempAux)<2 and(ingForm.__contains__(worlist[iterator]) or thirdForm.__contains__(worlist[iterator]))and sentenceSubjects!='they' and sentenceSubjects !='you' and sentenceSubjects!='we' and sentenceSubjects!='these' and sentenceSubjects!='those':
                    pass
                elif len (tempAux)==2 and tempAux[1]=='being' and(thirdForm.__contains__(worlist[iterator]) or thirdForm.__contains__(worlist[iterator]))and sentenceSubjects!='they' and sentenceSubjects !='you' and sentenceSubjects!='we' and sentenceSubjects!='these' and sentenceSubjects!='those':
                        pass

                elif article==True:
                    pass
                else:
                    print 'improper use of was',worlist[iterator],worlist[iterator+1],sentenceSubjects


            ###################################
            #     were Auxiliary  verb         #
            ###################################
            elif tempAux[0]=='were':
                if  len (tempAux)<2 and(ingForm.__contains__(worlist[iterator]) or thirdForm.__contains__(worlist[iterator]))and (sentenceSubjects=='they' or sentenceSubjects =='you' or sentenceSubjects=='we' or sentenceSubjects=='these' or sentenceSubjects=='those' or sentenceSubjects=='that'):
                        pass

                elif  len (tempAux)==2 and(thirdForm.__contains__(worlist[iterator]) or thirdForm.__contains__(worlist[iterator]))and (sentenceSubjects=='they' or sentenceSubjects =='you' or sentenceSubjects=='we' or sentenceSubjects=='these' or sentenceSubjects=='those' or sentenceSubjects=='that'):
                        pass
                elif article==True or sentenceSubjects==None:
                    pass
                else:
                        print "improper use of were",worlist[iterator],article,sentenceSubjects



            ###################################
            #     has Auxiliary  verb         #
            ###################################
            elif tempAux[0]=='has':
                 if  len (tempAux)<2 and( thirdForm.__contains__(worlist[iterator]) ) and sentenceSubjects!='i' and sentenceSubjects!='you' and sentenceSubjects!='we' and sentenceSubjects!='they' :
                        pass
                 elif  len (tempAux)==2 and tempAux[1]=='been' and (thirdForm.__contains__(worlist[iterator]) or ingForm.__contains__(worlist[iterator])) and sentenceSubjects!='i' and sentenceSubjects!='you' and sentenceSubjects!='we' and sentenceSubjects!='they' :
                        pass
                 elif article==True:
                    pass

                 else:
                        print 'improper use of has',sentenceSubjects,worlist[iterator]#,tempAux[:]


            ###################################
            #    have Auxiliary  verb         #
            ###################################
            elif tempAux[0]=='have':
                if  len (tempAux)<2 and thirdForm.__contains__(worlist[iterator]) and (sentenceSubjects=='i' or sentenceSubjects=='you' or sentenceSubjects=='we' or sentenceSubjects=='they' or sentenceSubjects=='these' or sentenceSubjects=='those' ):
                    pass
                elif  len (tempAux)==2 and tempAux[1]=='been' and (ingForm.__contains__(worlist[iterator])or thirdForm.__contains__(worlist[iterator])) and (sentenceSubjects=='i' or sentenceSubjects=='you' or sentenceSubjects=='we' or sentenceSubjects=='they' or sentenceSubjects=='these' or sentenceSubjects=='those'):
                    pass

                elif article==True or sentenceSubjects==None:
                    pass
                else:
                    print 'improper use of have',sentenceSubjects,worlist[iterator],tempAux[:],article


            ###################################
            #     had Auxiliary  verb         #
            ###################################
            elif tempAux[0]=='had':
                if thirdForm.__contains__(worlist[iterator]):
                    pass
                elif len(tempAux)==2 and tempAux[1]=='been' and (ingForm.__contains__(worlist[iterator]) or thirdForm.__contains__(worlist[iterator])):
                    pass
                elif article==True:
                    pass
                else:
                    print 'error in use of had',worlist[iterator],worlist[iterator+1],sentenceSubjects,article

        ##################################################
        #    position of be,being,been Auxiliary  verb   #
        ##################################################

        if worlist[iterator]=='be' or worlist[iterator]=='being' or worlist[iterator]=='been':
            if sub.__contains__(worlist[iterator+1]):
                print 'error in structure',worlist[iterator],worlist[iterator+1]

        ###################################
        #     am Auxiliary  verb          #
        ###################################
        if auxiliary.__contains__(worlist[iterator]) and worlist[iterator]=='am':
            if sentenceSubjects!=None and sentenceSubjects!='i':
                print 'subject should be I'


        ###################################
        #      is Auxiliary  verb         #
        ###################################
        if auxiliary.__contains__(worlist[iterator]) and worlist[iterator]=='is':
           # print sentenceSubjects,tempAux[:],article,worlist[iterator-2],worlist[iterator-1],worlist[iterator]
            if sentenceSubjects!=None and (sentenceSubjects!='i' and sentenceSubjects!='you' and sentenceSubjects!='they' and sentenceSubjects!='we'):
                pass
            elif sentenceSubjects==None or article==True:
                pass
            else:
                print 'error in use of is',sentenceSubjects

        ###################################
        #     are Auxiliary  verb         #
        ###################################
        if auxiliary.__contains__(worlist[iterator]) and worlist[iterator]=='are':
            if sentenceSubjects!=None and ( sentenceSubjects=='you' or sentenceSubjects=='they' or sentenceSubjects=='we' or sentenceSubjects=='who',sentenceSubjects=='these' or sentenceSubjects=='those' or sentenceSubjects=='which'):
                pass
            elif sentenceSubjects==None:
                pass
            elif article==True:
                pass
            else:
                print 'improper use of are',sentenceSubjects,worlist[iterator-1],worlist[iterator+1]

        ###################################
        #     was Auxiliary  verb         #
        ###################################
        elif worlist[iterator]=='was':
            if sentenceSubjects!='they' and sentenceSubjects !='you' and sentenceSubjects!='we' and sentenceSubjects!='these' and sentenceSubjects!='those':
                pass

            elif article==True or sentenceSubjects==None:
                    pass
            else:
                    print 'improper use of was',sentenceSubjects

        ###################################
        #     were Auxiliary  verb         #
        ###################################
        elif worlist[iterator]=='were':
            if sentenceSubjects!='he' and sentenceSubjects !='she' and sentenceSubjects!='it' and sentenceSubjects!='i' :
                pass

            elif article==True or sentenceSubjects==None:
                    pass
            else:
                    print 'improper use of were',worlist[iterator-2],sentenceSubjects,article

        ###################################
        #     has Auxiliary  verb         #
        ###################################
        elif worlist[iterator]=='has':
            if sentenceSubjects!='they' and sentenceSubjects !='i' and sentenceSubjects!='you' :
                pass

            elif article==True or sentenceSubjects==None:
                    pass
            else:
                    print 'improper use of have',sentenceSubjects,worlist[iterator],worlist[iterator+1]

        ###################################
        #     have Auxiliary  verb        #
        ###################################
        elif worlist[iterator]=='have' and not(tempAux.__contains__('will') or tempAux.__contains__('would') or tempAux.__contains__('should')):
            if sentenceSubjects!='he' and sentenceSubjects !='she' and sentenceSubjects!='it' :
                pass

            elif article==True or sentenceSubjects==None:
                    pass
            elif (length>iterator+1 and worlist[iterator+1]=='been') or(length>iterator+2 and worlist[iterator+2]=='been'):
                pass
            else:
                     print 'improper use of have',sentenceSubjects,worlist[iterator],worlist[iterator+1]


        ################################################
        #  use of for and since in perfect continuous  #
        ################################################
        if worlist[iterator]=='for' or worlist[iterator]=='since':
            if len(tempAux)<2:
                pass
            elif (tempAux[0]=='have' or tempAux[0]=='has' or tempAux[0]=='had' or tempAux[0]=='shall' or tempAux[0]=='will'):
                if tempAux[1]=='been' or tempAux[1]=='have':
                    if worlist[iterator]=='for' and iterator+2<len(worlist):
                        if timeCaluation.__contains__(worlist[iterator+2]) :#or (worlist[worlist.index(word+2)]=='whole' and worlist.index(word)+3<len(worlist)):
                             pass
                        elif (worlist.index(worlist[iterator])+3<len(worlist) and worlist[iterator+1]=='a' and worlist[iterator+2]=='long' ):
                            pass
                        else:
                            print 'improper use of for'

                    elif worlist[iterator]=='since' and iterator+1<len(worlist):
                        if worlist.index(worlist[iterator])+2<len(worlist) and timeCaluation.__contains__(worlist[iterator+2]) :#or (worlist[worlist.index(word+2)]=='whole' and worlist.index(word)+3<len(worlist)):
                             print 'improper use of since'

                    else:
                        print 'incomplete sentence'


        ###################################
        #          article sub            #
        ###################################
        if worlist[iterator]=='the' or worlist[iterator]=='a' or worlist=='an':# and verblist.has_key(worlist[iterator+1]):
            vowel='aeiou'
            if worlist[iterator]=='a' or worlist[iterator]=='an':
                sentenceSubjects=None
                article=True
                if not vowel.__contains__(worlist[iterator+1][0]) and worlist[iterator]=='an':
                    print 'improper use of "a"',worlist[iterator+1]
                elif vowel.__contains__(worlist[iterator+1][0]) and worlist[iterator]=='a':
                    print 'improper use of "a"',worlist[iterator+1]
            else:
                sentenceSubjects=None
                article=True

            del tempAux[:]
            sentenceVerbs=None


        ###################################
        #      relational subject         #
        ###################################
        if possivelist.__contains__(worlist[iterator]) and length>iterator+1:
            del tempAux[:]
            sentenceVerbs=None
            sentenceSubjects=None
            article=True

        ###################################
        #      relational subject         #
        ###################################
        #if  relationShip().__contains__(worlist[iterator]) and possiveSub().__contains__(worlist[iterator-1]) :
        #    if verblist.__contains__(worlist[iterator+1]) or auxiliary.__contains__(worlist[iterator+1]):

        #        del tempAux[:]
       #         sentenceVerbs=None

        if relation.__contains__(worlist[iterator]) and possivelist.__contains__(worlist[iterator-1]):
            article=True
            sentenceSubjects=None
            sentenceVerbs=None

        ###################################
        #          propositions           #
        ###################################
        if pronounsPreposition.__contains__(worlist[iterator]):
             if iterator+1==len(worlist):
                 pass
             elif  worlist[iterator+1]=='you' or worlist[iterator+1]=='it' or worlist[iterator+1]=='that' or worlist[iterator]=='this' or worlist[iterator]=='which':#( sub.__contains__(worlist[iterator+1] and worlist[iterator+1]!='it')and worlist[iterator+1]!='you'):
                    pass
             elif worlist[iterator+1]!=None and prepositionNouns.__contains__(worlist[iterator+1]):
                 print ' this is objective pronoun expected',worlist[iterator],worlist[iterator+1]
             elif  (iterator+2)>=len(worlist) and possivelist.__contains__(worlist[iterator+1]) :
                    print 'preposition error'
           #  elif worlist[iterator+1]!='her' and ( possivelist.__contains__(worlist[iterator+1]) and not relation.__contains__(worlist[iterator+2])):
            #        print 'possessive preposition error',worlist[iterator-2],worlist[iterator-1],worlist[iterator],worlist[iterator+1],
             sentenceSubjects=None
             del tempAux[:]
             article=False
             sentenceVerbs=None
        ###################################
        #            let use              #
        ###################################

        if  worlist[iterator]=='let':

             if worlist.index('let')+1<len(worlist) and((sub.__contains__(worlist[worlist.index('let')+1]) and not worlist[worlist.index('let')+1]=='you') or (possivelist.__contains__(worlist[worlist.index('let')+1]) and not worlist[worlist.index('let')+1]=='her') ):
                 print 'let error'
        ###################################
        #        end of sentence          #
        ###################################
        if endOfSentence==True:
            sentenceSubjects=None
            article=False
            del tempAux[:]
            sentenceVerbs=None
            endOfSentence=False

###################################
#                                 #
#           Main Function         #
#                                 #
###################################
def grammar(sentence):
    worlist=inputwords(sentence)
    tenses(worlist)


#if __name__ == "__main__":
 #   #sentence='he is my friend. you shall  be waiting for her when her friend arrived,he is with he ,She can run extremely quickly.his name is nasir khan and my name is khan,where is my uncle. have been i  living here since 1980 '
  #  sentence='One of the recent developments in modern technology, cellular phones, can be a threat to safety. A study for Donald Redmond and Robert Lim of the university of Toronto showed that cellular phones poses a risk to drivers. In fact people who talk by the phone while driving are for times more likely to have an automobile accident than those whom do not use the phone while drive. I like to used my cell phone when I is driving because it was convenient. The researchers studied 699 drivers. Who were in an automobile accident while they were using they\'re cellular phones. The researchers concluded that'
   # worlist=inputwords(sentence)
    #print '-------------------------------------------sentence is -----------------------------------------'
    #print sentence
  #  print ModeList().__contains__('pity')
    #print '-------------------------------------------grammar mistakes ------------------------------------'
    #tenses(worlist)

