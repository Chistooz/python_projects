import random
from random import choice

digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
punc = '!#$%&*+-=?@^_'

chars = ''


cntPass = int(input('Укажите количество паролей для генерации:'))
lenPass = int(input('Укажите длину одного пароля::'))
digOn = input('Включать ли цифры 0123456789? (y/n)')
ABCOn = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
puncOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
symbOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')


if digOn == 'y':
    chars += digits
if ABCOn == 'y':
    chars += uppercase_letters
if abcOn == 'y':
    chars += lowercase_letters
if puncOn == 'y':
    chars += punc
if symbOn == 'y':
    for c in 'il1Lo0O':
        chars.replace(c, '')



def generate_password (length, chars):
    password = ''
    for i in range (length):
        password += random.choice(chars)
    print(password)

for _ in range (cntPass):
    generate_password(lenPass, chars)