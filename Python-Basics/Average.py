import time
def Average():
  a = []
  n=int(input("how many time you want to input: "))
  for i in range(0,n):
    l=int(input())
    a.append(l)
  ask = input('Do you want to know the average amount of numbers? yes/no \n')
  if ask == 'yes':
    num = sum(a) / len(a)
    print("The average number is " +str(num))
  

Average()


