#最近某视频网站将使用已久的 av 视频编号升级成了新的 bv 号，新的编号扩充了编号的字符集，增加了编号的数量。首先，需要将 av 号中的正整数n异或上一个较大的正整数X再对其进行编码，得到编码后的串S，最后在S开头添加BV前缀即可。
#这里所使用的编码是指把一个整数转换成一个 62 进制数，并用编码表中指定的每一位代表的符号作为该位的字符，构成编码后的串。
#你的收藏中有n个 av 号，每个 av 号都符合上面的格式。
#第一行包含两个正整数n和X，代表 av 号的数量和异或的值。
#第二行包含一个长为 62 的字符串 T，Ti 表示编码时某一位的十进制数值为 i 时对应的编码字符。
#接下来，n行每行包含一个字符串，分别为要转换的 av 号串，长度不超过 11。
def av2bv():
    n,X = input("Plese input the count of av and X:").split(' ')
    n = int(n)
    X = int(X)
    T = input("Please input the T with the length of 62:")
    ans = []
    for i in range(n):
        av = input('Please input ith av:' )
        outout = 'BV'
        n = int(av[2:])
        n = n^X
        n_62 = []
        while n > 0:
            n_62.append(n%62) 
            n //= 62
        for i in range(len(n_62)-1,-1,-1):
            outout += T[n_62[i]]
        ans.append(outout)
    for i in range(len(ans)):
        print(ans[i])
             
if __name__ == '__main__':
    av2bv()
