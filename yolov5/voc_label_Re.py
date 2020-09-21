import xml.etree.ElementTree as ET
import pickle
import os
from collections import OrderedDict
from os import listdir, getcwd
from os.path import join

'''
    工作服检测 VOC2021 
'''
sets = [('2021', 'train')]
classes = ["reflective_clothes", "other_clothes"]  # 0-反光衣 1-其它
print(classes)

data_root = r'/home/helmet_dataset/'

# voc的训练txt 验证txt 必须在VOC*** 以及目录下  不能在Main目录下面；它是在统计目录下
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)  # 中心点坐标 wh

def convert_annotation(year, image_id):
    global data_root
    in_file = open(data_root + 'VOC%s/Annotations/%s.xml'%(year, image_id), encoding='utf-8')
    out_file = open(data_root + 'VOC%s/labels/%s.txt'%(year, image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes:  # or int(difficult)==1 不关心difficult
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

# wd = getcwd()

for year, image_set in sets:
    if not os.path.exists(data_root + 'VOC%s/labels/'%(year)):
        os.makedirs(data_root + 'VOC%s/labels/'%(year))
    image_ids = open(data_root + 'VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()#有空格的就不行了
    list_file = open(data_root + 'VOC%s/%s_%s.txt'%(year, year, image_set), 'w')
    for image_id in image_ids:
        print(image_id)
        list_file.write(data_root + 'VOC%s/JPEGImages/%s.jpg\n'%(year, image_id))
        convert_annotation(year, image_id)
    list_file.close()

# os.system("cat 2007_train.txt 2007_val.txt 2012_train.txt 2012_val.txt > train.txt")
# os.system("cat 2007_train.txt 2007_val.txt 2007_test.txt 2012_train.txt 2012_val.txt > train.all.txt")

