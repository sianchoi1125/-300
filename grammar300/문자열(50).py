ticker = "btc_krw"
UPticker= ticker.upper()
print(UPticker)

Lowtiker= UPticker.lower()
print(Lowtiker)

s= "hello"
Ss= s.capitalize()
print(Ss)

file_name= "letter.xlsx"
file_name.endswith(("xlsx","xls"))

name= "2020_letter.xlsx"
name.startswith("2020")

a= "hello world"
aa= a.split(" ")
print(aa)

print(a.split())

t= "btc_krw"
print(t.split("_"))

date= "2020-02-01"
print(date.split("-"))

data= "2323     "
print(data.rstrip())