name = input("What's your name? ")
print(f'Hello {name}, I am your phone book.')

num_string = input("How old are you? ")
x = num_string.isnumeric()
if x == False:
    print("That doesn't seem to be an integer.")
    exit()
age = int(num_string)
if age <= 18:
    print("You are so young! Life is ahead of you!")
elif age < 40:
    print("That's a nice age!!!!!!!!!!!!!!!")
else:
    print("You must be very wise!")
