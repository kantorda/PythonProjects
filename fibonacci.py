

def Fibonacci(idx):
    if idx == 1:
        return 1,0

    sum,last = Fibonacci(idx - 1)
    print("sum is", sum)
    print("last is", last)
    return sum + last, sum

if __name__ == "__main__":
    number,_ = Fibonacci(10)
    print("The tenth Fibonacci number is ", number)