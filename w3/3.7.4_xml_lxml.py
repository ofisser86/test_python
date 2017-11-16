from xml.etree import ElementTree

tree = ElementTree.parse('example.xml')
root = tree.getroot()

# print(tree)
# print(root, root.tag, root.attrib)

# for child in root:
#     print(child.tag)
#     for sub in child:
#         print(sub.text)

#print(root[0][0].text)
# for element in root.iter("score"):
#     for child in element:
#         print(child.text)
#     print(element)

tree.write('example_copy.xml')