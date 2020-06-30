# Cos, Sin and Tan.
def deg():
  
  degr, nummer = input("Enter cos, sin or tan and then the number: ").split()
  degr = degr.lower()
  import math
  if degr == "cos":
    result = math.cos(math.degrees(int(nummer)))
    print("The result is %s" % (result))
  
  elif degr == "sin":
    result = math.sin(math.radians(int(nummer)))
    print("The result is %s" % (result))
  
  elif degr == "tan":
    result = math.tan(math.radians(int(nummer)))
    print("The result is %s" % (result))
  
  else:
    print("Something went wrong.")
