from time import sleep

print('Welcome to JABA-WEB!')
sleep(0.5)

name = input('What is your name please?: ').capitalize()
sleep(0.3)

"""
   detectando erros com o for 
   """


def detecta_erro_name_for(nome):
    for word in nome.split():
        for lettr in word:
            if lettr.lower() not in "abcdefghijhlmnopqrstuvwxyzç":
                return 'Error'
    return "validate"


detecta_dentro = detecta_erro_name_for(name)

while "Error" in detecta_dentro:
    print(f'Error the name: {name} is NOT valid')
    name = input('What is your name please?: ').capitalize()
    sleep(0.3)
    detecta_dentro = detecta_erro_name_for(name)

"""
    3 partes da estrutura de repetição:
    - inicialização - 1 unica vez
    - condição - a cada vez
    - incremento - no final de cada vez
"""

'''def detecta_erro_name_while(nome):
    num_palavras = len(nome.split())
    palavras = nome.split()
    i = 0
    while i < num_palavras:
        j = 0
        palavra = palavras[i]
        while j < len(palavra):
            letra = palavra[j]
            if letra.lower() not in "abcdefghijhlmnopqrstuvwxyz":
                return "erro"
            j += 1
        i += 1
    return "acerto"
'''

email = input(f'Please {name} put your e-mail here: ')
sleep(0.3)

index = email.index('@')

owner = email[0:index]

domain = email[index + 1:]

print(f'{name} does your email have this domain: {domain}, and this name: {owner}?')
sleep(0.3)

chose = input('If yes type [Y], to no type [N]: ').upper()

while chose != 'Y' and chose != 'N':
    print(f'Error this {chose} is NOT valid!')

    print(f'{name} does your email have this domain: {domain}, and this name: {owner}?')
    sleep(0.3)

    chose = input('If yes type [Y], to no type [N]: ').upper()

while chose == 'N':
    email = input(f'Please {name} put your e-mail here: ')
    sleep(0.3)

    print(f'{name} does your email have this domain: {domain}, and this name: {owner}?')
    sleep(0.3)
    chose = input('If yes type [Y], to no type [N]: ').upper()

if chose == 'Y':
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
    sleep(0.5)

    print(f'Your name: {name}')
    sleep(0.5)

    print(f'Your email: {email}')
    sleep(0.5)

    print(f'And your username: {username}')
    sleep(0.4)

    print('Now we just need to know how old are you!')
    sleep(0.4)
    break

age = int(input(f'How old are you {name}: '))
sleep(0.4)

option1 = input(f'{name} are you {age} years old  [Y]/[N]?').upper()
sleep(0.4)

while option1 == 'N':
    int(input(f'How old are you {name}: '))
    sleep(0.4)

    input(f'{name} are you {age} years old  [Y]/[N]?').upper()
    sleep(0.4)

    if option1 != 'N' and option1 != 'Y':
        print(f'Error your option is NOT valid')

        age = int(input(f'How old are you {name}?: '))
        sleep(0.4)

        option1 = input(f'{name} are you {age} years old  [Y]/[N]?:').upper()
        sleep(0.4)

print('Your registration in this site was successfully completed!')
print(':D')
