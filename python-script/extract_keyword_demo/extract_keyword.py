# -*- coding:utf-8 -*-

import marisa_trie

app_name_by_scrapy_file = 'appNamesByScrapy'

fo = open(app_name_by_scrapy_file)
lines = fo.read().splitlines()
app_name_trie = marisa_trie.Trie(lines)
fo.close()