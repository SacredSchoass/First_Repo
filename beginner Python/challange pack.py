# Write code below 💖
planet = int(input('Give me your planet number:   '))
weight = float(input('What is youre weight in kg:   '))

deweight = 0

if planet ==1: 
  deweight = weight*0.38
  print(f'Your weight on Mercury is: {deweight} kg')
elif planet ==2:
  deweight = weight*0.91
  print(f'Your weight on Venus is: {deweight} kg')
elif planet ==3:
  deweight = weight*0.38
  print(f'Your weight on Mars is: {deweight} kg') 
elif planet ==4:
  deweight = weight*2.53
  print(f'Your weight on Jupiter is: {deweight} kg')
elif planet ==5:
  deweight = weight*1.07
  print(f'Your weight on Saturn is: {deweight} kg') 
elif planet ==6:
  deweight = weight*0.89
  print(f'Your weight on Uranus is: {deweight} kg')
elif planet ==7:
  deweight = weight*1.14
  print(f'Your weight on Neptune is: {deweight} kg' )
else:
  print('Invalid planet')