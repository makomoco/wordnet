import MeCab
import math
import string
import re
#import xlrd
#import xlwt
import numpy as np

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
	mecab = MeCab.Tagger('/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
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