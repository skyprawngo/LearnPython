n = int(input("number: "))
i = [int(input("value: ")) for i in range(n)]
sum = 0
s = set()
for e in i:
    if e not in s:
        s.add(e)
        sum = sum+e
print(sum)