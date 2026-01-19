a= "3"
b= "4"
print(a+ b)
print("Hi"*3)

print("-"*80)

t1= "python"
t2= "java"
print((t1+" "+t2+" ")*4)

name1 = "김민수"
age1= 10
name2 = "이철희"
age2= 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

상장주식수 = "5,969,782,550"
newnum= 상장주식수.replace(",","")
int_newnum= int(newnum)
print(int_newnum, type(int_newnum))

term = "2020/03(E) (IFRS연결)"
print(term[:7])

data= "   samsung   "
newdata= data.replace(" ","")
print(newdata)

data1= data.strip()
print(data1)