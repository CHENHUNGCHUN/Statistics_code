'''
某研究調查發現每個月發生的車禍平均次數2.24次 
某月實際檢視n=50
實際發生 0、1、2、3以及4次以上 分別為7次、8次、13次、10次、12次
檢定車禍發生次數是否符合普瓦松分配
'''
from scipy import stats


#H0 : 車禍發生"次數"符合普瓦松分配  Ha:車禍發生"次數"不符合普瓦松分配

lambda_x = 2.24
n=50
x = [0,1,2,3,4]  #車禍次數分類
o=[7,8,13,10,12] #實際觀察到的車禍次數
e=[]  #算出來的理論車禍"次數"    理論次數
for i in x:
    if i !=4:
        e.append(stats.poisson.pmf(i,lambda_x)*50)
    elif i ==4:
        e.append((1-stats.poisson.cdf(3,lambda_x))*50)  #1檢調3次(包含)以下的機率 (就是大於等於4次以上的機率)
        

chi_2 = [] 
for i,j in zip(o,e):
    chi=((i-j)**2)/j
    chi_2.append(chi)
    
chi_test_stastic = sum(chi_2)

#檢定
alpha = 0.05
k=len(x)  #車禍次數分類數
p= 1 #分配的參數個數
v=k-p-1
right_limit = stats.chi2.ppf(1-alpha,df=v)
print(right_limit,chi_test_stastic)
print(f'卡方檢定一律為右尾檢定。 因為卡方統計量{chi_test_stastic} 小於臨界值 {right_limit} ,故不拒絕H0,車禍發生"次數"符合普瓦松分配')





