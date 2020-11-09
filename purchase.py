def purchase():
    #动态比较每天的价格与前M天内的价格
    n,m = input("Please input the total days and the limited days:").split(' ')
    n = int(n)
    m = int(m)
    #开创n长的数组记录每天喝的可乐的 最低价格
    ans = [10**4]*n
    output = 0
    price = input("Please input the prices by days:").split(' ')
    for i in range(len(price)):
        if ans[i] > int(price[i]):
            days = min(m,n-i)
            ans[i:i+days] = [int(price[i])]*days
        output += int(ans[i])
    print("The minist cost is :%d " %output)
if __name__ == '__main__':
    purchase()
