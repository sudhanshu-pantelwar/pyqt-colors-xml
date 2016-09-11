from lxml import etree

xmlPath = "/home/jash/Desktop/pyQT/colors.xml"

colorList = []

def xmlData(xmlPath):
    tree = etree.parse(xmlPath)
    colors = tree.xpath('//colors/color')

    for color in colors:
        colorList.append(color.text)
    return colorList


