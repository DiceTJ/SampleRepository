startNum=int(input('Enter a number to be Collatz\'d: '))
jumps=int(0)
currentNum=int(startNum)
while currentNum!=1:

  if currentNum % 2 == 0:
    print('Even')
    currentNum=currentNum/2
    print(currentNum)
  else:
    print('Odd')
    currentNum=(currentNum*3)+1
    print(currentNum)
  jumps+=1

print('Starting Number: ',int(startNum))
print('Ending Number: ',int(currentNum))
print('Number of Jumps: ',jumps)
