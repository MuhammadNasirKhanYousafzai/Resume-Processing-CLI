import zipfile,re
def Experience(text):
    return re.findall('[0-9.]+', text.lower())   #convert text to lower case and return

def Client(path):
    z = zipfile.ZipFile(path)
    document=z.read("word/document.xml")
    string=""
    length=len(document)
    isTag=False
    paragraph={}
    paraCount=0
    addressParagraph=''
    EmailParagraph=''
    SkypeParagraph=''
    PhoneParagraph=''
    ExperienceParagraph=''
    isExperience=False
    totalExp=''
    for iterator in range(0,length):
        if iterator-5>0 and document[iterator-5:iterator]=='</w:p' and document[iterator]=='>':
            if len(string)>0:
                paragraph[paraCount]=string
                string=''
                paraCount=paraCount+1
        elif document[iterator]=='<':
            isTag=True
        elif document[iterator]=='>':
            isTag=False
        elif isTag==True:
            pass
        else:
            string=string+document[iterator]
    lengths=len(paragraph)
    #print paragraph[0]
    for iterator in range(0,lengths):
        #print paragraph[iterator].lower()
        if paragraph[iterator].lower()=='total experience:':
            totalExp=Experience( paragraph[iterator+1])
            print "Experience :",paragraph[iterator+1]

        elif paragraph[iterator].lower()=='total experience':
            totalExp=Experience( paragraph[iterator+1])
            print "Experience : ",paragraph[iterator+1]

        elif paragraph[iterator].lower()=='experience:' :
            totalExp=Experience( paragraph[iterator+1])
            print "Experience :",paragraph[iterator+1]
        elif paragraph[iterator].lower()=='experience':
            totalExp=Experience( paragraph[iterator+1])
            print "Experience :", paragraph[iterator+1]

        elif paragraph[iterator].lower()=='objectives' or paragraph[iterator].lower()=='summary':
            isExperience=True

        elif  paragraph[iterator].__contains__('Experience') or (paragraph[iterator].lower().__contains__('experience') and (paragraph[iterator].lower().__contains__('year') or paragraph[iterator].lower().__contains__('years') )) :
            totalExp=Experience( paragraph[iterator])
            if len(totalExp)>0:
                print totalExp
            pass
            #print paragraph[iterator]

        elif paragraph[iterator].lower()=='email':
            print "Email :", paragraph[iterator+1]

        elif paragraph[iterator].lower()=='email:':
            print "Email :",paragraph[iterator+1]

        elif paragraph[iterator].lower().__contains__('email:') or paragraph[iterator].lower().__contains__('email') :
            print paragraph[iterator]

        elif paragraph[iterator].lower()=='phone:':
            print "Phone :",paragraph[iterator+1]

        elif paragraph[iterator].lower()=='phone':
            print "Phone :",paragraph[iterator+1]

        elif paragraph[iterator].__contains__('Contact'):
            print paragraph[iterator]

        elif  paragraph[iterator].__contains__('Mobile Phone') or  paragraph[iterator].lower().__contains__('mobile phone#') or  paragraph[iterator].lower().__contains__('phone#') or paragraph[iterator].lower().__contains__('phone:') or \
            paragraph[iterator].lower().__contains__('cellPh#:') or paragraph[iterator].lower().__contains__('ph#:') :
            print paragraph[iterator]

        elif paragraph[iterator].lower()=='address:':
            print "Address :",paragraph[iterator+1]

        elif paragraph[iterator].lower().__contains__('contact adress') or paragraph[iterator].lower().__contains__('address:') :
            print paragraph[iterator]

        elif paragraph[iterator].lower()=='skype:':
            print "Skype :",paragraph[iterator+1]

        elif paragraph[iterator].lower()=='skype':
            print "Skype :",paragraph[iterator+1]
#Client("I://paragraph.docx")