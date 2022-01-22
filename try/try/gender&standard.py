import pandas as pd
from scipy import stats

# 列表（期望数据来自中国裁判文书网，截止2022-01-20-12：27）
observed_pd = pd.DataFrame(['女'] * int(5 * 100 / 93) + ['男'] * int(88 * 100 / 93))
expected_pd = pd.DataFrame(['女'] * int(929613 * 100 / 8185564) + ['男'] * int(7255951 * 100 / 8185564))
observed_table = pd.crosstab(index=observed_pd[0], columns='count')
expected_table = pd.crosstab(index=expected_pd[0], columns='count')
print(observed_table)
print('——————')
print(expected_table)
# 通过公式算出卡方值
observed = observed_table
expected = expected_table
chi_squared_stat = ((observed - expected) ** 2 / expected).sum()
print('chi_squared_stat')
print(chi_squared_stat)
crit = stats.chi2.ppf(q=0.95, df=2)  # 95置信水平 df = 自由度
print(crit)  # 临界值，拒绝域的边界 当卡方值大于临界值，则原假设不成立，备择假设成立
P_value = 1 - stats.chi2.cdf(x=chi_squared_stat, df=2)
print('P_value')
print(P_value)
