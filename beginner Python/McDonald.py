# Write code below 💖
menu = '''
    1. 🍔 Cheeseburger
    2. 🍟 Fries
    3. 🥤 Soda
    4. 🍦 Ice Cream
    5. 🍪 Cookie
    Welcome Menu = 🍔 Cheeseburger, 🍟 Fries and🥤 Soda
    '''

def welcome ():
  return '🍔 Cheeseburger''🍟 Fries''🥤 Soda'

def get_item (num):

    if num == 1:
        return '🍔 Cheeseburger'
    elif num == 2:
        return '🍟 Fries'
    elif num == 3:
        return '🥤 Soda'
    elif num == 4:
        return '🍦 Ice Cream'
    elif num == 5: 
        return '🍪 Cookie'
    else:
        return 'Invalid selection'

num = input('What number do you want? For Welcome Menu type "welcome"\n' + menu + '\n') 

if num.lower() == 'welcome':
    print(welcome())
else:
    num_int = int(num)
    print(get_item(num_int))
    