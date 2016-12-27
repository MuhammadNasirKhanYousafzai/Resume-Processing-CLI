import zipfile,textFormatting

#####################################
#   getting style from style.xml    #
####################################
def directSyling(docx,Document,end,isRunLevel):
    '''
    reading formatting that are applied in document.xml
    in parameters docx is formatting variable ,Document contain text
    end define ends of loop isRunLevel is bool variable for defining
    that it is run or paragraph level attribute
    '''

    endPoint=len(end)
    isPropertyName=False      #define reading of property name
    isPropertyValue=False   #define reading of value
    propertyName=""         #varible for contain name of property
    propertyvalue=""        #variable for containing value of property
    documentLength=len(Document)

    #loop to iterate through document to find values
    for iterator in range(0,documentLength):

        #if we are at end point return
        if iterator-endPoint>0 and Document[iterator-endPoint:iterator]==end:
            return

        #start reading of property name
        elif iterator-2>0 and Document[iterator-2:iterator]=='<w':
            isPropertyName=True

        #stop reading of property name
        elif isPropertyName==True and Document[iterator]==' ':
            isPropertyName=False

        #define end of named attribute like bold and italic
        elif  isPropertyValue==False and propertyvalue=="" and isPropertyName==True and propertyName!="" and (  Document[iterator:iterator+2]=='/>' or Document[iterator]=='>'):

            #if this is run level attribute
            if isRunLevel==True:
                namedAttributeRunLevel(docx,propertyName)

            #if this is not run level attribute
            else:
                namedAttribute(docx,propertyName)
            propertyName=""     #define name remove name of property
            isPropertyName=False    #stop reading name of property

        #reading name of property
        elif isPropertyName==True :
             propertyName=propertyName+Document[iterator]

        #start reading value of attribute
        elif iterator-6>0 and Document[iterator-6:iterator]=='w:val=':
            isPropertyValue=True

        #stop reading value of attribute
        elif isPropertyValue==True and Document[iterator]=='"':
             isPropertyValue=False

             #if is run level attribute
             if isRunLevel==True:
                attributeRunLevel(docx,propertyName,propertyvalue)

             #if is paragraph level attribute
             else:
                attribute(docx,propertyName,propertyvalue)
             propertyName=""        #remove name of attribute
             propertyvalue=""       #remove name of property

        elif isPropertyValue==True:
             propertyvalue=propertyvalue+Document[iterator]

#####################################
#   getting style from style.xml    #
####################################
def styleId(path,docx,styleFamily,isvisitedlink):
    z = zipfile.ZipFile(path)
    style=z.read("word/styles.xml")             #container for style.xml text
    length=len(style)
    styleName=""            #name of style
    requiredStyle=False     #variable that shows the style we are searching for
    isHeadingName=False     #if style is heading
    isPropertyName=False    #define start of reading property name
    isPropertyValue=False   #define start of reading value of property
    propertyName=""         # contain name of property
    propertyvalue=""        #contain value of property
    isAttribute=False       #define attribute
    defaultfontValue=""     #define default font value for style


    #loop through the style to find the required information
    for iterator in range(0,length):

        #define reading of start of style id
        if iterator-10>0 and style[iterator-10:iterator]=='w:styleId=':
           isHeadingName=True

        #define start of reading of font family
        elif requiredStyle==True and iterator-23>0 and style[iterator-23:iterator]=='<w:rFonts w:asciiTheme=':
            isAttribute=True


        #define end of reading of font family
        elif isAttribute==True and style[iterator]=='"':

           isAttribute=False

            #reading font family from style.xml if not found
           #then read font family from theme.xml
           if isPropertyName==True:

                if defaultfontValue=='minorHAnsi':
                    attributeRunLevel(docx,'font',getHAnsiFonts(path,False))
                elif defaultfontValue=='majorHAnsi':

                    attribute(docx,'font',getHAnsiFonts(path,True))
                else:
                    attribute(docx,'font',defaultfontValue)
           else:
                if defaultfontValue=='minorHAnsi':
                    attributeRunLevel(docx,'font',getHAnsiFonts(path,False))
                elif defaultfontValue=='majorHAnsi':

                    attribute(docx,'font',getHAnsiFonts(path,True))
                else:
                    attribute(docx,'font',defaultfontValue)

        #read defult font family
        elif isAttribute==True:
            defaultfontValue=defaultfontValue+style[iterator]

        elif iterator-7>0 and style[iterator-7:iterator]=='<w:pBdr' and style[iterator]=='>':

            getBorder(docx.paragraphProperties,style[iterator:],'</w:pBdr')

        #stop reading style id
        elif isHeadingName==True and style[iterator:iterator+2]=='">':
            isHeadingName=False

            #if name is same as styleFamily which is required to us
            #set requiredStyle to true
            if styleName==styleFamily:
                requiredStyle=True
            #delete name of style
            styleName=""

        #if heading name is true read style name
        elif isHeadingName==True:
            styleName=styleName+style[iterator]

        #define end of style stop reading attribute if this is required style
        elif requiredStyle==True and iterator-10>0 and style[iterator-10:iterator]=='</w:style>':
            requiredStyle=False

        #start reading name of property
        elif requiredStyle==True and iterator-2>0 and style[iterator-2:iterator]=='<w':
            isPropertyName=True

        #stop reading of property name
        elif isPropertyName==True and style[iterator]==' ':
            isPropertyName=False

        #if this is named attribute save property and delete value
        elif  isPropertyValue==False and propertyvalue=="" and isPropertyName==True and propertyName!="" and (  style[iterator:iterator+2]=='/>' or style[iterator]=='>'):
            namedAttribute(docx,propertyName)
            propertyName=""

        elif isPropertyName==True and ( style[iterator]=='/' or style[iterator]=='>') :
            isPropertyName=False
            namedAttribute(docx,propertyName)
            propertyName=""

        #read name of property
        elif isPropertyName==True :
             propertyName=propertyName+style[iterator]

        #start reading value of property values
        elif requiredStyle==True and style[iterator-6:iterator]=='w:val=':
            isPropertyValue=True

        #define end of property value
        elif isPropertyValue==True and style[iterator]=='"':
             isPropertyValue=False

             #save property and delete name and value from local varible
             attribute(docx,propertyName,propertyvalue)
             propertyName=""
             propertyvalue=""

        #read value as long as isPropertyValue is True
        elif isPropertyValue==True:
             propertyvalue=propertyvalue+style[iterator]

    #if property contain link to other property read format from that by recursion
    if docx.paragraphProperties.link!="" and isvisitedlink==False:

        styleId(path,docx,docx.paragraphProperties.link,True)



########################################
#   applying formatting to attribute   #
########################################
def attribute(docx,propertyName,propertyvalue):
    '''
    saving values of attributes for paragraph level elementss
    '''
    if propertyName=='color':
        docx.paragraphProperties.color="#"+propertyvalue
    elif propertyName=='sz':
        docx.paragraphProperties.forntSize=propertyvalue
    elif propertyName=='basedOn':
        docx.paragraphProperties.basedOn=propertyvalue
    elif propertyName=='link':
        docx.paragraphProperties.link=propertyvalue
    elif propertyName=='name':
        docx.paragraphProperties.name=propertyvalue
    elif propertyName=='font':
        docx.paragraphProperties.forntFamily=propertyvalue

