#给定一个任务的开始和结束时间，返回需要执行的时间，以秒数计算
import time
import datetime 

def data():

    start = input("Please input the start time:")
    # print(start)
    end = input('Please input the end time:')
    #将输入时间按照特定的模式记录
    data1 = datetime.datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
    data2 = datetime.datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
    dis = (data2-data1).total_seconds()
    print('相差时间为：%d'%dis )
if __name__ == '__main__':
    data()
