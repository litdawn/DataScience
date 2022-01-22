import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import json
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
path = "D:\\桌面\\新建文件夹 (2)\\标注100份\\"
province = {'北京市': 0,  '辽宁省': 1,  '江苏省': 2, '河南省': 3,  '湖南省': 4, '广东省': 5,  '四川': 6,
            '四川省': 6, '云南省': 7, '陕西省': 8,  '青海省': 9, '内蒙古自治区': 10, '广西壮族自治区': 11}
provinces = {'北京市': 0,  '辽宁省': 4, '吉林省':5,  '江苏省': 6,'河南省': 9, '湖南省': 11, '广东省': 12,
            '四川省': 14, '贵州省': 15, '云南省': 16, '陕西省': 17, '青海省': 19, '内蒙古自治区': 20, '广西壮族自治区': 21}
list_crime = [0,0,0,0,0,0,0,0,0,0,0,0]
list_educationyear =[12.64,10.34,10.21,9.79,9.88,10.38,9.24,8.75,10.26,8.85,10.08,9.54]
list_gdp = [164929,58969,121202,55346,62885,87899,58084,51942,66233,50777,72183,44199]
list_population=[1198,301,779,568,309,589,166,120,181,8,22,194]
list_city = [86.8,68.11,70.61,53.21,57.22,71.4,53.79,48.91,59.43,55.52,63.4,51.09]


cnt = 0
for i in range(1, 145):
    path_of_each = path + "标注" + str(i) + ".json"
    file = open(path_of_each, 'rb')
    fileJson = json.load(file)
    for key, value in province.items():
        for j in range(0, len(fileJson['出生地'])):
            if key in fileJson['出生地'][j]:
                list_crime[value]=list_crime[value]+1
                cnt = cnt +1
list = [list_crime,list_gdp,list_educationyear,list_population,list_city]
real_list=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],]
for i in range(0,len(list_crime)):
    real_list[i][0] = list_crime[i]
    real_list[i][1] = list_gdp[i]
    real_list[i][2] = list_educationyear[i]
    real_list[i][3] = list_population[i]
    real_list[i][4] = list_city[i]
print("共" + str(cnt) + "份有效数据")
df = pd.DataFrame(np.array(real_list),columns=["crime","gdp","education","population","city"],index=provinces.keys())
df.info()
df.head()
lm = ols('crime ~ gdp + education + population + city',data=df).fit()#多元线性
print(lm.summary())
Xi = np.array(list_gdp).reshape(-11, 1)
Xj = np.array(list_educationyear).reshape(-11,1)
Xm = np.array(list_city).reshape(-11,1)
Xn = np.array(list_population).reshape(-1,1)
Yi = np.array(list_crime).reshape(-100, 1)
#散点图
plt.scatter(Xm,Yi, s=10)
plt.show()
#一元多项式回归
minX = min(Xn)
maxX = max(Xn)
X = np.arange(minX, maxX).reshape([-1, 1])
poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(Xn)
lin_reg_2 = linear_model.LinearRegression()
lin_reg_2.fit(X_poly, Yi)
print(lin_reg_2.coef_)
plt.scatter(Xn, Yi, color='red',s = 50)
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.show()