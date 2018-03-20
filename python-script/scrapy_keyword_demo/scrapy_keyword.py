# -*- coding:utf-8 -*-

import requests
import re
import codecs

# j = 1
#
# html = requests.get('http://app.mi.com/topList')
#
# label = re.findall('<p class="app-desc">', html.text, re.S)
#
# pageAppNum = len(label)
#
# print(pageAppNum)
#
# appNum = 1000
#
# pageNum = math.ceil(float(appNum) / pageAppNum)
#
# # 先清空文件内容
# fo = open('../extract_keyword_demo/appNamesByScrapy', 'w')
# fo.truncate()
# fo.close()
#
# # 抓取并写入文件
# f = codecs.open('../extract_keyword_demo/appNamesByScrapy', 'a', 'utf-8')
#
# for i in range(1, int(pageNum + 1)):
#     html = requests.get('http://app.mi.com/topList?page=' + str(i))
#     title = re.findall('</a><h5><a href=".*?">(.*?)</a></h5><p class="app-desc">', html.text, re.S)
#     for each in title:
#         if j <= appNum:
#             print(str(j) + ":" + each)
#             f.writelines(each + '\n')
#         j = j + 1
#
# f.close()

j = 1

pageNum = 34

# 先清空文件内容
fo = open('../extract_keyword_demo/appNamesByScrapy', 'w')
fo.truncate()
fo.close()

# 抓取并写入文件
f = codecs.open('../extract_keyword_demo/appNamesByScrapy', 'a', 'utf-8')

for i in range(1, int(pageNum)):
    html = requests.get('http://www.appchina.com/category/40/' + str(i) + '_1_1_3_0_0_0.html')
    title = re.findall('<h1 class="app-name" title="(.*?)">', html.text, re.S)
    for each in title:
        print(str(j) + ":" + each)
        f.writelines(each + '\n')
        j = j + 1

for i in range(1, int(pageNum)):
    html = requests.get('http://www.appchina.com/category/30/' + str(i) + '_1_1_3_0_0_0.html')
    title = re.findall('<h1 class="app-name" title="(.*?)">', html.text, re.S)
    for each in title:
        print(str(j) + ":" + each)
        f.writelines(each + '\n')
        j = j + 1

f.close()
