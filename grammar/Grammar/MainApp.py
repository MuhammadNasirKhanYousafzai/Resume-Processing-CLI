import spellchecker,grammarchecker,novelty,re,zipfile,FormatDocument,ClientInfo,programing,os
from math import sqrt
from docx import Document


######################################
#    calculating scalar product      #
######################################
def scalar(collection):
  total = 0
  for coin, count in collection.items():
    total += count * count
  return sqrt(total)


######################################
#    calculating similarity product  #
######################################
def similarity(A,B): # A and B are coin collections
  '''

  this function use cosine similarity theory to calculate similarity between two documents
  '''
  total = 0
  for kind in A: # kind of coin
    if kind in B:
      total += A[kind] * B[kind]
  return float(total) / (scalar(A) * scalar(B))

###################################################################
# building priority dictionary of novel data found in documents   #
###################################################################

def buildpriorityDictionary(list):
    Dictionary={}
    for word in list:       #creating dictionary file for all possible words with initial priority of 1
            Dictionary[word]=0
    for word in list:
        Dictionary[word]=Dictionary[word]+1
    return Dictionary


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

#######################################
#      reading images from docx       #
######################################



#######################################
#      main function of module        #
######################################
def docxImages(path):
    z = zipfile.ZipFile(path)      #making zibfile of doc for reading image and data
                                             #in this case we just need images
    #print all files in zip archive
    all_files = z.namelist()            #getting all file from doc file
    #images will exist in side word/media/ directory that is default for maintaining images directory inside word side
    images = filter(lambda x: x.startswith('word/media/'), all_files)   #reading only images
    print 'images in doc',images
########################################################
#  Function for making list of  input words            #
########################################################

def inputwords(text):
    return re.findall('[A-Za-z0-9\'\".-]+', text.lower())

##################################################################
#   function for reading all docx files from a given directory   #
##################################################################
def list_files(path):
    # returns a list of names (with extension, without full path) of all files
    # in folder path
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            if name[-5:]=='.docx':

               files.append(path+"\\"+name)
    return files

if __name__ == "__main__":
    #####################################
    #            first document         #
    #####################################
    from datetime import datetime
    start_time = datetime.now()

    directory= raw_input('Enter directory of folder containing CVS (e.g E:\CV ) :')
    directory_files=list_files(directory)
    for path in directory_files:
        programing.SKILL(path)
        ClientInfo.Client(path)
        paragrahps=get_docx_text(path)
        grammarchecker.grammar(paragrahps)
        docxImages(path)        #images in document file
        FormatDocument.Document(path)
        print '\n\n\n\n--------------------next CV----------------------'
         #paragraphs in document fule
        #spellchecker.mainFunction(paragrahps)   #checking spell error
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))