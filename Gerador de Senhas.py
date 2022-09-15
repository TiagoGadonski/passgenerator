import random

from numpy import number

lower_case =  "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%¨&*()!^"

for_pass = lower_case + upper_case + numbers + symbols

size_pass = 12

password = "".join(random.sample(for_pass, size_pass))

print("Minha senha: {}".format(password))