# Password Generator 
import random  # random.shuffle and random.choice can be used 
upper = 'ABCDEFGHIJKLMNOPQRSTVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789'
symbols = ',./<>?:;"\'|}{[]+_=-!@#$%^&*()'

print("Welcome to the Generator")

all = upper + lower + symbols + number
length = int(input("Enter the length of the password: "))
password = ''.join(random.sample(all,length))
print(password)