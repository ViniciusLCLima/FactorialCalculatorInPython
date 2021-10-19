print("Let's calculate the factorial of a number!")
num=int(input("Enter the number you want: "))
if num==0:
  print(1)
else:
  for k in range(num,0,-1):
    if k>1:
      num*=k-1
  else:print(num)
