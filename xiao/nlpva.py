#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MeCab
import math
import string
import re
import xlrd
import xlwt
import numpy as np
from xlutils.copy import copy 
from gensim.models import word2vec
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from matplotlib import pyplot as plt
from matplotlib import rcParams

class Term:
	def __init__(self):
		self.word = ''
		self.length = 1
		self.n = 1 # total frequency of term in corpus
		self.t = 0 # long collocation frequency
		self.c = 0 # long collocation kind
		self.c_value = 0.0
		self.re_ranked_score = 0.0
		self.vector = np.zeros([100],dtype=np.float32)
		self.flag = True

# 正規表現で前処理
def format_text(file,new_file):
	f = open(file)
	ff = open(new_file,'w')
	line = f.readline()
	while line :
		line = line.upper()
		line = re.sub(r'[^A-Z　-龯\s]','、', line)
		ff.write(line)
		line = f.readline()
	f.close()
	ff.close()

# C_value高い順ソート
def sort_by_c(termlist):
	n = len(termlist)
	for i in range(n):
		for j in range(n-i-1):
			if termlist[j].c_value <termlist[j+1].c_value:
				termlist[j],termlist[j+1] = termlist[j+1],termlist[j]

# 連語種類と頻度の計算
def cal(termlist):
	n = len(termlist)
	for i in range(n):
		for j in range(n):
			if termlist[i].word in termlist[j].word and i!=j:
				termlist[i].c += 1
				termlist[i].t += termlist[j].n

# C_value計算
def c_value(termlist):
	n = len(termlist)
	for i in range(n):
		if termlist[i].c == 0 and termlist[i].length != 0 :
			termlist[i].c_value = math.log(termlist[i].length,2)*termlist[i].n
		else:
			if termlist[i].length != 0 :
				termlist[i].c_value = math.log(termlist[i].length,2)*(termlist[i].n - termlist[i].t/termlist[i].c)

# パターンによって抽出　名詞⁺
def analysis_1(termlist,file):
	mecab = MeCab.Tagger('')
	with open(file, 'r') as file:
		for line in file.readlines():
			temp_word = ''
			temp_length = 0
			process_line = line.strip()
			for chunk in mecab.parse(process_line).splitlines()[:-1]:
				term = Term()
				if '\t' in chunk :
					(surface , feature) = chunk.split('\t')
					# if feature.startswith('名詞') and feature != '名詞,サ変接続,*,*,*,*,*' :
					if feature.startswith('名詞') :
						temp_word += surface
						temp_length += 1
						if surface.isalpha() :
							temp_word += ' '
					else :
						if surface != '' and temp_word != '' :
							flag = 0
							for i in range(len(termlist)):
								if termlist[i].word == temp_word:
									termlist[i].n += 1
									flag = 1
							if flag == 0 :
								term.word = temp_word
								term.length = temp_length
								termlist.append(term)
							temp_word = ''
							temp_length = 0

			if temp_word != '' :
				flag = 0
				for i in range(len(termlist)):
					if termlist[i].word == temp_word:
						termlist[i].n += 1
						flag = 1
				if flag == 0 :
					term.word = temp_word
					term.length = temp_length
					termlist.append(term)
				temp_word = ''
				temp_length = 0

# パターンによって抽出　（名詞⁺）＋（を、に、から、へ）＋（サ変名詞OR動詞）
def analysis_2(termlist,file):
	mecab = MeCab.Tagger('')
	with open(file, 'r') as file:
		for line in file.readlines():
			temp_word = ''
			temp_length = 0
			pattern_start = 0
			pattern_end = 0
			process_line = line.strip()
			word_list = mecab.parse(process_line).splitlines()[:-1]
			for i , element in enumerate(word_list):
				term = Term()
				if '\t' in word_list[i] :
					(surface , feature) = word_list[i].split('\t')
					# if feature.startswith('名詞') and feature != '名詞,サ変接続,*,*,*,*,*' and surface != '' :
					if feature.startswith('名詞') and surface != '' :

						temp_word += surface
						temp_length += 1
						pattern_start = 1
						if surface.isalpha() :
							temp_word += ' '

					elif (surface =='を' or surface =='に' or surface =='から' or surface =='へ' or surface =='が') and (i+1 < len(word_list)):
						(next_surface , next_feature) = word_list[i+1].split('\t')
						if (next_feature.startswith('名詞,サ変接続') or next_feature.startswith('動詞')) and next_feature != '名詞,サ変接続,*,*,*,*,*' :
							temp_word += surface
							temp_word += next_surface
							temp_length += 2
							pattern_end = 1
							if surface.isalpha() :
								temp_word += ' '

							for i in range(len(termlist)) :
								if termlist[i].word == temp_word :
									termlist[i].n += 1
									temp_word = ''
									temp_length = 0
									pattern_start = 0
									pattern_end = 0

							if pattern_start == 1 and pattern_end == 1 :
								term.word = temp_word
								term.length = temp_length
								termlist.append(term)
								temp_word = ''
								temp_length = 0
								pattern_start = 0
								pattern_end = 0
						else :
							temp_word = ''
							temp_length = 0
							pattern_start = 0
							pattern_end = 0
					else :
						temp_word = ''
						temp_length = 0			
						pattern_start = 0
						pattern_end = 0

