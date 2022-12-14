from time import sleep

print('Welcome to your stopwatch!')
sleep(1)

my_time = int(input('Enter the time in seconds:'))
sleep(0.3)

while my_time:
    for x in range(my_time, 0, -1):
        print(f'{x}')
        sleep(0.5)
    print("Time's up!")
    break
