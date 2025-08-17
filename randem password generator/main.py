import random

while True:
    passleng = int(input("enter pass worde length"))
    a = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")
    password = "".join(random.sample(a,passleng))
    print(password)