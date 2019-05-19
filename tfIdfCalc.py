# coding=utf-8
from operator import itemgetter
import math

import progressBar as pB

#tf-idf値を出す
class tfIdfCalc():
	def __init__(self,eSAF):
		self.eSAF = eSAF

	# 各単語の文書ごとの出現回数
	def getDocumentFrequency(self,word):
		dF = 0
		for i in self.eSAF:
			for j in self.eSAF[self.eSAF.index(i)]:
				if(word == j[0]):
					dF += 1
		return dF

	# tf-idfリストを作る（ 単語.出現回数.出現文書数,tf-idf値）
	def makeTfIdfList(self):   
		subList=[]
		resultList=[]

		pB_obj = pB.progressBar(len(self.eSAF))	#プログレスバーの表示[1]

		for i in self.eSAF:
			for j in self.eSAF[self.eSAF.index(i)]:
				getdF = self.getDocumentFrequency(j[0])
				idf = math.log10(len(self.eSAF)/getdF) + 1
				subList.append([j[0],j[1],getdF,round(j[1]*idf,2)])
			else:
				subList.sort(key=itemgetter(3))
				subList.reverse()
				resultList.append(subList)
				subList=[]
			pB_obj.barCalc(self.eSAF.index(i)+1)	#プログレスバーの表示[2]

		return resultList