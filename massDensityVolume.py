mdv = input("Choose one to calculate(m,d,v) : ")

if mdv == 'm' or 'M':
    d = float(input("Please enter Density: "))
    v = float(input("Please enter Volume: "))
    result = d*v #This is for mass
elif mdv == 'd' or 'D':
    m = float(input("Please enter Mass: "))
    v = float(input("Please enter Volumn: "))
    result = m/v #This is for density
elif mdv == 'v' or 'V':
    m = float(input("Please enter Mass: "))
    d = float(input("Please enter Density: "))
    result = m/d;
print("%.2f" % result)