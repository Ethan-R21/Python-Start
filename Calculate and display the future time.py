from datetime import datetime, timedelta

now = datetime.now()
day = now.strftime("%A %B %Y (%H:%M:%S)")

print("The time right now is" , day)

question=input('Would you like to know what the time it will be in the future?')
if question in ('No', 'no', 'Nah', 'nah', 'No thanks', 'No Thanks', 'no thanks', 'No thank you', 'no thank you'):
  print('Thats okay, come again!')
else:
  time=int(input('Okey, please input an amount of seconds'))
print('The time '+str(time)+' seconds into the future will be', now+timedelta(seconds=time))
