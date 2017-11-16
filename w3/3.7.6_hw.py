from xml.etree import ElementTree

tree = ElementTree.parse("hw.xml") 
root = tree.getroot()


blocks = {'red':0, 'blue':0, 'green':0}
# red = 0
# blue = 0
# green = 0
for i in root:
    print(i.attrib['color'])
    if i.attrib['color'] == 'red':
        blocks[i.attrib['color']] += 1
print(blocks)