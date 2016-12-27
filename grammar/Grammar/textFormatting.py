# -*- coding: utf-8 -*-
#####################################
#     define all possible style     #
#####################################
class style:
    def __init__(self):
        self.forntFamily=""
        self.forntSize=""
        self.color=""
        self.backgroundColor=""
        self.bold=False
        self.italic=False
        self.underline=""
        self.delete=False
        self.styleName=""
        self.spacingBefore=""
        self.spacingAfter=""
        self.lineHeight=""
        self.verticleLine=""
        self.horizontalLine=""
        self.name=""
        self.basedOn=""
        self.parent=''
        self.link=""
        self.borderTop=""
        self.borderLeft=""
        self.borderBottom=""
        self.borderRight=""
        self.borderBetween=""
        self.borderBar=""
        self.runLevelBorder=""



##################################################################
# define formatting of text in terms of paragraph and run level  #
##################################################################
class formatting:

    def __init__(self):
        self.paragraphProperties=style()
        self.DefaultstyleFormatting=style()
        self.parent=""
        self.runLevelProperties={}




########################################################
#     contain style and text of run level elements     #
########################################################
class runlevel():
    def __init__(self):
        self.properties=style()
        self.Text=""


####################################################
#         contain formatting of table              #
####################################################
class table():
    def __init__(self):

       self.tableProperties=tableProperties()
       #self.cellMargin=cellsMargin()
       self.aboutTable=generalTableProperties()
       self.textProperty=textProperties()
       self.firstRow=tableStyleProperties()
       self.lastRow=tableStyleProperties()
       self.firstCol=tableStyleProperties()
       self.lastCol=tableStyleProperties()
       self.band1Vert=tableStyleProperties()
       self.band1Horz=tableStyleProperties()
       self.grid={}
       self.cols=0
       self.rows=0


####################################################
#         block and span level properties          #
####################################################
class textProperties():
    def __init__(self):
        self.generalParagraphProperties=style()
        self.generalRunProperties=style()


####################################################
#  class for maintaining cells and rows properties #
####################################################
class tableStyleProperties():
    def __init__(self):
        self.cellTextProperties=textProperties()
        self.tableCellsProperties=tableCellProperty()

#####################################################
#    class for table properties like margin,border  #
#####################################################
class tableProperties():
    def __init__(self):
        self.tblBorders=tableBorder()
        self.tblCellMar=cellsMargin()
        self.tblStyleRowBandSize=''
        self.tblStyleColBandSize=''


#########################################
#    contain table cell properties      #
#########################################
class tableCellProperty():
    def __init__(self):
        self.tblBorder=tableBorder()
        self.shade=""
        self.width=''



#################################################
#        contain border of tables cells         #
#################################################
class tableBorder():
    def __init__(self):
        self.borderTop=""
        self.borderLeft=""
        self.borderBottom=""
        self.borderRight=""
        self.borderInsideH=""
        self.borderInsideV=""



###################################################
#     define margin within the cells of table     #
###################################################
class cellsMargin():
    def __init__(self):
        self.top=""
        self.left=""
        self.bottom=""
        self.right=""

###################################################
#            general table properties             #
###################################################
class generalTableProperties():
    def __init__(self):
        self.name=""
        self.styleId=""
        self.basedOn=""
class tablePropertiesWithText():
    def __init__(self):
        self.tblTextPropertiese={}
        self.parent=textProperties
        self.tblCellProperty=tableCellProperty()

#########################################################
#      class for holding style name and information     #
#########################################################
class stylesInDocuments():
    def __init__(self):
        self.forntFamily=""
        self.forntSize=""
        self.color=""
        self.name=""



#########################################################
#           class for text boxes information            #
#########################################################
class textBox():
    def __init__(self):
        self.textBoxContant={}
        self.textBoxProperties=TextBoxProperties()


#########################################################
#           class for text boxes properties             #
#########################################################
class TextBoxProperties():
    def __init__(self):
        self.fillColor=''
        self.stokeColor=''
        self.stokeWeight=''
        self.shadowColor=''
        self.IsShadow=False
class listStyle():
    def __init__(self):
        self.numberFormat=''
        self.levelText=''
        self.levelJustify=''

#print len('<w:lvlJc w:val=')
#print ord(u'')