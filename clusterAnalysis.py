# coding=utf-8

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

import gc
import numpy as np
from cycler import cycler
from operator import itemgetter

class clusterAnalysis():
	def __init__(self,pCL):
		self.pCL = pCL

	# 行列の転置
	def typeConversion(self):
		array_pCL = np.array(self.pCL)

		#メモリ解放
		del self.pCL
		gc.collect()

		array_pCL_T = array_pCL.transpose()	

		#メモリ解放
		del array_pCL
		gc.collect()

		return array_pCL_T

	#クラスタリングしてプロット
	def clustering(self,clusterNum,pB,tNL):
		self.clusterNum = clusterNum	#クラスタ数
		self.pB = pB	
		self.tNL = tNL

		N_JOBS = 2	#CPUのコア数

		apCLT = self.typeConversion()

		#主成分分析
		pca = PCA(n_components=2)
		pca.fit(apCLT)
		pca_data = pca.fit_transform(apCLT)
		
		#k平均法
		model = KMeans(n_clusters=self.clusterNum,n_jobs=N_JOBS).fit(pca_data)

		color = plt.rcParams['axes.prop_cycle'].by_key()['color']


		lNum=[]
		# クラスタリング結果のプロット
		plt.figure()
		plt.grid(True)
		for i in range(pca_data.shape[0]):
			if int(model.labels_[i]) not in lNum:
				plt.scatter(pca_data[i,0], pca_data[i,1], c=color[int(model.labels_[i])],label=str(int(model.labels_[i])))
				lNum.append(int(model.labels_[i]))
			else :
				plt.scatter(pca_data[i,0], pca_data[i,1], c=color[int(model.labels_[i])])
		plt.legend(loc='upper right')
		plt.title('k-means scatter plot')
		plt.xlabel('x')
		plt.ylabel('y')

		kcC = model.cluster_centers_
		for i in kcC:
			plt.scatter(i[0], i[1],marker="x",c="black")

		plt.savefig('result.png') 
		if self.pB == True:
			plt.show()
		print("プロット保存完了")

		#各ドキュメントの２次元座標とクラスタ番号のリスト
		pcaD_list = pca_data.tolist()
		for i in range(len(pcaD_list)):
			pcaD_list[i].append(int(model.labels_[i]))

		#文書名を追加
		for i in range(len(pcaD_list)):
			pcaD_list[i].insert(0,self.tNL[i])
		
		pcaD_list.sort(key=itemgetter(3))

		return pcaD_list

