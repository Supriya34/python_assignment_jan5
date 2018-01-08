my_list=list(range(0,100))
prime=[]
with open("primenumber2.txt","w") as fp:
    for num in my_list:
        for i in range(2, num - 1):
            if (num % i == 0):
                break
        else:
            prime.append(num)

    fp.write(str(prime))