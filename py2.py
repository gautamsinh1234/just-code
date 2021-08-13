# fibonachi serise
0,1,1,2,3,5,8,13,21

def fibo(n):
    if n == 1:
       return 1
    
    elif n == 2:
        return 1

    else:

       return   fibo(n-1) + fibo(n-2)    
        
  
t  = fibo(8)
print(t)

# op = list(map(lambda x))


from functools  import reduce

q = [1,2,3,4]

op= reduce(lambda x,y: x*y,q)
print(op) 
 

# print(opo)
    







aa   = ["nfk",'kjdncd','dn','dkn']

print(len(aa))
















