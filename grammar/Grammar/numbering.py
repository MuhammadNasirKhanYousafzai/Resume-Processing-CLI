import zipfile,textFormatting
def indentLevel(style):
    isNumberFormat=False
    isLevelText=False
    levelValue={}
    lvlCount=0
    isJustification=False
    length=len(style)

    for iterator in range(0,length):
        if iterator-7>0 and style[iterator-7:iterator]=='<w:lvl ':
            levelValue[lvlCount]=textFormatting.listStyle()


        elif iterator-7>0 and style[iterator-7:iterator]=='</w:lvl' and style[iterator]=='>':
            lvlCount=lvlCount+1

        elif style[iterator-16:iterator]=='<w:numFmt w:val=':
            isNumberFormat=True

        elif isNumberFormat==True and style[iterator]=='"':
            isNumberFormat=False

        elif isNumberFormat==True:
            levelValue[lvlCount].numberFormat=levelValue[lvlCount].numberFormat+style[iterator]

        elif iterator-17>0 and style[iterator-17:iterator]=='<w:lvlText w:val=':
            isLevelText=True

        elif isLevelText==True and style[iterator]=='"':
            isLevelText=False

        elif isLevelText==True :
            levelValue[lvlCount].levelText=levelValue[lvlCount].levelText+style[iterator]

        elif iterator-15>0 and style[iterator-15:iterator]=='<w:lvlJc w:val=':
            isJustification=True

        elif isJustification==True and style[iterator]=='"':
            isJustification=False

        elif isJustification==True:
            levelValue[lvlCount].levelJustify=levelValue[lvlCount].levelJustify+style[iterator]

    return levelValue
    #for i in range(0,lvlCount):
     #   print levelValue[i].levelText

def main():
    z = zipfile.ZipFile('I://paragraph.docx')
    style=''
    abstractList={}
    abstractListCount=0
    try:
        style=z.read("word/numbering.xml")             #container for style.xml text

    except:
        print 'not found here'
    length=len(style)
    #print length
    start=0
    isAbstractNum=True
    for iterator in range(0,length):
        if iterator-15>0 and style[iterator-15:iterator]=='</w:abstractNum':
            abstractList[abstractListCount]=indentLevel(style[start:iterator])
            abstractListCount=abstractListCount+1
            isAbstractNum=False
        elif iterator-16>0 and style[iterator-15:iterator]=='<w:abstractNum ':
            start=iterator
            isAbstractNum=True
        elif isAbstractNum==True :
            pass
    requiredList=''
    styleList={}
    isNumId=False
    isAbs=False
    absNm=''
    for iterator  in range(0,length):
        if iterator-15>0 and style[iterator-15:iterator]=='<w:num w:numId=':
            isNumId=True
        elif isNumId==True and style[iterator]=='"':
            isNumId=False
        elif isNumId==True:
            requiredList=requiredList+style[iterator]
        elif iterator-23>0 and  style[iterator-23:iterator]=='<w:abstractNumId w:val=':
            isAbs=True
        elif isAbs==True and style[iterator]=='"':
            isAbs=False
            styleList[int(requiredList)]=abstractList[int(absNm)]

            requiredList=''
            absNm=''
        elif isAbs==True :
            absNm=absNm+style[iterator]


main()