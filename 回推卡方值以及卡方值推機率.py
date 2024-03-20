from  scipy import stats

#計算p-value
print(stats.chi2.sf(32.85,19) )
print(1-stats.chi2.cdf(32.85,19))


#計算卡方值
print(stats.chi2.ppf(0.025, 19))
print(stats.chi2.ppf(0.975, 19))
#現在問題是怎麼求左邊的卡方值