import random

print('Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%#()?0123456789'

num = input("How many passwords do you want to generate? ")
num = int(num)

length = input("Input your password length: ")
length = int(length)

print('\nHere are you passwords: ')

for pwd in range(num):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
