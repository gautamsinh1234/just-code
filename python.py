# list , dict , tuple , set/


a1 = [1,2,3,4,5,6,"thi",'is','it',5.2]


# if you just print only string then use isalpha()
        
print(a1)
for i in a1:
    if str(i).isalpha():
        print(i)


# if you just print only number then use isalpha()
        
print(a1)
for i in a1:
    if str(i).isnumeric():
        print(i)






##########################33333333


a4 =  ['abc','bca','ccd','aav']


for i in a4:
    if "a" in i:
        print(i)




# if print all list + and anser giving than 


from functools import reduce

a5 =  [1,2,3,45,6,7,8,900]



p =   reduce(lambda x ,y : x+y,a5)


print(p)




############ second method to eassy

a = sum(a5)
print(a)


# insert data   in use index and value 

 
a5.insert(3,12)

print(a5)


## remove perticuler element

a5.remove(12)





a5.reverse()

a5.sort()



a5[3]=566


t = a5.count(45)
print(t)


print(a5)





a6  = [1,2,3,2,5,4,5,6,5,8,5,5,66,565,5,211,244,4,5,2,55,5,62,2,5,6,22,2,55,]


p = set(a6)

a = list(p)
print(a)

o = p.intersection([1,2,3,4,5,6,1,2,3,4,5,6])


print(o)


l = p.union([1,2,3,4,5,6,1,2,3,4,5,6])
print(l)






b1 = [1,2,3,4,5,6,4,5,6,7,8,9,10]



          

def abc():
    for i in b1:
     if i%2==0:
        print(i,end=',') 
         

print(abc())

# po = list(map(lambda x: (x%2 == 0), b1 ))


# print(po)
        




















