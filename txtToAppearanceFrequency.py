# coding=utf-8

from janome.tokenizer import Tokenizer
from janome.tokenfilter import POSKeepFilter
from janome.analyzer import Analyzer
from janome.tokenfilter import TokenCountFilter
from operator import itemgetter
import glob

import progressBar as pB

# テキスト名の取得
class getReadTxtName():
	def __init__(self,path):
		self.path = path	#指定パス

	def getTxtNameList(self):
		tNL = glob.glob(self.path)
		return tNL

# テキストを取得
class getTxt():
	def __init__(self,tNL,characterCode):
		self.tNL = tNL 
		self.characterCode = characterCode

	def openTxtList(self):
		txtList = []

		pB_obj = pB.progressBar(len(self.tNL))	#プログレスバーの表示[1]
		

		for i in self.tNL:
			with open(i, mode='r',encoding=self.characterCode) as f:
				s = f.read()
				txtList.append(s)
			pB_obj.barCalc(self.tNL.index(i)+1)	#プログレスバーの表示[2]
		return txtList

#str中の単語の出現頻度
class appearanceFrequency_count():
	def __init__(self,filter,threshold):
		self.filter = filter	# 例) "名詞,一般"
		self.threshold = int(threshold)	# str->int

	def tokenize(self,documentList):	#単語と出現頻度のタプルのリストを返す
		self.documentList = documentList
		aFList = []

		pB_obj = pB.progressBar(len(self.documentList))	#プログレスバーの表示[1]

		fS = self.filter.split('_')

		for i in self.documentList:
			t = Tokenizer()
			token_filters = [POSKeepFilter(fS),TokenCountFilter(sorted=True)]
			analyzer = Analyzer([], t, token_filters)
			tokens_count = [token for token in analyzer.analyze(i) if token[1] >= self.threshold]
			aFList.append(tokens_count)
			pB_obj.barCalc(self.documentList.index(i)+1)	#プログレスバーの表示[2]
		return aFList

	def allTokenDisplay(self):	#品詞付きで全ての単語の表示
		t = Tokenizer()
		for token in t.tokenize(self.document):
		    print(token)