################################################################
# function for getting presence of attribute without values    #
################################################################
def namedAttribute(docx,propertyName):
    '''

    saving value of named formatting properties for paragraph level attribute
    '''
    if propertyName=='b':
        docx.paragraphProperties.bold=True
    if propertyName=='i':
        docx.paragraphProperties.italic=True

#####################################################
#   applying run leveling formatting to attribute   #
#####################################################
def attributeRunLevel(docx,propertyName,propertyvalue):
    '''
    saving value of formatting for run level attributes
    '''

    if propertyName=='color':
        docx.color="#"+propertyvalue
    elif propertyName=='sz':
        docx.forntSize=propertyvalue
    elif propertyName=='basedOn':
        docx.basedOn=propertyvalue
    elif propertyName=='link':
        docx.link=propertyvalue
    elif propertyName=='name':
        docx.name=propertyvalue
    elif propertyName=='u':

        docx.underline=propertyvalue
    elif propertyName=='font':
        docx.forntFamily=propertyvalue
    elif propertyName=='spacingBefore':
        docx.spacingBefore=propertyvalue
    elif propertyName=='spacingAfter':
        docx.spacingAfter=propertyvalue
    elif propertyName=='lineHeight':
        docx.lineHeight=propertyvalue

#########################################################################
# function for getting run level  presence of attribute without values  #
#########################################################################
def namedAttributeRunLevel(docx,propertyName):
    '''
    saving presence of named attribute like bold and underline for run level elements
    '''
    if propertyName=='b':
        docx.bold=True
    if propertyName=='i':
        docx.italic=True


###########################################################
#  getting default font family of minor text(paragraphs)  #
###########################################################
def getHAnsiFonts(path,isMajor):
    '''
    reads defualt fonts family from theme.xml for both major and minor font
    isMajor is bool variable which True if we want to find major font and False
    if we want minor font
    '''
    z = zipfile.ZipFile(path)   #reading files from docx file
    document=z.read("word/theme/theme1.xml")             #container for style.xml text
    docxLength=len(document)    #getting length of document

    #getting starting index of major font if isMajor property is True
    if isMajor==True:
        start=document.index('<a:majorFont>')

    #getting starting index of minor  font if isMajor is False
    else:
        start=document.index('<a:minorFont>')
    font=""     #contain font name
    isFont=False    #variable for define starts of reading name

    #loop thougth from starting to find font
    for iterator in range(start,docxLength):
        #from typeface=" font family name will be start
        if document[iterator-9:iterator]=='typeface=':
            isFont=True

        # at (") font family name will be end
        elif isFont==True and document[iterator]=='"':
            break


        elif isFont==True:
            font=font+document[iterator]

    return font


###################################
# define relation between styles  #
###################################
def cpyFormat(docxStyle,style):
    '''
    copying formatting between to element in such a way that only those attribute are copied with are not None
    '''
    #copy font family
    if style.forntFamily!="":
        docxStyle.forntFamily=style.forntFamily

    #copy font size
    if style.forntSize!="":
        docxStyle.forntSize=style.forntSize

    #copy text color
    if style.color!="":
        docxStyle.color=style.color


    #copy back ground color
    if style.backgroundColor!="":
        docxStyle.backgroundColor=style.backgroundColor

    #copy bold property
    if style.bold!=False:
        docxStyle.bold=style.bold

    #copy italic property
    if style.italic!=False:
        docxStyle.italic=style.italic

    #copy underline property
    if style.underline!="":
        docxStyle.underline=style.underline

    #copy delete text property
    if style.delete!=False:
        docxStyle.delete=style.delete

    #copy style name of formatting
    if style.styleName!="":
        docxStyle.styleName=style.styleName

    #copy spacing before
    if style.spacingBefore!="":
        docxStyle.spacingBefore=style.spacingBefore

    #copy after spacing
    if style.spacingAfter!="":
        docxStyle.spacingAfter=style.spacingAfter

    #copy line height
    if style.lineHeight!="":
        docxStyle.lineHeight=style.lineHeight

    #copy vertical line property
    if style.verticleLine!="":
        docxStyle.verticleLine=style.verticleLine

    #copy horizontal line property
    if style.horizontalLine!="":
        docxStyle.horizontalLine=style.horizontalLine

    #copy name of style
    if style.name!="":
        docxStyle.name=style.name

    #copy name of basic style
    if style.basedOn!="":
        docxStyle.basedOn=style.basedOn

    #copy parent of property
    if style.parent!="":
        docxStyle.parent=style.parent

##########################################
#  get border of paragraph or run level  #
##########################################
def getBorder(docx,document,endPoint):
    length=len(document)
    getAttribute=False
    border=""       #contain value of border
    borderName=""   # name of border
    isborder=False   #define border
    ends=len(endPoint)  #define end of loop
    attribute=""    #attribute name
    value=""        #value for attribute

    #loop throught the document
    for iterator in range(0,length):

        # reading values for border top
        if document[iterator-6:iterator]=='<w:top':
            borderName='top'
            isborder=True

        # reading values for border left
        elif document[iterator-7:iterator]=='<w:left':
            borderName='left'
            isborder=True

        # reading values for border bottom
        elif document[iterator-9:iterator]=='<w:bottom':
            borderName='bottom'
            isborder=True

        # reading values for border right
        elif document[iterator-8:iterator]=='<w:right':
            borderName='right'
            isborder=True

        # reading values for border between
        elif document[iterator-10:iterator]=='<w:between':
            borderName='between'
            isborder=True

        # reading values for border   bar
        elif document[iterator-6:iterator]=='<w:bar':
            borderName='bar'
            isborder=True

        # reading values for border of run level element
        elif document[iterator-6:iterator]=='<w:bdr':
            borderName='runlevel'
            isborder=True

        elif document[iterator-10:iterator]=='<w:insideH':
            borderName='insideH'
            isborder=True

        elif document[iterator-10:iterator]=='<w:insideV':
            borderName='insideV'
            isborder=True
        # stop reading of properties of border and assign values to border
        elif isborder==True and document[iterator-1]=='/' and document[iterator]=='>':
            isborder=False

            if borderName=='top':
                docx.borderTop=border

            elif borderName=='left':
                docx.borderLeft=border

            elif borderName=='bottom':
                docx.borderBottom=border

            elif borderName=='right':
                docx.borderRight=border

            elif borderName=='between':
                docx.borderBetween=border

            elif borderName=='bar':
                docx.borderBar=border
            elif borderName=='runlevel':
                docx.runLevelBorder=border
            elif borderName=='insideH':
                docx.borderInsideH=border
            elif borderName=='insideV':
                docx.borderInsideV=border

            #remove all the elements of border from
            border=""
         #reading value for type of border
        elif isborder==True and  document[iterator-6:iterator]=='w:val=':
            getAttribute=True
            attribute='type'

        #reading value for font size of border
        elif isborder==True and document[iterator-5:iterator]=='w:sz=':
            getAttribute=True
            attribute='size'
        #reading value for space of border
        elif isborder==True and document[iterator-8:iterator]=='w:space=':
            getAttribute=True
            attribute='space'
         # reading value of color for border
        elif isborder==True and document[iterator-8:iterator]=='w:color=':
            getAttribute=True
            attribute='color'
        elif isborder==True and document[iterator-13:iterator]=='w:themeColor=':
            getAttribute=True
            attribute='theme'

        #define end of reading of border attribute value
        elif isborder==True and getAttribute==True and document[iterator]=='"':
            getAttribute=False
            #if color is auto assign black color as default for document
            if attribute=='color' and value=='auto':
                border=border+" "+attribute+" "+"#000000"
            else:
                border=border+" "+attribute+" "+value
            #remove value from temp variable container
            value=""

        #reading value as long as condition is true
        elif getAttribute==True:
            value=value+document[iterator]

        #define end of document
        elif document[iterator-ends:iterator]==endPoint:
            break

