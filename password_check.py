min_length = 5
password = input("enter password:")
while len(password) < min_length:
    print(f"password is less than {min_length}")
    password = input("enter password:")
for i in range(0, len(password), 1):
    print("*", end='')
