li3 = []
for n in li:
    if n not in li2:
        li3.append(n)

for n in li2:
    if n not in li:
        li3.append(n)

li3.sort()
print(li3)