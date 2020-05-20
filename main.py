import xml.etree.ElementTree as ET
import os
import glob
import shutil

path = 'C:/XML/'

if not os.path.exists(path):
    os.mkdir(path)

for infile in glob.glob( os.path.join(path, '*.xml') ):
        tree = ET.parse(infile)
        root = tree.getroot()
        cidade = root[0][0][2][2][4].text
        folder = path+'/'+cidade+'/'
        if not os.path.exists(folder):
            os.makedirs(folder)
        shutil.move(infile, folder)
        continue
