import os
import time
from bs4 import BeautifulSoup
import requests
import json
import sys
import random
import pprint
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import utils

archive_dir = 'archive'
cookie = '_zap=1dacec19-471e-4b4a-b2e4-7c1492fad30f; d_c0="APARiAnkdxGPToFkp7-VMzm5b_uSZjtoack=|1592883509"; _ga=GA1.2.970764465.1592883510; _xsrf=cae30116-fb4a-4d1f-a808-697f912b80cb; _gid=GA1.2.201703007.1593153659; capsion_ticket="2|1:0|10:1593154645|14:capsion_ticket|44:YzNmMGM0MmE5NWRmNDAzOGJkZjk4N2UyYmQwYzQxMzI=|d65cae80a0223188629b1d114343cf3626ed747ab936632e7c047840f2d6de38"; SESSIONID=tAQ3tYSt3wWBvMD4cEKVxGlnp8jshDMAXuqEv2LSS5P; JOID=V1kSAk2LuubhGkEBDI99_bVDq30f-_2x1W0cVH67ybelaw9BPt4mErsdQwENBtouywLV2GngKtqVeciZu7uFDvM=; osd=UlASBUyOs-bmG0QIDIh8-LxDrHwa8v221GgVVHm6zL6lbA5EN94hE74UQwYMA9MuzAPQ0WnnK9-cec-YvrKFCfI=; z_c0="2|1:0|10:1593154647|4:z_c0|92:Mi4xZUcwaUFBQUFBQUFBOEJHSUNlUjNFU1lBQUFCZ0FsVk5WLXJpWHdEY1docnkyVktaeWxOSlB0SXlJZ1NaWGloZkt3|c0d159d0907885bdac19b1d4935b147c2e4d7df3d1316029d9fa2c2c4d46b1eb"; tst=r; q_c1=2d2bd9133eaa44dfad478f4e84874ae6|1593156281000|1593156281000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1592883510,1593153657,1593156278,1593163691; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1593179495; KLBRSID=031b5396d5ab406499e2ac6fe1bb1a43|1593179517|1593179477'

print 'zhihu archive start ...'

#sync following list
json_file = os.path.join(archive_dir, 'index.json')
if os.path.exists(archive_dir) and os.path.exists(json_file):
    print 'following list exists'
    pass
else:
    if not os.path.exists(archive_dir):
        print 'new node, create archive folder'
        os.makedirs(archive_dir)
    print 'sync following list'
    utils.get_follow_by_author(archive_dir, 'xjq314', cookie)

#sync answer by author
author_folders = os.listdir(archive_dir)
for f in author_folders:
    if f != 'index.json':
        print 'dealing with author: ' + f
        answer_folder = os.path.join(archive_dir, f, 'answer')
        json_file = os.path.join(answer_folder, 'index.json')
        if os.path.exists(answer_folder) and os.path.exists(json_file):
            print 'answer list exists'
        else:
            if not os.path.exists(answer_folder):
                print 'new followee, create answer folder'
                os.makedirs(answer_folder)
            print 'sync answers of author: ' + f
            utils.get_answers_by_author(archive_dir, f, cookie)

#sync collection by author
author_folders = os.listdir(archive_dir)
for f in author_folders:
    if f != 'index.json':
        print 'dealing with author: ' + f
        collection_folder = os.path.join(archive_dir, f, 'collections')
        json_file = os.path.join(collection_folder, 'index.json')
        if os.path.exists(collection_folder) and os.path.exists(json_file):
            print 'collection list exists'
        else:
            if not os.path.exists(collection_folder):
                print 'new followee, create collection folder'
                os.makedirs(collection_folder)
            print 'sync collection of author: ' + f
            utils.get_collections_by_author(archive_dir, f, cookie)

#sync answers by collection
author_folders = os.listdir(archive_dir)
for f in author_folders:
    collections_dir = os.path.join(archive_dir, f, 'collections')
    collection_folders = os.listdir(collections_dir)
    if len(collection_folders) <= 1:
        continue
    for c in collection_folders:
        if c != 'index.json':
            print 'dealing with collection: ' + c
            answer_folder = os.path.join(collections_dir, c)
            json_file = os.path.join(answer_folder , 'index.json')
            if os.path.exists(answer_folder) and os.path.exists(json_file):
                print 'answer list exists'
            else:
                print 'sync answer of collection: ' + c 
                utils.get_answers_by_collection(archive_dir, c, f, cookie) 

print 'end of program'