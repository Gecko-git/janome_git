# coding=utf-8

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

import numpy as np

class clusterAnalysis():
	def __init__(self,pCL):
		self.pCL = pCL

	# 行列の転置
	def typeConversion(self):
		array_pCL = np.array(self.pCL)

		array_pCL_T = array_pCL.transpose()	
		return array_pCL_T

	#クラスタリングしてプロット
	def clustering(self,clusterNum,pB):
		self.clusterNum = clusterNum	#クラスタ数
		self.pB = pB	

		N_JOBS = 2	#CPUのコア数

		apCLT = self.typeConversion()

		model = KMeans(n_clusters=self.clusterNum, n_jobs=N_JOBS).fit(apCLT)

		pca = PCA(n_components=2)
		pca.fit(apCLT)
		pca_data = pca.fit_transform(apCLT)

		color = plt.rcParams['axes.prop_cycle'].by_key()['color']

		# クラスタリング結果のプロット
		plt.figure()
		for i in range(pca_data.shape[0]):
			plt.scatter(pca_data[i,0], pca_data[i,1], c=color[int(model.labels_[i])])
		#plt.legend()
		plt.savefig('result.png') 

		if self.pB == True:
			plt.show()
		print("プロット保存完了")

		return model.labels_