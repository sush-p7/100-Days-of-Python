# Interview Question Sciative Solutions
# test input = [('name','gender','age'),('name','gender','age'),('name','gender','age')]
# output == [[age,occurence]]


from collections import Counter
from operator import itemgetter
test = [('h','G',22),('g','Male',23),('d','Male',25),('ggjd','Male',22),('sush','Male',20),('sush','Male',16),('sush','Male',19),('sush','Male',25),('sush','Male',24),('sush','Male',23),('sush','Male',20),('sush','Male',23),('sush','Male',20),('sush','Male',22)]
t = []
for i in test:
    t.append(i[2])
temp = Counter(t)
print(dict(temp))
def check(test):
    new_test = sorted(test, key=itemgetter(2))
    result = []
    for i in new_test:
        age =  i[2]
        count = 0
        for j in new_test:
            if age==j[2]:
                count +=1
        result.append([age,count])
    return result
print(check(test))

# [sss[aaa[bbbb[ccc]]][ddd]]
# [1:2,2:1,3:1]
# A = [('aaa','aaa',20,(690,(0))),('aaa','aaa',20,(5,(1))),('aaa','aaa',20,(8,(1))),('aaa','aaa',20,(7,(1)))]
# print(sorted(A ,key=lambda e: (e[3],e[1],e[1])))