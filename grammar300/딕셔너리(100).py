inventory = {"melona":[300,20],
             "vivivic": [400,3],
             "shark": [250,100]
}

print(inventory["melona"][0],"원")
print(inventory["melona"][1], "개")

inventory["worldcone"]= [500, 7]
print(inventory)

icecream = {
    "tank":1200,
    "pola":1200,
    "pan":1800,
    "cone":1500,
    "memon":1000
}

print(icecream.keys())
print(icecream.values())
print(sum(icecream.values()))

new = {
    "good":1200,
    "nice":1900
}

icecream.update(new)
print(icecream)

keys= ('a','b','c')
values= (1,2,3)

result= dict(zip(keys, values))
print(result)

