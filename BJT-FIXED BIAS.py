x = int(input("Enter Vcc: "))
y = float(input("Enter Vbe: "))
z = int(input("Enter Rb: "))
o = int(input("Enter ib: "))
a = int(input("Enter beta value: "))
b=int(input("Enter rc"))



if z:
    IB = (x - y) / z
    RB = z
    
else:
    IB = o
    RB = (x - y) / o

IC = a * IB
VCE=x-IC*b

print("The value of IB is:", IB)
print("The value of IC is:", IC)
print("The value of RB is:", RB)
print("The value of VCE is:",VCE)




