def fact(n):
  if n==1: return 1
  return n*fact(n-1)

num= int(input("Enter the no. you want factorial of: "))

print(fact(num))