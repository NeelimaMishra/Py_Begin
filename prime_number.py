# to check if a number is prime or not

def prime(n):
    if n == 1: # 1 is not prime
        return False
    for i in range(2,n):
        if n % i == 0:
            flag = False # n is not prime
            break
        else:
            flag = True # n is prime
    return flag

def main():
    n = int(input("Enter number: "))
    result = prime(n)
    if result == True:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

if __name__ == "__main__":
    main()