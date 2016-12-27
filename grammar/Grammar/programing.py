import re
import zipfile
from docx import Document
#########################
#  defining alphabets   #
#########################

alphabet = 'abcdefghijklmnopqrstuvwxyz' #set of alphabets

########################################################
#  Function for making list of  words with lower cass  #
########################################################
def inputwords(text):
    return re.findall('[A-Za-z0-9-.@+*#:]+', text.lower())


#def words(text):
 #   return re.findall('[a-z]+', text.lower())   #convert text to lower case and return
######################################
#    reading text from docx file     #
######################################
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile

"""
Module that extract text from MS XML Word document (.docx).
(Inspired by python-docx <https://github.com/mikemaccana/python-docx>)
"""


WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'

def get_docx_text(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)

    paragraphs = []
    for paragraph in tree.getiterator(PARA):
        texts = [node.text
                 for node in paragraph.getiterator(TEXT)
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))

    return '\n\n'.join(paragraphs)


#################################
#        Php Programming        #
#################################
def phpProg():
    file=open('trainingset//php.txt','r')
    subjectForm=file.read()
    subjectList={}
    for verb in subjectForm.split("\n"):
        subjectList[verb.lower()]=1
    return subjectList

#################################
#      javascript function      #
#################################
def javascriptProg():
    file=open('trainingset//javascript.txt','r')
    subjectForm=file.read()
    subjectList={}
    for verb in subjectForm.split("\n"):
        subjectList[verb.lower()]=1
    return subjectList

#####################################
#        android Programming        #
#####################################
def andriodProg():
    file=open('trainingset//android.txt','r')
    subjectForm=file.read()
    subjectList={}
    for verb in subjectForm.split("\n"):
        subjectList[verb.lower()]=1
    return subjectList

#############################################
#        database   cms  Programming        #
#############################################
def cmsProg():
    file=open('trainingset//cms.txt','r')
    subjectForm=file.read()
    subjectList={}
    for verb in subjectForm.split("\n"):
        subjectList[verb.lower()]=1
    return subjectList

#################################
#        database server        #
#################################
def databaseSeverProg():
    file=open('trainingset//databaseSever.txt','r')
    subjectForm=file.read()
    subjectList={}
    for verb in subjectForm.split("\n"):
        subjectList[verb.lower()]=1
    return subjectList


##########################################
#        html and css programming        #
##########################################
def htmandcssProg():
    file=open('trainingset//htmlCss.txt','r')
    subjectForm=file.read()
    subjectList={}
    for verb in subjectForm.split("\n"):
        subjectList[verb.lower()]=1
    return subjectList


#################################
#          ides tools           #
#################################
def IdesSeverProg():
    file=open('trainingset//Ides.txt','r')
    subjectForm=file.read()
    subjectList={}
    for verb in subjectForm.split("\n"):
        subjectList[verb.lower()]=1
    return subjectList


#################################
#          ORMs tools           #
#################################
def ormProg():
    file=open('trainingset//ORM.txt','r')
    subjectForm=file.read()
    subjectList={}
    for verb in subjectForm.split("\n"):
        subjectList[verb.lower()]=1
    return subjectList


#################################
#        java programming       #
#################################
def javaProg():
    file=open('trainingset//java.txt','r')
    subjectForm=file.read()
    subjectList={}
    for verb in subjectForm.split("\n"):
        subjectList[verb.lower()]=1
    return subjectList

##################################
#       python programming       #
##################################
def pythonProg():
    file=open('trainingset//python.txt','r')
    subjectForm=file.read()
    subjectList={}
    for verb in subjectForm.split("\n"):
        subjectList[verb.lower()]=1
    return subjectList


##################################
#       dotNet programming       #
##################################
def dotNetProg():
    file=open('trainingset//dotNEt.txt','r')
    subjectForm=file.read()
    subjectList={}
    for verb in subjectForm.split("\n"):
        subjectList[verb.lower()]=1
    return subjectList



