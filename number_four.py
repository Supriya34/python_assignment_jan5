my_list=list(range(0,100))
primeno=[]
fp = open("prime_number.txt","w")

for each in my_list:
    for i in range(2, each - 1):
        if (each % i == 0):
            break
    else:
        primeno.append(each)


fp.write(str(primeno))
fp.close()