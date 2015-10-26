sum=lambda x: x*(x+1)/2
T=input()
for i in xrange(0,T):
        N=input()
        print "checking",N
        d=1
        n=1
        while d<=N:
                #print "d:",d
                if d%2==0:
                        if sum(d/2)>=N:
                               print d
                               break
                        else:
                                d=d+1
                else:
                        if sum(d/2)+(d+1)>=N:
                                print d
                                break
                        else:
                                d=d+1
        '''
        while True and N>1:
                if 2*sum(n)==N:
                        days=2*(days)+1
                        break
                
                if (2*sum(n))+(n+1)==N:
                        days=2*days+1
                        break
                #print n,sum(n),days
                n=n+1
                days=days+1
        print days'''
        
