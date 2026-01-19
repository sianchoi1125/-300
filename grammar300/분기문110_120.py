print( 3==5 )
print( 3< 5)
print(3>=4)

#a= input("please type anything")
#print(a, a)

#s= int(input("type any number:"))
#print( s+10 )

#w= int(input("number input:"))
#if w%2 == 0 :
    #print("even number")
#else:
    #print("odd number")

#r=input("number:")
#num= int(r)+20
#if num > 255:
    #print(255)
#else:
   #print(num)


#t=int(input("num:"))
#w= t-20
#if t<0:
    #print(0)
#elif t>255:
    #print(255)
#else: 
    #print(w)

time= input("정각일까요? 입력(00:00):")
if time[-2:] == "00" :
    print("yes 정각")

else: 
    print("ㄴㄴ")

fruit= ["apple", "grape", "blueberry"]
a= input("what's your favorite fruit? :")
if a in fruit:
    print("I also like it!")
else:
    print("you have bad taste;;")

warn= ["M", "G", "B", "K", "S"]
ans= input("tell me your investment")
if ans in warn:
    print("you are doomed")
else:
    print("wow..keep going")

sweet= {"spring":"strawberry", "summer":"starfruit", "autumn":"pumpkin", "winter":"nothing"}

oin= input("fav fruit?:")

if oin in sweet.values():
    print("approved")
else:
    print("try again")

