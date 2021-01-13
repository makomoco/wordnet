# -*- coding:utf-8 -*-

import sys
import numpy as np
import csv
from nlpva import analysis_1, analysis_2, cal, c_value, sort_by_c, filter

if __name__ == '__main__':
    processed_file = sys.argv[1]

    termlist = []
    termlist_ = []
    analysis_1(termlist,processed_file)
    analysis_2(termlist,processed_file)
    cal(termlist)
    c_value(termlist)
    sort_by_c(termlist)
    filter(termlist,termlist_)


    # print result
    for e in termlist_:
        print(e.to_csv())



