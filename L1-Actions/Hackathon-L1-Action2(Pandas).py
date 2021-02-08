'''
Action2: 统计全班的成绩
班里有5名同学，现在需要你用Python来统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
'''
#导入相关模块
from pandas import DataFrame
import pandas as pd

# 将数据构建为DataFrame类型
data={'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df=DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'],columns=['语文','数学','英语'])
print(df,'\n')

# 利用describe函数统计平均成绩、最小成绩、最大成绩、标准差
# print(df.describe())
# print(df.describe().loc[['mean','min','max','std']])
df1=df.describe().loc[['mean','min','max','std']]

# 利用var函数统计方差、
# print(df.var())
df11=df.var().to_frame(name='var')
# print(df11)

# DataFrame 行列转置
df12=df11.stack().unstack(0)
# print(df12)

# 将两个dataframe数据按行方向合并
df13=pd.concat([df1,df12],axis=0)
# 保留两位小数
pd.options.display.precision=2
# 打印平均成绩、最小成绩、最大成绩、标准差、方差
print('平均成绩、最小成绩、最大成绩、标准差、方差如下：\n',df13,'\n')

# 求每个人的总分成绩
df2=df.sum(axis=1)
# print(df2)

# 将Series转化为DataFrame
df2=df2.to_frame(name='总分')
# print(df2)

# 将两个dataframe数据按列方向合并
df3=pd.concat([df,df2],axis=1)
# print(df3)

# 对df3的'sum'列从大到小进行排序
df4=df3.sort_values('总分', ascending=False)
# print(df4)

# 用reset_index还原索引，重新变为默认的整型索引
df4.reset_index(inplace=True)

# 将index从Series转化为DataFrame
df5=df4.index.to_frame(name='名次')
# print(df5)

# 将两个dataframe数据按列方向合并
df6=pd.concat([df4,df5],axis=1)
# print(df6)

# 利用index，显示每个人的名次
for i in range(len(df6['名次'])):
    df6.loc[i,['名次']]=df6.loc[i,['名次']]+1
print('总成绩排名如下：\n',df6)