#######################################
#      cells margins for tables       #
#######################################
def tableCellMargin(tableMargin,document,endpoint):
        length=len(document)
        endLength=len(endpoint)
        isMargin=False
        isMarginWidth=False
        isMarginType=False
        margin=""
        value=""
        for iterator in range(0,length):
            if iterator-endLength>0 and document[iterator-endLength:iterator]==endpoint:
                break

            elif iterator-6>0 and document[iterator-6:iterator]=='<w:top':
                margin='top'
                isMargin=True

            elif iterator-6>0 and document[iterator-7:iterator]=='<w:left':
                margin='left'
                isMargin=True

            elif iterator-6>0 and document[iterator-9:iterator]=='<w:bottom':
                margin='bottom'
                isMargin=True

            elif iterator-6>0 and document[iterator-8:iterator]=='<w:right':
                margin='right'
                isMargin=True


            elif isMargin==True and document[iterator-4:iterator]=='w:w=':
                isMarginWidth=True
                value=value+" width "

            elif (isMarginWidth==True or isMarginType==True) and document[iterator]=='"':
                isMarginType=False
                isMarginWidth=False

            elif isMarginWidth==True:
                value=value+document[iterator]

            elif iterator-8>0 and document[iterator-7:iterator]=='w:type=':
                isMarginType=True
                value=value+" type "

            elif isMarginType==True:
                value=value+document[iterator]

            elif isMargin==True and document[iterator-1:iterator+1]=='/>':
                if margin=="top":
                    tableMargin.top= value
                elif margin=='bottom':
                    tableMargin.bottom= value
                elif margin=='left':
                    tableMargin.left= value
                elif margin=='right':
                    tableMargin.top= value
                value=''
##########################################
#     handling tables in documents       #
##########################################
def tableProperties(path,document):
    tableId=textFormatting.table()  #table for containing values of table
    length=len(document)    #length of document
    #endLength=len(endpoint) #legth of end string
    isTableStyleName=False
    styleName=""
    isTableGrid=False
    readGrid=False
    colsCount=0
    tblGrid={}
    gridValue=''
    rowsCount=0
    innerTableList=[]
    for iterator in range(0,length):


        if iterator-6>0 and document[iterator-6:iterator]=='<w:tbl' and document[iterator]=='>':

            innerTableList.append(1)
        elif len(innerTableList)>0 and document[iterator-7:iterator]=='</w:tbl' and document[iterator]=='>':
            innerTableList.pop()
        elif  len(innerTableList)>0:
            pass

        elif iterator-19>0 and document[iterator-18:iterator]=='<w:tblStyle w:val=':
            isTableStyleName=True

        elif isTableStyleName==True and document[iterator]=='"':
            isTableStyleName=False
            tableStyleID(path,tableId,styleName)

        elif isTableStyleName==True :
            styleName=styleName+document[iterator]
        elif iterator-6>0 and document[iterator-6:iterator]=='</w:tr' and document[iterator]=='>':
            rowsCount=rowsCount+1
            tableId.rows=rowsCount

        elif iterator-10>0 and document[iterator-10:iterator]=='<w:tblGrid':
                isTableGrid=True

        elif iterator-11>0 and document[iterator-11:iterator]=='</w:tblGrid':
            isTableGrid=False
            tableId.cols=colsCount

        elif isTableGrid==True and document[iterator-15:iterator]=='<w:gridCol w:w=':
            readGrid=True

        elif readGrid==True and document[iterator]=='"':
            readGrid=False
            tblGrid[colsCount]=gridValue
            tableId.grid[colsCount]=gridValue
            gridValue=''
            colsCount=colsCount+1

        elif readGrid==True :
            gridValue=gridValue+document[iterator]

    return tableId

######################################################
# function for getting properties from row and cols  #
######################################################
def colsRowsCellsProperties(document,endPoint):
    length=len(document)
    tableCells=textFormatting.tableStyleProperties()
    endPointLength=len(endPoint)
    isCellborder=False
    isRunLevel=False
    isparagraphLevel=False
    property=''
    value=''
    isPropertyName=False
    isValue=False

    for iterator in range(0,length):
        if iterator-endPointLength>0 and document[iterator-endPointLength:iterator]==endPoint:
            break

        elif iterator-13>0 and document[iterator-13:iterator]=='<w:tcBorders>':
            isCellborder=True
            getBorder(tableCells.tableCellsProperties.tblBorder,document[iterator:],'</w:tcBorders>')

        elif iterator-13>0 and document[iterator-14:iterator]=='</w:tcBorders>':
            isCellborder=False

        elif isCellborder==True:
            pass
        elif document[iterator-6:iterator]=='<w:pPr':
            isparagraphLevel=True

            property=''

        elif document[iterator-8:iterator]=='</w:pPr>':
            isparagraphLevel=False
            property=''

        elif document[iterator-6:iterator]=='<w:rPr':
            isRunLevel=True
            property=''
        elif document[iterator-7:iterator]=='</w:rPr':
            isRunLevel=False
            property=''

        elif document[iterator-2:iterator]=='<w' and document[iterator]==':':
            isPropertyName=True
            property=''

        elif isPropertyName==True and document[iterator]==' ':
            isPropertyName=False


        elif property!='' and isPropertyName==True and (document[iterator:iterator+2]=='/>' or document[iterator]=='>'):

            if isRunLevel==True:
                namedAttributeRunLevel(tableCells.cellTextProperties.generalRunProperties,property)
            elif isparagraphLevel==True:
                namedAttributeRunLevel(tableCells.cellTextProperties.generalParagraphProperties,property)
            property=''

        elif isPropertyName==True:
            property=property+document[iterator]

        elif document[iterator-6:iterator]=='w:val=':
            isValue=True

        elif isValue==True and document[iterator]=='"':
            isValue=False

            if isRunLevel==True:
                attributeRunLevel(tableCells.cellTextProperties.generalRunProperties,property,value)
            elif isparagraphLevel == True:
                attributeRunLevel(tableCells.cellTextProperties.generalParagraphProperties,property,value)
            value=''
            property=''

        elif isValue==True:
            value=value+document[iterator]
    return tableCells
