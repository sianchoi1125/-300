letters= "python"
print(letters[0], letters[2])

license_plate = "24가 2210"
print(license_plate[4:])
print(license_plate[-4:])

string= "홀짝홀짝홀짝"
print(string[0], string[2], string[4])
print(string[::2])
print(string[::3])

string= "PYTHON"
print(string[::-1])

phone_number = "010-1111-2222"
phone_number2= phone_number.replace("-"," ")
print(phone_number2)

phone_number3= phone_number2.replace(" ","")
print(phone_number3)

url = "hhtp://sharebook.kr"
print(url[-2:])

url_split= url.split(".")
print(url_split[-1])

string= "abcdfe2a354a32a"
Astring= string.replace("a","A")
print(Astring)
