
#'🦁 Gryffindor'
#'🦅 Ravenclaw'
#'🦡 Hufflepuff'
#'🐍 Slytherin'

#Qestion 1
print("Q1: Do you like Dawn or Dusk?\n 1: Dawn \n 2: Dusk")

answer1=int(input('Enter your answer (1-2): '))
if answer1 ==1: 
  print('Gryffindor and Ravenclaw both get a +1')
elif answer1==2: 
  print('Hufflepuff and Slytherin both get a +1')
else: 
  print('Wrong input.')

#Question2
print("Q2: When I'm dead, I want people to remember me as:\n 1: The Good \n 2: The Great \n 3: The Wise \n 4: The Bold")   
answer2=int(input('Enter your answer (1-4): '))
if answer2 ==1: 
  print('Hufflepuff gets a +2')
elif answer2==2: 
  print('Slytherin gets a +2')
elif answer2==3:
  print('Ravenclaw gets a +2')
elif answer2==4:
  print('Gryffindor gets a +2')
else:
  print('Wrong input.')
#Question3
print("Q3: Which kind of instrument most pleases your ear?\n 1: The violin \n 2: The trumpet \n 3: The piano \n 4: The drum")
answer3=int(input('Enter your answer (1-4): ')) 
if answer3 ==1: 
  print('Slytherin gets a +4')  
elif answer3==2: 
  print('Hufflepuff gets a +4') 
elif answer3==3:
  print('Ravenclaw gets a +4')  
elif answer3==4:
  print('Gryffindor gets a +4') 
else:
  print('Wrong input.')

#Calculations
gryffindor = 0
ravenclaw = 0   
hufflepuff = 0
slytherin = 0
if answer1 == 1:
    gryffindor += 1
    ravenclaw += 1 
elif answer1 == 2:
    hufflepuff += 1
    slytherin += 1

if answer2 == 1:
    hufflepuff += 2
elif answer2 == 2:
    slytherin += 2  
elif answer2 == 3:
    ravenclaw += 2
elif answer2 == 4:
    gryffindor += 2

if answer3 == 1:
    slytherin += 4
elif answer3 == 2:
    hufflepuff += 4
elif answer3 == 3:
    ravenclaw += 4 
elif answer3 == 4:
    gryffindor += 4
    
#Final Calculation 

houses = {
    'Gryffindor': gryffindor,
    'Ravenclaw': ravenclaw,
    'Hufflepuff': hufflepuff,
    'Slytherin': slytherin
}

final = max(houses, key=houses.get)   

#Final message
print('Thank you for answering the questions! The Sorting Hat is now making a decision...')
print('Congratulations! You have been sorted into... ')
print(final + '!')