################################################
#   reading style properties from style.xml    #
################################################
def tableStyleID(path,table,styleName):
    z = zipfile.ZipFile(path)
    styleXML=z.read("word/styles.xml")             #container for style.xml text
    length=len(styleXML)
    starts=styleXML.index(styleName)
    isPropertyName=False
    istableLevelProperties=True
    isValue=False
    property=''
    value=''
    isafterSpace=False
    isLine=False
    isparagraphLevel=False
    isRunLevel=False
    istableBorder=False
    isTblCellMar=False
    isRow_CellName=False
    rowCellName=''
    ispropertyType=False
    tableInstanceProperties(table.aboutTable,'styleId',styleName)
    for iterator in range(starts,length):
        if styleXML[iterator:iterator+10]=='</w:style>':
            break

        elif styleXML[iterator-13:iterator]=='<w:tblBorders':
                istableBorder=True
                getBorder(table.tableProperties.tblBorders,styleXML[iterator:],'</w:tblBorders')

        elif styleXML[iterator-14:iterator]=='</w:tblBorders':
            istableBorder=False

        elif istableBorder==True:
            pass

        elif styleXML[iterator-13:iterator]=='<w:tblCellMar':
            isTblCellMar=True
            tableCellMargin(table.tableProperties.tblCellMar,styleXML[iterator:],'</w:tblCellMar>')

        elif isTblCellMar==True and styleXML[iterator-14:iterator]=='</w:tblCellMar':
            isTblCellMar=False

        elif isTblCellMar==True:
            pass

        elif styleXML[iterator-21:iterator]=='<w:tblStylePr w:type=':
            isRow_CellName=True

        elif isRow_CellName==True and styleXML[iterator]=='"':
            isRow_CellName=False

            temp=colsRowsCellsProperties(styleXML[iterator:],'</w:tblStylePr>')
            ispropertyType=True
            if rowCellName=='firstRow':
                table.firstRow=temp

            elif rowCellName=='lastRow':
                table.lastRow=temp

            elif rowCellName=='firstCol':
                table.firstCol=temp

            elif rowCellName=='lastCol':
                table.lastCol=temp

            elif rowCellName=='band1Vert':
                table.band1Vert=temp

            elif rowCellName=='band1Horz':
                table.band1Horz=temp

            rowCellName=''

        elif isRow_CellName==True:
            rowCellName=rowCellName+styleXML[iterator]
        elif ispropertyType==True and styleXML[iterator-15:iterator]=='</w:tblStylePr>':
            ispropertyType=False
        elif ispropertyType==True:
            pass
        elif styleXML[iterator-6:iterator]=='<w:pPr':
            isparagraphLevel=True
            istableLevelProperties=False
            property=''

        elif styleXML[iterator-8:iterator]=='</w:pPr>':
            isparagraphLevel=False
            property=''

        elif styleXML[iterator-6:iterator]=='<w:rPr':
            isRunLevel=True
            property=''
        elif styleXML[iterator-7:iterator]=='</w:rPr':
            isRunLevel=False
            property=''

        elif styleXML[iterator-2:iterator]=='<w' and styleXML[iterator]==':':
            isPropertyName=True
            property=''

        elif isPropertyName==True and styleXML[iterator]==' ':
            isPropertyName=False


        elif property!='' and isPropertyName==True and (styleXML[iterator:iterator+2]=='/>' or styleXML[iterator]=='>'):

            if isRunLevel==True:
                namedAttributeRunLevel(table.textProperty.generalRunProperties,property)
            elif isparagraphLevel==True:
                namedAttributeRunLevel(table.textProperty.generalParagraphProperties,property)
            property=''

        elif isPropertyName==True:
            property=property+styleXML[iterator]

        elif styleXML[iterator-6:iterator]=='w:val=':
            isValue=True

        elif isValue==True and styleXML[iterator]=='"':
            isValue=False

            if istableLevelProperties==True:
                tableInstanceProperties(table.aboutTable,property,value)

            elif isRunLevel==True:
                attributeRunLevel(table.textProperty.generalRunProperties,property,value)
            elif isparagraphLevel == True:
                attributeRunLevel(table.textProperty.generalParagraphProperties,property,value)
            elif property=='tblStyleRowBandSize':
                table.tableProperties.tblStyleRowBandSize=value
            elif property=='tblStyleColBandSize':
                table.tableProperties.tblStyleColBandSize=value
            value=''
            property=''

        elif isValue==True:
            value=value+styleXML[iterator]

##############################################
#      update table properties value         #
##############################################
def tableInstanceProperties(tableInstance,property,value):
    if property=='styleId':
        tableInstance.styleId=value

    elif property=='name':
        tableInstance.name=value

    elif property=='basedOn':
        tableInstance.basedOn=value


##############################################
#    function for default text formatting    #
##############################################
def getDefaultFormatting(path):
    z = zipfile.ZipFile(path)
    style=z.read("word/styles.xml")             #container for style.xml text
    runLevelDefault=False               #bool variable for checking for run level style
    defaultTextFormatting=textFormatting.textProperties()
    spacing=False                       #bool variable for checking spacing
    isAttribute=False
    isfontvalue=False
    fontValue=""
    defaultValue=""
    isColor=False

    length=len(style)
    #loop through the style.xml element for getting default style
    for iterator in range(0,length):

        #define starting of rub level default element
       if iterator-13>0 and style[iterator-13:iterator]=='<w:rPrDefault':
                runLevelDefault=True

       #define end of default elements
       elif style[iterator:iterator+15]=="</w:docDefaults":

           #if not color is found then text color must be black by default
           if defaultTextFormatting.generalRunProperties.color=="":
               defaultTextFormatting.generalRunProperties.color="#000000"
               defaultTextFormatting.generalParagraphProperties.color='#000000'
           #stop looping through the remaining elements because we have checked all default properties
           break

       #define starting font family of from document run level default properties
       elif runLevelDefault==True and style[iterator-23:iterator]=='<w:rFonts w:asciiTheme=':
            isAttribute=True

       #define end of name of font family of documents default
       elif isAttribute==True and style[iterator]=='"':
           isAttribute=False
           #if default value is minorHansi get font family from theme.xml
           if defaultValue=='minorHAnsi':

             defaultTextFormatting.generalRunProperties.forntFamily=getHAnsiFonts(path,False)
             defaultTextFormatting.generalParagraphProperties.forntFamily=getHAnsiFonts(path,False)
           #if not assing the name of font to run level default as the default font family
           else:
               defaultTextFormatting.generalParagraphProperties.forntFamily=defaultValue
               defaultTextFormatting.generalParagraphProperties.forntFamily=defaultValue

       #reading default font family from style.xml
       elif isAttribute==True:
           defaultValue=defaultValue+style[iterator]

       #reading name value of font size of text for default run level text
       elif runLevelDefault==True and style[iterator-12:iterator]=='<w:sz w:val=':
           isfontvalue=True

       #define end of of reading name of from style.xml
       elif isfontvalue==True and style[iterator]=='"':
            isfontvalue=False
            defaultTextFormatting.generalRunProperties.forntSize=fontValue
            defaultTextFormatting.generalParagraphProperties.forntSize=fontValue

       #read font size from style.xml as long isFontvalue is true
       elif isfontvalue==True:
           fontValue=fontValue+style[iterator]

       elif iterator-14 >0 and style[iterator-14:iterator]=='w:color w:val=':
            isColor=True
       elif isColor==True and style[iterator]=='"':
           isColor=False
       elif isColor==True:
           if defaultTextFormatting.generalParagraphProperties.color!="":
               defaultTextFormatting.generalParagraphProperties.color=defaultTextFormatting.generalParagraphProperties.color+style[iterator]
               defaultTextFormatting.generalRunProperties.color=defaultTextFormatting.generalRunProperties.color+style[iterator]

           else:
               defaultTextFormatting.generalParagraphProperties.color='#'+style[iterator]
               defaultTextFormatting.generalRunProperties.color='#'+style[iterator]
    #return default formatting for document
    defaultTextFormatting.generalParagraphProperties.styleName='Normal'
    return defaultTextFormatting



