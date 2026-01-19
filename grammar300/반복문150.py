list= [100, 200, 300]
for i in list:
    print(int(i)+10)

menu= ["pasta", "chicken", "pizza"]
for i in menu:
    print("today's menu:", str(i))

comp= ["LG", "SK", "SS"]
for i in comp:
    length= len(i)
    print(length)
    
name= ["cat", "dog", "rabbit"]
for i in name:
    co= len(i)
    print(i, co)

for i in name:
    go= i[0]
    print(go)

letter= ["a","v", "g", "q"]
for i in letter[: :2]:
    print(i)

for i in letter[: :-1]:
    print(i)

