'''
Action3: 对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem类型 => 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数
哪个品牌的平均车型投诉最多
'''
import pandas as pd
import numpy as np

# 数据加载
df=pd.read_csv('E:/LY/2021数据黑马训练营/L1/car_data_analyze/car_complain.csv')
print('\n汽车质量投诉原始数据如下：\n',df)

'''
数据统计
对数据进行探索：品牌投诉总数，车型投诉总数
哪个品牌的平均车型投诉最多
'''
# 数据清洗，将别名合并
def f(x):
    x=x.replace('一汽-大众','一汽大众')
    return x
df['brand']=df['brand'].apply(f)

# 品牌投诉总数
result=df.groupby(['brand'])['id'].agg(['count'])
result=result.sort_values('count',ascending=False)
print('\n品牌投诉总数如下：\n',result)

# 车型投诉总数
result1=df.groupby(['car_model'])['id'].agg(['count'])
result1=result1.sort_values('count',ascending=False)
print('\n车型投诉总数如下：\n',result1)

#求品牌的平均车型投诉
result2=df.groupby(['brand','car_model'])['id'].agg(['count'])
result3=result2.groupby(['brand']).mean()
result3=result3.sort_values('count',ascending=False)

# 用reset_index还原索引，重新变为默认的整型索引
result3.reset_index(inplace=True)

# 将index从Series转化为DataFrame
result4=result3.index.to_frame(name='名次')

# 将两个dataframe数据按列方向合并
result5=pd.concat([result3,result4],axis=1)

# 保留两位小数
pd.options.display.precision=2

# 利用index，显示排名
for i in range(len(result5['名次'])):
    result5.loc[i,['名次']]=result5.loc[i,['名次']]+1
print('\n品牌的平均车型投诉排名如下：\n', result5)
