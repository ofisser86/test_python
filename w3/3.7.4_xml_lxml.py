from xml.etree import ElementTree

tree = ElementTree.parse('example.xml')
root = tree.getroot()

print(tree)
print(root, root.tag, root.attrib)