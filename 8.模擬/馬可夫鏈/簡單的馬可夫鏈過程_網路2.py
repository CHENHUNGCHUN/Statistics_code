import numpy as np
import random as rm

# 狀態
states = ["Black_tea","Bubble_tea","Coffee"]

# 可能的路徑
transitionName = [["BB","BT","BC"],["TB","TT","TC"],["CB","CT","CC"]]

# 轉換矩陣
transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[1]) != 3:
    print("是不是機率計算錯了呢?")
else: print("沒問題，繼續下一步吧！")


def activity_forecast(days):
    # 這邊可以更改起始的 state
    activityToday = "Black_tea"
    print("Start state: " + activityToday)
    
    activityList = [activityToday]
    i = 0
    # To calculate the probability of the activityList
    prob = 1
    while i != days:
        if activityToday == "Black_tea":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "BB":
                prob = prob * 0.2
                activityList.append("Black_tea")
                pass
            elif change == "BT":
                prob = prob * 0.6
                activityToday = "Bubble_tea"
                activityList.append("Bubble_tea")
            else:
                prob = prob * 0.2
                activityToday = "Coffee"
                activityList.append("Coffee")
        elif activityToday == "Bubble_tea":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "TT":
                prob = prob * 0.6
                activityList.append("Bubble_tea")
                pass
            elif change == "TB":
                prob = prob * 0.1
                activityToday = "Black_tea"
                activityList.append("Black_tea")
            else:
                prob = prob * 0.3
                activityToday = "Coffee"
                activityList.append("Coffee")
        elif activityToday == "Coffee":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "CC":
                prob = prob * 0.1
                activityList.append("Coffee")
                pass
            elif change == "CB":
                prob = prob * 0.2
                activityToday = "Black_tea"
                activityList.append("Black_tea")
            else:
                prob = prob * 0.7
                activityToday = "Bubble_tea"
                activityList.append("Bubble_tea")
        i += 1  
    print("Possible states: " + str(activityList))
    print("End state after "+ str(days) + " days: " + activityToday)
    print("Probability of the possible sequence of states: " + str(prob))

# 預測 5 天後的 state
activity_forecast(5)




####################################################################################################################################################################################################################################




def activity_forecast(days):
    # 這邊可以更改起始狀態
    activityToday = "Black_tea"
    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "Black_tea":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "BB":
                prob = prob * 0.2
                activityList.append("Black_tea")
                pass
            elif change == "BT":
                prob = prob * 0.6
                activityToday = "Bubble_tea"
                activityList.append("Bubble_tea")
            else:
                prob = prob * 0.2
                activityToday = "Coffee"
                activityList.append("Coffee")
        elif activityToday == "Bubble_tea":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "TT":
                prob = prob * 0.6
                activityList.append("Bubble_tea")
                pass
            elif change == "TB":
                prob = prob * 0.1
                activityToday = "Black_tea"
                activityList.append("Black_tea")
            else:
                prob = prob * 0.3
                activityToday = "Coffee"
                activityList.append("Coffee")
        elif activityToday == "Coffee":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "CC":
                prob = prob * 0.1
                activityList.append("Coffee")
                pass
            elif change == "CB":
                prob = prob * 0.2
                activityToday = "Black_tea"
                activityList.append("Black_tea")
            else:
                prob = prob * 0.7
                activityToday = "Bubble_tea"
                activityList.append("Bubble_tea")
        i += 1    
    return activityList

# 儲存每個 activityList
list_activity = []
count = 0


for iterations in range(1,10000):
        list_activity.append(activity_forecast(5)) # 5 天後

# Check out all the `activityList` we collected    
#print(list_activity)

# 獲取以 state:'Bubble_tea' 結尾的所有活動的計數
for smaller_list in list_activity:
    if(smaller_list[2] == "Bubble_tea"):
        count += 1

# 計算從 state:'Black_tea' 開始到 state:'Bubble_tea' 結束的機率

percentage = (count/10000) * 100
print("The probability of starting at state:'Black_tea' and ending at state:'Bubble_tea'= " + str(percentage) + "%")