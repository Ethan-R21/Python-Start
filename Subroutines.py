#Subroutines

def multiply(): #Use def blabla() to make function/subroutine
  numb1=float(input('Number 1='))
  numb2=float(input('Number 2='))
  print('Your number is', numb1*numb2)
  
def divide():
  numb3=float(input('Number 1='))
  numb4=float(input('Number 2='))
  print('Your number is', numb3/numb4)
  
quest1=input('Would you like to multiply or divide?')

if quest1.lower()=='multiply':#Use .lower() instead of doing to check for capitals 
  multiply()
elif quest1.lower()=='divide':
  divide()
else:
  print('Sorry! Thats not an option.')