#############################################
#       getting paragraphs properties       #
#############################################
def paragraphsTextProperties(path,docx,document):
    property=''
    isProperty=False
    value=''
    isValue=False
    isRunLevel=False
    isParagraphLevel=False
    getProperty=False
    length=len(document)
    paraRuns=0
    isText=False
    textInRun=''
    isRunLevelFontFamily=False
    fontFamily=''
    isborder=False
    grammarErrors=0
    isTextBox=False
    isTextBoxRun=False
    tmpStyle=''

    for iterator in range(0,length):
        #print document[iterator-10:iterator+10],document[iterator:iterator+2]

        if isRunLevel==True and document[iterator-7:iterator]=='<w:pict':
            isTextBox=True
            isTextBoxRun=True
            isRunLevel=False
            del docx.runLevelProperties[paraRuns]
        elif isTextBox==True and document[iterator-8:iterator]=='</w:pict':
            isTextBox =False

        elif isTextBox==True:
            pass

        elif isTextBoxRun==True and document[iterator-5:iterator]=='</w:r' and document[iterator]=='>':
            isTextBoxRun=False


        elif iterator-28 and document[iterator-28:iterator]== '<w:proofErr w:type="spellEnd':
            grammarErrors=grammarErrors+1

        elif iterator-6>0 and document[iterator-6:iterator]=='<w:pPr' and document[iterator]=='>':
            isParagraphLevel=True
            isProperty=False
            property=''
        elif iterator-7>0 and document[iterator-7:iterator]=='</w:pPr' and document[iterator]:
            isParagraphLevel=False
        elif isParagraphLevel==True and iterator-16>0 and  document[iterator-16:iterator]=='<w:pStyle w:val=':
            getProperty=True
            isProperty=False
            property=''
        elif iterator-7>0 and document[iterator-7:iterator]=='<w:pBdr':
            isProperty=False
            property=''
            isborder=True
         #   getBorder(docx.paragraphProperties,document[iterator:],'</w:pBdr')
        elif isborder==True and document[iterator-8:iterator]=='</w:pBdr':
            isborder=False
        elif isborder==True:
            pass

        #stop getting name of paragraph style
        elif getProperty==True  and document[iterator:iterator+2]==r'"/':
            getProperty=False
            docx.paragraphProperties.styleName= tmpStyle

            styleId(path,docx,docx.paragraphProperties.styleName,False)
            cpyFormat(docx.DefaultstyleFormatting,docx.paragraphProperties)
            tmpStyle=''
        #condition for getting style of paragraph
        elif getProperty==True:
            tmpStyle=tmpStyle+document[iterator]

        elif iterator - 23 > 0 and document[iterator-23:iterator]=='<w:rFonts w:asciiTheme=':
            isProperty=False
            property=''
            isRunLevelFontFamily=True
            fontFamily=''
        elif iterator-18>0 and  document[iterator-18:iterator]=='<w:rFonts w:ascii=':
            isProperty=False
            property=''
            isRunLevelFontFamily=True
            fontFamily=''

        elif isRunLevelFontFamily==True and document[iterator]=='"':
            isRunLevelFontFamily=False
            if isParagraphLevel==True:

                if fontFamily=='minorHAnsi':
                    attributeRunLevel(docx.paragraphProperties,'font',getHAnsiFonts(path,False))
                    pass
                elif fontFamily=='majorHAnsi':

                    attributeRunLevel(docx.paragraphProperties,'font',getHAnsiFonts(path,True))
                else:
                    attributeRunLevel(docx.paragraphProperties,'font',fontFamily)
            else:
                if fontFamily=='minorHAnsi':
                    attributeRunLevel(docx.runLevelProperties[paraRuns].properties,'font',getHAnsiFonts(path,False))
                elif fontFamily=='majorHAnsi':
                    attributeRunLevel(docx.runLevelProperties[paraRuns].properties,'font',getHAnsiFonts(path,True))
                else:
                    attributeRunLevel(docx.runLevelProperties[paraRuns].properties,'font',fontFamily)


        elif isRunLevelFontFamily==True:
            fontFamily=fontFamily+document[iterator]

        elif iterator-4>0 and document[iterator-4:iterator]=='<w:t' and document[iterator]=='>':
            isText=True
            isProperty=False
            property=''

        elif iterator-25>0 and document[iterator-25:iterator]=='<w:t xml:space="preserve"':
            isText=True
            isProperty=False
            property=''

        elif isText==True and document[iterator:iterator+6]=='</w:t>' :
            isText=False

            docx.runLevelProperties[paraRuns].Text=textInRun
            textInRun=''

        elif isText==True:
            textInRun=textInRun+document[iterator]


        elif document[iterator-4:iterator]=='<w:r' and (document[iterator]==' ' or document[iterator]=='>' ):

                property=''
                isRunLevel=True
                isProperty=False
                docx.runLevelProperties[paraRuns]=textFormatting.runlevel()
                cpyFormat(docx.runLevelProperties[paraRuns].properties,docx.DefaultstyleFormatting)


        elif isRunLevel==True and document[iterator-7:iterator]=='</w:rPr' and document[iterator]=='>':
                pass
        elif document[iterator-5:iterator]=='</w:r' and document[iterator]=='>':
            isRunLevel=False
            if docx.paragraphProperties.styleName=="":
               docx.paragraphProperties.styleName='Normal'
            paraRuns=paraRuns+1
        elif iterator-2>0 and document[iterator-2:iterator]=='<w' and document[iterator]==':':
            isProperty=True
            property=''

        elif isProperty==True  and value=='' and (document[iterator]=='/' or document[iterator]=='>'):
            isProperty=False

            if isRunLevel==True:

                namedAttributeRunLevel(docx.runLevelProperties[paraRuns].properties,property)
            elif isParagraphLevel==True:
                namedAttributeRunLevel(docx.paragraphProperties,property)
            property=''

        elif isProperty==True and document[iterator]==' ':
            isProperty=False

        elif isProperty==True:
            property=property+document[iterator]

        elif iterator-6>0 and document[iterator-6:iterator]=='w:val=':
            isValue=True
            value=''
        elif isValue==True and document[iterator]=='"':
            isValue=False

            if isParagraphLevel==True:
                attributeRunLevel(docx.paragraphProperties,property,value)

            elif isRunLevel==True:

                attributeRunLevel(docx.runLevelProperties[paraRuns].properties,property,value)

            property=''
            value=''

        elif isValue==True:
            value=value+document[iterator]
    #if grammarErrors>0:
       # print 'spelling errors in paragraph', grammarErrors


