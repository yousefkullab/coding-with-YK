import re
import random

lines = []
with open("input.txt", "r") as file:
    for line in file:
        lines.append(line)

winners = []
pattern = r"[A-z0-9]+@"
for line in lines:
    if re.search(pattern, line):
        winners.append(line)

winner = random.choice(winners)
with open("output.txt", "w") as file:
    file.write(f"The winner is: {winner}")