# エクセルファイルに保存
def write_to_excel(termlist,workbook,sheet):
	oldwkb = xlrd.open_workbook(workbook)
	newwkb = copy(oldwkb)

	sh = newwkb.add_sheet(sheet,cell_overwrite_ok=True)

	j = 0
	for i in range(len(termlist)) :
		sh.write(j,0,termlist[i].word)
		sh.write(j,1,termlist[i].n)
		sh.write(j,2,termlist[i].c_value)
		sh.write(j,3,termlist[i].c)
		sh.write(j,4,termlist[i].t)
		j = j + 1

	newwkb.save(workbook)

# C_valueフィルター
def filter(termlist,newlist):
	for i in range(len(termlist)) :
		if termlist[i].c_value > 1 :
			newlist.append(termlist[i])

# IT用語フィルター
def filter_Iterm(termlist,newlist,file_Iterm):
	Itermlist = []
	with open(file_Iterm,'r') as file :
		for line in file.readlines() :
			process_line = line.strip()
			Itermlist.append(process_line)
	for i in range(len(termlist)) :
		if termlist[i].word not in Itermlist :
			newlist.append(termlist[i])
		else :
			print (termlist[i].word)
	print ('************************')

# 対比分析
def contrastive_analysis(termlist1,termlist2,workbook,sheet):
	con_term = []
	con_frequency = []
	for i in range(len(termlist2)):
		con_term.append(termlist2[i].word)
		con_frequency.append(termlist2[i].n)
	Fc = []
	for i in range(len(termlist1)):
		if termlist1[i].word in con_term:
			Fc.append(con_frequency[con_term.index(termlist1[i])])
		else:
			Fc.append(0)
	Nc = sum(Fc)
	for i in range(len(termlist1)):
		termlist1[i].re_ranked_score = math.atan(math.log(termlist1[i].c_value,2))*(termlist1[i].c_value/((Fc[i]+1)/Nc))
	for i in range(len(termlist1)):
		for j in range(len(termlist1)-i-1):
			if termlist1[j].re_ranked_score <termlist1[j+1].re_ranked_score:
				termlist1[j],termlist1[j+1] = termlist1[j+1],termlist1[j]

	oldwkb = xlrd.open_workbook(workbook)
	newwkb = copy(oldwkb)
	sh1 = newwkb.add_sheet(sheet,cell_overwrite_ok=True)
	for i in range(len(termlist1)) :
		sh1.write(i,0,termlist1[i].word)
		sh1.write(i,1,termlist1[i].n)
		sh1.write(i,2,termlist1[i].c_value)
		sh1.write(i,3,termlist1[i].re_ranked_score)
	newwkb.save(workbook)

# ベクトル化
def word2vec_vector(termlist):

	model = word2vec.Word2Vec.load('/Users/xiaoyuedong/Desktop/研究/code/wiki_wakati_new.model')
	mecab = MeCab.Tagger('-Owakati')
	for i in range(len(termlist)):
		watati = mecab.parse(termlist[i].word).split(' ')
		for j in range(termlist[i].length):

			try:
				termlist[i].vector += model[watati[j]]
			except KeyError:
				termlist[i].vector += np.zeros([100],dtype=np.float32)

		termlist[i].vector = np.divide(termlist[i].vector,termlist[i].length)

