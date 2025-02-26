from random import randint

while True:
  rannumb=randint(1,1000)
  numb1=int(input('Please guess a number between 1 and 1000.'))
  if numb1==rannumb:
    print('Well done you guessed it correctly!!')
  else:
    print('Sorry! Wrong number, try again.')
  user_input=input('Type STOP to end the game or enter any character to play again.')
  if user_input in('stop', 'STOP'):
    break
  else:
      print('Okey, playing again.')
