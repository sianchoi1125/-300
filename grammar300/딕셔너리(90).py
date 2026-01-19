scores = [8.8, 9.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _=scores
print(valid_score)

a, b, *valid_score = scores
print(valid_score)

temp= {}
name= {
    "melona":1000,
    "polapo":1200,
    "panparae":1800,
}
print(name)

name["worldcone"] = 1500
name["shark"] = 1200
print(name)

print("melona price:", name["melona"])

name["melona"] = 1300
print(name)

del name["melona"]
print (name)

print(name["worldcone"])

