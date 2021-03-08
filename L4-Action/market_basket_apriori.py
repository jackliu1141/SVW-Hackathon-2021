import pandas as pd

# 设置最大显示列数 pd.options.display.max_columns=None
pd.set_option('max_columns', None)
# 数据加载
dataset=pd.read_csv('./MarketBasket/Market_Basket_Optimisation.csv',header=None)
print(dataset)
print(dataset.shape) # (7501, 20)

# 建立transanctions交易清单
transactions=[]
# 按照行进行遍历
for i in range(0,dataset.shape[0]):
    # 记录一行transaction
    temp=[]
    # 按照列进行遍历
    for j in range(0, dataset.shape[1]):
        if (str(dataset.values[i,j])!='nan'):
            temp.append(dataset.values[i,j])
    transactions.append(temp)
# print(transactions)

# 利用efficient_apriori模块挖掘频繁项集，挖掘关联规则
from efficient_apriori import apriori
itemsets, rules = apriori(transactions, min_support=0.02, min_confidence=0.3)
print('频繁项集：', itemsets)
print('关联规则: ', rules)