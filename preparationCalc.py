# coding=utf-8

import progressBar as pB

#類似度を出す前の準備＿（リスト作成）
class preparationCalc():
    def __init__(self,tIL):
        self.tIL = tIL

    #各文書中で同単語のtf-idf値を取得
    def sameWordGet(self,eachWord):   
        sameList = []

        if len(self.tIL[0][0]) == 2:
            eNum = 1
        elif len(self.tIL[0][0]) == 4:
            eNum = 3

        #sameList.append(eachWord)  #これ入れることによって文書と単語の行列を入れ替えできないから消した
        for i in self.tIL:
            for j in self.tIL[self.tIL.index(i)]:
                if eachWord == j[0]:
                    sameList.append(j[eNum])
                    break
            else:
                sameList.append(0)

        return sameList

    #計算用のリスト作成
    def makeDocumentWordList(self):
        dwList =[]

        pB_obj = pB.progressBar(len(self.tIL)) #プログレスバーの表示[1]

        for i in self.tIL:
            for j in self.tIL[self.tIL.index(i)]:
                if not j[0] in [ i[0] for i in dwList ]:
                    dwList.append(self.sameWordGet(j[0]))
            pB_obj.barCalc(self.tIL.index(i)+1)    #プログレスバーの表示[2]

        return dwList