#python3

import xml.etree.ElementTree as et
xml=""""""
for _ in range(int(input())):
    xml+=input()
tree = et.ElementTree(et.fromstring(xml))
root = tree.getroot()
count=len(root.attrib)
for child_of_root in root:
    if len(child_of_root): 
        for subchild in child_of_root:
            count=count+len(subchild.attrib)
    else:
        count=count+len(child_of_root.attrib)
    #print(child_of_root.attrib)
print(count)
