for _ in range(int(input())):
    s=input()
    st=[]
    for i in s:
        if i in ['(','{','[']:
            st.append(i)
        else:
            if len(st) and ((st[-1]=='(' and i==')')or(st[-1]=='{' and i=='}')or(st[-1]=='[' and i==']')):
                st.pop()
            else:
                st.append(i)
    if len(st):
        print("False")
    else:
        print("True")