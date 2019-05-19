# coding=utf-8

import pprint 

#途中結果を表示するか
class consolePrint():
	def __init__(self,pJudg):
		self.pJudg = pJudg

	def cPrint(self,printData):
		self.printData = printData

		if self.pJudg == True:
			pprint.pprint(self.printData)