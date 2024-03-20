'''
https://dotblogs.com.tw/Ryuichi/2021/09/21/173635
'''
import os
import glob
import pandas as pd
import numpy as np
import datetime

#設定顯示所有欄位
pd.set_option('display.max_columns', None)
np.set_printoptions(precision=6, suppress=True, formatter={'float': '{: 0.4f}'.format})#float限定在小數點4位

#設定優劣等級threshold
high = 80
low = 60

#設定狀態維度(threshold分界數+1)
dim = 3

#設定資料最大天數日期
dateTimeString = '20210430'

#以dateTimeString為基底-(0~times-1)的資料
times = 11

#馬可夫鏈迭代次數
roundNum = 1000

#讀多個csv檔, merge成一個dataframe
def get_merged_csv(flist, **kwargs):
    return pd.concat([pd.read_csv(f, **kwargs) for f in flist], ignore_index=True)

#將所有要input的檔案整到一個資料夾下
path = 'D:/markovechain_pythonfile/inputFile'

#指定檔案的命名規則
fmask = os.path.join(path, 'grade_*.csv')

#讀取
full_data = get_merged_csv(glob.glob(fmask), index_col=None)#, usecols=['col1', 'col3']

#列印
#print(full_data.shape)

#取出要用的欄位
lst = ['DateTime','Student','grade']
full_data = full_data[full_data.columns.intersection(lst)]
full_data.info(verbose=True)#列出所有欄位的型態

print('------------------------------------')
#列印空值狀況
print(full_data.isnull().sum())
#踢掉有空值的資料
full_data.dropna(inplace=True)

#依據優劣等級threshold轉換數值為狀態
full_data['grade'] = np.where(full_data['grade'] > high, 0, np.where(full_data['grade'] >= low, 1 ,2))

#print(full_data.head())
data = {'DateTime':[],'Student':[],'Grade-H':[],'Grade-A':[],'Grade-L':[]}
predictResult = pd.DataFrame(data)
full_data = full_data[full_data['Student'].isin(['Evan'])]#只拿Evan同學作範例
#最大天數往前算前n日的狀況
for index in range(times):
    #進度條使用
    cnt = 1
    #取出指定日期前(含)的資料
    full_data_filter = full_data[full_data['DateTime'] <= int(dateTimeString)]
    #取出學生清單計算
    studentList = full_data_filter['Student'].unique().tolist()
    for student in studentList:
        #顯示進度
        print('*************************************************',dateTimeString+"["+str(cnt)+"/"+str(len(studentList))+"]")
        cnt = cnt +1
        targetData = full_data_filter[full_data_filter['Student'] == student]
        
        #依據日期排序
        targetData.sort_values('DateTime')
        grade = targetData['grade']
        stat = np.zeros((dim, dim), dtype=float)
        #stat = np.ones((dim, dim), dtype=float) -> 若你觀察的分數結果之歸類沒有 0 or 1 or 2 其中一種, 建議先將矩陣初始值設定成1, 避免馬可夫鏈無法計算
        ############################################
        #算出移轉次數矩陣
        for i in range(len(targetData)-1):
            x = grade.values[i]
            y = grade.values[i+1]
            stat[x, y] += 1.0
        
        #計算機率移轉矩陣
        summary = np.zeros(dim, dtype=float)
        percent = np.zeros((dim, dim), dtype=float)
        for i in range(dim):
            summary[i] = np.sum(stat[i])
            for j in range(dim):
                if stat[i, j] != 0:
                    percent[i ,j] = stat[i, j] / summary[i]
        ##########################################
        #矩陣相乘計算穩態
        matrix = percent
        for i in range(3,roundNum):
            matrix_1 = percent.dot(matrix)
            # for j in range(0, len(matrix)):
            #     for k in range(0, len(matrix_1[j])):
            #         matrix_1[j][k] = '{0:.4f}'.format(matrix_1[j][k])
                    
            if((matrix_1==matrix).all()):     #檢查是否穩態
                break
            matrix = matrix_1
        Grade_H = [row[0] for row in matrix_1]
        Grade_H = np.max(Grade_H)
        Grade_A = [row[1] for row in matrix_1]
        Grade_A = np.max(Grade_A)
        Grade_L = [row[2] for row in matrix_1]
        Grade_L = np.max(Grade_L)
        
        new_row = {'DateTime':str(dateTimeString),'Student':str(student),'Grade-H':str(Grade_H),'Grade-A':str(Grade_A),'Grade-L':str(Grade_L)}
        predictResult = predictResult.append(new_row, ignore_index=True)
        
    dateTimeObject = datetime.datetime.strptime(dateTimeString, '%Y%m%d')
    dateTimeObject = dateTimeObject - datetime.timedelta(days=1)
    dateTimeString = dateTimeObject.strftime("%Y%m%d")
predictResult.to_csv('./markovePredictResult_status.csv', index=False)#將預測結果儲存到檔案