import random, string
print('Welcome to the password generator')
length = int(input('\nLength of password:'))
all = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
generate = random.sample(all, length)
password = "".join(generate)
print(password)