#####################################################
#          getting table & text properties          #
#####################################################
def tablesInfo(path,document,endPoint,docDefaults):
    tblProperties=tableProperties(path,document)

    length=len(document)
    endLength=len(endPoint)
    rowCount=0
    tblCells={}
    colCount=0
    isParagraph=False
    paragraphCounts=0
    istbleCellProperty=False
    index=''
    isWith=''
    paragraphFlaged=False
    tableWithFormat=[]
    tableWithFormat.append(tblProperties)
    startingParagraphIndex=0
    isInnerTable=False
    innertable=[]
    hasText=False
    checkForText=False
    #loop for iterating through the document to find cell and text formatting to table
    for iterator in range(0,length):

        #check if this is end of table stop searching cells and text properties for table

        if iterator-6>0 and document[iterator-6:iterator]=='<w:tbl' and document[iterator]=='>':

            innertable.append(1)

        elif len(innertable)>0 and document[iterator-7:iterator]=='</w:tbl' and document[iterator]=='>':

            innertable.pop()
        elif len(innertable)==0 and document[iterator-7:iterator]=='</w:tbl' and document[iterator]=='>':

            break
        elif len(innertable)>0:

            pass

        #increment table row by one as end of table is encounter and sex columns of table to 0
        elif iterator-6>0 and document[iterator-6:iterator]=='</w:tr' and document[iterator]=='>':
            rowCount=rowCount+1
            colCount=0

        #define start of table cell get index(rows and cols number as index) of this cell
        elif iterator-5>0 and document[iterator-5:iterator]=='<w:tc' and( document[iterator]==' ' or document[iterator]=='>'):
            index=str(rowCount)+str(colCount)
            #print index
            tblCells[index]=textFormatting.tablePropertiesWithText()

        #define end of table cell. increment cell count by 1
        elif iterator-6>0 and document[iterator-6:iterator]=='</w:tc' and document[iterator]=='>':
            colCount=colCount+1
            paragraphCounts=0
            #print document[iterator-70:iterator+70]

        #define table cell properties
        elif iterator-7>0 and document[iterator-7:iterator]=='<w:tcPr' and (document[iterator]=='>' or document[iterator]==' '):
            istbleCellProperty=True

        #define table cell width for current table
        elif iterator-11>0 and istbleCellProperty==True and document[iterator-11:iterator]=='<w:tcW w:w=':
            isWith=True

        #if isWith property is true and current index is " stop reading with value
        elif isWith==True and document[iterator]=='"':
            isWith=False

        #if isWith property is true read data from document as width of cell
        elif isWith==True :
            tblCells[index].tblCellProperty.width=tblCells[index].tblCellProperty.width+document[iterator]

        #define start of paragraph .just flag it,because it could be an empty paragraph
        elif iterator-4>0 and document[iterator-4:iterator]=='<w:p' and document[iterator]==' ':
            paragraphFlaged=True

        elif checkForText==True and document[iterator-4:iterator]=='<w:r' and (document[iterator]=='>' or document[iterator]==' '):
            hasText=True

        #if paragraph is not empty find text paragraph properties for text.set flag to false and isParagraph to true
        elif paragraphFlaged==True  and document[iterator]=='>' and document[iterator-1]!='/':
            isParagraph=True
            paragraphFlaged=False
            startingParagraphIndex=iterator
            checkForText=True
        #THIS is empty paragraph set paragraph flag to false
        elif paragraphFlaged==True and document[iterator]=='>' and document[iterator-1]=='/':
            paragraphFlaged=False

        #define end of paragraph set isParagraph property to False
        elif isParagraph==True and hasText==True and document[iterator-5:iterator]=='</w:p' and document[iterator]=='>':
            isParagraph=False
            hasText=False
            #call function to manipulating paragraph formatting
            tblCells[index].tblTextPropertiese[paragraphCounts]=textFormatting.formatting()
            #apply default paragraph level formatting to cell paragraph
            cpyFormat(tblCells[index].tblTextPropertiese[paragraphCounts].paragraphProperties,docDefaults.generalParagraphProperties)
            cpyFormat(tblCells[index].tblTextPropertiese[paragraphCounts].DefaultstyleFormatting,docDefaults.generalParagraphProperties)
            #apply table paragraph level properties to cell paragraph
            cpyFormat(tblCells[index].tblTextPropertiese[paragraphCounts].paragraphProperties,tblProperties.textProperty.generalParagraphProperties)
            cpyFormat(tblCells[index].tblTextPropertiese[paragraphCounts].DefaultstyleFormatting,tblProperties.textProperty.generalParagraphProperties)
            # apply table run level properties to table cell paragraph properties
            cpyFormat(tblCells[index].tblTextPropertiese[paragraphCounts].paragraphProperties,tblProperties.textProperty.generalRunProperties)
            cpyFormat(tblCells[index].tblTextPropertiese[paragraphCounts].DefaultstyleFormatting,tblProperties.textProperty.generalRunProperties)
            paragraphsTextProperties(path,tblCells[index].tblTextPropertiese[paragraphCounts],document[startingParagraphIndex:iterator])
           # print index
            paragraphCounts=paragraphCounts+1
    tableWithFormat.append(tblCells)
    return  tableWithFormat
#####################################################################
#      finding textin formatting present in header and footer       #
#####################################################################
def headerFoooterFormatting(path,document,docDefault):

    isParagraph=False
    length=len(document)
    paragraphInHeader={}
    paragraphCounts=0
    paragraphFlaged=False
    startingParagraphIndex=0
    for iterator in range(0,length):
        if document[iterator-5:iterator]=='<w:p ':
            #isParagraph=True
            paragraphFlaged=True
        elif paragraphFlaged==True and document[iterator]=='>' and document[iterator-1]!='/':
            #create a temporary variable for holding default properties properties

            paragraphFlaged=False
            isParagraph=True
            startingParagraphIndex=iterator

        elif paragraphFlaged==True and document[iterator]=='>' and document[iterator-1]=='/':
            paragraphFlaged=False

        elif isParagraph==True and document[iterator-5:iterator]=='</w:p' and document[iterator]=='>':
            isParagraph=False
            paragraphInHeader[paragraphCounts]=textFormatting.formatting()
            #assign document paragraphs default to tmp variable
            cpyFormat(paragraphInHeader[paragraphCounts].paragraphProperties,docDefault.generalParagraphProperties)
            cpyFormat(paragraphInHeader[paragraphCounts].DefaultstyleFormatting,docDefault.generalParagraphProperties)
            paragraphsTextProperties(path,paragraphInHeader[paragraphCounts],document[startingParagraphIndex:iterator])
            paragraphCounts=paragraphCounts+1


        elif isParagraph==True:
            pass

    return paragraphInHeader
