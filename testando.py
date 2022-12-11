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
        for letra in word:
            if letra.lower() not in "abcdefghijhlmnopqrstuvwxyz":
                return f'Error the name: {nome} is NOT valid!'
    return f"Your name {nome} was validate"


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

while name == '' or name == ' ' or len(name) <= 1:
    print(f'Error the name: {name} is NOT valid!')

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

while chose != 'Y' and 'N':
    print(f'Error this {chose} is NOT valid!')

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

    print(f'Your name: {name}')

    print(f'Your email: {email}')

    print(f'And your username: {username}')

    print('Now we just need to know how old are you')
    break

age = int(input(f'How old are you {name}: '))

print(f'{name} are you {age} years old ?')
