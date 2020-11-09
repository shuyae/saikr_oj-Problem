def main():
    N = int(input("Please input N preasenting the number of str:"))
    ans = 0
   
    while N >0:
        length = int(input("Please input n preasenting the length of str:"))
        psw = "Jyouhou"
        info = input()
        index = 0
        for i in info:
            if i == psw[index]:
                index += 1
            if index == 6:
                index = 0
                ans += 1
        N -= 1
    print(ans)
if __name__ == '__main__':
    main()
