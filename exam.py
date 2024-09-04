def collaz(n):
    l=[n]
    while n!=1:
        if n%2==0:
            n=n//2
        elif n%2!=0:
            n=3*n+1
        l.append(n)
    return l
        
def large(n):
    maxn,r=0,0
    for i in range(1,n):
        p=collaz(i)
        # print(i,len(p))
        if(maxn<len(p)):
            maxn=len(p)
            r=i
            # print(r,i)
        else:
            continue
        # maxn=max(maxn,len(p))
        # print(r)
    return r





n=int(input())
p=collaz(n)
for i in range(len(p)):
    print(p[i],end="->")

print("\n")
n=large(1000000)
print(n)