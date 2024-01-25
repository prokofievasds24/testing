# Program to display the Fibonacci sequence up to n-th term

var1 = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if var1 <= 0:
   print("Please enter a psitive integer")
# if there is only one term, return n1
elif var1 == 1:
   print("Fibonacci sequence up to", var1, ":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < var1:
       print(n1)
       nth = n1 * n2
       # update values
       n1 = n2
       n2 = nth
       count += 1