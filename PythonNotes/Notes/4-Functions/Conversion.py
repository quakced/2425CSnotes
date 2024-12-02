#chemistry
#moles to gram 
def moles2grams(a,b):
    return(a*b)
    print(f"moles to grams is {moles2grams}")
def grams2moles(a,b):
    return(a/b)
    print(f"grams to moles is {grams2moles}")
a = 1.55
b = 333.77
print()
# molecules to moles
def molecules2moles(x):
    return x/6.022*10**23
    print(f"molecules to moles is {molecules2moles}")
def moles2molecules(x):
    return x*6.022*10**23
    print(f"moles to molecules is {moles2molecules}")

# atoms to moles
#physics
# mph to kph
def mph2kph(x):
    return x*1.60934
    # kph to mph
def kph2mph(x):
    return x*.621371
    # m/s**2 to ft/s**2
def mssq2ftssq(x):
    return x*3.28084
    # ft/s**2 to m/s**2
def ftssq2mssq(x):
    return x*.3048

print(mph2kph(20))
print(kph2mph(20))
print(mssq2ftssq(20))
print(ftssq2mssq(20))


#ft/s to m/s vv
def fts2ms(speed):
    print(f"{speed} ft/s is {speed/3.281} m/s")
def ms2fts(speed):
    print(f"{speed} m/s is {speed*3.281} ft/s")
    #km/s to m/s vv
def kms2ms(speed):
    print(f"{speed} km/s is {speed*1000} m/s")
def ms2kms(speed):
    print(f"{speed} m/s is {speed/1000} km/s")

#general dimensions
#in to ft 
inches=(1)
feet=(12)
oz=(8)
centimeters=(2.54)
cups=(1)
print(inches/feet)
print(feet/inches)
print(centimeters/inches)
print(inches/centimeters)
print(oz/cups)
print(cups/oz)

'''
    define each f(x) forward and back 
        each f(x) needs to return the value

    Ex: print(in2ft(12))
    1
'''
