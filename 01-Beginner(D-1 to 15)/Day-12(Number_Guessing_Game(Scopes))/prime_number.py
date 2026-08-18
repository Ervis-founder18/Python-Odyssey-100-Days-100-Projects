def is_prime(num):
    count=0
    for i in range(1,num+1):   # because prime number is a number which is divisible by 1 and itself only so we will check for all the numbers from 1 to that number# factor will be within the choosen number itself so num+1
        if num%i==0:
            count=count+1
    if count==2:
        print("IT IS A PRIME NUMBER")
        return True
    else:
        print("IT IS NOT A PRIME NUMBER")
        return False


num=int(input("Enter a Number :"))

is_prime(num)
                      