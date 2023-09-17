def add(x,y):
    total = x + y
    return total
def sub(x,y):
    total = x - y
    return total
def div(x,y):
    total = x / y
    return total
def mul(x,y):
    total = x * y
    return total

num1 = int(input("Enter Number 1 "))
num2 = int(input("Enter Number 2 "))

total = add(num1,num2)
print("Total of the addition process is ",total)
total = sub(num1,num2)
print("Total of the subtraction process is ",total)
total = div(num1,num2)
print("Total of the division process is ",total)
total = mul(num1,num2)
print("Total of the multiplication process is ",total)
