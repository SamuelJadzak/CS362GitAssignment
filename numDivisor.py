def divisors(n):
    for x in range(1,n+1):
        if n % x == 0:
            print(x)
number = input("please input number to find all divisors")
divisors(int(number))