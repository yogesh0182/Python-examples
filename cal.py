a=int(input("enter the value A ="))
ope=str(input("+,-,*,/ ="))
b=int(input("enter the  value B="))

if ope=="+":
    print("add:",a+b)
elif ope=="-":
    print("sub:",a-b)
elif ope=="*":
    print("mul:",a*b)
elif ope=="div":
    if b!=0:
        print("div:",a/b)
    else:
        print("error")
else:
    print("invalid operator")            
      