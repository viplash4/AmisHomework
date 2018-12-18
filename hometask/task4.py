string = "Food apple hotdog burger"
string = string.split()
dataset = dict()
if string[0] in dataset.keys():
    dataset[string[0]].append(string[1:])
else:
    dataset[string[0]] = string[1:]

print(dataset)