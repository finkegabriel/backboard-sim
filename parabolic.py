
#projectile motion equations
def x_distance():
    return 0

def parabolic(xsquare,b,c,n):
    final = []
    for l in range(0,n):
        final.append((((xsquare*l)**2))+(b*l)+c)
    return final

def line(m,b,n):
    #y=mx+b
    final = []
    for l in range(0,n):
        print("n ",l)
        final.append(m*(l)+b)
    return final

def trajectory(x,y,z):
    #x^2+0x+0
    return 0
    