##################################################
#          comparing text formatting             #
#################################################
def compareTextFormatting(docx1,docx2):
    level=0

    if docx1.forntFamily!=docx2.forntFamily:
        level=level + 1
    if docx1.forntSize!=docx2.forntSize:
        level = level + 1
    if docx1.color != docx2.color:

        level = level + 1
    try:
        if docx1.backgroundColor!=docx2.backgroundColor:
            level= level + 1
    except:
        pass
    return level



####################################################
#      finding formatting errors in document       #
####################################################
def formattingErrors(paragraphInDocument):
    para= len(paragraphInDocument)
    #formatting errors in document paragraphs

    errors=0

    #listing styles exist in document
    styleList=[]
    styleDetail=[]
    errorsCount=[]
    fontFamilyList=[]
    fontSizeList=[]
    textColorList=[]

    #################################################
    #   finding formatting errors in paragraphs     #
    #################################################
    #outer loop for finding formatting error
    for pargraphs in range(0,para):
        #number of run level elements in paragraph if run level elements are o then paragraph is empty
        totleRuns=len(paragraphInDocument[pargraphs].runLevelProperties)
        #finding formatting mistakes with in the paragraphs and it's runs
        runs=0
       ## for runs in range(0,totleRuns-1):
           #if there are more then one run levels in paragraph
        for run in range(runs,totleRuns):
            if not textColorList.__contains__(paragraphInDocument[pargraphs].runLevelProperties[run].properties.color):
                textColorList.append(paragraphInDocument[pargraphs].runLevelProperties[run].properties.color)

            if not fontFamilyList.__contains__(paragraphInDocument[pargraphs].runLevelProperties[run].properties.forntFamily):
                fontFamilyList.append(paragraphInDocument[pargraphs].runLevelProperties[run].properties.forntFamily)

            if not fontSizeList.__contains__(paragraphInDocument[pargraphs].runLevelProperties[run].properties.forntSize):
                fontSizeList.append(paragraphInDocument[pargraphs].runLevelProperties[run].properties.forntSize)


        if len(textColorList)>1:

            errors=errors+len(textColorList)-1

        if len(fontFamilyList)>1:
            errors=errors+len(fontFamilyList)-1

        if len(fontSizeList)>1:
            errors=errors+len(fontSizeList)-1

        del fontFamilyList[:]
        del textColorList[:]
        del fontSizeList[:]
        if not(styleList.__contains__(paragraphInDocument[pargraphs].paragraphProperties.styleName)):
            #iterate through the document to find all paragraphs of with same style
            for innerparagraphs in range(pargraphs+1,para):
                #If two paragraph have same style name check there properties
                if paragraphInDocument[pargraphs].paragraphProperties.styleName == paragraphInDocument[innerparagraphs].paragraphProperties.styleName:

                      errors=errors +  compareTextFormatting(paragraphInDocument[innerparagraphs].paragraphProperties,paragraphInDocument[pargraphs].paragraphProperties)

                      #innerparagraphs=para
                      break
        #IF style does not exist in document style list append style styleList
        if not styleList.__contains__(paragraphInDocument[pargraphs].paragraphProperties.styleName):
            styleList.append(paragraphInDocument[pargraphs].paragraphProperties.styleName)
            tmp=textFormatting.stylesInDocuments()
            tmp.color=paragraphInDocument[pargraphs].paragraphProperties.color
            tmp.name=paragraphInDocument[pargraphs].paragraphProperties.styleName
            tmp.forntFamily=paragraphInDocument[pargraphs].paragraphProperties.forntFamily
            tmp.forntSize=paragraphInDocument[pargraphs].paragraphProperties.forntSize
            styleDetail.append(tmp)
    stycount=len(styleDetail)
    for style in range(0,stycount-1):
      #  print styleDetail[style].name
        for innerstyle in range(style+1,stycount):
            if  compareTextFormatting(styleDetail[style],styleDetail[innerstyle])==0:
                errors=errors+1
    return errors


def mainApp(path,document):
    #getting default formatting for document
    docDefaults=getDefaultFormatting(path)
    paragraphCounts=0
    isParagraph=False
    isTableProperty=False
    paragraphInDocument={}
    length=len(document)
    tableCount=0
    paragraphFlaged=False
    startingParagraphIndex=0
    isTextBox=False
    textBoxCount=0
    #looping through the document to find all paragraphs with
    for iterator in range(0,length):

        if isParagraph ==True and document[iterator-7:iterator]== '<w:pict':
            isTextBox=True
           # textBoxesInDocument[textBoxCount]=textBoxContent(document[iterator],'</w:pict')
        elif isTextBox==True and document[iterator-8:iterator]=='</w:pict':
            isTextBox=False
            textBoxCount=textBoxCount+1
        elif isTextBox==True:
            pass
        #is paragraph isn't in table and its the start of paragraph
        elif isTableProperty==False and document[iterator-4:iterator]=='<w:p' and document[iterator]==' ':
            paragraphFlaged=True

        elif paragraphFlaged==True and document[iterator]=='>' and document[iterator-1]!='/':
            isParagraph=True
            paragraphFlaged=False
            startingParagraphIndex=iterator

        elif paragraphFlaged ==True and document[iterator]=='>' and document[iterator-1]=='/':
            paragraphFlaged=False

        elif isParagraph==True and document[iterator-5:iterator]=='</w:p' and document[iterator]=='>':
            isParagraph=False

             #create a temporary variable for holding default properties
            paragraphInDocument[paragraphCounts]=textFormatting.formatting()
            #assign document paragraphs default to tmp variable
            cpyFormat( paragraphInDocument[paragraphCounts].paragraphProperties,docDefaults.generalParagraphProperties)
            cpyFormat( paragraphInDocument[paragraphCounts].DefaultstyleFormatting,docDefaults.generalParagraphProperties)
            paragraphsTextProperties(path,paragraphInDocument[paragraphCounts],document[startingParagraphIndex:iterator])

            paragraphCounts=paragraphCounts+1

        elif isParagraph==True:
            pass
        #comments
        elif iterator - 6 > 0 and document[iterator-7:iterator] =='<w:tbl>' :
            isTableProperty=True
        #comments
        elif iterator-7>0 and document[iterator-7:iterator]=='</w:tbl' and document[iterator]=='>':

            isTableProperty=False
            tableCount=tableCount+1

        elif isTableProperty==True:
            pass
    return paragraphInDocument

