# -*- coding:utf-8 -*-

import sys
import numpy as np
import csv
from nlpva import Term, word2vec_vector, hierarchy_cluster

if __name__ == '__main__':
    newlist = [Term.csv2instance(row) for row in csv.reader(sys.stdin)]

    word2vec_vector(newlist)

    wordlist=[e.word for e in newlist]

    arr = np.vstack((newlist[0].vector,newlist[1].vector))
    for i in range(2,len(newlist)):
        arr = np.vstack((arr,newlist[i].vector))

    num_clusters, indices = hierarchy_cluster(arr,wordlist)

    print('done')