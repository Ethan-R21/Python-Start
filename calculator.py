opt1=int(input('Enter a number'))

opt3=int(input('Please choose another number'))

print('Addition, Subtraction, Multiplication or Division')

opt2=input('Please choose a method for the calculation')

if opt2 in('addition', 'Addition', 'Add', 'add'):
  print('Your number is',opt1+opt3)

elif opt2 in ('multiplication', 'Multiplication', 'Multiply', 'multiply', 'times'):
  print('Your number is',opt1*opt3)
  
elif opt2 in ('Subtraction', 'subtraction', 'Takeaway', 'takeaway', 'Subtract', 'subtract', 'Minus', 'minus'):
  print('Your number is',opt1-opt3)
  
elif opt2 in ('Division', 'division', 'Divide', 'divide'):
  print('Your number is',opt1/opt3)
