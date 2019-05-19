# coding=utf-8
import re

# 文書を文章ごとに区切る
class separateSentence(): #引数：文書（str）,区切り文字(str)
	def __init__(self,sentence,delimiter):
		self.sentence = sentence
		self.delimiter = delimiter

	def separate(self):
		sS = re.split(self.delimiter,self.sentence)
		return sS