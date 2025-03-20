#A program that asks a user to input the length of a side in a square. Write a function that takes this value and returns it to be printed.

def times(numb1,numb2):
  total=numb1*numb2
  return(total)

numb1=int(input('Length of base='))
numb2=int(input('Length of height='))

answer=times(numb1,numb2)
print('The area is', answer)
