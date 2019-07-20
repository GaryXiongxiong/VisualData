'''
@Author: Gary J
@Date: 2019-07-20 19:26:49
@LastEditors: Gary J
@LastEditTime: 2019-07-20 20:58:12
@Description: Print visual table for given data.
'''

# 获取数据行数
n = input();
# 转化为整型
n = int(n);
# 获取排序方式
sortPattern=input().split(" ")
# 创建数据二维数组
data = []
# 记录最长名称
max_size = 0;
# 记录最大值
max_value = 0;
for i in range(n):
    data.append(input().split(" "))
    data[i][1] = int(data[i][1])
    curr_size = len(data[i][0])
    curr_value= data[i][1]
    if curr_size > max_size:
        max_size = curr_size
    if curr_value > max_value:
        max_value = curr_value
# 如果按姓名排序，则直接排序
if sortPattern[0] == "Name":
    data.sort()
# 如需按值排序，先反转二维数组的第二维后进行排序，排序完成后再反转回来即完成了按第二列-值进行排序
elif sortPattern[0] == "Value":
    dataReverse = [[d[1],d[0]] for d in data]
    dataReverse.sort()
    data = [[d[1],d[0]] for d in dataReverse]
# 非法值报错
else:
    raise ValueError('Invalid value:'+sortPattern[0])
# 数组排序完成，检测如果要求倒叙则反转数组
if sortPattern[1] == "DESC":
    data.reverse()
# 非法值报错
elif sortPattern[1] != "ASC":
    raise ValueError('Invalid value:'+sortPattern[1])

# 开始打印
print("┌"+"─"*max_size+"┬"+"─"*20+"┐")
# 计算每块色块对应的值
perblock = max_value/20
for i in range(n):
    # 计算需要的色块数
    blocks = int(data[i][1]/perblock)
    # 按照要求格式化输出行
    print("│%*s│" %(max_size,data[i][0])+"█"*blocks+" "*(20-blocks)+"│")
    if i != n-1:
        # 如果是最后一行则不输出中间分割线
        print("├"+"─"*max_size+"┼"+"─"*20+"┤")
# 打印底栏
print("└"+"─"*max_size+"┴"+"─"*20+"┘")


   