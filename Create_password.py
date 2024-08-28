import random
length_of_password = int (input("Enter the length of Password : "))
upper_alpha = "ABCDEFGHIJKLMNOPQUVWXYZ"
lower_alpha = "abcdefghijklmnopquvwxyz"
numaric = "123456789"
special_symbol = "!@#$%^&*()_."
password = upper_alpha+lower_alpha+numaric+special_symbol
generated_password = " ".join(random.sample(password,length_of_password))
print(f"Strong Password is : ",generated_password)