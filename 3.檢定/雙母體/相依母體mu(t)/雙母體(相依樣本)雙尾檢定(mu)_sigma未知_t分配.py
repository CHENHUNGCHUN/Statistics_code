from scipy import stats
'''
主管 事前 事後 成果
1	32	34	2
2	31	31	0
3	29	35	6
4	10	16	6
5	30	33	3
6	33	36	3
7	22	24	2
8	25	28	3
9	32	26	-6
10	20	26	6
11	30	36	6
12	20	26	6
13	24	27	3
14	24	24	0
15	31	32	1
16	30	31	1
17	15	15	0
18	32	34	2
19	23	26	3
20	23	26	3
'''

# H0: mu_d <=0 Ha:mu_d > 0
#####################################################臨界值檢定#####################################################
#轉成t統計量 
mu_d=0
d_bar = 2.5
s_d = 2.893
s_d_sq = s_d**2
alpha= 0.05 
n=20
v=n-1
t_test_statics=(d_bar-mu_d)/(s_d_sq/n)**(1/2)
right_limit = stats.t.ppf(1-alpha,v)
print(f'因為t統計量 {t_test_statics} 大於臨界值 {right_limit},所以拒絕H0')

#####################################################p-value檢定#####################################################
#轉成t統計量 
mu_d=0
d_bar = 2.5
s_d = 2.893
s_d_sq = s_d**2
alpha= 0.05 
n=20
v=n-1
t_test_statics=(d_bar-mu_d)/(s_d_sq/n)**(1/2)
p_value = 1-stats.t.cdf(t_test_statics,v) #因為是右尾檢定 所以要1-p_value
print(f'因為p-value {p_value} 小於alpha {alpha},所以拒絕H0')