import os

from xml.etree import ElementTree as ET

root = ET.Element('root',{'age':'18'})

son=ET.SubElement(root,'root',{'age':'18'})
ET.SubElement(son,'haha',{'bb':'fhfhf'})

tree = ET.ElementTree(root)
tree.write('aha.xml')