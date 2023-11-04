x = int(input("Enter vcc: "))
y = float(input("Enter Vbe: "))
z=int(input("Enter rb:"))
o = int(input("Enter ib: "))
a = int(input("Enter beta value: "))
b=int(input("Enter rc"))
t=int(input("Enter Re"))
c=int(input("enter r1"))
d=int(input("enter r2"))
ETH=(d*x)/(c+d)
RTH=(c*d)/(c+d)
print("value of ETH",ETH)
print("value of RTH",RTH)



if z:
    IB = (ETH - y) / RTH + (a + 1) * t
    RB = z
    
else:
    IB = o
    RB = (x - y) / o

IC = a * IB
VCE=x-IC*(b+t)

print("The value of IB is:", IB)
print("The value of IC is:", IC)
print("The value of RB is:", RB)
print("The value of VCE is:",VCE)


