# coding=utf-8
import matplotlib.pyplot as plt

class outputResult():
	def __init__(self,cR,tNL):
		self.cR = cR
		self.tNL = tNL

	# 分類した文書をリストにする
	def categorize(self):
		doucmentCategorizeList=[[] for i in range(max(self.cR+1))]	#最大値が2だったら3で３つの要素

		for i,j in enumerate(self.cR):
			doucmentCategorizeList[j].append(self.tNL[i])

		return doucmentCategorizeList

	# テキストとして出力
	def outputTxt(self):
		s=""
		color = plt.rcParams['axes.prop_cycle'].by_key()['color']

		dCL = self.categorize()

		for i in dCL:
			s += "[ クラスタ：{0} ]\n".format(color[dCL.index(i)])
			for j in i:
				s += "\t{0}\n".format(j)

		with open("result.txt", mode='w') as f:
			f.write(s)
		print("クラスタデータ保存完了")

		return s