def Document(path):
    headersInDocument={}
    footersInDocument={}
    table={}
    textBoxesInDocument={}
    docDefaults=getDefaultFormatting(path)
    z = zipfile.ZipFile(path)

    style=z.read("word/styles.xml")             #container for style.xml text
    document=z.read("word/document.xml")
    #this is function will return all paragraphs in document with formatting
    paragraphsInDocument=mainApp(path,document)
    length=len(document)
    txbxlist=[]
    textBoxPropertiesList={}
    textBoxPropertiesListIndex=-1
    isTextBox=False
    textBoxCount=0
    isShadow=False
    isShadowTrue=False
    isFillColor=False
    isStokeColor=False
    isStokeWeight=False
    isShadowColor=False
    isShape=False
    errors=0
    for iterator in range(0,length):

        if iterator-7>0 and document[iterator-7:iterator]== '<w:pict':
            isTextBox=True
            textBoxPropertiesListIndex=textBoxPropertiesListIndex+1
            txbxlist.append(iterator)
            textBoxPropertiesList[textBoxPropertiesListIndex]=textFormatting.TextBoxProperties()

        elif isTextBox==True and document[iterator-13:iterator]=='<v:shadow on=':
            isShadow=True

            isShadowTrue=True
        elif isTextBox==True and document[iterator-9:iterator]=='<v:shape ':
            isShape=True

        elif (isShadow==True or isShape==True) and  document[iterator]=='>':
            isShadow=False
            isShape=False

        elif isShadowTrue==True and document[iterator]=='"' :
            isShadowTrue=False

        elif isShadowTrue==True :
            if document[iterator]=='t':
                textBoxPropertiesList[textBoxPropertiesListIndex].IsShadow=True
            else:
                textBoxPropertiesList[textBoxPropertiesListIndex].IsShadow=False

        elif isShape==True and document[iterator-10:iterator]=='fillcolor=':
            isFillColor=True

        elif isFillColor==True and document[iterator]==' ':
            isFillColor=False

        elif isFillColor==True:
            textBoxPropertiesList[textBoxPropertiesListIndex].fillColor=textBoxPropertiesList[textBoxPropertiesListIndex].fillColor+document[iterator]

        elif isShape==True and document[iterator-12:iterator]=='strokecolor=':
            isStokeColor=True

        elif isStokeColor==True and document[iterator]==' ':
            isStokeColor=False

        elif isStokeColor==True:
            textBoxPropertiesList[textBoxPropertiesListIndex].stokeColor=textBoxPropertiesList[textBoxPropertiesListIndex].stokeColor+document[iterator]

        elif isShape==True and document[iterator-13:iterator]=='strokeweight=':
            isStokeWeight=True

        elif isStokeWeight==True and document[iterator]=='"':
            isStokeWeight=False

        elif isStokeWeight==True:
            textBoxPropertiesList[textBoxPropertiesListIndex].stokeWeight=textBoxPropertiesList[textBoxPropertiesListIndex].stokeWeight+document[iterator]

        elif isShadow==True and document[iterator-6:iterator]=='color=':
            isShadowColor=True

        elif isShadowColor==True and document[iterator]==' ':
            isShadowColor=False

        elif isShadowColor==True:
            textBoxPropertiesList[textBoxPropertiesListIndex].shadowColor=textBoxPropertiesList[textBoxPropertiesListIndex].shadowColor+document[iterator]

        elif isTextBox==True and document[iterator-8:iterator]=='</w:pict':
            isTextBox=False
            start=int(txbxlist.pop())
            #print start
            textBoxesInDocument[textBoxCount]=textFormatting.textBox()
            textBoxesInDocument[textBoxCount].textBoxProperties=textBoxPropertiesList[textBoxPropertiesListIndex]
            textBoxesInDocument[textBoxCount].textBoxContant=mainApp(path,document[start:iterator])
            del textBoxPropertiesList[textBoxPropertiesListIndex]
            textBoxPropertiesListIndex=textBoxPropertiesListIndex-1
            textBoxCount=textBoxCount+1
            if len(txbxlist)>0:
                isTextBox=True
        elif isTextBox==True:
            pass
    ################################################################
    #  formatting errors in document tex box  ma main paragraph    #
    ################################################################
    for iterator in range(0,textBoxCount):
       errors=errors+ formattingErrors(textBoxesInDocument[iterator].textBoxContant)
    paragraphInDocument=mainApp(path,document)

    errors=formattingErrors(paragraphInDocument)
    ###################################################
    #       finding formatting errors in tables       #
    ###################################################
    tableCount=0
    isTable=False
    tableStart=[]
    for iterator in range(0,length):
        if iterator-6>0 and document[iterator-6:iterator]=='<w:tbl' and document[iterator]=='>':
            isTable=True
            tableStart.append(iterator)
        elif isTable==True and document[iterator-8:iterator]=='</w:tbl>': #and document[iterator]=='>':
            starts=tableStart.pop()
            #print 'test for table ',tableCount
            table[tableCount]= tablesInfo(path, document[starts:iterator],'</w:tbl>',docDefaults)
            tableCount=tableCount+1


        elif isTable==True:
            pass
    for tblCnt in range(0,tableCount):
       # print ,
        rowsCount=table[tblCnt][0].rows
        colsCount=table[tblCnt][0].cols
        #print rowsCount,colsCount

        for row in range(0,rowsCount):

            for col in range(0,colsCount):
                index=str(row)+str(col)

                errors=errors+formattingErrors(table[tblCnt][1][index].tblTextPropertiese)

    errors=errors+formattingErrors(paragraphsInDocument)
    #######################################################
    #         reading header format from docx file        #
    #######################################################
    headExist=True
    headerCount=0
    header={}
    count=1
    while headExist==True:
        try:

            docname="header"+str(count)+".xml"
            headerdoc=z.read("word/"+docname)             #container for style.xml text

            headersInDocument[headerCount]=headerFoooterFormatting(path,headerdoc,docDefaults)

            count=count+1
            headerCount=headerCount+1
        except:
            headExist=False


    #######################################################
    #         reading footer format from docx file        #
    #######################################################
    footerExist=True
    footerCount=0
    count=1

    while footerExist==True:

        try:
            docname="footer"+str(count)+".xml"
            footerDocument=z.read("word/"+docname)             #container for style.xml text
            footersInDocument[footerCount]= headerFoooterFormatting(path,footerDocument,docDefaults)

            count=count+1
            footerCount=footerCount+1
        except:
            footerExist=False



    ###################################################
    #       finding formatting errors in header       #
    ###################################################
    tmp=errors
    for header in range(0,headerCount):
        #paragraphs=len(headersInDocument[header])
        errors=errors+formattingErrors(headersInDocument[header])

    if errors>tmp:
        errors=errors-2

    ###################################################
    #       finding formatting errors in footer       #
    ###################################################
    tmp=errors
    for footer in range(0,footerCount):
        errors=errors+formattingErrors(footersInDocument[footer])
    if errors>tmp:
        errors=errors-2

    print 'Formatting Errors',errors