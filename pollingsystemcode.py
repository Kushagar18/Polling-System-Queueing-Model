import numpy as np

n=int(input('n='))
lamda=list(float(x) for x in input("lambda= ").split())
b=list(float(x) for x in input("b= ").split())
b2=[]
for i in range(n):
    b2.append((2)*((b[i])**(2)))
p1=[]
for i in range(n):
    p1.append(lamda[i]*b[i])
p=np.sum(p1)
r1=list(float(x) for x in input("r(i)= ").split())
r=np.sum(r1)
delta2=[]
for i in range(n):
    delta2.append((r1[i])**(2))
triangle=np.sum(delta2)
typ=int(input("type= "))
lst1=[]
lst2=[]

if typ==1:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i>j:
                t1=[]
                for k in range(n**2):
                    t1.append(0)
                for m in range(i+1,n+1):
                    t1[(j-1)*(n)+(m-1)]-=1
                for m in range(1,j):
                    t1[(j-1)*(n)+(m-1)]-=1
                for m in range(j,i):
                    t1[(m-1)*(n)+(j-1)]-=1
                t1[(i-1)*n+j-1]+=((1-p1[i-1])/(p1[i-1]))
                lst1.append(t1)
                t2=0
                lst2.append(t2)
            elif j>i:
                t1=[]
                for k in range(n**2):
                    t1.append(0)
                for m in range(i+1,j):
                    t1[(j-1)*(n)+(m-1)]-=1
                for m in range(j,n+1):
                    t1[(m-1)*(n)+(j-1)]-=1
                for m in range(1,i):
                    t1[(m-1)*(n)+(j-1)]-=1
                t1[(i-1)*n+j-1]+=((1-p1[i-1])/(p1[i-1]))
                lst1.append(t1)
                t2=0
                lst2.append(t2)
            else:
                t1=[]
                for k in range(n**2):
                    t1.append(0)
                t1[(i-1)*n+i-1]+=1
                for m in range(1,n+1):
                    if i!=m:
                        t1[(i-1)*n+m-1]-=((p1[i-1])/(1-p1[i-1]))
                lst1.append(t1)
                temp=0
                temp+=(((delta2[i-2])**(2))/(1-p1[i-1])**(2))
                temp+=(lamda[i-1]*b2[i-1]*r*(1-p1[i-1])/((1-p)*((1-p1[i-1])**(3))))
                lst2.append(temp)

    final=np.linalg.solve(lst1,lst2)
    print(final)
    qt=[]
    for i in range(1,n+1):
        temp=0
        temp+=(lamda[i-1]*b2[i-1])/(2*(1-p1[i-1]))
        temp+=r*(1-p1[i-1])/(2*(1-p))
        sum=0
        for j in range(1,n+1):
            if i!=j:
                sum+=final[(i-1)*n+(j-1)]
        sum*=((1-p1[i-1])/p1[i-1])
        sum+=delta2[i-2]**2
        sum/=(r*(1-p1[i-1])*2/(1-p))
        temp+=sum
        print(temp)
        qt.append(temp)

if typ==2:

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i>j:
                t1=[]
                for k in range(n**2):
                    t1.append(0)
                for m in range(i,n+1):
                    t1[(j-1)*(n)+(m-1)]-=1
                for m in range(1,j):
                    t1[(j-1)*(n)+(m-1)]-=1
                for m in range(j,i):
                    t1[(m-1)*(n)+(j-1)]-=1
                t1[(i-1)*n+j-1]+=((1)/(p1[i-1]))
                lst1.append(t1)
                t2=0
                lst2.append(t2)
            elif j>i:
                t1=[]
                for k in range(n**2):
                    t1.append(0)
                for m in range(i,j):
                    t1[(j-1)*(n)+(m-1)]-=1
                for m in range(j,n+1):
                    t1[(m-1)*(n)+(j-1)]-=1
                for m in range(1,i):
                    t1[(m-1)*(n)+(j-1)]-=1
                t1[(i-1)*n+j-1]+=((1)/(p1[i-1]))
                lst1.append(t1)
                t2=0
                lst2.append(t2)
            else:
                t1=[]
                for k in range(n**2):
                    t1.append(0)
                t1[(i-1)*n+i-1]+=1
                for m in range(1,n+1):
                    if i!=m:
                        t1[(i-1)*n+m-1]-=p1[i-1]
                for m in range(1,n+1):
                    t1[(m-1)*n+(i-1)]-=((p1[i-1])**2)
                lst1.append(t1)
                temp=0
                temp+=((delta2[i-1])**(2))
                temp+=(lamda[i-1]*b2[i-1]*r/(1-p))
                lst2.append(temp)

    final=np.linalg.solve(lst1,lst2)
    print(final)
    qt=[]

    for i in range(1,n+1):
        temp=0
        temp+=((1+p1[i-1])*(r)/(2*(1-p)))
        sum=0
        for j in range(1,n+1):
            if i!=j:
                sum+=final[(i-1)*n+(j-1)]
        sum*=((1)/p1[i-1])
        for j in range(1,n+1):
            sum+=final[(j-1)*n+(i-1)]
        temp+=((1-p)*(1+p1[i-1])*(sum)/(2*r))
        print(temp)
        qt.append(temp)


    



            
