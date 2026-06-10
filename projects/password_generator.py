#random password generator using python
import random
letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
special_characters="@#$%^&*"
all_characters=letters+digits+special_characters
n=int(input("enter the length of password:"))
new_password=""
for i in range(n):
    new_password+=(random.choice(all_characters))
print("the new strong password is:",new_password)

