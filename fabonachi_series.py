# fabonachi series

def fabo(n):
    a, b = 0, 1
    if n < 0:
        print("incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
    return b

def main():
    n = int(input("Enter a number: "))
    result = fabo(n)
    print("fabonachi series is: {}".format(result))

if __name__ == "__main__":
    main()

