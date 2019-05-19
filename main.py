# coding=utf-8

import txtToAppearanceFrequency as tTAF
import tfIdfCalc as tIC
import preparationCalc as pC
import similarityCalc as sC
import clusterAnalysis as cA
import outputResult as oR
import consolePrint as cP

s1 = input("> テキストのパス（例：./dir/*.trn1）：")
s2 = input("> 品詞フィルター（例：名詞,一般）：")
s3 = input("> しきい値（例：5）：")
s4 = input("> クラスタ数（データ数以下）：")
s5 = input("> 結果を表示するか(y/n)：")
s6 = input("> 文字コード（例：cp932）：")

if s5 == 'y':
	printBool = True
elif s5 == 'n':
	printBool = False

cP_obj = cP.consolePrint(printBool)

# データ名前の読み込み＿（指定パスのテキストの名前リストを返す）
print("\n●データ名の取得")
gRTN_obj = tTAF.getReadTxtName(s1)
tNList = gRTN_obj.getTxtNameList()
print(len(tNList),"件読み込み\n")
cP_obj.cPrint(tNList)

# テキストの読み込み＿（指定テキストのそれぞれの内容をリストで返す）
print("●テキストの読み込み")
gT_obj = tTAF.getTxt(tNList,s6)
txtStrList = gT_obj.openTxtList()
cP_obj.cPrint(txtStrList)

# 出現頻度を取得＿（テキストの内容からそれぞれの出現頻度をリストで返す）
print("●各テキストの出現頻度取得")
aF_obj = tTAF.appearanceFrequency_count(s2,s3)
everyDocument_aFList = aF_obj.tokenize(txtStrList)
cP_obj.cPrint(everyDocument_aFList)

# tf-idf値の計算＿（各文字のtfIdf値のリストを返す）
print("●tf-idf値の計算")
tIC_obj = tIC.tfIdfCalc(everyDocument_aFList)
tfIdfList = tIC_obj.makeTfIdfList()
cP_obj.cPrint(tfIdfList)

# 類似度計算のためのリスト準備
print("●類似度計算のためのリスト準備")
pC_obj = pC.preparationCalc(tfIdfList)
pCList = pC_obj.makeDocumentWordList()
cP_obj.cPrint(pCList)

#クラスタリング分析
print("●クラスタリング")
cA_obj = cA.clusterAnalysis(pCList)
clusteringResult = cA_obj.clustering(int(s4),printBool)
cP_obj.cPrint(clusteringResult)

#結果を出力
print(" \n●結果出力")
oR_obj = oR.outputResult(clusteringResult,tNList)
oTxt = oR_obj.outputTxt()
cP_obj.cPrint(oTxt)


# クラスタリング分析にはtfidf値しか使わなかった
# #類似度を計算
# print(" ●類似度計算")
# sC_obj = sC.similarityCalc(pCList,tNList)
# txtSimilarityList = sC_obj.comparison()
# pprint.pprint(txtSimilarityList)
# print("-----------------------------------------------")

	

#---------------------------------
# グラフにラベル付ける
# 各点がどれだかわかるようにする
# 本当に取れてるか確認する
# 理解する
#--------------------------------