
def num(n):

    a = 0
    b = 1
    print("Fibonacci sequence: " ,a)
    print("Fibonacci sequence: " ,b)
    for y in range(2,n):

        sum = a + b
        a=b
        b= sum

        print ("Fibonacci sequence: " , sum)

num(10)
