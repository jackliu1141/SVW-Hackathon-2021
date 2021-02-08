# Action1：求2+4+6+8+...+100的求和，用Python该如何写
#导入numpy
import numpy as np  
'''
使用 arange 函数从数值范围创建数组，并返回 ndarray 对象，函数格式如下：
numpy.arange(start, stop, step, dtype)
根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray。
'''
x= np.arange(2,102,2)
print(x)
# 利用for循环遍历数组x，累加。
sum = 0
for number in x:
    sum = sum + number
print('2+4+6+8+...+100 =',sum)
