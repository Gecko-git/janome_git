# coding=utf-8
import matplotlib.pyplot as plt
import csv

class outputResult():
	def __init__(self):
		pass
		
	# テキストとして出力
	def outputTxt(self,result,name):
		self.result = result
		self.name = name

		with open(self.name, 'w') as f:
			writer = csv.writer(f,lineterminator='\n')
			writer.writerows(self.result)

		print("クラスタデータ保存完了")

		return self.result