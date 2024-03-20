import pandas as pd
import matplotlib.pyplot as plt

first_win = 8
win_pro = 0.5
profit = 0

toss_list = []
bet_list = []
profit_list = []
winlose_list = []

#toss=1
bet = 1  #下注籌碼
bet_list.append(bet)
for toss in range(1,first_win):
    toss_list.append(toss)
    winlose_list.append('Lose')
    
    profit -= bet
    bet *= 2 
    
    bet_list.append(bet)
    profit_list.append(profit)
    
    toss +=1
    
if toss == first_win:
    toss_list.append(toss)   
    winlose_list.append('Win')
    profit += bet 
    profit_list.append(profit)

results = pd.DataFrame(
    {
     'Toss': toss_list,
     'Bet': bet_list,
     'Win/Lose': winlose_list,
     'Profit': profit_list
     }                    
    )

print(results)

results.plot.bar(x='Toss')
plt.xlabel('Toss')
plt.ylabel('Bet/Profit')
plt.title('Bet and profit')
plt.show()
