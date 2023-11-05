a=int(input("enter VGS:"))
b=int(input("enter VDS:"))
d=int(input("enter VDD:"))
e=int(input("enter id:"))
f=int(input("enter rd:"))
if a==0:
    VGS=d-(e*f)
    
else:
    VGS=a

print("the value of VGS is",VGS)
    
