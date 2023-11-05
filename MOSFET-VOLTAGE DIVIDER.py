a=int(input("enter VGS:"))
d=int(input("enter VDD:"))
e=int(input("enter id:"))
f=int(input("enter rs:"))
g=int(input("enter r1:"))
h=int(input("enter r2:"))
VG=(h*d)/(g+h)
print("the value of VG is",VG)


if a==0:
    VGS=VG-(e*f)
    
else:
    VGS=a

print("the value of VGS is",VGS)
    
