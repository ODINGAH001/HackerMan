#python3

import xml.etree.ElementTree as et
maxx=0

def perf_func(elem, level=0):
    global maxx
    if(maxx<level):
        maxx=level
    for child in elem.getchildren():
        perf_func(child, level+1)

xml=""
for _ in range(int(input())):
    xml+=input()
tree = et.ElementTree(et.fromstring(xml))
perf_func(tree.getroot())
print(maxx)
