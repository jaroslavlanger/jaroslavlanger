import xml.etree.ElementTree as etree

tree = etree.parse('jidelnicek_podle_Jarda.xml')

root = tree.getroot()

#print('Root:', root.tag)
#print('Root:', dir(root))
"""
for child in root:
    print(child)
"""
print(root.findall('.//jidelnicek'))