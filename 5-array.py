#数组操作 array ,有一个长度为 n的数组,你需要对它进行 q 次操作，每次操作可能为：修改ai的值为 x；修改数组中所有小于x 的值为 x
# 请求出进行完所有操作后的数组。
#第一行包含两个正整数 n 和q,表示数组长度和进行的操作数
#第二行给定n 个数值，即数组
#接下来q来表示进行的操作
# 1 i x 表示ai改为x
# 2 x 表示数组中所有小于x的值改为x
def array():
    n,q = input('Please input the length of arr and the count of operations:').split(' ')
    n = int(n)
    q = int(q)

    input_arr = list()
    input_arr += (input().split(' '))
    for i in range(q):
        op = input().split(' ')
        if len(op) == 2:
            for i in range(n):
                if int(input_arr[i]) < int(op[1]):
                    input_arr[i] = op[1]
        else:
            input_arr[int(op[1])] = op[2]
    print(' '.join(input_arr))
if __name__ == '__main__':
    array()
