dataset = {"bob":19,
           "boba":20,
           "biba":15,
           "baba":10}
a = []
for ele in dataset.values():
    a.append(ele)
a.sort()
x = -1
while x>-1:
    for key,ele in dataset.items():
        if ele==a[x]:
            print(key)
    x = x-1