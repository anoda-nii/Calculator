# Line slope

def line():
  x = int(input("Enter x coordinates: "))
  y = int(input("Enter y coordinates: "))
  x2= int(input("Enter the second x coordinates: "))
  y2 = int(input("Enter the secondy coordinates: "))

      
  print("The line slope is %s." % (slope(ys(y2,y),xs(x2,x))))

def ys(y2,y):
    return y2-y
def xs(x2,x):
    return x2-x

def slope(ys,xs):
    if ys == xs:
      raise ValueError('The points are the same')      
      
    return ys/xs

  