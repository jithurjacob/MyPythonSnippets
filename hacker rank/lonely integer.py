if __name__ == '__main__':
    a = input()
    while(a >= 1):
        b = map(int, raw_input().strip().split(" "))
        for x in b:
            if b.count(x) ==1:
                print(x)
                break

        a-=1
