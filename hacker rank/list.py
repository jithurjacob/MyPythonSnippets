n=int(raw_input())
outp=[]
for i in range(0,n):
    st=raw_input()
    st=st.split()
    if st[0]=="insert":
        #print int(st[1])
        outp.insert(int(st[1]),int(st[2]))
    elif st[0]=="print":
        print outp
    elif st[0]=="remove":
        outp.remove(int(st[1]))
    elif st[0]=="append":
        outp.append(int(st[1]))
    elif st[0]=="sort":
        outp.sort()
    elif st[0]=="pop":
        outp.pop()
    elif st[0]=="reverse":
        outp.reverse()
    
    
