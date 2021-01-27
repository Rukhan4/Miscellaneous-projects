# Start with a number *n > 1*. Find the number of steps it takes to reach one using the following process:
# If *n* is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1

def Collatz_Conjecture(n, count=0):
    if n <= 1:
        return count
    if n % 2 == 0:
        return Collatz_Conjecture(n/2, count+1)
    else:
        return Collatz_Conjecture(n*3+1, count+1)


while True:  # Validate user input
    x = int(input("Enter a number to find it's Collatz Conjecture: "))
    if x > 1:
        y = Collatz_Conjecture(x)
        print("The value returned by the Collatz Conjecture Algorithm is:", y)
        break
    else:
        print("Please enter a number!")
        continue
