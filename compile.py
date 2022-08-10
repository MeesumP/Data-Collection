with open('names.txt', 'r') as f:
    lines = f.readlines()

finalnames = []

for string in lines:
    string = string.replace('\n', '')
    finalnames.append(string)

with open('location.txt', 'r') as f:
    locations = f.readlines()

finallocation = []

for string in locations:
    string = string.replace('\n', '')
    finallocation.append(string)