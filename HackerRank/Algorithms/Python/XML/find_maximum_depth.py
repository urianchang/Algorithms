# Python 3.7
# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for e in elem:
        depth(e, level)

if __name__ == '__main__':
    n = int(raw_input())
    xml = ""
    for i in range(n):
        xml =  xml + raw_input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print maxdepth
