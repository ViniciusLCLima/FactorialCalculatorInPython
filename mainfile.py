print("Let's calculate the factorial of a number!")
num=int(input("Enter the number you want: "))
while num<0:
  num=int(input("Factorial is just for not negative numbers, try again with another one: "))
if num==0:
  print(1)
else:
  for k in range(num,0,-1):
    if k>1:
      num*=k-1
  else:print("Result: ",num)
