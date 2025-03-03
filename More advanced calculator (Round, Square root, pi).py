import math

my_list=('Addition', 'Subtraction', 'Multiplication', 'Division', 'Square root', 'Round', 'pi')

print('Please choose a method.')
for item in my_list: #Use this for when I need vertical lists.
    print(item)

opt2=input('Enter here-')

if opt2 in ('addition', 'Addition', 'Add', 'add', 'multiplication', 'Multiplication', 'Multiply', 'multiply', 'times', 'Subtraction', 'subtraction', 'Takeaway', 'takeaway', 'Subtract', 'subtract', 'Minus', 'minus', 'Division', 'division', 'Divide', 'divide'):
  opt1=float(input('Enter a number'))

  opt3=float(input('Please choose another number'))

#Round time
if opt2 in ('Round', 'round', 'Rounding', 'rounding'):
    num = float(input('Please enter a decimal to be rounded: '))
    direction = input('Would you like to round up or down? ')

    if direction in ('up', 'Up'):
      print('The number rounded up is:', math.ceil(num))  #Round up

    elif direction in ('down', 'Down'):
      print('The number rounded down is:', math.floor(num)) #Round down
#End of Round time

#Pi time
my_list2=('Addition', 'Subtraction', 'Multiplication', 'Division')

if opt2 in ('pi', 'Pi'):
  pinumb = float(input('Please enter a number: '))

  print("Available methods for Pi:")
  for item in my_list2:
    print(item)
  
  methodpi = input('Please choose the method: ')

  if methodpi in ('addition', 'Addition', 'Add', 'add'):
    print('Your number is', pinumb+math.pi)

  elif methodpi in ('multiplication', 'Multiplication', 'Multiply', 'multiply', 'times'):
    print('Your number is', pinumb*math.pi)

  elif methodpi in ('Subtraction', 'subtraction', 'Takeaway', 'takeaway', 'Subtract', 'subtract', 'Minus', 'minus'):
    print('Your number is', pinumb-math.pi)

  elif methodpi in ('Division', 'division', 'Divide', 'divide'):
    print('Your number is', pinumb/math.pi)
#End of Pi time

if opt2 in('addition', 'Addition', 'Add', 'add'):
  print('Your number is',opt1+opt3)

elif opt2 in ('multiplication', 'Multiplication', 'Multiply', 'multiply', 'times'):
  print('Your number is',opt1*opt3)
  
elif opt2 in ('Subtraction', 'subtraction', 'Takeaway', 'takeaway', 'Subtract', 'subtract', 'Minus', 'minus'):
  print('Your number is',opt1-opt3)
  
elif opt2 in ('Division', 'division', 'Divide', 'divide'):
  print('Your number is',opt1/opt3)
  
#Square time
elif opt2 in ('Square root', 'square root', 'Square Root', 'square', 'Square'):
    square = float(input('Please enter a number to be square rooted: '))
    print('The square root is:', math.sqrt(square))#Square root code
#End of Square time