########################################################
#        function for getting programming terms        #
########################################################
def SKILL(path):
    file=open('trainingset//programmingterms.txt','r')
    paragrahps=get_docx_text(path)
    subjectList={}
    subjectForm=file.read()
    programmingTerms=[]
    wordlist=inputwords(paragrahps)
    for verb in subjectForm.split("\n"):
        subjectList[verb.lower()]=1
    length=len(wordlist)

    for iterator in range(0,length):
        if wordlist[iterator-1]=='sql' and wordlist[iterator]=='sever':
            print 'this is test'
        if iterator-2>0 and subjectList.has_key(str(wordlist[iterator-2]+' '+wordlist[iterator-1]+' '+wordlist[iterator])):
            programmingTerms.append(str(wordlist[iterator-2]+' '+wordlist[iterator-1]+' '+wordlist[iterator]))
        elif iterator-1>0 and subjectList.has_key(str(wordlist[iterator-1]+' '+wordlist[iterator])):

            programmingTerms.append(str(wordlist[iterator-1]+' '+wordlist[iterator]))
        elif iterator-1>0 and subjectList.has_key(str("microsoft "+str(wordlist[iterator-1]+' '+wordlist[iterator]))):
            programmingTerms.append(str("microsoft "+str(wordlist[iterator-1]+' '+wordlist[iterator])))
        elif subjectList.has_key(str(wordlist[iterator])):
            programmingTerms.append(str( wordlist[iterator]))
        elif subjectList.has_key(str(wordlist[iterator]+" cms")):
            programmingTerms.append( wordlist[iterator]+' cms')
    programmingTerms=set(programmingTerms[:])
    ##################################
    #    programming skill ranking   #
    ##################################
    python=pythonProg()
    php=phpProg()
    java=javaProg()
    ORM=ormProg()
    databaseSevers=databaseSeverProg()
    ides=IdesSeverProg()
    andriod=andriodProg()
    htmlcss=htmandcssProg()
    cms=cmsProg()
    dotNet=dotNetProg()
    javascript=javascriptProg()

    ######################################
    #    variables for holding ranking   #
    ######################################

    pythonPt=0
    phpPt=0
    javaPt=0
    ORMPt=0
    databaseSeversPt=0
    idesPt=0
    andriodPt=0
    htmlcssPt=0
    cmsPt=0
    dotNetPt=0
    javascriptPt=0
    for progLng in programmingTerms:
        if python.has_key(progLng):
            pythonPt=pythonPt+1
        elif php.has_key(progLng):
            #print progLng
            phpPt=phpPt+1
        elif java.has_key(progLng):
            javaPt=javaPt+1
        elif databaseSevers.has_key(progLng):
            databaseSeversPt=databaseSeversPt+2
        elif ides.has_key(progLng):
            print 'ide',progLng
            idesPt=idesPt+1
        elif andriod.has_key(progLng):
            andriodPt=andriodPt+1
        elif htmlcss.has_key(progLng):
            htmlcssPt=htmlcssPt+1
        elif dotNet.has_key(progLng):
            dotNetPt=dotNetPt+1
        elif javascript.has_key(progLng):
            javascriptPt=javascriptPt+1
        if ORM.has_key(progLng):
            ORMPt=ORMPt+1
        if cms.has_key(progLng):
            cmsPt=cmsPt+1
    #######################################
    #  printing programmer skills
    #######################################
    if cmsPt>0:
        print 'cms :',cmsPt,
    if pythonPt>0:
        print 'Python :',pythonPt
    if phpPt > 0:
        print 'Php :',phpPt,
    if javaPt>0:
        print 'Java :',javaPt
    if databaseSeversPt>0:
        print 'database severs :',databaseSeversPt
    if idesPt>0:
        print 'IDE\'s :',idesPt,
    if andriodPt>0:
        print 'andriod :',andriodPt,
    if htmlcssPt>0:
        print 'html and css :',htmlcssPt
    if dotNetPt>0:
        print '.NET :',dotNetPt,
    if ORMPt>0:
        print 'ORM :',ORMPt,
    if javascriptPt>0:
        print 'JavaScript :',javascriptPt

    #print programmingTerms



