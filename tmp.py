

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)





FibArray = [0,1] 
  
def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 
  
# Driver Program 
print("Recursive")
print (fib(5))

print("Dynamic Programming")
print(fibonacci(100)) 