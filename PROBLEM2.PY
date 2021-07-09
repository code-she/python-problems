n = int(input(""))
n>=100 and n<=1

if (n % 2) > 0:
    print("Weird")
elif(n % 2)==0 and 2<=n and 5>=n:
    print("Not Weird")
elif(n % 2)==0 and 6<=n and 20>=n:
    print("Weird")
elif(n % 2)==0 and n>20:
    print("Not Weird")
