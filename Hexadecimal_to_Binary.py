for _ in range(int(input())):
    s=input()
    for i in s:
        if i=='0':
            print("0000",end='')
        if i=='1':
            print("0001",end='')
        if i=='2':
            print("0010",end='')
        if i=='3':
            print("0011",end='')
        if i=='4':
            print("0100",end="")
        if i=='5':
            print("0101",end="")
        if i=='6':
            print("0110",end="")
        if i=='7':
            print("0111",end="")
        if i=='8':
            print("1000",end="")
        if i=='9':
            print("1001",end="")
        if i=='A' or i=='a':
            print("1010",end="")
        if i=='b' or i=='B':
            print("1011",end="")
        if i=='C' or i=='c':
            print("1100",end="")
        if i=='D' or i=='d':
            print("1101",end="")
        if i=='E' or i=='e':
            print("1110",end="")
        if i=='F' or i=='f':
            print("1111",end="")
    print()