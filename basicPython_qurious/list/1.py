a = [{"aaa":"bbb"}]

a.append([])
a.append([])
a.append([])
a.append([])

while True:
    if [] in a:
        a.remove([])
    else: break
print(a)