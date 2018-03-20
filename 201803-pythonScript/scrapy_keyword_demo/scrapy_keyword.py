# -*- coding: UTF-8 -*-

import requests
import re
import codecs

j = 1

# 应用汇
pageNum = 34

# 先清空文件内容
fo = open('../extract_keyword_demo/appNamesByScrapy', 'w')
fo.truncate()
fo.close()

# 抓取并写入文件
f = codecs.open('../extract_keyword_demo/appNamesByScrapy', 'a', 'utf-8')

# 411~424-游戏 301~315,60-软件
for a in range(1, 15):
    for i in range(1, int(pageNum)):
        html401 = requests.get('http://www.appchina.com/category/' + str(410+a) + '/1_1_' + str(i) + '_1_0_0_0.html')
        html402 = requests.get('http://www.appchina.com/category/' + str(410+a) + '/1_' + str(i) + '_1_2_0_0_0.html')
        html403 = requests.get('http://www.appchina.com/category/' + str(410+a) + '/' + str(i) + '_1_1_3_0_0_0.html')
        html301 = requests.get('http://www.appchina.com/category/' + str(300+a) + '/1_1_' + str(i) + '_1_0_0_0.html')
        html302 = requests.get('http://www.appchina.com/category/' + str(300+a) + '/1_' + str(i) + '_1_2_0_0_0.html')
        html303 = requests.get('http://www.appchina.com/category/' + str(300+a) + '/' + str(i) + '_1_1_3_0_0_0.html')
        title = re.findall('<h1 class="app-name" title="(.*?)">', html401.text, re.S)
        title = title + re.findall('<h1 class="app-name" title="(.*?)">', html402.text, re.S)
        title = title + re.findall('<h1 class="app-name" title="(.*?)">', html403.text, re.S)
        title = title + re.findall('<h1 class="app-name" title="(.*?)">', html301.text, re.S)
        title = title + re.findall('<h1 class="app-name" title="(.*?)">', html302.text, re.S)
        title = title + re.findall('<h1 class="app-name" title="(.*?)">', html303.text, re.S)
        if len(title) == 0:
            continue
        for each in title:
            print str(j) + ":" + each
            f.writelines(each + '\n')
            j = j + 1
        print '------' + str(a) + '------' + str(i) + '-------' + str(len(title))

f.close()
