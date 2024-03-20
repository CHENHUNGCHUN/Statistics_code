import numpy as np
from scipy import stats

#卡方只有右尾檢定

#單樣本f_test
def f_test_1smp(data,sigma_sq):
    n=np.array(data).size
    chi_squre = (n-1)*np.var(data,ddof=1)/sigma_sq
    p_value =1-stats.chi2.cdf(chi_squre,n-1)
    return chi_squre,p_value


#雙樣本f_test
def f_test(group1,group2):
    f = np.var(group1,ddof=1)/np.var(group2,ddof=1)
    x=np.array(group1)
    y=np.array(group2)
    nun = x.size-1
    dun = y.size-1
    p_value = 1-stats.f.cdf(f,nun,dun)  
    return f,p_value
##########################################################





