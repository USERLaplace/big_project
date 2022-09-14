import pandas as pd
import matplotlib.pyplot as plt

def search(data):
    # 时间输入
    print('请分别输入时间')
    print('请输入日：')
    day = input()
    day = int(day)
    print('请输入时：')
    hour = input()
    hour = int(hour)
    print('请输入分：')
    minute = input()
    minute = int(minute)
    # 将时间转换为时间戳类型
    time = day * 60 * 24 + hour * 60 + minute
    Time = pd.to_datetime([time], unit='m', origin=pd.Timestamp('2022-06-30'))
    # 记录索引
    index = 0
    for x in data['Datetime']:
        if x == Time:
            print('成功')
            break
        index += 1
    # 打印日期查询得到的power值
    print('Datetime:', data['Datetime'][index])
    print('Power(MW):', data['Power(MW)'][index])

    return

def visualize(data):
    print("请输入所要查看数据的日期")
    print("请输入日:")
    day = input()

    pre='2022-7-'
    day1= pre+day

    day= str(int (day)+1)
    day2=pre+day
    #筛选日期
    data = data[(data['Datetime'] >= day1) & (data['Datetime'] < day2)]

    #横坐标数据
    xtime = data['Datetime']
    #纵坐标数据
    ypower = data['Power(MW)']

    #横纵坐标数据导入图表
    plt.plot(xtime, ypower)
    #横坐标
    plt.xlabel('Datetime', fontsize=16)
    #纵坐标
    plt.ylabel('Power(MW)', fontsize=16)
    plt.show()

    return


def test(data):
    data = data[(data['Datetime'] >= '2022-7-22') & (data['Datetime'] < '2022-7-23')]
    print(type('2022-7-22'))
    return
i=1
while i==1:
    if __name__ == '__main__':
        print("1.光伏发电")
        print("2.风伏发电")
        print("请选择想要展示的数据")
        num_1=int(input())
        # execl文件路径
        if num_1==1:
            fpath = './feature_gf_power.xlsx'
        else:
            fpath = './feature_fd_power.xlsx'
        # 获取execl文件数据
        data = pd.read_excel(fpath)
        # 将数据中的时间对象转换为时间戳
        data['Datetime'] = pd.to_datetime(data['Datetime'])

        print('1.查询')
        print('2.可视化')
        print('请选择要进行的操作：')
        num=input()
        if num=='1':
            # 日期查询
            search(data)
        elif num=='2':
            # 可视化
            visualize(data)
    i=int(input("Restart? 0 or 1  "))
import pandas as pd
import matplotlib.pyplot as plt

def search(data):
    # 时间输入
    print('请分别输入时间')
    print('请输入日：')
    day = input()
    day = int(day)
    print('请输入时：')
    hour = input()
    hour = int(hour)
    print('请输入分：')
    minute = input()
    minute = int(minute)
    # 将时间转换为时间戳类型
    time = day * 60 * 24 + hour * 60 + minute
    Time = pd.to_datetime([time], unit='m', origin=pd.Timestamp('2022-06-30'))
    # 记录索引
    index = 0
    for x in data['Datetime']:
        if x == Time:
            print('成功')
            break
        index += 1
    # 打印日期查询得到的power值
    print('Datetime:', data['Datetime'][index])
    print('Power(MW):', data['Power(MW)'][index])

    return

def visualize(data):
    print("请输入所要查看数据的日期")
    print("请输入日:")
    day = input()

    pre='2022-7-'
    day1= pre+day

    day= str(int (day)+1)
    day2=pre+day
    #筛选日期
    data = data[(data['Datetime'] >= day1) & (data['Datetime'] < day2)]

    #横坐标数据
    xtime = data['Datetime']
    #纵坐标数据
    ypower = data['Power(MW)']

    #横纵坐标数据导入图表
    plt.plot(xtime, ypower)
    #横坐标
    plt.xlabel('Datetime', fontsize=16)
    #纵坐标
    plt.ylabel('Power(MW)', fontsize=16)
    plt.show()

    return


def test(data):
    data = data[(data['Datetime'] >= '2022-7-22') & (data['Datetime'] < '2022-7-23')]
    print(type('2022-7-22'))
    return
i=1
while i==1:
    if __name__ == '__main__':
        print("1.光伏发电")
        print("2.风伏发电")
        print("请选择想要展示的数据")
        num_1=input()
        # execl文件路径
        if num_1==1:
            fpath = './02 His_Power_GF.xlsx'
        else:
            fpath = './02 His_Power_GF.xlsx'
        # 获取execl文件数据
        data = pd.read_excel(fpath)
        # 将数据中的时间对象转换为时间戳
        data['Datetime'] = pd.to_datetime(data['Datetime'])

        print('1.查询')
        print('2.可视化')
        print('请选择要进行的操作：')
        num=input()
        if num=='1':
            # 日期查询
            search(data)
        elif num=='2':
            # 可视化
            visualize(data)
    i=int(input("Restart? 0 or 1  "))
