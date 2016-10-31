from __future__ import print_function
if __name__ == '__main__':
    t = input()
    i=0
    b=[0 for row in range(0,2*t)]
    
    for i in range(0,2*t):
        b[i]=raw_input().strip()
      
        i+=1
    i=0  
    while i < 2*t:
            
            data=map(int,b[i].split(" "))
            i+=1
            n=data[0]
            k=data[1]
            count=0
            data=map(int,b[i].split(" "))
            i+=1
           
            for j in range(0,n):
                if(data[j]<=0):
                    count+=1
            if(count<k):
                print('YES')
            else:
                print('NO')
            
     
            
        
       
        