# 階層型クラスタリング
def hierarchy_cluster(data, wordlist, method='ward', metric='euclidean'):
    
    data = np.array(data)
 
    linkage_result = linkage(data, method=method, metric=metric)

    plt.figure(num=None, figsize=(16, 9), dpi=200, facecolor='w', edgecolor='k')
    rcParams['font.family']='IPAexGothic'
    plt.title('feature')

    # threshold = 0.7 * np.max(linkage_result[:, 2])
    # print(threshold)
    threshold = 30
    dendrogram(linkage_result,labels=wordlist,color_threshold=threshold)
    plt.show()
    
    cluster_assignments = fcluster(linkage_result, threshold, criterion='distance')
    num_clusters = cluster_assignments.max()

    indices = []
    for cluster_number in range(1, num_clusters + 1):
        indices.append(np.where(cluster_assignments == cluster_number)[0])
 
    return num_clusters, indices

def get_cluster_indices(cluster_assignments):

    n = cluster_assignments.max()
    indices = []
    for cluster_number in range(1, n + 1):
        indices.append(np.where(cluster_assignments == cluster_number)[0])
    
    return indices

if __name__ == '__main__':

	workbook = '/Users/xiaoyuedong/Desktop/研究/結果/pot_feature.xls' 
	
# 要求仕様書１
	termlist1 = []
	newlist1 = []
	file1 = '/Users/xiaoyuedong/Desktop/研究/code/仕様書/POT_Specification_v6_手動.txt'
	new_file1 = '/Users/xiaoyuedong/Desktop/研究/code/仕様書/POT_Specification_v6_0206.txt'
	sheet1 = 'new_v6_nofilter'
	# format_text(file1,new_file1)
	analysis_1(termlist1,new_file1)
	analysis_2(termlist1,new_file1)
	cal(termlist1)
	c_value(termlist1)
	sort_by_c(termlist1)
	filter(termlist1,newlist1)
	# write_to_excel(termlist1,workbook,sheet1)
	word2vec_vector(newlist1)

# 要求仕様書２
	# termlist2 = []
	# newlist2 = []
	# newlist2_ = []
	# file2 = '/Users/xiaoyuedong/Desktop/研究/code/仕様書/POT_Specification_v7.txt'
	# new_file2 = '/Users/xiaoyuedong/Desktop/研究/code/仕様書/POT_Specification_v7_1112.txt'
	# sheet2 = 'v7'
	# # format_text(file2,new_file2)
	# analysis_1(termlist2,new_file2)
	# analysis_2(termlist2,new_file2)
	# cal(termlist2)
	# c_value(termlist2)
	# sort_by_c(termlist2)
	# filter(termlist2,newlist2)
	# # write_to_excel(newlist2,workbook,sheet2)
	# word2vec_vector(newlist2)

# クラスター　ランキング
	wordlist = []
	cluster_sum = []
	cluster_average = []

	for i in range(len(newlist1)):
		wordlist.append(newlist1[i].word)

	arr = np.vstack((newlist1[0].vector,newlist1[1].vector))
	for i in range(2,len(newlist1)):
		arr = np.vstack((arr,newlist1[i].vector))
		
	num_clusters, indices = hierarchy_cluster(arr,wordlist)
	# print("%d clusters" % num_clusters)
	for k, ind in enumerate(indices):
		score_sum = 0
		for i in range(len(indices[k])):
			score_sum = score_sum + newlist1[indices[k][i]].c_value
		score_average = score_sum / len(indices[k])
		cluster_sum.append(score_sum)
		cluster_average.append(score_average)
	# 	# print ("cluster", k, "is", ind, "num:", len(indices[k]), "sum:", score_sum, "average:", score_average)

#################
	# print ("rank by sum:")
	# rank_sum=sorted(enumerate(cluster_sum), key=lambda x:x[1], reverse=True)
	# for i in range(len(rank_sum)):
	# 	for j in range(len(indices[rank_sum[i][0]])):
	# 		print (newlist1[indices[rank_sum[i][0]][j]].word)
#################
	# print ("rank by average:")
	rank_average=sorted(enumerate(cluster_average), key=lambda x:x[1], reverse=True)
	for i in range(len(rank_average)):
		for j in range(len(indices[rank_average[i][0]])):
			print (newlist1[indices[rank_average[i][0]][j]].word)
#################
	# print ('done')























