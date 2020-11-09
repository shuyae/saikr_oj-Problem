#第3题，银行bank，亿万光年外的艾泽拉斯大陆战事不断，被战火划分为了100000100000个领地，每个领地都有一个编号，分别为11到100000。在每个领地都有一个银行。商人工会在这100000个领地的银行开户时都存了33块大洋，为了保证工会资产的安全，工会将不时地派人手去清点存款或者改变存款。而艾泽拉斯大陆的求和运算相当于地球的乘法运算。即开户时存款总额其实为3^{100000}3100000。
# 在艾泽拉斯大陆，货币面额有6060种，恰为最小的前6060个素数。所有人的存款都可以由这6060个面额表示。（所有的资产面额都只能由这60个基本面额表示，即设当前的资产为正整数M，则。M=p_1^{k_1}p_2 ^ {k_2}……p_{60}^{K_{60}}M=p1k1 p2k2……p60K60
# 工会有时会派人手对第aa个领地的银行到第bb个领地的银行，即编号在[a,b][a,b]内的领地银行进行资产清点：先对这些资产做乘法运算，然后求解此结果的欧拉函数值。有时，工会也会拍人手到某个银行改变存款。现在请你对工会的每个清点操作求出区间内资产求积之后的欧拉函数值。
#
def bank():
    N = int(input("Please input the count of operations: "))
    bank = [3]* 10**5
    for i in range(N):
        a,b,c = input().split(' ')
        a = int(a)
        b = int(b)
        c = int(c)
        if a == 1:
            bank[b] = c
        else:
            ans = 1
            for j in range(b,c+1):
                ans *= bank[j]
            print(Ola(ans))

#构建计算欧拉函数值的函数（ N的 小于N的与之互质的元素的个数）
def Ola(num):
    if (0).__class__ is num.__class__:
        if num>0:
            F = 0
            for i in range(num):
                x,y = num,i
                while y>0:
                    x,y = y,x%y
                if x == 1:
                    F += 1
                    
            return F 
        # while num >0:
        #     res = num
        #     n = num
        #     for i in range(2,n//2):
        #         if n % i == 0:
        #             n //= i 
        #             res = (res//n)*(n-1)
        #     return res 

if __name__ == '__main__':
    bank()
