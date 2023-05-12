
 n=int(input())
 a=[]
 for i in range (0,n):
   ai=int(input())
   a.append(ai)
 summa=0
 for i in range (0,n):
   if a[i]%2==0:
    summa=summa+a[i]
 print(summa)
 

