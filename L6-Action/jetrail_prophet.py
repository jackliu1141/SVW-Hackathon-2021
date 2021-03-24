import pandas as pd

# 数据加载
data_train=pd.read_csv('E:/LY/2021数据黑马训练营/L6/jetrail/train.csv')
data_train
# 需要将Datetime字段转化为pandas中的日期格式
data_train['Datetime']=pd.to_datetime(data_train['Datetime'])
data_train
# 将Datetime字段作为index
data_train.index=data_train['Datetime']
data_train
# 将数据中的ID和Datetime字段drop掉
data_train.drop(['ID','Datetime'], axis=1, inplace=True)
data_train
# 按照天进行采样
daily_data_train=data_train.resample('D').sum()
daily_data_train
# 添加ds和y保留字段
daily_data_train['ds']=daily_data_train.index
daily_data_train['y']=daily_data_train['Count']
daily_data_train
# drop掉Count字段
daily_data_train.drop(['Count'], axis=1, inplace=True)
daily_data_train

from fbprophet import Prophet
import numexpr as ne
# 创建模型
m = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
# 模型训练
m.fit(daily_data_train)
# 预测未来7个月，213天
future = m.make_future_dataframe(periods=213)
future
forecast=m.predict(future)
forecast
m.plot(forecast)