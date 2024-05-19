from random import sample, choice

num_letter_series = ['2', '3', '5', '10', '9', '1', '34', '11', '16', 'e', 't', 'r', 'o', 'p']
winning_series = sample(num_letter_series, 4)
print(f"Winning series is: {winning_series}.  Any ticket that matches these numbers or letters wins a prize")

my_ticket = []
count = 0

# Looping through the list to match the winning series
while winning_series:
    current_pick = choice(num_letter_series)
    print(f"Checking if the pick matched any of the winning series")
    print(f"Current pick is {current_pick}")
    if current_pick in winning_series:
        print(f"\nPick {current_pick} matched the winning series")
        winning_series.remove(current_pick)
        my_ticket.append(current_pick)
    count += 1
print(f"\nHurray!!, you won the lottery for the series {my_ticket}")
print(f"Number of times it went through the loop: {count}")