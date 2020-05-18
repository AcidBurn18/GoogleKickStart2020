t=int(input())
x=1          #For Printing Purpose only
while(t>0):
    c=0
    t-=1
    n=int(input())
    p=[int(p) for p in input().split()]
    temp=p
    o=p[0]
    l=p[-1]
    p.sort(reverse=True)
    if(p[0]==p[-1]):
        print("Case #{}: 0".format(x))
        x+=1

    elif(p[0]==o or p[0]==l): 
        
        print("Case #{}: 0".format(x))
        
        x+=1
        
    else:
        t=p[0]
        for i in p:
            if(i==t):
                c+=1
        print("Case #{}: {}".format(x,c))
        x+=1
        
