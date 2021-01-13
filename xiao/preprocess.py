#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import re

# 正規表現で前処理
if __name__ == '__main__':
    for line in sys.stdin:
        proccessed = re.sub(r'[^a-zA-Z一-龠　-ー\n\s]','、', line)
        print(proccessed.upper())
