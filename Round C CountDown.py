t=int(input())      #Test Case
x=0
while(t>0):
    x+=1
    t-=1
    n=[int(n) for n in input().split()]
    cont=0
    a=[int(a) for a in input().split()]
    for i in range(n[0]):
        if(a[i]==n[1]):                       #If the initial element is there or not means K
            r=1
            if((n[0]-i)>=n[1]):
                for j in range(i,i+n[1]-1):
                    if(a[j]==a[j+1]+1):         #check for pattern like factorial
                        continue
                    else:
                        r=0
                        break                   #Reduce the Running time
                if(r==1):
                    cont+=1
    print("Case #{}: {}".format(x,cont))      #format printing
                
    
            
        
