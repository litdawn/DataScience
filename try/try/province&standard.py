import pandas as pd
from scipy import stats

# 列表（期望数据来自中国裁判文书网，截止2022-01-21-21：05）
observed_pd = pd.DataFrame(['新疆'] * int(1 * 100 / 101) + ['重庆'] * int(1 * 100 / 101)+ ['辽宁'] * int(10 * 100 / 101)+ ['江苏'] * int(5 * 100 / 101)+ ['吉林'] * int(4 * 100 / 101)+ ['内蒙'] * int(2 * 100 / 101)+ ['广西'] * int(10 * 100 / 101)+ ['福建'] * int(3 * 100 / 101)+ ['山西'] * int(2 * 100 / 101)+ ['四川'] * int(6 * 100 / 101)+ ['北京'] * int(2 * 100 / 101)+ ['河南'] * int(7 * 100 / 101)+ ['云南'] * int(6 * 100 / 101)+ ['湖北'] * int(3 * 100 / 101)+ ['湖南'] * int(9 * 100 / 101)+ ['甘肃'] * int(2 * 100 / 101)+ ['陕西'] * int(8 * 100 / 101)+ ['青海'] * int(3 * 100 / 101)+ ['贵州'] * int(4 * 100 / 101)+ ['海南'] * int(1 * 100 / 101)+ ['河北'] * int(3 * 100 / 101)+ ['江西'] * int(2 * 100 / 101)+ ['广东'] * int(7 * 100 / 101))
expected_pd = pd.DataFrame(['新疆'] * int(93485 * 100 / 8361427) + ['重庆'] * int(305240 * 100 / 8361427)+ ['辽宁'] * int(275540 * 100 / 8361427)+ ['江苏'] * int(545547 * 100 / 8361427)+ ['吉林'] * int(278594 * 100 / 8361427)+ ['内蒙'] * int(176045 * 100 / 8361427)+ ['广西'] * int(432612 * 100 / 8361427)+ ['福建'] * int(385070 * 100 / 8361427)+ ['山西'] * int(250016 * 100 / 8361427)+ ['四川'] * int(593351 * 100 / 8361427)+ ['北京'] * int(242997 * 100 / 8361427)+ ['河南'] * int(667583 * 100 / 8361427)+ ['云南'] * int(525423 * 100 / 8361427)+ ['湖北'] * int(383643 * 100 / 8361427) + ['湖南'] * int(534285 * 100 / 8361427)+ ['甘肃'] * int(147802 * 100 / 8361427)+ ['陕西'] * int(210754 * 100 / 8361427)+ ['青海'] * int(48797 * 100 / 8361427)+ ['贵州'] * int(381997 * 100 / 8361427)+ ['海南'] * int(58167 * 100 / 8361427)+ ['河北'] * int(417579 * 100 / 8361427)+ ['江西'] * int(322014 * 100 / 8361427)+ ['广东'] * int(651914 * 100 / 8361427))
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
crit = stats.chi2.ppf(q=0.95, df=24)  # 95置信水平 df = 自由度
print(crit)  # 临界值，拒绝域的边界 当卡方值大于临界值，则原假设不成立，备择假设成立
P_value = 1 - stats.chi2.cdf(x=chi_squared_stat, df=24)
print('P_value')
print(P_value)
