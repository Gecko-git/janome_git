# coding=utf-8
from operator import itemgetter
import pprint 

# 文章の要約
class summarize():
	def __init__(self,tfidfL):
		self.tfidfL = tfidfL

	# 各文章の強さを計算
	def sentenceStrengthCalc(self):

		sSL = []
		tfIdfSum =0
		for i,j in enumerate(self.tfidfL):
			for k in self.tfidfL[self.tfidfL.index(j)]:
				print(k,len(self.tfidfL[self.tfidfL.index(j)]))
				tfIdfSum += k[3]
			else:
				if len(self.tfidfL[self.tfidfL.index(j)]) != 0:
					sSValue = tfIdfSum / len(self.tfidfL[self.tfidfL.index(j)])
				else:
					sSValue = 0
				sSL.append([i,sSValue])
				tfIdfSum = 0

		sSL.sort(key=itemgetter(1),reverse=True)
		pprint.pprint(sSL)

		return sSL

	# 要約文生成
	def makeSummary(self,tsSList,n):
		self.tsSList = tsSList
		sSL = self.sentenceStrengthCalc()
		mS = []

		for i,j in enumerate(sSL):
			if i >= n:
				break

			mS.append([j[0],self.tsSList[j[0]]])

		mS.sort(key=itemgetter(0))
		print(mS)

		return mS


