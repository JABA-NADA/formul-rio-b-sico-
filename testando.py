from time import sleep

print('Welcome to JABA-WEB!')
sleep(0.5)

name = input('What is your name please?: ').capitalize()
sleep(0.3)

email = input(f'Please {name} put your e-mail here: ')
sleep(0.3)

index = email.index('@')

owner = email[0:index]

domain = email[index + 1:]

print(f'{name} does your email have this domain: {domain}, and this name: {owner}?')
sleep(0.3)

chose = input('If yes type [Y], to no type [N]: ').upper()

if chose != 'Y' and 'N':
    print(f'Error this {chose} is NOT valid!')

while chose == 'N':

    email = input(f'Please {name} put your e-mail here: ')
    sleep(0.3)

    index = email.index('@')

    owner = email[0:index]

    domain = email[index + 1:]

    print(f'{name} does your email have this domain: {domain}, and this name: {owner}?')
    sleep(0.3)

    chose = input('If yes type [Y], to no type [N]: ').upper()

    if chose != 'Y' and 'N':
        print(f'Error this {chose} is NOT valid!')
    else:
        print(f'Nice {name}, the e-mail: {email} was validate')
        sleep(0.5)

print('Now you will create an username for you!')
sleep(0.4)

username = input(f'{name}, please write your username here: ')
sleep(0.3)

while len(username) <= 0 or username == '' or username == ' ':
    print(f'Error the username {username} is NOT valid!')
    sleep(0.3)

    username = input(f'{name}, please write your username here: ')
    sleep(0.3)

print(f'{name} is this your username: {username}?')

option = input('If it is type [Y], if it is not type [N]').upper()

while option == 'N':
    username = input(f'{name}, please write your username here: ')
    sleep(0.3)

    print(f'{name} is this your username: {username}?')

    option = input('If it is type [Y], if it is not type [N]').upper()

while option == 'Y':
    print(f'Nice {name}! Now we have some information about you:')

    print(f'Your name: {name}')

    print(f'Your email: {email}')

    print(f'And your username: {username}')

    print('Now we just need to know how old are you')

    age = int(input(f'How old are you {name}: '))
    break

print(f'{name} are you {age} years old ?')
