#cow= input("문자열 입력")

#if cow.islower():
    #print(cow.upper())

#else:
    #print(cow.lower())


#score= input("score:")
#score= int(score)
#if score > 80:
    #print("A")
#elif 60 < score < 81:
    #print("B")
#elif 40 < score < 61:
    #print("C")
#else:
    #print("D")



#change = {
    #"dollar": 1167,
    #"yen": 1.096,
   # "baht": 35
#}
#money= input("dollar, yen, baht please: ")

#num, currency = money.split()
#print(float(num)*change[currency], "won")

#a= int(input("n1:"))
#b= int(input("n2:"))
#c= int(input("n3:"))

#if a >= b and a>= c:
#print(a)
#elif b>= a and b>=c:
    #print(b)
#else:
    #print(c)



a= input("please type the phone number 000-0000-0000: ")
b= a.split("-")[0]


if b== "011":
    s= "SKT"
elif b== "016":
    s= "KT"
elif b== "019":
    s= "LG"
else:
    s="unknown"

print(f"you are a {s} user!")


post= input("5 digit post numbers: ")

if post[-1] in ("0", "1", "2"):
    print("gangbuk")
elif post[-1] in ("3", "4", "5"):
    print("dobong")
else: 
    print("nowan")

person= input("type identification num:")
a=person.split("-")[1]
if a[0] in ("1", "3"):
    print("male")
else: 
    print("female")

if 0 <= int(a[1:3]) <= 8:
    print("seoul")
else: 
    print("nope")


