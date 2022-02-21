startNum=int(input('Enter a number to be Collatz\'d: ')) #Ask the User for a number
jumps=int(0) #Start the counter for jumps at zero
currentNum=int(startNum) #Assign the starting number to the current number
while currentNum!=1: #Start the primary loop

  if currentNum % 2 == 0: #Assess if the number is Even
    print('Even') #Show the current step
    currentNum=currentNum/2 #Do math
    print(currentNum) #Show the new number
  else:
    print('Odd') #Print that the number is Odd
    currentNum=(currentNum*3)+1 #Do the math
    print(currentNum) #Show the new Number
  jumps+=1 #Add one to the jumps counter

print('Starting Number: ',int(startNum)) #Print total jumps at the end
print('Ending Number: ',int(currentNum)) #Print ending number at the end (Should be 1)
print('Number of Jumps: ',jumps) #Print number of jumps
