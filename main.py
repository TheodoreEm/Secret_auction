from art import logo
from os import system, name


# function for clearing the terminal
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print(logo)
biding_log = {}
new_bidders = True
while new_bidders:
    name = input("What is your name?: ")
    print(name)
    price = int(input('What is your bid?: $'))
    print(f"${price}")
    biding_log[name] = price
    q_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if q_bidders == 'no':
        new_bidders = False
    else:
        clear()

biggest_bid_name = ""
biggest_bid = 0

for name in biding_log:
    if biding_log[name] > biggest_bid:
        biggest_bid = biding_log[name]
        biggest_bid_name = name
print(f"The winner is {biggest_bid_name} with a bid of ${biggest_bid}")
