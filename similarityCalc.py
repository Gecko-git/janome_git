# coding=utf-8
import math

# 類似度の計算
class similarityCalc():
	def __init__(self,pCL,tNL):
		self.pCL = pCL
		self.tNL = tNL

	#ユークリッド距離の計算
	def euclid(self,tA,tB):  
	    powA = 0
	    eDistance=0

	    for i in self.pCL:
	        powA += pow(self.pCL[self.pCL.index(i)][tA] - self.pCL[self.pCL.index(i)][tB],2)
	    eDistance = round(math.sqrt(powA),3)

	    return eDistance

	#コサイン類似度の計算
	def cosine(self,tA,tB):  
	    denominator =0
	    molecule_xi=0
	    molecule_yi=0

	    cSimilarity=0

	    for i in self.pCL:
	        denominator += self.pCL[self.pCL.index(i)][tA]*self.pCL[self.pCL.index(i)][tB]
	        molecule_xi += pow(self.pCL[self.pCL.index(i)][tA],2)
	        molecule_yi += pow(self.pCL[self.pCL.index(i)][tB],2)

	    cSimilarity = round(denominator/ ( math.sqrt(molecule_xi)*math.sqrt(molecule_yi) ),3)

	    return cSimilarity

	#各文書の比較＿（文書数（0から）がpCL.index[i]の要素数に対して0番目の単語を飛ばすため+1する）
	def comparison(self):    
		ecList =[]
		for i in self.tNL:
			for j in self.tNL:
				if len(self.tNL)-(self.tNL.index(i)+1) > self.tNL.index(j) :  #4以下のとき
					for k in self.tNL:
						if self.tNL.index(i)+1 < self.tNL.index(k)+1:
							euclidCalc = self.euclid(self.tNL.index(i)+1,self.tNL.index(k)+1)
							cosineCalc = self.cosine(self.tNL.index(i)+1,self.tNL.index(k)+1)
							ecList.append([self.tNL.index(i),self.tNL.index(k),euclidCalc,cosineCalc])
					break
			print("\r{0}{1}".format(round(self.tNL.index(i)/len(self.tNL)*100,1),"%"), end="")
		return ecList
