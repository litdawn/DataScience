import pandas as pd
import numpy as np
from scipy import stats
import json

path = "D:\\桌面\\新建文件夹 (2)\\案件文本加标注100份(fin)\\标注100份\\"
#北京上海 0 15w以上
#江苏福建浙江 1 10-15w
#广东、天津、重庆、湖北、山东、内蒙、陕西、四川、辽宁、宁夏、江西、新疆、西藏、云南安徽湖南海南河南 2 5w-10w
#青海、贵州、河北、山西、吉林、广西、黑龙江、甘肃 3
def violate_property():
    province= {'北京市':0,'天津市':2,'上海市':0,'重庆市':2,'河北省':3,'山西省':3,'辽宁省':2,'吉林省':3,'黑龙江省':3,'江苏省':1,'浙江省':1,'安徽省':2,
               '福建省':1,'江西省':2,'山东省':2,'河南省':2,'湖北省':2,'湖南省':2,'广东省':2,'海南省':2,'四川':2,'四川省':2,'贵州省':3,
               '云南省':2,'陕西省':2,'甘肃省':3,'青海省':3,'内蒙古自治区':2,'广西壮族自治区':3,'宁夏回族自治区':2}
    an_you = {'交通肇事':0,'以危险方法危害公共安全':0,'非法吸收公众存款':0,'非法制造枪支':0,'危险驾驶':0,'涉嫌犯危险驾驶':0,'赌博':0,'受贿':0,'贪污':0,
              '非法捕捞水产品':0,'贩卖毒品':0,'运输毒品':0,'诈骗':1,'组织领导传销活动':0,'盗窃':1,'故意杀人':0,'故意伤害':0,'抢劫':1,'妨害公务':0,
              '合同诈骗':0}
    list = [[0,0,0,0,],
            [0,0,0,0,]]
    cnt=0
    for i in range(1,145):
        path_of_each = path+"标注"+str(i)+".json"
        file = open(path_of_each,'rb')
        fileJson = json.load(file)
        first =[]
        second =[]
        for key,value in province.items():
            for j in range(0,len(fileJson['出生地'])):
                if key in fileJson['出生地'][j]:
                    first.append(value)
                    break
        for key,value in an_you.items():
            if key in fileJson['案由']:
                second.append(value)
        if len(first)!=0 and len(second) != 0:
            for an in range(0,len(second)):
                for pro in range(0,len(first)):
                    list[second[an]][first[pro]]=list[second[an]][first[pro]]+1
                    cnt = cnt+1
    print("共"+str(cnt)+"份有效数据")
    index = ["非侵犯财产","侵犯财产"]
    column = ["15w以上","10w-15w","5w-10w","5w以下"]
    d = np.array(list)
    r,s = d.shape
    df = pd.DataFrame(d,columns=column,index=index)
    print(df)
    df1 = df[:]
    df1= pd.DataFrame(df1)
    df1['r_tot']=np.sum(df1,axis=1)
    df1.loc['c_tot']=np.sum(df1, axis=0)
    r_tot = df1['r_tot'][:-1]
    c_tot=df1.loc['c_tot'][:-1]
    print(df1)
    total = np.sum(r_tot)
    data = np.zeros((r,s))
    for i in range(len(r_tot)):
        for j in range(len(c_tot)):
            data[i,j]=r_tot[i]*c_tot[j]/total
    df2=pd.DataFrame(data,columns=column,index=index)
    chi_square=np.sum((df-df2)**2/df2).sum()
    print(stats.chi2.sf(chi_square, df=(r-1)*(s-1)))
def accusation_education():
    province = {'北京市': 0, '天津市': 0, '上海市': 0, '重庆市': 2, '河北省': 2, '山西省': 1, '辽宁省': 1, '吉林省': 1, '黑龙江省': 2, '江苏省': 1,
                '浙江省': 2, '安徽省': 2, '福建省': 2, '江西省': 2, '山东省': 2, '河南省': 2, '湖北省': 1, '湖南省': 2, '广东省': 1, '海南省': 1, '四川': 2,
                '四川省': 2, '贵州省': 3, '云南省': 3, '陕西省': 1, '甘肃省': 2, '青海省': 3, '内蒙古自治区': 1, '广西壮族自治区': 2, '宁夏回族自治区': 2}
    an_you = {'交通肇事': 0, '以危险方法危害公共安全': 0, '非法制造枪支': 0, '危险驾驶': 0, '涉嫌犯危险驾驶': 0, '赌博': 3,
              '非法捕捞水产品': 3, '贩卖毒品': 3, '运输毒品': 3, '诈骗': 2, '盗窃': 2, '故意杀人': 1, '故意伤害': 1, '抢劫': 2, '妨害公务': 3,
              }
    list = [[0, 0, 0, 0, ],
            [0, 0, 0, 0, ],
            [0, 0, 0, 0, ],
            [0, 0, 0, 0, ],
            ]
    cnt = 0
    for i in range(1, 145):
        path_of_each = path + "标注" + str(i) + ".json"
        file = open(path_of_each, 'rb')
        fileJson = json.load(file)
        first = []
        second = []
        for key, value in province.items():
            for j in range(0, len(fileJson['出生地'])):
                if key in fileJson['出生地'][j]:
                    first.append(value)
                    break
        for key, value in an_you.items():
            if key in fileJson['案由']:
                second.append(value)
        if len(first) != 0 and len(second) != 0:
            for an in range(0, len(second)):
                for pro in range(0, len(first)):
                    list[second[an]][first[pro]] = list[second[an]][first[pro]] + 1
                    cnt = cnt + 1
    print("共" + str(cnt) + "份有效数据")
    # 危害国家安全罪:         0
    # 危害公共安全罪:         1-交通肇事、危险驾驶、非法制造枪支、以危险方法危害公共安全 0
    # 破坏社会主义经济秩序罪:  2、合同诈骗、非法吸收存款、传销活动 1
    # 侵犯公民人身权利、民主权利罪:3 故意杀人、故意伤害 2
    # 侵犯财产罪:            4-诈骗、抢劫、盗窃 3
    # 妨害社会管理秩序罪:      5、妨害公务、赌博、非法捕捞水产品、贩卖运输毒品 4
    # 危害国防利益罪:         6
    # 贪污贿赂罪:           7受贿、贪污 5
    index = ["危害 公共 安全 罪","侵犯人身权、民主权","侵  犯 财 产  罪","妨害社会管理秩序罪",]
    column = ["11年以上", "10-11年", "9-10年", "9年以下"]
    d = np.array(list)
    r, s = d.shape
    df = pd.DataFrame(d, columns=column, index=index)
    print(df)
    df1 = df[:]
    df1 = pd.DataFrame(df1)
    df1['r_tot'] = np.sum(df1, axis=1)
    df1.loc['c_tot'] = np.sum(df1, axis=0)
    r_tot = df1['r_tot'][:-1]
    c_tot = df1.loc['c_tot'][:-1]
    print(df1)
    total = np.sum(r_tot)
    data = np.zeros((r, s))
    for i in range(len(r_tot)):
        for j in range(len(c_tot)):
            data[i, j] = r_tot[i] * c_tot[j] / total
    df2 = pd.DataFrame(data, columns=column, index=index)
    chi_square = np.sum((df - df2) ** 2 / df2).sum()
    print(stats.chi2.sf(chi_square, df=(r - 1) * (s - 1)))
if __name__ == '__main__':
    accusation_education()
    violate_property()